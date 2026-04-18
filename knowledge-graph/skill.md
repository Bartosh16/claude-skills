---
name: knowledge-graph
description: Buduje knowledge graph + SERP consensus + query fan-out dla frazy SEO. Trigger gdy użytkownik prosi o knowledge graph, topical map, analizę SERP, query fan-out, mapę encji/podtematów, lub semantyczną mapę tematu. Skill odpalany też jako krok w pipeline /seo-writer przed etapem semantyki — `04-pisanie.md`, `03-outline.md` i `02-semantyka.md` czytają wyjście tego skilla z `./articles/[slug]/knowledge-graph.md`.
---

# Skill: knowledge-graph

## Cel
Zbudować mapę semantyczną tematu SEO na 3 warstwach:
1. **Query Fan-Out** — rozbicie frazy głównej na podzapytania (podtematy, long-taile, PAA, related)
2. **SERP Consensus** — co TOP 10 konkurencji pokrywa wspólnie, a gdzie są luki
3. **Knowledge Graph** — encje (osoby, organizacje, pojęcia, produkty) + relacje między nimi

Wyjście ma być jednym, samowystarczalnym plikiem, z którego kolejne skille (outline, pisanie, semantyka, JSON-LD) korzystają jako źródła prawdy o temacie.

## Kiedy używać

**Uruchom bezpośrednio gdy:**
- użytkownik prosi o "knowledge graph", "topical map", "mapę tematu", "mapę encji"
- użytkownik chce "analizę SERP", "SERP consensus", "co pokrywa konkurencja"
- użytkownik prosi o "query fan-out", "podzapytania", "rozbicie tematu"
- użytkownik chce "semantykę tematu" jako oddzielny deliverable

**Uruchom jako część pipeline'u gdy:**
- odpalony został `/seo-writer` — ten skill jest obowiązkowym krokiem 1.5 (po researchu, przed semantyką)

**Nie uruchamiaj gdy:**
- temat dotyczy tylko JSON-LD / Schema.org dla istniejącego artykułu (wtedy użyj innego flow)
- użytkownik prosi tylko o listę słów kluczowych bez kontekstu semantycznego

## Wejście (zapytaj jeśli brakuje)

1. **Fraza główna** (wymagane) — np. "automatyzacja contentu z n8n"
2. **Frazy poboczne** (opcjonalne) — lista fraz pokrewnych do uwzględnienia
3. **Język** (domyślnie: polski) — knowledge graph będzie w tym języku
4. **Katalog docelowy** (domyślnie: `./articles/[slug]/`) — slug = fraza główna zamieniona na kebab-case bez polskich znaków
5. **Głębokość** (domyślnie: 2) — ile poziomów podzapytań generować (1 = tylko fraza główna + PAA, 2 = + rozwinięcia, 3 = + rozwinięcia rozwinięć)

## Pipeline — 5 kroków

Wykonuj sekwencyjnie. Nie przechodź do kolejnego, dopóki poprzedni nie zapisał danych do pamięci roboczej / pliku tymczasowego.

---

### Krok 1 — Query Fan-Out (generowanie podzapytań)

**Cel:** Z jednej frazy głównej zrobić drzewo ~20–40 podzapytań, które razem definiują pełny zakres tematu.

**Źródła danych:**
1. **Claude reasoning** (off the bat): rozpisz co powinno znaleźć się w artykule dla tej frazy — warianty intencji (informacyjna / transakcyjna / nawigacyjna / komercyjna), podtematy, pytania edge-case
2. **WebSearch** dla frazy głównej → wyciągnij:
   - "People Also Ask" (PAA)
   - "Related searches"
   - Autocomplete suggestions (jeśli widoczne)
3. **WebSearch** dla 3 najbardziej obiecujących podzapytań z kroku 2 → pobierz ich PAA/related (drugi poziom)

**Struktura wyjścia (trzymaj w pamięci, zapis w kroku 5):**
```
Fraza główna: X
├── Podtemat A (hub)
│   ├── A1 (long-tail)
│   ├── A2 (PAA)
│   └── A3 (comparison)
├── Podtemat B (hub)
│   ├── B1
│   └── B2
└── ...
```

**Zasady:**
- Każde podzapytanie oznacz typem: `[hub] / [long-tail] / [PAA] / [related] / [comparison] / [edge-case]`
- Deduplikuj zapytania podobne semantycznie (nie literalnie)
- Odrzuć podzapytania niezwiązane z intencją frazy głównej
- Cel: 20–40 finalnych podzapytań (nie mniej, nie więcej)

---

### Krok 2 — SERP Scraping (pobranie TOP wyników)

**Cel:** Mieć treść TOP 10 dla frazy głównej + TOP 5 dla 3–5 najważniejszych podzapytań. Z tego wyciągniesz encje i consensus.

**Wybór narzędzia scrapowania — kolejność prób:**

```bash
# Sprawdź co jest dostępne lokalnie:
which crawl4ai 2>/dev/null || echo "no_crawl4ai"
which playwright 2>/dev/null || python -c "import playwright" 2>/dev/null && echo "has_playwright" || echo "no_playwright"
```

1. **Priorytet 1: crawl4ai** (jeśli dostępne) — najlepsze dla dynamicznych stron, renderuje JS
2. **Priorytet 2: playwright / puppeteer** (jeśli dostępne) — dobre, wolniejsze, pełen render
3. **Fallback: WebFetch** (zawsze dostępne w Claude Code) — bez JS rendering, ale wystarczające dla większości artykułów

**Procedura:**

Dla frazy głównej:
1. `WebSearch` → zbierz TOP 10 URL
2. Dla każdego URL → pobierz treść (narzędzie z wyboru)
3. Wyciągnij: `<title>`, H1–H3, pierwsze 500 słów, autor (jeśli widoczny), data publikacji (jeśli widoczna)

Dla 3–5 podzapytań z kroku 1 (wybierz te o najwyższej wadze semantycznej — hub'y i mocne long-taile):
1. `WebSearch` → TOP 5 URL każde
2. Pobierz treść — ale krótszy extract (title + H1–H2 + snippet)

**Zasady:**
- Ignoruj URL-e z rozszerzeniami `.pdf`, `.doc`, `.xls`, mediów społecznościowych (facebook.com, twitter.com, linkedin.com/posts)
- Jeśli scraping URL-a zwróci < 200 słów treści — oznacz jako "low-content", ale zostaw
- Max 10 sekund timeout na URL; jeśli padnie, idź dalej
- Nie używaj `Bash` z `curl` — `WebFetch` załatwia sprawę i respektuje robots.txt

---

### Krok 3 — SERP Consensus (analiza TOP 10)

**Cel:** Znaleźć wspólny mianownik tematyczny — co wszystkie/większość TOP 10 pokrywa. To musi pojawić się w artykule, inaczej Google uzna go za niekompletny.

**Dla TOP 10 frazy głównej wyciągnij:**

1. **Wspólne nagłówki** — tematy podejmowane przez ≥ 30% konkurencji (≥ 3/10). Grupuj semantycznie, nie literalnie. Dla każdego podaj: `[nazwa tematu] — pokrywa X/10 artykułów`
2. **Wspólne encje** — osoby, firmy, narzędzia, pojęcia, liczby/statystyki wymienione przez ≥ 3/10 artykułów
3. **Wspólne pytania FAQ** — pytania, które konkurencja zadaje w treści (nie tylko sekcja FAQ, też nagłówki pytające)
4. **Struktura typowa** — jaka jest średnia długość? Ile H2? Ile list? Czy jest FAQ? Czy jest tabela porównawcza?
5. **Luki — czego nikt nie pokrywa** (lub pokrywa słabo) — to kandydaci na unikalne USP artykułu
6. **Intencja dominująca** — informacyjna / komercyjna / transakcyjna / mix (na podstawie tego co serwuje Google)

**Zasady:**
- Nie kopiuj nagłówków 1:1 — grupuj po znaczeniu (np. "Co to jest n8n" i "Czym jest n8n" = jedno)
- Encję uznaj za "wspólną" gdy pojawia się w min. 3 źródłach, a nie 3 razy w jednym
- Dla każdej luki podaj krótkie uzasadnienie: dlaczego to luka i czemu to może być nasza przewaga

---

### Krok 4 — Knowledge Graph (ekstrakcja encji i relacji)

**Cel:** Z treści TOP 10 wyciągnąć encje i relacje wokół **frazy głównej jako central_entity**. Format kompatybilny z backendem Topical Map Builder (source_entity, target_entity, relationship, description, strength).

**Procedura — dwa runy (jak w notatniku Colab):**

**Run 1: central_entity = fraza główna**
Przeanalizuj treści TOP 10 pod kątem: jakie encje łączą się z frazą główną? W jaki sposób?

**Run 2: central_entity = intencja/odbiorca frazy**
Jeśli fraza jest query-like (np. "jak automatyzować content z AI"), zdefiniuj centralną encję jako temat/osobę/narzędzie, którego dotyczy (np. "automatyzacja contentu z AI"). Uruchom ekstrakcję ponownie dla tej encji.

**Zmerguj wyniki** — deduplikuj relacje po kluczu `(source, type, target)`.

**Dozwolone typy relacji** (używaj tylko tych, inaczej traci się kompatybilność z backendem):

| Typ | Znaczenie |
|-----|-----------|
| `is_a` / `type_of` | X jest rodzajem Y (generalizacja) |
| `instance_of` | X jest konkretnym przykładem Y |
| `part_of` | X jest częścią większej całości Y |
| `has_part` | X zawiera w sobie Y |
| `causes` | X powoduje Y |
| `prevents` | X zapobiega Y |
| `enables` | X umożliwia/ułatwia Y |
| `requires` | X wymaga Y |
| `has_attribute` / `has_property` | X ma właściwość Y |
| `uses` | X używa Y do realizacji zadania |
| `produces` | X wytwarza Y |
| `consumes` | X zużywa Y |
| `located_in` | X jest w lokalizacji Y |
| `related_to` | X ma luźny, ale istotny związek z Y (ostateczność) |
| `represents` | X jest symbolem/reprezentacją Y |
| `competes_with` | X konkuruje z Y |
| `integrates_with` | X integruje się z Y (dla narzędzi) |
| `alternative_to` | X jest alternatywą dla Y |

**Dla każdej relacji przypisz `strength` (50–100):**
- **90–100** (Core/Unique): fundamentalne, bezpośrednie, unikalne dla central_entity. Absolutnie obowiązkowe w artykule.
- **80–89** (Strong/Direct): silny, jawny związek z central_entity, istotny. Powinno być w artykule.
- **70–79** (Relevant/Contextual): kontekstowy, wartościowy, ale nie kluczowy. Warto wspomnieć.
- **60–69** (Moderate/Indirect): pośredni związek. Opcjonalnie.
- **50–59** (Peripheral): słaby/pośredni, dla kompletności. Prawdopodobnie pomiń.

**Zasady:**
- Priorytetyzuj relacje gdzie `central_entity` jest source albo target
- Encje i opisy w **języku docelowym** (polski, chyba że inaczej)
- Nazwy encji: krótkie, rzeczownikowe, w mianowniku (np. "n8n", "automatyzacja marketingu", nie "automatyzacja marketingowa")
- Nie wymyślaj encji niewystępujących w źródłach — jeśli potrzeba encji z wiedzy ogólnej, oznacz jako `[inferred]` w properties
- Cel: 15–40 encji, 20–60 relacji

**sameAs (linki do zaufanych źródeł):**
Dla encji, które mają publiczne strony autorytatywne (Wikipedia, Wikidata, GitHub, oficjalne strony producenta), dodaj `sameAs: [url1, url2]` w properties encji. To będzie pożywka dla JSON-LD w późniejszym kroku.

---

### Krok 5 — Pokrycie tematyczne + zapis plików

**Cel:** Na podstawie kroków 1–4 zbudować jednoznaczną listę "co MUSI być w artykule". To czyta kolejny skill (outline/pisanie) i wie dokładnie, co zaadresować.

**Zbuduj sekcję "Pokrycie tematyczne":**
- **MUST-HAVE** (nie pojawi się → artykuł jest niekompletny): wspólne nagłówki ≥ 5/10 + relacje o strength ≥ 90 + top 3 wspólne pytania FAQ
- **SHOULD-HAVE** (dobry artykuł to pokrywa): wspólne nagłówki 3–4/10 + relacje o strength 80–89 + dalsze pytania FAQ
- **UNIQUE-ANGLE** (nasza przewaga): luki z consensus + relacje z run 2, których nie ma konkurencja

**Zapis — ZAWSZE dwa pliki:**

1. **`./articles/[slug]/knowledge-graph.md`** — główny deliverable, format w [output-template.md](output-template.md)
2. **`./articles/[slug]/knowledge-graph.json`** — sidecar dla structured data (JSON-LD, backend TMB, Neo4j import)

**Utwórz katalog jeśli nie istnieje:**
```bash
mkdir -p "./articles/[slug]"
```

Slug: fraza główna → małe litery → spacje na myślniki → polskie znaki usunięte (ą→a, ś→s, itd.). Przykład: "Automatyzacja Contentu" → `automatyzacja-contentu`.

## Format wyjścia

Dokładny template w pliku [output-template.md](output-template.md). W skrócie:

### `knowledge-graph.md` — sekcje
```
# Knowledge Graph: [fraza]

## Metadata
## 1. Query Fan-Out
## 2. SERP Consensus (TOP 10)
## 3. Knowledge Graph — Encje
## 4. Knowledge Graph — Relacje
## 5. Pokrycie tematyczne
## 6. Źródła
```

### `knowledge-graph.json` — struktura
```json
{
  "central_entity": "...",
  "language": "pl",
  "generated_at": "YYYY-MM-DD",
  "query_fanout": {...},
  "serp_consensus": {...},
  "entities": [...],
  "relationships": [...]
}
```

Format relacji w JSON **musi być** zgodny z `from_dict` w `Relationship` (backend TMB) — `source_entity`, `target_entity`, `relationship`, `relationship_description`, `relationship_strength`.

## Integracja z innymi skill'ami

### `/seo-writer`
Pipeline seo-writer wywołuje ten skill jako **krok 1.5** (po `01-research.md`, przed `02-semantyka.md`). Plik `knowledge-graph.md` jest czytany przez:
- `02-semantyka.md` — używa encji i LSI z grafu
- `03-outline.md` — układa strukturę artykułu wokół pokrycia tematycznego (MUST/SHOULD/UNIQUE)
- `04-pisanie.md` — wplata encje i relacje w treść
- `02-semantyka.md` (przy JSON-LD) — używa encji z `sameAs` do Schema.org

### Standalone
Gdy użytkownik uruchamia skill bezpośrednio, zapisz pliki w `./[nazwa-projektu]/knowledge-graph.md` lub `./knowledge-graph/[fraza-slug].md` — dostosuj do kontekstu katalogu roboczego.

## Raportowanie po zakończeniu

Wypisz użytkownikowi:
- Ścieżki utworzonych plików
- Liczba podzapytań w fan-out
- Liczba encji w grafie
- Liczba relacji z rozbiciem po strength (ile 90+, ile 80–89, itd.)
- TOP 5 luk w SERP consensus (największe przewagi do wykorzystania)
- Ile URL-i udało się pobrać z TOP 10 (jeśli < 10, wyjaśnij dlaczego)

## Referencje

- [output-template.md](output-template.md) — dokładny format wyjścia
- [relationship-types.md](relationship-types.md) — pełna lista typów relacji z przykładami
- Backend TMB: `Topical Map Builder/backend/src/domain/entities/knowledge_graph.py` — kontrakt struktury (jeśli kompatybilność z backendem jest potrzebna)
- Notatnik Colab: `Topical Map Builder/Kopia_notatnika_Topical_map_builder.ipynb` — referencja dla promptu ekstrakcji encji (linia ~5548)
