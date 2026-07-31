# Polska typografia – źródło prawdy

Single source of truth dla wszystkich skilli pisarskich (humanizacja, seo-writer, seo-article, landing-page-writer, article-reviewer, ai-search-optimizer, eeat-analyzer, fact-checker, insurance-content, kampania, instagram-carousel itd.).

Każdy skill pisarski musi PRZECZYTAĆ ten plik przed zakończeniem i ZASTOSOWAĆ wszystkie reguły. Po edycji uruchom walidator: `python ~/.claude/skills/_shared/walidator-typografii.py [plik]`.

## 1. Cudzysłowy – dokładne kody Unicode

W polskim tekście używaj WYŁĄCZNIE dwóch znaków cudzysłowu:

- **otwierający:** U+201E (`„` DOUBLE LOW-9 QUOTATION MARK)
- **zamykający:** U+201D (`”` RIGHT DOUBLE QUOTATION MARK)

Poprawnie: `„tekst”` – U+201E na początku, U+201D na końcu.

### ZAKAZANE w treści (dozwolone wyłącznie w atrybutach HTML/Markdown typu `id="..."`)

- **U+0022** – ASCII quote (`"`). Łamie typografię.
- **U+201C** – LEFT DOUBLE (`“`). To **angielski OTWIERAJĄCY**, NIGDY polski zamykający.
- **U+0027** – ASCII apostrof (`'`).

### Pułapka modeli LLM

U+201C wygląda prawie identycznie jak U+201D w renderingu fontu, ale to dwa różne znaki. Modele językowe domyślnie mieszają oba. **Zawsze zamykasz cytat znakiem U+201D, nigdy U+201C ani ASCII `"`.**

## 2. Kolejność interpunkcji – PL vs EN (KRYTYCZNE)

W polskim cudzysłów zamykający stoi **PRZED** znakiem interpunkcyjnym. W angielskim odwrotnie. Modele LLM domyślnie idą angielskim torem.

| Znak | PL (poprawny) | EN (BŁĘDNY w polskim) |
|------|---------------|------------------------|
| Kropka | `„tekst”.` | `"text."` |
| Przecinek | `„tekst”,` | `"text,"` |
| Średnik | `„tekst”;` | `"text;"` |
| Dwukropek | `„tekst”:` | `"text:"` |

### Wyjątek dla `?` i `!`

Znaki zapytania i wykrzykniki **zostają WEWNĄTRZ** cudzysłowu, jeśli są częścią cytowanej wypowiedzi:

- Cytowane pytanie: `„Czy to działa?” – zapytał klient.`
- Pytanie ramowe o cytat: `Czy klient powiedział „działa”?`

## 3. Myślniki i dywizy

- **Półpauza** `–` (U+2013) ze spacjami po obu stronach – polski standard dla wtrąceń. `Daniel – ekspert SEO – mówi tak.`
- **Em-dash** `—` (U+2014) – ZAKAZANY. To angielski standard.
- **Dywiz** `-` (U+002D) – tylko w złożeniach słownych. `biało-czerwony`, `e-commerce`. Nigdy jako myślnik.

## 4. Separator poziomy `---`

`---` w treści MD to znak wodny AI. Sekcje rozdziela sam nagłówek (H2, H3). Jedyny dozwolony przypadek: ograniczenie YAML frontmatter (`---` przed i po metadanych pliku).

## 5. Nagłówki

Sentence case – tylko pierwsze słowo z wielkiej litery (oraz nazwy własne). Nigdy Title Case.

- POPRAWNIE: `## Jak pisać o ubezpieczeniach`
- BŁĘDNIE: `## Jak Pisać O Ubezpieczeniach`

## 6. Listy

- Po dwukropku mała litera (chyba że nazwa własna).
- Każdy element pełnym zdaniem – kropka.
- Każdy element równoważnikiem zdania – przecinek lub średnik, ostatni kropka.

## 7. Apostrofy w skrótach angielskich

Apostrof `'` (U+2019, RIGHT SINGLE QUOTATION MARK) w odmianie angielskich skrótów: `n8n'a`, `WordPress'a`, `OpenAI'owi`. Nie ASCII `'`.

## 8. Skrótowce w nawiasach

Wywal nawias, jeśli skrót jest powszechnie znany (AI, SEO, KNF, CTR). Jeśli niezbędny – wprowadź naturalnie w kolejnym zdaniu: `Komisja Nadzoru Finansowego wydała oświadczenie. KNF podkreśla, że...`.

## Programowy check po edycji (obowiązkowy)

Uruchom walidator: `python ~/.claude/skills/_shared/walidator-typografii.py [plik.md]`.

Walidator sprawdza:

1. `n_open == n_close` – sparowane cudzysłowy (U+201E i U+201D)
2. Brak U+201C w treści (poza atrybutami HTML)
3. Brak ASCII `"` w treści (poza atrybutami HTML)
4. Brak `.”`, `,”`, `;”`, `:”` (zła kolejność interpunkcji)
5. Brak em-dash `—` w treści
6. Brak `---` jako separatora między sekcjami (tylko YAML frontmatter)

Jeśli walidator zwróci błędy – popraw i uruchom ponownie. Nie oddawaj tekstu z błędami typografii.
