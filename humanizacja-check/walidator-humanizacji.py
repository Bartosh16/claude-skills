#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Walidator humanizacji - sprawdza, czy tekst po humanizacji faktycznie sie zmienil
i czy sygnaly AI zniknely. Deterministycznie, bez oceny "wyglada lepiej".

Uzycie:
    python walidator-humanizacji.py --before przed.md --after po.md --lang pl
    python walidator-humanizacji.py --before before.md --after after.md --lang en

Exit 0 = ZWALIDOWANE (moga byc ostrzezenia), exit 1 = WRACA DO POPRAWEK.

Tylko stdlib.
"""

import argparse
import difflib
import re
import statistics
import sys
import unicodedata

# ---------------------------------------------------------------- konsola

def _init_stdout():
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
    except (AttributeError, ValueError):
        pass


# ---------------------------------------------------------------- wzorce
# Kazda pozycja: (etykieta, regex, tier)
# tier "hard"  - musi zniknac calkowicie, obecnosc w after = FAIL
# tier "soft"  - liczymy, FAIL tylko przy regresji (after > before)
# tier "info"  - heurystyka z falszywymi pozytywami, tylko do wgladu

SYGNALY_PL = [
    ("wata slowna", r"w dzisiejszym|w obecnych czasach|w dzisiejszych czasach|"
                    r"w erze cyfrowej|w tym artykule (przyjrzymy|omowimy|sprawdzimy)|"
                    r"warto (zauwazyc|zaznaczyc|podkreslic|wspomniec)|"
                    r"nalezy pamietac|nie sposob nie zauwazyc|poniz(ej|szy) przedstawiam", "hard"),
    ("atrybucja bez zrodla", r"badania (pokazuja|wskazuja|dowodza)|eksperci (sa zgodni|twierdza|uwazaja)|"
                             r"powszechnie (uwaza|przyjmuje) sie|wiele osob (uwaza|twierdzi)|"
                             r"obserwatorzy (wskazuja|zauwazaja)|raporty branzowe|"
                             r"niektorzy (krytycy|eksperci)|specjalisci (podkreslaja|zalecaja)", "hard"),
    ("falszywa autentycznosc", r"moi klienci (pytaja|mowia)|ostatnio coraz czesciej slysze|"
                               r"znam to z autopsji|widze to u kazdego klienta|i szczerze\?", "hard"),
    ("coachingowy belkot", r"uwolnij (swoj )?potencjal|odkryj autentyczn|turbodoladuj|"
                           r"wejdz na wyzszy poziom|zmien swoje zycie|"
                           r"czytaj dalej|zostan ze mna do konca", "hard"),
    ("otwarcie 'jako [rola]'", r"\bjako \w+[\w\s]{0,30}(z \w+letnim|z wieloletnim|z \d+[- ]letnim)", "hard"),
    ("generyczne zakonczenie", r"podsumowujac[,\s]|przyszlosc (rysuje sie|zapowiada sie)|"
                               r"przed nami ekscytujac", "hard"),
    ("miekka komunikacja", r"\bwarto \w+c\b|\bnalezy \w+c\b|powinno sie|zaleca sie|"
                           r"dobrze jest \w+c|moze pomoc|moze sprzyjac", "soft"),
    ("slownik AI", r"\bkluczow\w*|\bdynamiczn\w*|\bkompleksow\w*|\binnowacyjn\w*|"
                   r"\bsynergi\w*|\bfundamentaln\w*|\bholistyczn\w*|\bniezwykl\w*|"
                   r"\bfascynujac\w*|\bznaczaco\b|potezne narzedzie|zmienia zasady gry", "soft"),
    ("unikanie 'jest'", r"\bstanowi\b|pelni (funkcje|role)|sluzy jako|charakteryzuje sie|"
                        r"oferuje mozliwosc|wyroznia sie \w+", "soft"),
    ("napuszona waznosc", r"kluczow\w+ rol|przelomow\w+ (moment|chwil)|stanowi dowod|"
                          r"wpisuje sie w|ma fundamentalne znaczenie", "soft"),
    ("imieslow doklejony", r",\s*(co )?(podkresla|pokazuje|uwypukla|potwierdza|swiadczy)|"
                           r",\s*\w+ac (zaangazowanie|znaczenie|wage|trend)|,\s*wpisujac sie", "soft"),
    ("bezosobowosc", r"\b(uwaza|przyjmuje|stosuje|zaleca|zauwaza) sie\b|"
                     r"\bzosta(l|la|lo|ly|li) \w+(ny|na|ne|ni|te|ta|ty)\b", "soft"),
    ("rzeczownik odczasownikowy na starcie", r"(?:^|(?<=[.!?]\s))(Zrozumienie|Wdrazanie|Wdrozenie|"
                                             r"Zapewnienie|Monitorowanie|Stosowanie|Wykorzystanie|"
                                             r"Budowanie|Tworzenie) \w+", "soft"),
    ("kalki z angielskiego", r"adresowac (problem|kwesti)|na koniec dnia|dostarczac (rezultat|wartosc)|"
                             r"podjac akcje|krajobraz (technologiczn|biznesow)|tetniac\w* zyciem|"
                             r"podniesc na wyzszy poziom|zaglebmy sie|zanurzmy sie", "soft"),
    ("naduzycie 'bez'", r"\bbez \w+", "soft"),
    ("triada anaforyczna", r"(\bbez \w+,\s*){2}bez \w+|(\bzero \w+,\s*){2}zero \w+", "hard"),
    ("konstrukcja 'nie tylko'", r"nie tylko[^.!?]{1,60}\bale\b|to nie \w[^.!?]{1,40}, to \w|"
                                r"cos wiecej niz", "hard"),
    ("regula trzech (heurystyka)", r"\b\w+,\s+\w+\s+i\s+\w+\b", "info"),
]

SYGNALY_EN = [
    ("filler phrases", r"in today'?s [\w\s-]{0,20}world|in the ever-evolving|"
                       r"it'?s worth noting|it is important to note|at the end of the day|"
                       r"in this article,? we'?ll|when it comes to|in order to\b", "hard"),
    ("weasel attribution", r"studies show|experts agree|it is widely (believed|regarded)|"
                           r"observers (note|argue)|many (argue|believe)|industry reports|"
                           r"some critics|research (shows|suggests) that", "hard"),
    ("chatbot artifacts", r"i hope this helps|let me know if|feel free to (adjust|modify|reach)|"
                          r"as of my last (update|training)|great question|"
                          r"here'?s a draft|\[insert [\w\s]+\]", "hard"),
    ("throat-clearing", r"here'?s the thing|let me be clear|the uncomfortable truth|"
                        r"what if i told you|plot twist|here'?s the kicker|"
                        r"what nobody tells you|let'?s dive into|let'?s be honest|"
                        r"here'?s what most people get wrong", "hard"),
    ("credential opener", r"as an? (seasoned|experienced|veteran) \w+|"
                          r"with (over )?\w+ years of experience,? i", "hard"),
    ("generic ending", r"in conclusion|the future looks bright|exciting times (lie )?ahead|"
                       r"^ultimately,", "hard"),
    ("slop vocabulary", r"\bdelv\w+|\bleverag\w+|\brobust\b|\btapestr\w+|\bseamless\w*|"
                        r"\bshowcas\w+|\btestament\b|\bunderscor\w+|\bpivotal\b|\bvibrant\b|"
                        r"\bmyriad\b|\bplethora\b|cutting-edge|game-chang\w+|\bnavigat\w+|"
                        r"\bstreamlin\w+|\bholistic\b|\bcrucial\b|\bfoster\w*|\brealm\b|"
                        r"\bintricate\b|\bnuanced\b|\belevat\w+|\bunlock\w*|\bempower\w*", "soft"),
    ("corporate jargon", r"\bsynergi\w+|circle back|touch base|double down|move the needle|"
                         r"low-hanging fruit|best-in-class|world-class|actionable insights|"
                         r"deep dive|\bbandwidth\b|align on|\bideate\b|\butilize\w*|operationalize", "soft"),
    ("hedging", r"may help|can potentially|could potentially|it could be argued|"
                r"one (should|might)|it is recommended|can be beneficial", "soft"),
    ("copula avoidance", r"serves as|functions as|stands as|\bboasts\b|features an?\b|"
                         r"represents a|constitutes the", "soft"),
    ("importance puffery", r"plays? an? (crucial|vital|key|pivotal) role|testament to|"
                           r"pivotal moment|marks? a (turning|defining) point|"
                           r"reflects? a broader", "soft"),
    ("participial tail", r",\s+(highlighting|underscoring|emphasizing|showcasing|reflecting|"
                         r"demonstrating|contributing to|cementing)\b", "soft"),
    ("passive / subjectless", r"\b(was|were|been|being) \w+(ed|en)\b|it is (believed|thought|considered)", "soft"),
    ("gerund opener", r"(?:^|(?<=[.!?]\s))(Understanding|Implementing|Ensuring|Leveraging|"
                      r"Navigating|Building|Creating|Establishing) \w+", "soft"),
    ("negative promises", r"\bno \w+", "soft"),
    ("anaphoric triple", r"(\bno \w+[,.]\s*){2}no \w+|(\bzero \w+,\s*){2}zero \w+", "hard"),
    ("negative parallelism", r"not just [^.!?]{1,50},? but|it'?s not [^.!?]{1,50}\.\s*it'?s |"
                             r"more than just", "hard"),
    ("rule of three (heuristic)", r"\b\w+,\s+\w+,?\s+and\s+\w+\b", "info"),
]


# ---------------------------------------------------------------- pomocnicze

def bez_ogonkow(t):
    """Do dopasowania wzorcow PL bez zalezosci od diakrytykow."""
    return "".join(c for c in unicodedata.normalize("NFD", t)
                   if unicodedata.category(c) != "Mn")


def zdania(tekst):
    czysty = re.sub(r"^#{1,6}\s.*$", "", tekst, flags=re.M)      # naglowki
    czysty = re.sub(r"^\s*[-*|>].*$", "", czysty, flags=re.M)     # listy, tabele, cytaty
    czysty = re.sub(r"```.*?```", "", czysty, flags=re.S)         # bloki kodu
    return [z.strip() for z in re.split(r"(?<=[.!?])\s+", czysty) if len(z.strip()) > 1]


def licz(wzorce, tekst, lang):
    baza = bez_ogonkow(tekst).lower() if lang == "pl" else tekst.lower()
    wynik = {}
    for etykieta, wzor, tier in wzorce:
        wynik[etykieta] = (len(re.findall(wzor, baza, re.M)), tier)
    return wynik


def typografia(tekst, lang):
    """Zwraca liste (opis, liczba, tier)."""
    body = re.sub(r'\b\w+="[^"]*"', "", tekst)          # atrybuty HTML poza analiza
    body = re.sub(r"^---\s*$.*?^---\s*$", "", body, flags=re.M | re.S, count=1)  # frontmatter
    out = []
    if lang == "pl":
        out.append(("em dash U+2014 (zakazany w PL)", body.count(chr(0x2014)), "hard"))
        out.append(("ASCII quote U+0022 w tresci", body.count('"'), "hard"))
        out.append(("U+201C (angielski otwierajacy)", body.count(chr(0x201C)), "hard"))
        otw, zam = body.count(chr(0x201E)), body.count(chr(0x201D))
        out.append(("niesparowane cudzyslowy", abs(otw - zam), "hard"))
        zla = len(re.findall(r"(?<!\.\.)\." + re.escape(chr(0x201D)), body))
        zla += len(re.findall(r"[,;:]" + re.escape(chr(0x201D)), body))
        out.append(("zla kolejnosc interpunkcji (PL: tekst”.)", zla, "hard"))
    else:
        em = body.count(chr(0x2014))
        out.append(("em dashes (limit 2)", max(0, em - 2), "hard"))
        out.append(("curly quotes", sum(body.count(c) for c in "“”‘’"), "hard"))
    out.append(("separator --- miedzy sekcjami",
                len(re.findall(r"^\s*---\s*$", body, flags=re.M)), "hard"))
    out.append(("naglowki Title Case",
                len([h for h in re.findall(r"^#{1,6}\s+(.+)$", body, flags=re.M)
                     if len(re.findall(r"\b[A-Z][a-z]+", h)) >= 3]), "soft"))
    return out


def liczby(tekst):
    return set(re.findall(r"\b\d[\d\s.,]*\d\b|\b\d+\s?%|\b\d{4}\b", tekst))


# ---------------------------------------------------------------- raport

def main():
    _init_stdout()
    ap = argparse.ArgumentParser()
    ap.add_argument("--before", help="tekst przed humanizacja; pominiety = tryb scan-only")
    ap.add_argument("--after", required=True)
    ap.add_argument("--lang", choices=["pl", "en"], default="pl")
    a = ap.parse_args()

    after = open(a.after, encoding="utf-8").read()
    scan_only = a.before is None
    before = after if scan_only else open(a.before, encoding="utf-8").read()
    wzorce = SYGNALY_PL if a.lang == "pl" else SYGNALY_EN

    bledy, ostrzezenia = [], []
    print("=" * 62)
    print(f"WALIDACJA HUMANIZACJI [{a.lang.upper()}]" + (" - TRYB SCAN-ONLY" if scan_only else ""))
    print("=" * 62)

    zb, za = zdania(before), zdania(after)

    # --- 1. czy cokolwiek sie zmienilo
    if scan_only:
        print("\n[1] ZAKRES ZMIAN - pominiete (brak tekstu zrodlowego)")
    else:
        ratio = difflib.SequenceMatcher(None, before, after).ratio()
        wspolne = len(set(zb) & set(za))
        proc_id = 100 * wspolne / len(za) if za else 0

        print("\n[1] ZAKRES ZMIAN")
        print(f"  podobienstwo tekstow      : {ratio:.3f}")
        print(f"  zdania niezmienione       : {wspolne}/{len(za)} ({proc_id:.0f}%)")
        if ratio >= 0.92:
            bledy.append(f"kosmetyka zamiast humanizacji (podobienstwo {ratio:.3f} >= 0.92)")
        elif ratio >= 0.80:
            ostrzezenia.append(f"zmiany plytkie (podobienstwo {ratio:.3f})")
        if proc_id >= 50 and len(za) > 4:
            bledy.append(f"{proc_id:.0f}% zdan przepisanych bajt w bajt")

    # --- 2. sygnaly AI
    print("\n[2] SYGNALY AI" + (" (skan tekstu)" if scan_only else " (przed -> po)"))
    lb, la = licz(wzorce, before, a.lang), licz(wzorce, after, a.lang)
    naglowek = (f"  {'kategoria':<38} {'znalezione':>10}  tier" if scan_only
                else f"  {'kategoria':<38} {'przed':>6} {'po':>6}  status")
    print(naglowek)
    print("  " + "-" * (len(naglowek) - 2))
    for etykieta, (npo, tier) in la.items():
        nprzed = lb[etykieta][0]
        if scan_only:
            if npo:
                print(f"  {etykieta:<38} {npo:>10}  {tier}")
                if tier == "hard":
                    bledy.append(f"'{etykieta}' obecne ({npo}x) - kategoria twarda")
                elif tier == "soft":
                    ostrzezenia.append(f"'{etykieta}' obecne ({npo}x)")
            continue
        if tier == "info":
            status = "info"
        elif npo > nprzed:
            status = "REGRESJA"
            bledy.append(f"regresja: '{etykieta}' {nprzed} -> {npo}")
        elif tier == "hard" and npo > 0:
            status = "ZOSTALO"
            bledy.append(f"'{etykieta}' nadal obecne ({npo}x) - kategoria twarda")
        elif npo < nprzed:
            status = "ok"
        elif npo > 0:
            status = "bez zmian"
            ostrzezenia.append(f"'{etykieta}' bez zmian ({npo}x)")
        else:
            status = "czysto"
        if nprzed or npo:
            print(f"  {etykieta:<38} {nprzed:>6} {npo:>6}  {status}")

    # --- 3. rytm
    print("\n[3] RYTM ZDAN")
    pary = (("po", za),) if scan_only else (("przed", zb), ("po", za))
    for nazwa, zd in pary:
        dl = [len(z.split()) for z in zd]
        if len(dl) >= 2:
            sd, sr = statistics.pstdev(dl), statistics.mean(dl)
            cv = sd / sr if sr else 0          # wspolczynnik zmiennosci, niezalezny od skali
            print(f"  {nazwa:<6} srednia {sr:5.1f} slow, odchylenie {sd:5.1f}, zmiennosc {cv:.2f}")
            if nazwa == "po" and len(dl) >= 5:
                if cv < 0.25:
                    bledy.append(f"metronom: zmiennosc dlugosci zdan {cv:.2f} < 0.25")
                elif cv < 0.40:
                    ostrzezenia.append(f"rytm plaski: zmiennosc {cv:.2f} (ludzki tekst zwykle 0.5+)")
                if sr < 7:
                    ostrzezenia.append(f"sieczka staccato: srednia dlugosc zdania {sr:.1f} slowa")

    # --- 4. typografia
    print("\n[4] TYPOGRAFIA")
    czysto = True
    for opis, n, tier in typografia(after, a.lang):
        if n:
            czysto = False
            print(f"  {opis:<45} {n:>4}")
            (bledy if tier == "hard" else ostrzezenia).append(f"typografia: {opis} ({n}x)")
    if czysto:
        print("  bez zastrzezen")

    # --- 5. wiernosc
    if scan_only:
        print(f"\n[5] WIERNOSC - pominieta (brak tekstu zrodlowego). Dlugosc: {len(after.split())} slow")
    else:
        print("\n[5] WIERNOSC WOBEC ORYGINALU")
        wb, wa = len(before.split()), len(after.split())
        delta = 100 * (wa - wb) / wb if wb else 0
        print(f"  dlugosc: {wb} -> {wa} slow ({delta:+.0f}%)")
        if abs(delta) > 35:
            bledy.append(f"dlugosc poza limitem: {delta:+.0f}% (skill dopuszcza +/-20%)")
        elif abs(delta) > 20:
            ostrzezenia.append(f"dlugosc poza limitem: {delta:+.0f}% (limit +/-20%)")
        nowe = liczby(after) - liczby(before)
        if nowe:
            print(f"  nowe liczby w tekscie po: {', '.join(sorted(nowe)[:10])}")
            ostrzezenia.append(f"nowe liczby ({len(nowe)}) - sprawdz, czy nie zmyslone")
        else:
            print("  brak nowych liczb")

    # --- werdykt
    print("\n" + "=" * 62)
    if bledy:
        print("WERDYKT: WRACA DO POPRAWEK")
        print("=" * 62)
        for b in bledy:
            print(f"  [BLAD] {b}")
        for o in ostrzezenia:
            print(f"  [UWAGA] {o}")
        return 1
    print("WERDYKT: ZWALIDOWANE")
    print("=" * 62)
    for o in ostrzezenia:
        print(f"  [UWAGA] {o}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
