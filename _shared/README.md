# `_shared/` – wspólne reguły dla skilli pisarskich

Single source of truth dla zasad, które obowiązują we wszystkich skillach pisarskich (humanizacja, seo-writer, seo-article, landing-page-writer, article-reviewer, ai-search-optimizer, eeat-analyzer, fact-checker, insurance-content, kampania, instagram-carousel).

## Pliki

- **`polska-typografia.md`** – pełna specyfikacja zasad typografii polskiej (cudzysłowy, kolejność interpunkcji, myślniki, nagłówki, listy)
- **`walidator-typografii.py`** – programowy check uruchamiany po edycji pliku MD; zwraca exit 1 jeśli wykryje błędy

## Jak używać w skillu pisarskim

W SKILL.md każdego skilla pisarskiego powinna być sekcja:

```markdown
## Polska typografia (obowiązkowa)

Stosuj zasady z `~/.claude/skills/_shared/polska-typografia.md`.
Skondensowane reguły:

- cudzysłowy: U+201E + U+201D (`„tekst”`), nigdy ASCII `"` ani U+201C
- kolejność: `„tekst”.` (kropka PO cudzysłowie), nie `„tekst.”`
- myślniki: półpauza `–` ze spacjami, nigdy em-dash `—`
- separator `---` tylko w YAML frontmatter

**Po edycji uruchom walidator:**
`python ~/.claude/skills/_shared/walidator-typografii.py [twoj-plik.md]`

Jeśli walidator zwróci błędy – popraw i uruchom ponownie. Nie oddawaj tekstu z błędami.
```

## Synchronizacja z Cowork

Skille Cowork siedzą w `AppData/Roaming/Claude/local-agent-mode-sessions/skills-plugin/.../skills/` i są **niezależnymi kopiami**, nie symlinkami. Po zmianie reguł w `~/.claude/skills/` uruchom:

```
python ~/.claude/sync-cowork-skills.py
```

Skrypt skopiuje wszystkie skille (z `_shared` włącznie) z lokalnej lokalizacji do folderu Cowork.

## Zasada DRY

NIE duplikuj pełnych zasad typografii w SKILL.md każdego skilla. Wskaż na `_shared/polska-typografia.md` jako source of truth + skondensowany cheat sheet (4-6 punktów) + wywołanie walidatora. To wystarczy.
