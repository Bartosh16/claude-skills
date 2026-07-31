# claude-skills

Skille do Claude Code, których używam w codziennej pracy nad treściami i SEO. Głównie polski kontekst.

## Co jest w środku

### /humanizacja – pełna przebudowa tekstu AI

Audyt tekstu pod kątem 19 kategorii sygnałów AI (monotonny rytm zdań, bezosobowość, miękka komunikacja, słowa-wytrychy, reguła trzech, atrybucja bez źródła, napuszona ważność, unikanie „jest", karuzela synonimów, fałszywa autentyczność i inne), a potem przepisanie całości tak, żeby brzmiała jak napisana przez człowieka. Sens i długość zostają, styl się zmienia.

Wymaga folderu `_shared` (polska typografia + walidator).

### /ai-search-optimizer

Optymalizacja treści pod AI Search i cytowania przez LLM-y: BLUF, koszt pozyskania informacji, struktura nagłówków, gęstość informacyjna.

### /knowledge-graph

Knowledge graph + konsensus SERP + query fan-out dla frazy SEO. Mapa encji i podtematów przed pisaniem artykułu.

### /od-zera-do-zlecenia

Roadmapa pierwszego zarobku z AI dla początkujących: wywiad, hipotezy nisz, research rynku, plan działania.

### _shared – polska typografia

Wspólne zasady typograficzne (cudzysłowy „", półpauza, kolejność interpunkcji przy cytatach) plus walidator w Pythonie. Skill humanizacja z niego korzysta.

## Instalacja

Skopiuj foldery do katalogu skilli Claude Code:

```
cp -r humanizacja _shared knowledge-graph od-zera-do-zlecenia ~/.claude/skills/
```

Na Windows: `C:\Users\<user>\.claude\skills\`.

## Powiązane

Skille /frazy-ai (chirurgiczne cięcie fraz AI, minimalny diff) i /stylometria (odcisk palca stylu autora) mieszkają w repo [AI-Ninjas](https://github.com/Bartosh16/AI-Ninjas). Zasada kciuka: najpierw /frazy-ai, a jeśli tekst dalej brzmi jak AI – /humanizacja.

## Autor

Daniel Bartosiewicz – [DBest Content](https://dbest-content.com). Skille powstały do codziennej pracy nad treściami, nie jako demo.
