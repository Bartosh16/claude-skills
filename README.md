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

### /fact-checker – weryfikacja twierdzeń + poprawiony tekst

Wyławia z tekstu twierdzenia sprawdzalne (liczby, daty, statystyki, cytaty, opisy produktów), weryfikuje każde przez WebSearch na co najmniej 2–3 źródłach i składa raport z werdyktami PRAWDA / FAŁSZ / NIEWERYFIKOWALNE, uzasadnieniem i linkami.

Na końcu nie zostawia samej diagnozy: generuje gotowy tekst po korekcie plus prompt do dalszej edycji. Zasada nadrzędna – każda liczba dostaje atrybucję źródła w nawiasie, a jeżeli źródła pierwotnego nie ma, liczba jedzie z oznaczeniem `[źródło: podać]` zamiast cicho przechodzić do publikacji.

### /ai-search-optimizer

Optymalizacja treści pod AI Search i cytowania przez LLM-y: BLUF, koszt pozyskania informacji, struktura nagłówków, gęstość informacyjna.

### /ymyl-analyzer – klasyfikacja i audyt treści YMYL

Analiza tekstu według Search Quality Rater Guidelines Google (edycja wrzesień 2025). Trzy tryby: klasyfikacja (czy temat jest YMYL i w której kategorii – spektrum wyraźnie / może być / raczej nie), audyt (6 wymiarów po 0–5, m.in. odpowiedzialność za treść, zgodność z konsensusem ekspertów, adekwatność typu ekspertyzy; twarda bramka KRYTYCZNE przy flagach Lowest) i poprawki (konkretne zmiany z BEFORE/AFTER). Wykrywa wiele branż naraz i ładuje wytyczne per branża: zdrowie, finanse, ubezpieczenia, prawo, bezpieczeństwo, społeczeństwo/news, e-commerce. Każdy finding ma numer sekcji SQRG.

Wymaga folderu `_shared` (walidator typografii). Dobrze gra w parze z /eeat-analyzer: YMYL mówi, jak ostry próg obowiązuje, E-E-A-T mierzy siłę sygnałów.

### /knowledge-graph

Knowledge graph + konsensus SERP + query fan-out dla frazy SEO. Mapa encji i podtematów przed pisaniem artykułu.

### /od-zera-do-zlecenia

Roadmapa pierwszego zarobku z AI dla początkujących: wywiad, hipotezy nisz, research rynku, plan działania.

### /stylometria – odcisk palca stylu

Analiza stylu konkretnej osoby lub marki z jej tekstów (transkrypty YT, posty, artykuły, e-booki, wklejony tekst) w trzech warstwach – **mikro** (słowo, gramatyka, interpunkcja), **mezo** (zdanie, akapit, środki stylistyczne) i **makro** (ton, kohezja, architektura tekstu) – zapakowana w trzy artefakty: raport analityczny ze statystykami (n-gramy, TTR, rytm zdań, strona bierna, słowa-przejścia), styleguide do ręcznej pracy oraz execution-ready system prompt dla agentów piszących w tym głosie. Działa na pliku, folderze, URL-u albo wklejonym tekście – minimum użyteczne ~10 000 słów, optimum 30 000+.

Self-contained (Python stdlib only) – nie potrzebuje folderu `_shared`. W zestawie templaty skryptu analizującego, pobieraczki transkryptów z YouTube i trzech dokumentów wyjściowych.

### _shared – polska typografia

Wspólne zasady typograficzne (cudzysłowy „", półpauza, kolejność interpunkcji przy cytatach) plus walidator w Pythonie. Skill humanizacja z niego korzysta.

## Instalacja

Skopiuj foldery do katalogu skilli Claude Code:

```
cp -r humanizacja humanize humanizacja-check _shared fact-checker knowledge-graph od-zera-do-zlecenia stylometria ymyl-analyzer ~/.claude/skills/
```

Na Windows: `C:\Users\<user>\.claude\skills\`.

## Powiązane

Skill /frazy-ai (chirurgiczne cięcie fraz AI, minimalny diff) mieszka w repo [AI-Ninjas](https://github.com/Bartosh16/AI-Ninjas). Zasada kciuka: najpierw /frazy-ai, a jeśli tekst dalej brzmi jak AI – /humanizacja.

## Autor

Daniel Bartosiewicz – [DBest Content](https://dbest-content.com). Skille powstały do codziennej pracy nad treściami, nie jako demo.
