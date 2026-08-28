#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
metryki.py - twarde liczby do audytu ai-audit.

Uzycie:
    python metryki.py plik.md
    python metryki.py folder/            # tryb korpusu
    python metryki.py a.md b.md c.md     # tryb korpusu
    python metryki.py folder/ --json     # surowy JSON

Skrypt NIE ocenia i NIE wykrywa "czy to AI". Liczy tylko rzeczy, ktore czlowiek
musialby liczyc recznie: rytm zdan, gestosc konkretow, powtarzalnosc szkieletu.
Interpretacja nalezy do audytora.
"""

import sys, os, re, json, glob, statistics as st
from itertools import combinations

# ---------- katalogi wzorcow ----------

FRAZY_PRZEJSCIOWE = [
    r"znacznie lepsz\w*", r"problem zaczyna si\w*", r"nie chodzi jednak o",
    r"dzi[ei]ki temu zamiast", r"w tym (poradniku|artykule|wpisie) (przejdziemy|pokaz\w+|znajdziesz)",
    r"to jedna z naj\w+", r"nie ma jednej (uniwersalnej )?odpowiedzi",
    r"wystarczy jednak", r"co wi[ee]cej", r"warto (jednak )?pami[ee]ta[cc]",
    r"kluczow\w+ jest", r"nie tylko\b.{0,40}\bale (tez|i)\b",
    r"w dzisiejszych czasach", r"w erze \w+", r"swiat \w+ zmienia si[ee]",
    r"pami[ee]taj, ze", r"podsumowuj[aa]c", r"reasumuj[aa]c",
    r"to wlasnie dlatego", r"i tu pojawia si[ee] \w+",
    r"brzmi (prosto|banalnie|znajomo)\?", r"efekt\? ", r"rezultat\? ",
    r"(pozwala|umozliwia|sprawia, ze) \w+ szybciej i (skuteczniej|lepiej|efektywniej)",
]

HIPOTETYCZNE = [
    r"zalozmy", r"wyobraz sobie", r"powiedzmy, ze", r"hipotetyczn\w+",
    r"przykladowo", r"na przyklad (pewien|pewna|firma|freelancer|sklep|agencja)",
    r"jesli prowadzisz (sklep|firm|agencj|blog)", r"dla przykladu",
]

PIERWSZA_OSOBA = [
    # zaimki
    r"\bja\b", r"\bmoj\w+\b", r"\bmnie\b", r"\bmi\b", r"u mnie",
    # czas przeszly 1 os. - wzorce z samogloska tematyczna, zeby nie lapac
    # rzeczownikow typu "problem", "system", "poziom"
    r"\w{2,}[aeiouy]lem\b", r"\w{2,}[aeiouy]lam\b",
    r"\bmoglem\b", r"\bmoglam\b", r"\bszedlem\b", r"\bwzielem\b",
    # czas terazniejszy 1 os. - najczestsze czasowniki relacji
    r"\b(robie|zrobilem|uzywam|testowalem|sprawdzam|widze|uwazam|polecam|odradzam)\b",
]

CTA = [
    r"\bebook\w*", r"\bkliknij\b", r"\bpobierz\b", r"\bzapisz si[ee]\b", r"\bnewsletter\b",
    r"\bkup\b", r"sprawdz ofert", r"\bdolacz\b", r"\bzamow\b", r"\bkurs\w* za\b",
]

HEDGING = [
    r"\bmoze byc\b", r"\bwarto\b", r"\bnalezy\b", r"\btrzeba\b", r"\bzazwyczaj\b",
    r"\bczesto\b", r"\bzwykle\b", r"w wi[ee]kszosci przypadkow", r"\bgeneralnie\b",
]

WYCIEKI_PROMPTU = [
    r"propozycje linkowania", r"\[wstaw\b", r"\[tutaj\b", r"\bTODO\b", r"\bplaceholder\b",
    r"jako model j[ee]zykowy", r"oto (artykul|tekst|propozycja)",
    r"^#+\s*(meta|slug|title tag|opis meta|slowa kluczowe)", r"\[link do",
    r"^\s*\{\{", r"\bLorem ipsum\b",
]

TYPY_SEKCJI = {
    "faq": ["faq", "najczestsze pytania", "czesto zadawane"],
    "podsumowanie": ["podsumowanie", "na koniec", "kluczowe wnioski", "w skrocie", "tl;dr", "tldr"],
    "checklista": ["checklista", "lista kontrolna", "sciaga"],
    "bledy": ["blad", "bledy", "pulapki", "czego unikac"],
    "prompty": ["prompt", "prompty", "gotowe prompty"],
    "krok-po-kroku": ["krok", "kroki", "workflow", "proces", "instrukcja"],
    "dlaczego": ["dlaczego", "czy warto", "po co", "czy ai"],
    "cta": ["ebook", "newsletter", "oferta", "zapisz"],
    "narzedzia": ["narzedzia", "tools", "aplikacje"],
    "przyklady": ["przyklad", "przyklady", "case", "scenariusz"],
}

DIAKR = str.maketrans("ąćęłńóśźż",
                      "acelnoszz")


def norm(s):
    return s.lower().translate(DIAKR)


def czytaj(path):
    for enc in ("utf-8", "utf-8-sig", "cp1250", "latin2"):
        try:
            with open(path, encoding=enc) as f:
                return f.read()
        except (UnicodeDecodeError, LookupError):
            continue
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def zliczaj(wzorce, tekst_norm, slowa):
    trafienia = {}
    total = 0
    for w in wzorce:
        n = len(re.findall(w, tekst_norm, re.I | re.M))
        if n:
            trafienia[w] = n
            total += n
    per1000 = round(total * 1000 / max(slowa, 1), 2)
    return total, per1000, dict(sorted(trafienia.items(), key=lambda x: -x[1])[:12])


def naglowki(tekst):
    md = re.findall(r"^\s{0,3}(#{2,4})\s+(.+?)\s*$", tekst, re.M)
    html = re.findall(r"<h([2-4])[^>]*>(.*?)</h\1>", tekst, re.I | re.S)
    out = [(len(h), re.sub(r"[*_`\[\]]", "", t).strip()) for h, t in md]
    out += [(int(h), re.sub(r"<[^>]+>", "", t).strip()) for h, t in html]
    return out


def typ_sekcji(tytul):
    t = norm(tytul)
    for typ, kw in TYPY_SEKCJI.items():
        if any(k in t for k in kw):
            return typ
    return "tresc"


def analizuj(path):
    raw = czytaj(path)
    # zdejmij frontmatter i bloki kodu - to nie jest proza
    tekst = re.sub(r"^---\n.*?\n---\n", "", raw, flags=re.S)
    tekst = re.sub(r"```.*?```", " ", tekst, flags=re.S)

    hh = naglowki(tekst)
    szkielet = [typ_sekcji(t) for _, t in hh]
    # do porownan miedzy tekstami liczy sie szkielet funkcjonalny, nie kazdy naglowek:
    # sekcje merytoryczne ("tresc") sa z natury rozne, wiec zwijamy ich ciagi do jednego znacznika
    szkielet_fn = []
    for s in szkielet:
        if not szkielet_fn or szkielet_fn[-1] != s:
            szkielet_fn.append(s)

    proza = re.sub(r"^\s{0,3}#{1,6}\s+.*$", " ", tekst, flags=re.M)
    proza = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", proza)
    slowa_lista = re.findall(r"[A-Za-zĄĆĘŁŃÓŚŹŻ"
                             r"ąćęłńóśźż]{2,}", proza)
    slowa = len(slowa_lista)

    zdania = [z.strip() for z in re.split(r"(?<=[.!?…])\s+|\n{2,}", proza) if len(z.strip()) > 1]
    dl = [len(re.findall(r"\S+", z)) for z in zdania if re.findall(r"\S+", z)]
    srednia = round(st.mean(dl), 1) if dl else 0
    odch = round(st.pstdev(dl), 1) if len(dl) > 1 else 0
    burst = round(odch / srednia, 3) if srednia else 0

    tn = norm(proza)

    # TTR liczony w oknach 400 slow - odporny na dlugosc tekstu
    okno = [norm(w) for w in slowa_lista]
    ttr = []
    for i in range(0, max(len(okno) - 399, 0), 400):
        frag = okno[i:i + 400]
        ttr.append(len(set(frag)) / len(frag))
    ttr_sr = round(st.mean(ttr), 3) if ttr else round(len(set(okno)) / max(len(okno), 1), 3)

    liczby = len(re.findall(r"\b\d[\d\s.,]*\s*(?:%|zl|proc|pkt|x|godz|min|dni|tys|mln|USD|EUR|PLN)\b",
                            proza, re.I))
    lata = len(re.findall(r"\b(?:19|20)\d{2}\b", proza))
    linki_zew = len(re.findall(r"https?://", tekst))

    etykieta = os.path.basename(path)
    if etykieta.lower() in ("artykul-v2-humanized.md", "index.md", "artykul.md", "content.md",
                            "artykul-v1.md", "readme.md"):
        etykieta = os.path.basename(os.path.dirname(os.path.abspath(path)))

    res = {
        "plik": etykieta,
        "sciezka": path,
        "slowa": slowa,
        "zdania": len(dl),
        "srednia_dlugosc_zdania": srednia,
        "odchylenie_dlugosci": odch,
        "burstiness": burst,
        "zdania_do_5_slow_proc": round(100 * sum(1 for d in dl if d <= 5) / max(len(dl), 1), 1),
        "zdania_od_25_slow_proc": round(100 * sum(1 for d in dl if d >= 25) / max(len(dl), 1), 1),
        "ttr_okno400": ttr_sr,
        "naglowki": len(hh),
        "szkielet": szkielet,
        "szkielet_funkcjonalny": szkielet_fn,
        "szkielet_tytuly": [t for _, t in hh],
        "konkrety_per_1000": round((liczby + lata) * 1000 / max(slowa, 1), 2),
        "liczby_z_jednostka": liczby,
        "lata": lata,
        "linki_zewnetrzne": linki_zew,
        "linki_zewnetrzne_per_1000": round(linki_zew * 1000 / max(slowa, 1), 2),
    }
    tn_pelny = norm(tekst)  # wycieki promptu siedza czesto w naglowkach, nie w prozie
    for nazwa, wz in (("frazy_przejsciowe", FRAZY_PRZEJSCIOWE), ("hipotetyczne", HIPOTETYCZNE),
                      ("pierwsza_osoba", PIERWSZA_OSOBA), ("cta", CTA),
                      ("hedging", HEDGING), ("wycieki_promptu", WYCIEKI_PROMPTU)):
        total, per1000, trafienia = zliczaj(wz, tn_pelny if nazwa == "wycieki_promptu" else tn, slowa)
        res[nazwa] = total
        res[nazwa + "_per_1000"] = per1000
        res[nazwa + "_trafienia"] = trafienia
    return res


def podobienstwo_szkieletu(docs):
    pary = []
    for a, b in combinations(docs, 2):
        sa, sb = set(a["szkielet_funkcjonalny"]), set(b["szkielet_funkcjonalny"])
        jac = len(sa & sb) / max(len(sa | sb), 1)
        # zgodnosc kolejnosci sekcji = znormalizowany najdluzszy wspolny podciag
        x, y = a["szkielet_funkcjonalny"], b["szkielet_funkcjonalny"]
        m = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]
        for i in range(len(x)):
            for j in range(len(y)):
                m[i + 1][j + 1] = m[i][j] + 1 if x[i] == y[j] else max(m[i][j + 1], m[i + 1][j])
        # normalizacja po dluzszym szkielecie: dwa teksty sa "z tej samej formy" tylko wtedy,
        # gdy pokrywaja sie prawie cale, a nie gdy krotszy jest podzbiorem dluzszego
        lcs = m[len(x)][len(y)] / max(len(x), len(y), 1)
        pary.append({"a": a["plik"], "b": b["plik"], "jaccard": round(jac, 2),
                     "kolejnosc": round(lcs, 2), "dlugosc_szkieletow": [len(x), len(y)]})
    return pary


def tabela(docs):
    kol = [("plik", 30), ("slowa", 7), ("burst", 7), ("<=5sl%", 8), ("ttr", 7),
           ("konkr/1k", 10), ("1os/1k", 8), ("hipot/1k", 10), ("frazy/1k", 10),
           ("cta/1k", 8), ("link/1k", 8)]
    print("".join(n.ljust(w) for n, w in kol))
    print("-" * sum(w for _, w in kol))
    for d in docs:
        row = [d["plik"][:29], d["slowa"], d["burstiness"], d["zdania_do_5_slow_proc"], d["ttr_okno400"],
               d["konkrety_per_1000"], d["pierwsza_osoba_per_1000"], d["hipotetyczne_per_1000"],
               d["frazy_przejsciowe_per_1000"], d["cta_per_1000"], d["linki_zewnetrzne_per_1000"]]
        print("".join(str(v).ljust(w) for v, (_, w) in zip(row, kol)))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    as_json = "--json" in sys.argv
    if not args:
        print(__doc__)
        sys.exit(1)
    pliki = []
    for a in args:
        if os.path.isdir(a):
            for ext in ("md", "txt", "html", "htm"):
                pliki += sorted(glob.glob(os.path.join(a, "**", "*." + ext), recursive=True))
        else:
            pliki.append(a)
    if not pliki:
        print("Brak plikow do analizy.")
        sys.exit(1)

    docs = [analizuj(p) for p in pliki]
    wynik = {"dokumenty": docs}
    if len(docs) > 1:
        pary = podobienstwo_szkieletu(docs)
        wynik["podobienstwo_szkieletu"] = pary
        wynik["szkielet_sredni_jaccard"] = round(st.mean([p["jaccard"] for p in pary]), 2)
        wynik["szkielet_srednia_kolejnosc"] = round(st.mean([p["kolejnosc"] for p in pary]), 2)

    if as_json:
        print(json.dumps(wynik, ensure_ascii=False, indent=2))
        return

    tabela(docs)
    print()
    for d in docs:
        naj = list(d["frazy_przejsciowe_trafienia"].items())[:5]
        if naj:
            print(d["plik"] + ": frazy -> " + ", ".join(k + " x" + str(v) for k, v in naj))
        if d["wycieki_promptu"]:
            print(d["plik"] + ": MOZLIWY WYCIEK PROMPTU -> " + str(d["wycieki_promptu_trafienia"]))
    if len(docs) > 1:
        print("\nPodobienstwo szkieletu (srednia): jaccard "
              + str(wynik["szkielet_sredni_jaccard"]) + ", kolejnosc "
              + str(wynik["szkielet_srednia_kolejnosc"]))
        for p in sorted(wynik["podobienstwo_szkieletu"], key=lambda x: -x["kolejnosc"])[:10]:
            print("  " + p["a"] + " vs " + p["b"] + ": jaccard " + str(p["jaccard"])
                  + ", kolejnosc " + str(p["kolejnosc"]) + ", dlugosc " + str(p["dlugosc_szkieletow"]))
        print("\nSzkielety funkcjonalne (kolejnosc rozpoznanych typow sekcji):")
        for d in docs:
            print("  " + d["plik"] + ": " + " > ".join(d["szkielet_funkcjonalny"]))
        print("Uwaga: porownanie szkieletow ma sens dopiero przy 4+ rozpoznanych sekcjach na tekst.")


if __name__ == "__main__":
    main()
