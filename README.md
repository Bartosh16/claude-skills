# claude-skills

Skille do Claude Code, których używam w codziennej pracy nad treściami i SEO. Głównie polski kontekst.

## Co jest w środku

### /humanizacja – pełna przebudowa tekstu AI (polski)

Audyt tekstu pod kątem 19 kategorii sygnałów AI (monotonny rytm zdań, bezosobowość, miękka komunikacja, słowa-wytrychy, reguła trzech, atrybucja bez źródła, napuszona ważność, unikanie „jest", karuzela synonimów, fałszywa autentyczność i inne), a potem przepisanie całości tak, żeby brzmiała jak napisana przez człowieka. Sens i długość zostają, styl się zmienia.

Wymaga folderu `_shared` (polska typografia + walidator).

### /humanize – to samo dla angielskiego

Osobny skill, nie tłumaczenie. Warstwa strukturalna jest wspólna z wersją polską, ale leksyka, typografia i interpunkcja już nie: po angielsku em dash nie jest błędem (tylko najsilniejszym sygnałem AI), kropka wchodzi do środka cudzysłowu, a proste cudzysłowy są normą zamiast usterki. 20 kategorii, w tym artefakty czatbota i throat-clearing, których polski model nie generuje.

### /humanizacja-check – walidacja wyniku

Sprawdza deterministycznie, czy humanizacja faktycznie zaszła: porównuje wersję przed i po pod kątem zakresu zmian, liczników sygnałów per kategoria (z wykrywaniem regresji – naprawione jedno, wstawione drugie), rytmu zdań, typografii i wierności wobec oryginału. Werdykt ZWALIDOWANE albo WRACA DO POPRAWEK z listą konkretów. Działa dla polskiego i angielskiego, ma też tryb scan-only dla tekstu bez wersji źródłowej.

Model, który przed chwilą przepisał tekst, jest najgorszym sędzią własnej roboty – ten skill zastępuje „wygląda lepiej" pomiarem.

### /ai-audit – audyt AI slop ze SLOP-score

Odpowiada na jedno pytanie: czy tekst powstał jako czyjaś praca, czy jako produkcja liniowa z master promptu. Ocenia siedem ważonych wymiarów – brak doświadczenia z pierwszej ręki, zerowy information gain, szablonowość struktury, wzorce językowe LLM, ślady maszynowej produkcji, treść podporządkowana lejkowi, równość jakości – i zwraca SLOP-score 0–100, werdykt, dowody z cytatami oraz plan naprawy. Działa na pojedynczym tekście, folderze i na cudzym blogu (audyt konkurencji).

Zaczyna od liczb, nie od wrażenia: `scripts/metryki.py` (Python 3, stdlib) liczy burstiness, gęstość konkretów, pierwszej osoby, ram hipotetycznych i fraz przejściowych. To diagnoza, nie naprawa – naprawia /humanizacja.

### /fact-checker – weryfikacja twierdzeń + poprawiony tekst

Wyławia z tekstu twierdzenia sprawdzalne (liczby, daty, statystyki, cytaty, opisy produktów), weryfikuje każde przez WebSearch na co najmniej 2–3 źródłach i składa raport z werdyktami PRAWDA / FAŁSZ / NIEWERYFIKOWALNE, uzasadnieniem i linkami.

Na końcu nie zostawia samej diagnozy: generuje gotowy tekst po korekcie plus prompt do dalszej edycji. Zasada nadrzędna – każda liczba dostaje atrybucję źródła w nawiasie, a jeżeli źródła pierwotnego nie ma, liczba jedzie z oznaczeniem `[źródło: podać]` zamiast cicho przechodzić do publikacji.

### /ai-search-optimizer

Optymalizacja treści pod AI Search i cytowania przez LLM-y: BLUF, koszt pozyskania informacji, struktura nagłówków, gęstość informacyjna.

### /hooki – 5 hooków do kreacji + matryca wyboru

Dostaje wsad (post, skrypt wideo, reklamę, artykuł, brief) i proponuje 5 hooków – każdy innym, nazwanym mechanizmem psychologicznym, z uzasadnieniem i metryką do obserwacji. Dobór nie jest losowy: wynika z matrycy wyboru na czterech osiach – platforma × poziom świadomości Schwartza × cel treści × temperatura ruchu. Każda propozycja przechodzi check anty-wzorców (engagement bait, clickbait bez payoffu, wypalone formuły, dark patterns).

W references siedzi baza: 22 typy hooków tekstowych, 24 typy hooków wideo, formuły nagłówkowe (Bly, Caples, AIDA/PAS/4U) z danymi empirycznymi, mechanizmy psychologiczne (Loewenstein, Zeigarnik, Berger, Cialdini) oraz benchmarki platform 2025/2026 z progami decyzyjnymi (hook rate, retencja, cutoffy). Self-contained – nie potrzebuje folderu `_shared`.

### /ymyl-analyzer – klasyfikacja i audyt treści YMYL

Analiza tekstu według Search Quality Rater Guidelines Google (edycja wrzesień 2025). Trzy tryby: klasyfikacja (czy temat jest YMYL i w której kategorii – spektrum wyraźnie / może być / raczej nie), audyt (6 wymiarów po 0–5, m.in. odpowiedzialność za treść, zgodność z konsensusem ekspertów, adekwatność typu ekspertyzy; twarda bramka KRYTYCZNE przy flagach Lowest) i poprawki (konkretne zmiany z BEFORE/AFTER). Wykrywa wiele branż naraz i ładuje wytyczne per branża: zdrowie, finanse, ubezpieczenia, prawo, bezpieczeństwo, społeczeństwo/news, e-commerce. Każdy finding ma numer sekcji SQRG.

Wymaga folderu `_shared` (walidator typografii). Dobrze gra w parze z /eeat-analyzer: YMYL mówi, jak ostry próg obowiązuje, E-E-A-T mierzy siłę sygnałów.

### /knowledge-graph

Knowledge graph + konsensus SERP + query fan-out dla frazy SEO. Mapa encji i podtematów przed pisaniem artykułu.

### /model-biznesowy

Wywiad o kompetencjach, preferencjach, awersjach i ekonomice osobistej, który kończy się gotowym Business Model Canvas (9 bloków), policzonym progiem rentowności, dwoma kanałami dotarcia z progami wyłączenia i planem B z warunkami wyzwalającymi.

Rdzeń wyróżniający: przed domknięciem canvasu skill zatrzymuje się i wymusza research – najlepiej żywy, w postaci 8-12 rozmów z ludźmi z segmentu wg zasad Mom Testa, a nie dane pozbierane z sieci. Model, który nie spina się arytmetycznie, wraca do poprawki zamiast iść dalej jako ładna tabelka. Różnica od `/od-zera-do-zlecenia`: tamten prowadzi kogoś bez doświadczenia do pierwszego zlecenia, ten jest dla kogoś, kto już coś potrafi i potrzebuje z tego modelu zarabiania.

Zawiera też wersję standalone bez Claude Code – [`model-biznesowy/prompt-model-biznesowy.md`](model-biznesowy/prompt-model-biznesowy.md), jeden prompt do wklejenia w ChatGPT, Claude.ai albo Gemini. Szczegóły w [`model-biznesowy/README.md`](model-biznesowy/README.md).

Wymaga folderu `_shared` (walidator typografii).

### /od-zera-do-zlecenia

Roadmapa pierwszego zarobku z AI dla początkujących: wywiad, hipotezy nisz, research rynku, plan działania.

### /stylometria – odcisk palca stylu

Analiza stylu konkretnej osoby lub marki z jej tekstów (transkrypty YT, posty, artykuły, e-booki, wklejony tekst) w trzech warstwach – **mikro** (słowo, gramatyka, interpunkcja), **mezo** (zdanie, akapit, środki stylistyczne) i **makro** (ton, kohezja, architektura tekstu) – zapakowana w trzy artefakty: raport analityczny ze statystykami (n-gramy, TTR, rytm zdań, strona bierna, słowa-przejścia), styleguide do ręcznej pracy oraz execution-ready system prompt dla agentów piszących w tym głosie. Działa na pliku, folderze, URL-u albo wklejonym tekście – minimum użyteczne ~10 000 słów, optimum 30 000+.

Self-contained (Python stdlib only) – nie potrzebuje folderu `_shared`. W zestawie templaty skryptu analizującego, pobieraczki transkryptów z YouTube i trzech dokumentów wyjściowych.

### /formularz-apps-script – bezpieczny formularz Google Apps Script

Buduje kompletny formularz jako Google Apps Script Web App: trzy pliki do przeklejenia (Code.gs, Index.html, appsscript.json), backend na Apps Script, dane w Google Sheets, komunikacja przez `google.script.run`. Cały front traktowany jako niezaufany – prawdziwa walidacja siedzi w Code.gs: allowlisty pól zamkniętych, twarda neutralizacja formula injection (`=1+1` ląduje jako tekst, nie jako wynik `2`), limity długości, schema validation, honeypot, LockService, minimalne oauthScopes, sekrety tylko w Script Properties. Kończy własnym code review, werdyktem `SECURITY REVIEW — PASS` i dokładną instrukcją wdrożenia.

Leży w podfolderze [`skills/formularz-apps-script/`](skills/formularz-apps-script/). Obok SKILL.md jest [`PROMPT.md`](skills/formularz-apps-script/PROMPT.md) – ten sam proces jako jeden prompt do wklejenia w czacie, bez skilla.

### _shared – polska typografia

Wspólne zasady typograficzne (cudzysłowy „", półpauza, kolejność interpunkcji przy cytatach) plus walidator w Pythonie. Skill humanizacja z niego korzysta.

## Instalacja

Skopiuj foldery do katalogu skilli Claude Code:

```
cp -r humanizacja humanize humanizacja-check _shared ai-audit fact-checker hooki knowledge-graph model-biznesowy od-zera-do-zlecenia stylometria ymyl-analyzer ~/.claude/skills/
```

Na Windows: `C:\Users\<user>\.claude\skills\`.

## Powiązane

Skill /frazy-ai (chirurgiczne cięcie fraz AI, minimalny diff) mieszka w repo [AI-Ninjas](https://github.com/Bartosh16/AI-Ninjas). Zasada kciuka: najpierw /frazy-ai, a jeśli tekst dalej brzmi jak AI – /humanizacja.

## Autor

Daniel Bartosiewicz – [DBest Content](https://dbest-content.com). Skille powstały do codziennej pracy nad treściami, nie jako demo.
