---
name: stylometria
description: Analizuje styl konkretnej osoby/marki na podstawie dostarczonego korpusu tekstów (transkrypty YT, posty social, artykuły blogowe, e-booki, transkrypcje podcastów, wklejony tekst). Wynik: 3 artefakty — raport analityczny ze statystykami (n-gramy, TTR, długość zdań, otwarcia/zamknięcia), styleguide (frazy-kotwice, rytm, hooki, do/don't, adaptacja per kanał) oraz execution-ready system prompt dla agentów piszących w tym głosie. ZAWSZE używaj tego skilla gdy użytkownik mówi „zrób stylometrię", „przeanalizuj styl X", „styleguide z tych tekstów", „nauczcz mnie pisać jak Y", „system prompt w stylu Z", „głos marki z tych transkryptów", „voice fingerprint", „idiolekt", „stylowy odcisk palca", „klonuj styl pisania", „analiza języka X", „raport stylu autora". Pierwsza akcja skilla to ZAWSZE pytanie „Masz tekst, czy mam znaleźć?" przez AskUserQuestion. Skill działa na pojedynczym pliku, folderze plików, URL do bloga/kanału YT/profilu social albo wklejonym tekście — minimum użyteczne to ~10 000 słów, optimum 30 000+. Dla profili medialnych preferuj 20-40 ostatnich materiałów.
---

# Stylometria – analiza stylu i ekstrakcja głosu

Cel: wyciągnąć z korpusu tekstów (lub transkryptów) charakterystyczny styl konkretnej osoby/marki i przepakować go w 3 użyteczne artefakty — raport analityczny, styleguide do ręcznej pracy i system prompt do automatyzacji.

Skill jest celowo agnostyczny względem domeny — działa tak samo dla twórcy YouTube, autora bloga, klienta Daniela, jak i dla samego Daniela. Wszystko zależy od korpusu, który dostanie na wejściu.

## Workflow

### Krok 0 — pytanie startowe (OBOWIĄZKOWE, ZAWSZE jako pierwsza akcja)

Zanim cokolwiek zaczniesz, zadaj jedno pytanie przez `AskUserQuestion`:

> **Masz tekst, czy mam znaleźć?**

Dwie opcje:

1. **Mam tekst** — użytkownik wskaże plik, folder, URL albo wklei treść.
2. **Znajdź** — użytkownik poda osobę/markę, Ty znajdziesz źródła.

Nie zakładaj odpowiedzi. Nie zaczynaj research'u zanim user nie wybierze. Jedyny wyjątek: jeśli w komendzie startowej użytkownik wyraźnie podał już ścieżkę/URL/tekst (np. „zrób stylometrię z pliku C:\X\Y.txt") — pomijasz Krok 0 i lecisz dalej.

### Krok 1A — branch „Mam tekst"

Dopytaj o lokalizację jeśli nie podana. Akceptowane wejścia:

- **Pojedynczy plik** (.txt, .md, .docx, .pdf, .json3, .vtt). Dla .docx użyj skilla `docx`, dla .pdf — `pdf`. Dla json3/vtt (napisy YT) — zekstrahuj plaintext z eventów.
- **Folder** z plikami tekstowymi — załaduj wszystkie pliki tekstowe rekurencyjnie.
- **URL** — bloga (lista postów), kanału YT (transkrypty filmów), profilu Instagram/Threads/LinkedIn (eksport postów), strony autorskiej. Dla YT skorzystaj z procesu opisanego w „Pozyskiwanie z YouTube" niżej.
- **Wklejony tekst** w wiadomości — zapisz do tymczasowego pliku, idź dalej.

Sprawdź rozmiar:
- < 10 000 słów: ostrzeż użytkownika, że to mało, zapytaj czy idziesz dalej czy dorzuca.
- 10 000-30 000: OK, ostrzeż że n-gramy mogą być zaszumione.
- 30 000+: OK, leć.
- 100 000+: dział, ale powiedz że analiza zajmie chwilę dłużej.

### Krok 1B — branch „Znajdź"

Dopytaj o:
- Imię i nazwisko / nazwę marki.
- Preferowane źródło (kanał YT, blog, social media, e-book, książka).
- Jeśli wiadomo — handle/URL (oszczędza search).

Pipeline znajdowania:

1. **WebSearch** — zlokalizuj profile/kanały tej osoby (YouTube, LinkedIn, blog, Twitter/X, Threads).
2. **Spytaj o preferencję źródła** (jeśli jest wybór).
3. Dla **YouTube** użyj sekcji „Pozyskiwanie z YouTube" niżej.
4. Dla **bloga/strony autorskiej** użyj WebFetch na listingu + iteracyjnie pobierz top 20-30 artykułów.
5. Dla **social** — jeśli user ma eksport (CSV/JSON), poproś o ścieżkę. Bez eksportu social to ślepa uliczka, bo platformy nie dają lekkiego dostępu.

### Krok 2 — pozyskiwanie z YouTube (subrutyna)

Daniel ma lokalną aplikację Next.js do batch-pobierania transkryptów: `C:\Users\danie\Documents\Firmowe\DanielProgramista\YT mass transcript` (port 3000). Apka ma 2 znane bugi (sortuje języki alfabetycznie → trafia w `ab`/abchaski; przerywa pobieranie URL na 429 z jednego języka, gubiąc plik z innego). **Pomijaj apkę, idź yt-dlp bezpośrednio** według wzorca:

1. **Scan kanału:**
   ```powershell
   yt-dlp --flat-playlist --dump-json --no-warnings --playlist-end 50 "https://www.youtube.com/channel/UC..."
   ```
   Jeśli handle ma kropkę (np. `@geekwork.pl`) — używa channel ID, nie handle (handle z kropką rzuca 404).
2. **Wybierz N najnowszych** dłuższych niż 5 min (shorty się nie nadają — za krótki sygnał stylu).
3. **Pobierz transkrypty sekwencyjnie z opóźnieniem** (3-5 s między requestami):
   ```powershell
   yt-dlp --quiet --skip-download --write-subs --write-auto-subs --sub-format json3 --sub-langs pl,pl-PL,en,en-US -o "tmp/%(id)s.%(ext)s" "URL"
   ```
4. **Retry na 429** (Too Many Requests) z backoffem 20-60 s, max 3 próby na język.
5. **Parsuj json3** — wyciągnij `events[].segs[].utf8`, zlej w plaintext.
6. Zapisz do `transkrypcje-yt/01_VIDEOID.txt` z nagłówkiem (tytuł, URL, ID, długość, język) + separator `---` + treść.

Wzorzec skryptu PowerShell — w `references/fetch_youtube.ps1.template` (sąsiednie pliki skilla).

### Krok 3 — przygotowanie korpusu

1. Zlicz wszystkie pliki i znajdź ich łączną długość w słowach.
2. Stwórz folder roboczy `stylometria/` — w folderze klienta jeśli kontekst sugeruje konkretnego klienta, inaczej w folderze, z którego pochodzi korpus.
3. Skopiuj skrypt analizujący jako `_stylometry.py` (template w `references/stylometry.py.template`) i dostosuj ścieżki:
   - `ROOT` = folder roboczy
   - `CORPUS_DIR` = folder z surowymi tekstami (transkrypty / posty / artykuły)
   - `OUT_JSON` = `_stats.json`
   - `OUT_MD` = `_stats-raw.md`

### Krok 4 — analiza Pythonem

Uruchom skrypt. Skrypt liczy:

- Summary: liczba tekstów, tokenów, types, TTR, zdań, średnia/mediana długości zdań, % pytań, dystrybucja długości słów, zdania krótkie/długie.
- **Warstwy mikro/mezo/makro** (blok `layers` w JSON i sekcja w raw MD):
  - **MIKRO** — strona bierna (heurystyka, na 1000 słów) + rozkład interpunkcji na 1000 słów (przecinek, średnik, dwukropek, półpauza, em-dash, wielokropek, wykrzyknik, nawias, dywiz).
  - **MEZO** — % zdań złożonych vs prostych, liczba akapitów, ile plików ma >1 akapit, średni akapit (słowa i zdania), markery porównań.
  - **MAKRO** — słowa-przejścia (kohezja): łączna liczba, na 1000 słów, top 15.
- Top content words (50) — bez stopwordów.
- Top n-gramy: bigramy (60), trigramy (60), 4-gramy (40), 5-gramy (30).
- Top sentence openers (40) — pierwsze 2 słowa zdania.
- Top sentence enders (30) — ostatnie 2 słowa zdania.
- Próbki: 30 bardzo krótkich zdań (≤5 słów), 10 otwarć filmów/postów (pierwsze 3 zdania), 10 zamknięć.
- Signature phrases — szukaj zdefiniowanych przez Ciebie fraz (możesz dostosować listę po obejrzeniu top n-gramów).

Skrypt zapisuje stats JSON i markdown z próbkami.

> **Uwaga o akapitach.** Metryki mezo/makro (akapity, kohezja) mają sens tylko na korpusie z **całymi tekstami**. Auto-caption YT to jeden ciąg bez akapitów — skrypt to wykryje (`files_with_multiple_paragraphs: 0`) i wypisze ostrzeżenie. Wtedy warstwę mezo/makro czytaj **per materiał** w Kroku 5, nie ze zbiorczych liczb, bo zlepek transkryptów zafałszuje strukturę akapitu i łuk całości.

### Krok 5 — analiza jakościowa w trzech warstwach (czytaj próbki)

Framework: **mikro → mezo → makro** (za StylMaster AI Workbook). Mikro klonuje głos na poziomie słowa, mezo — budowę zdania i akapitu, makro — architekturę całego tekstu. Generowanie „w stylu X" najczęściej sypie się na mezo i makro, więc nie odpuszczaj tych warstw, nawet gdy mikro wygląda mocno.

Otwórz `_stats-raw.md` i wyciągnij, warstwa po warstwie:

#### MIKRO — słowo, gramatyka, interpunkcja

- **Słownictwo i dobór słów** — unikalne/powtarzalne słowa i zwroty, żargon vs potoczność, słowa proste vs złożone, poziom zaawansowania. (top content words + n-gramy)
- **Wzorce gramatyczne** — strona czynna vs bierna (metryka MIKRO), dominujące czasy, osoba (ja/my/on/ty), świadome odejścia od normy. Podaj jako **instrukcję** dla modelu (np. „pisz stroną czynną: «pomalował dom», nie «dom został pomalowany»").
- **Interpunkcja** — które znaki autor lubi, jak buduje nimi rytm i akcent (metryka MIKRO na 1000 słów). Wychwyć manierę (np. wielokropek, myślnik-cios, brak przecinków przed „że").

#### MEZO — zdanie, środki stylistyczne, akapit

- **Struktura i długość zdań** — proste/złożone (metryka MEZO), % krótkich (≤5–10) i długich (≥30), różnorodność otwarć, czy tnie na dynamikę czy rozbudowuje.
- **Środki stylistyczne** — metafory, porównania, analogie, powtórzenia, pytania retoryczne, ironia, hiperbola, anegdota. Wskaż powtarzalne (np. „analogia z życia fizycznego przy każdym trudnym pojęciu").
- **Struktura akapitu** — jak buduje pojedynczy blok: dedukcja (teza→dowód) czy indukcja (obraz→wniosek), długość akapitu, zdania wprowadzające, **przejścia między akapitami** (czym łączy, czy tnie na sucho). Na mowie: rób to per materiał.

#### MAKRO — tekst jako całość

- **Ton i nastrój** — formalny/luźny/sarkastyczny/poważny, gdzie zmienia rejestr i czym (dobór słów, składnia, obraz).
- **Spójność i kohezja** — jak spina myśli w całość (metryka MAKRO: słowa-przejścia), struktura równoległa, powtórzenie jako spoiwo, czy trzyma jedną myśl czy skacze.
- **Architektura materiału** — szkielet całości: **wzorzec hooka** (2–4 typy), rozwinięcie, **wzorzec outra**, ile „ruchów" ma typowy tekst, gdzie kulminacja, proporcje setup/mięso/CTA.
- **Idiosynkrazje** — niekonwencjonalna pisownia, wymyślone słowa, charakterystyczne frazy-manie, które są podpisem autora.
- **Język figuratywny** — personifikacja, metonimia, synekdocha; częstotliwość i skuteczność.
- **Dialog** (jeśli dotyczy) — jak podaje mowę, interpunkcja dialogu, spójność głosów postaci.

#### Warstwy wspólne (niezależne od poziomu)

- **Czego NIE robi** — które AI-izmy/korpożargon/kotwice marketingowe są nieobecne (dowód z korpusu: 0 lub prawie 0 wystąpień).
- **Sponsoring / wewnętrzny CTA** — jak buduje mid-roll, jak CTA.

Jeśli korpus pokrywa wiele rejestrów (np. YT + LinkedIn + landing), dodatkowo:
- **Tabela różnic per kanał** — gdzie luźniejszy, gdzie twardszy, co adaptujesz na każdej z trzech warstw.

Zasada z Workbooka: **każdą obserwację zapisuj jako instrukcję dla modelu z przykładem dobrym i złym z korpusu**, nie jako opis akademicki. „Zaczynaj akapit od sceny, potem wniosek: «Klient dzwoni o 23. Dlatego mam wyłączony telefon po 20»" bije „autor stosuje indukcję" za każdym razem.

**Lesson learned — code-switching i wtręty obcojęzyczne.** Polskie auto-caption YT (i większość ASR) zżera krótkie wtręty obcojęzyczne — transkrybuje je fonetycznie po polsku albo gubi. Jeśli korpus pochodzi z auto-caption, a osoba żyje w branży tech / IT / startup, **zapytaj usera off-corpus**, czy autor wtrąca anglicyzmy („what can I say?", „who cares", „doesn't matter", „come on", „by the way", „game changer", „trust me", „big deal", „end of story"). Jeśli tak — dodaj to do styleguide jako sygnaturę rytmiczną z konkretną częstotliwością (typowo 1 wtręt na 100-200 słów mowy, 1 na 300-400 słów pisma LinkedIn, 0-1 na całą formalną formę). Auto-caption NIE jest tu wiarygodnym źródłem — wprost ostrzegaj o tym w raporcie.

### Krok 6 — wygenerowanie 3 artefaktów

Stwórz w `stylometria/`:

#### 6.1 `01-raport-analityczny.md`

Struktura (wzorzec — patrz `references/01-raport.template.md`). Raport jest **pogrupowany w trzy warstwy** (mikro/mezo/makro), żeby wynik dało się wprost przełożyć na styleguide i system prompt:

1. Rozmiar próby i tabela summary (+ tabela metryk warstwowych).
2. **MIKRO** — słownictwo i frazy-kotwice (n-gramy + content words), wzorce gramatyczne (strona czynna/bierna, osoba, czasy), interpunkcja.
3. **MEZO** — struktura i długość zdań (proste/złożone), środki stylistyczne, struktura akapitu i przejścia.
4. **MAKRO** — ton i nastrój, kohezja (słowa-przejścia), architektura materiału (hook → rozwinięcie → outro, proporcje), idiosynkrazje, język figuratywny.
5. Otwarcia i zakończenia zdań — co mówią o stylu.
6. N sygnatur stylu (każda 2-3 zdania z konkretem liczbowym z korpusu).
7. Czego NIE robi w piśmie/mowie.
8. Charakterystyczne pary stylistyczne (robi / nie robi).
9. Mid-roll / sponsoring (jeśli dotyczy).
10. Adaptacja per kanał (jeśli korpus to pokrywa).
11. Pliki źródłowe analizy.

#### 6.2 `02-styleguide.md`

Działający styleguide do ręcznej pracy (wzorzec — `references/02-styleguide.template.md`):

1. 5 reguł rdzennych (niepodlegających dyskusji).
2. **MIKRO** — frazy-kotwice z dawkowaniem (ile na 500 słów, żeby nie brzmieć parodyjnie), gramatyka (strona czynna, osoba), maniery interpunkcyjne.
3. **MEZO** — rytm (długie/krótkie zdania), struktura akapitu (jak buduje blok + przejścia), środki stylistyczne (analogie, powtórzenia, pytania retoryczne).
4. **MAKRO** — architektura tekstu (hook → rozwinięcie → outro z proporcjami), ton i jego zmiany, kohezja.
5. Hook — wzorce z konkretami.
6. Struktura wniosków / list.
7. Storytelling mikroskali (scenka → wniosek).
8. CTA — wzorce per kanał.
9. Sponsoring / mid-roll (jeśli dotyczy).
10. Lista do/don't — szybka ściąga.
11. Obowiązkowe sygnatury w dłuższych formach.
12. Co naprawiać w draftach AI „uciekających" w korpo (tabela typowych błędów + fixów).
13. Adaptacja per kanał.
14. Test końcowy — checklist „czy to brzmi jak X?" (pozycje z każdej z trzech warstw).

#### 6.3 `03-system-prompt.md`

Execution-ready prompty (wzorzec — `references/03-system-prompt.template.md`):

- **Wersja A** — uniwersalna (główny ton bazy).
- **Wersja B** — adaptacja per kanał (jeśli korpus to obejmuje, np. „LinkedIn vs YT" albo „landing vs newsletter").
- Każda wersja pokrywa trzy warstwy: **mikro** (reguły rdzenne, frazy-kotwice, gramatyka, interpunkcja), **mezo** (rytm zdań, budowa akapitu/argumentu, środki stylistyczne), **makro** (architektura tekstu: hook → rozwinięcie → outro, ton, kohezja), plus CTA i test końcowy. Bez bloku makro agent pisze poprawne zdania w złej kompozycji.
- **Few-shot examples** — 2 realne mini-przykłady user→assistant w stylu osoby.
- Sekcja „Jak używać tych promptów" + sekcja „Aktualizacja stylu" (kiedy odświeżyć).

### Krok 7 — surowe dane razem z artefaktami

Skopiuj do `stylometria/`:
- `_stats.json` (output Pythona)
- `_stats-raw.md` (output Pythona)
- `_stylometry.py` (dostosowany skrypt — do reuse'u przy aktualizacji)

Surowy korpus (`transkrypcje-yt/` lub odpowiednik) — zostaw w nadrzędnym folderze (nie kopiuj, żeby nie duplikować).

### Krok 8 — zapis do pamięci projektu (jeśli kontekst)

Jeśli stylometria była robiona dla konkretnego klienta / projektu z istniejącą pamięcią (`~/.claude/projects/.../memory/MEMORY.md`):

1. Stwórz wpis `<nazwa>-stylometria.md` z opisem co jest, gdzie i kluczowymi sygnaturami stylu (3-5 punktów).
2. Dodaj linię do `MEMORY.md`.

Spytaj usera czy dodajesz (krótko, bez naciskania). Jeśli stylometria była dla samego Daniela / DBest Content — domyślnie tak.

### Krok 9 — raport podsumowujący

Na koniec zwróć Danielowi (lub użytkownikowi):

- **Lista plików** ze ścieżkami.
- **Skrócone summary** — rozmiar korpusu, najmocniejsza obserwacja (np. „275× «po prostu»").
- **Top 3 sygnatury stylu** — najsilniejsze odkrycia.
- **Kiedy odświeżyć** — propozycja kadencji (zwykle 6 miesięcy).

## Zasady i ograniczenia

- **Minimum korpusu:** 10 000 słów to próg sensowności. Poniżej rezultaty są zaszumione przez przypadkowe powtórzenia.
- **Jeden styl = jeden rejestr.** Nie mieszaj różnych rejestrów (np. e-mail prywatny + sales letter) bez tablicy adaptacji.
- **Transkrypty YT auto-caption** mają artefakty (np. „cloud" zamiast „Claude" jeśli ktoś mówi „kloud"). Zaznacz to w raporcie żeby agenci nie powielali pomyłki.
- **Nie zmyślaj liczb własnych osoby.** W styleguide i system promptach możesz dawać slot „LICZBA TUTAJ" / [LICZBA Z FIRMY] — agent generujący treści dostanie liczby od użytkownika.
- **Zero przedstawiania się** — jeśli korpus pochodzi z YouTuba, styleguide MA opisywać kiedy i jak osoba się przedstawia, ale system prompt powinien dawać slot „[INTRO/SKIP — decyzja zależy od formatu]".
- **Anti-em-dash:** w wynikowych dokumentach Daniela zawsze używaj półpauzy (–) ze spacjami, nigdy em-dasha (—).

## Output finalny

Folder `stylometria/` zawiera:

```
stylometria/
├── 01-raport-analityczny.md
├── 02-styleguide.md
├── 03-system-prompt.md
├── _stats.json
├── _stats-raw.md
└── _stylometry.py
```

Korpus (`transkrypcje-yt/` lub równoważnik) — w folderze nadrzędnym.

Pamięć projektu — opcjonalnie zaktualizowana.

## References

Pliki szablonowe leżą w `references/` obok SKILL.md:

- `stylometry.py.template` — skrypt analizujący (Python 3.10+, stdlib only).
- `fetch_youtube.ps1.template` — skrypt pobierający transkrypty YT z yt-dlp.
- `01-raport.template.md` — szablon raportu analitycznego.
- `02-styleguide.template.md` — szablon styleguide'u.
- `03-system-prompt.template.md` — szablon system prompta.

Czytaj te szablony przed pisaniem artefaktów — utrzymują spójność dokumentów między różnymi przebiegami skilla.
