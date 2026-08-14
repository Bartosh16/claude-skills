# Stylometria {NAZWA_OSOBY_LUB_MARKI} – raport analityczny

> Korpus: {N} tekstów ze źródła {ŹRÓDŁO}.
> Pobrane: {DATA}. Surowe pliki: `{ŚCIEŻKA_DO_KORPUSU}`.
> Charakter materiału: {MÓWIONY/PISANY/MIX}. Tematyka: {TEMATY}.

Raport jest ułożony w trzech warstwach za frameworkiem **mikro → mezo → makro** (StylMaster AI Workbook):

- **Mikro** – słowo, gramatyka, interpunkcja (odcisk palca na poziomie znaku i wyrazu).
- **Mezo** – zdanie, środki stylistyczne, akapit (jak buduje myśl i blok).
- **Makro** – tekst jako całość: ton, kohezja, architektura, idiosynkrazje.

Generowanie „w stylu {OSOBY}" najczęściej sypie się na mezo i makro. Mikro to warunek konieczny, nie wystarczający.

## 1. Rozmiar próby

| Wymiar | Wartość |
|---|---|
| Tekstów | {N} |
| Tokenów (słów) | {TOKENY} |
| Słów unikalnych (types) | {TYPES} |
| Type-Token Ratio (TTR) | {TTR} |
| Zdań | {ZDANIA} |
| Średnia długość zdania | {AVG} słów |
| Mediana długości zdania | {MEDIAN} słów |
| Pytania | {Q} ({Q_PCT}%) |
| Stwierdzenia | {DECL} ({DECL_PCT}%) |
| Słowa ≤4 znaki | {SHORT_PCT}% |
| Słowa 5-8 znaków | {MID_PCT}% |
| Słowa ≥9 znaków | {LONG_PCT}% |
| Zdania ≤5 słów | {VERY_SHORT_N} ({VERY_SHORT_PCT}%) |
| Zdania ≥30 słów | {LONG_N} ({LONG_PCT}%) |

### Metryki warstwowe (z bloku `layers` w `_stats.json`)

| Warstwa | Metryka | Wartość |
|---|---|---|
| MIKRO | Strona bierna (approx) | {PASSIVE_N} ({PASSIVE_1000}/1000 słów) |
| MIKRO | Przecinki / 1000 słów | {COMMA_1000} |
| MIKRO | Półpauza / em-dash / 1000 | {DASH_1000} |
| MIKRO | Wielokropek / wykrzyknik / 1000 | {ELLIPSIS_1000} / {EXCLAIM_1000} |
| MEZO | Zdania złożone | {COMPLEX_PCT}% (proste {SIMPLE_PCT}%) |
| MEZO | Akapity (pliki z >1 akapitem) | {PARA_N} ({MULTI_PARA_FILES}/{FILES}) |
| MEZO | Średni akapit | {PARA_WORDS} słów / {PARA_SENTS} zdań |
| MAKRO | Słowa-przejścia / 1000 słów | {TRANS_1000} (łącznie {TRANS_N}) |

Interpretacja:
- {INTERPRETACJA_TTR — porównaj do typowego mówionego PL ~0,14 / pisanego PL ~0,20}
- {INTERPRETACJA_RYTMU — co mówi różnica średnia/mediana}
- {INTERPRETACJA_PROSTOTY — % słów krótkich}
- {INTERPRETACJA_PYTAŃ — czy autor pyta czy stwierdza}
- {INTERPRETACJA_ZŁOŻONOŚCI — dużo zdań złożonych = wywód; dużo prostych = rytm cięty}

> {JEŚLI KORPUS BEZ AKAPITÓW (mowa/auto-caption): zaznacz, że metryki akapitowe/kohezji liczone są per materiał, nie ze zlepka — patrz ostrzeżenie skryptu.}

## 2. MIKRO — słowo, gramatyka, interpunkcja

### 2.1 Słownictwo i frazy-kotwice (top n-gramów)

#### Bigramy (top 20)
{TABELA bigramów z liczbami}

#### Trigramy i dłuższe (signature)
{TABELA trigramów + 4-gramów + 5-gramów z interpretacją czym są te wzorce}

#### Słowa-naczynia (top content words)
{LISTA 20-30 najczęstszych content words z interpretacją}

**Tematycznie** dominuje: {LISTA TEMATÓW z liczbami}. **Rejestr:** {żargon/potoczność, słowa proste vs złożone, poziom zaawansowania}.

### 2.2 Wzorce gramatyczne

- **Strona czynna vs bierna:** {WNIOSEK z metryki PASSIVE — instrukcja dla modelu, np. „pisz stroną czynną: «pomalował dom», nie «dom został pomalowany»"}
- **Osoba i zaimki:** {czy dominuje „ja"/„my"/„ty"/„on" — z liczbami}
- **Czasy i tryby:** {dominujące czasy, tryb rozkazujący, warunkowy}
- {ŚWIADOME ODEJŚCIA OD NORMY / powtarzalne konstrukcje}

### 2.3 Interpunkcja

{Z metryk MIKRO — które znaki autor lubi, jak buduje nimi rytm i akcent. Wychwyć manierę: np. myślnik-cios, wielokropek zawieszający, brak przecinka przed „że", pytajniki seriami.}

## 3. MEZO — zdanie, środki stylistyczne, akapit

### 3.1 Struktura i długość zdań

- **Proste vs złożone:** {COMPLEX_PCT}% złożonych. {WNIOSEK — wywód czy rytm cięty}
- **Krótkie/długie:** {% ≤5-10 słów i ≥30 słów, co to daje}
- **Otwarcia zdań (pierwsze 2 słowa):**

{TABELA top 15 otwarć}

Wniosek: {czy filler-otwarcia dominują, czy autor wchodzi w meritum}

### 3.2 Środki stylistyczne

{Z próbek — metafory, porównania, analogie, powtórzenia, pytania retoryczne, ironia, hiperbola, anegdota. Wskaż POWTARZALNE, z przykładem z korpusu.}

- **Powtarzalny środek 1:** {NAZWA} – „{PRZYKŁAD}"
- **Powtarzalny środek 2:** {NAZWA} – „{PRZYKŁAD}"

### 3.3 Struktura akapitu i przejścia

- **Budowa bloku:** {dedukcja teza→dowód czy indukcja obraz→wniosek; długość akapitu z metryki}
- **Zdanie wprowadzające:** {jak otwiera akapit}
- **Przejścia:** {czym łączy akapity, czy tnie na sucho}

> Na korpusie mówionym (bez akapitów) opisz to per materiał, nie ze zbiorczych liczb.

## 4. MAKRO — tekst jako całość

### 4.1 Ton i nastrój

{Ogólny rejestr emocjonalny; gdzie i czym zmienia ton; jak buduje nastrój doborem słów/składni/obrazu; ewentualne niespójności.}

### 4.2 Spójność i kohezja

{Z metryki MAKRO (słowa-przejścia: {TRANS_TOP}) — jak spina myśli w całość: przejścia, struktura równoległa, powtórzenie jako spoiwo. Czy trzyma jedną myśl czy skacze.}

### 4.3 Architektura materiału

**Wzorzec otwarcia (hook).** Z pierwszych 3 zdań w {N} materiałach – {LICZBA} typów:

1. **{NAZWA_TYPU_A}:** „{PRZYKŁAD}"
2. **{NAZWA_TYPU_B}:** „{PRZYKŁAD}"
3. **{NAZWA_TYPU_C}:** „{PRZYKŁAD}"
4. **{NAZWA_TYPU_D}:** „{PRZYKŁAD}"

Hook to **{N} zdań, ~{M} słów**. {czy autor przedstawia się od razu, czy po hooku}.

**Wzorzec zakończenia (outro).**
- {ELEMENT_1}
- {ELEMENT_2}
- {ELEMENT_3}

{czy to stała formuła czy luźny szkielet}

**Szkielet całości i proporcje:** {ile „ruchów" ma typowy materiał, gdzie kulminacja, w % ile to setup / mięso / CTA}.

### 4.4 Idiosynkrazje i cechy charakterystyczne

{Niekonwencjonalna pisownia, wymyślone słowa, charakterystyczne frazy-manie, powtarzalne dziwactwa stylistyczne — podpis autora.}

### 4.5 Język figuratywny

{Personifikacja, metonimia, synekdocha; częstotliwość i skuteczność. Jeśli marginalny — zaznacz to.}

### 4.6 Dialog (jeśli dotyczy)

{Jak podaje mowę, interpunkcja dialogu, spójność głosów postaci. Pomiń, jeśli korpus nie zawiera dialogu.}

## 5. Anatomia stylu – {N} sygnatur

Najmocniejsze wzorce z trzech warstw, każda z konkretną liczbą z korpusu:

1. **{NAZWA_SYGNATURY_1}.** {OPIS 2-3 zdania z liczbą}
2. **{NAZWA_SYGNATURY_2}.** {OPIS}
3. **{NAZWA_SYGNATURY_3}.** {OPIS}
4. ...
{minimum 5, optimum 10 sygnatur}

## 6. Czego {OSOBA} NIE robi w {ROZMIAR}

- **Nie używa {X}.** {DOWÓD — 0 lub bardzo mało wystąpień w korpusie}
- **Nie {Y}.** {DOWÓD}
- **Nie {Z}.** {DOWÓD}

{UWAGA O ARTEFAKTACH AUTO-TRANSKRYPCJI jeśli dotyczy — np. „cloud" zamiast „Claude"}

## 7. Charakterystyczne pary stylistyczne (do/avoid)

| Robi (charakter) | Nie robi (poza rejestrem) |
|---|---|
| {PRZYKŁAD_1A} | {PRZYKŁAD_1B} |
| {PRZYKŁAD_2A} | {PRZYKŁAD_2B} |
| {PRZYKŁAD_3A} | {PRZYKŁAD_3B} |
| ... | ... |
{minimum 8 par}

## 8. Mid-roll i sponsoring (jeśli dotyczy)

{OPIS — jak partner się pojawia, w którym momencie, jak wraca pod koniec, jaką ma strukturę}

## 9. Adaptacja per kanał (jeśli korpus to pokrywa)

| Aspekt | {KANAŁ_A} | {KANAŁ_B} |
|---|---|---|
| Relacja | {OPIS} | {OPIS} |
| Otwarcia (makro) | {OPIS} | {OPIS} |
| Rytm zdań (mezo) | {OPIS} | {OPIS} |
| Interpunkcja (mikro) | {OPIS} | {OPIS} |
| CTA | {OPIS} | {OPIS} |
| Język liczb | {OPIS} | {OPIS} |

Wniosek: {KIEDY KORZYSTAĆ Z BAZY, KIEDY ADAPTOWAĆ}

## 10. Pliki źródłowe analizy

- `_stylometry.py` – skrypt liczący (Python 3.10+, stdlib only)
- `_stats.json` – surowe statystyki (w tym blok `layers`: mikro/mezo/makro)
- `_stats-raw.md` – czytelny dump statystyk z próbkami
- `{KORPUS_DIR}/` – surowe teksty
