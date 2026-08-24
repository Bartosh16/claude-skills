# /model-biznesowy

Wywiad o kompetencjach, preferencjach, awersjach i ekonomice osobistej, który kończy się gotowym Business Model Canvas (9 bloków), policzonym progiem rentowności, dwoma kanałami dotarcia z progami wyłączenia i planem B z warunkami wyzwalającymi.

## Rdzeń wyróżniający

Przed domknięciem canvasu skill zatrzymuje się i wymusza research – najlepiej żywy, w postaci 8-12 rozmów z ludźmi z segmentu wg zasad Mom Testa (pytaj o przeszłość i wydane pieniądze, nigdy o hipotezy), a nie dane pozbierane z sieci. Ścieżka bez researchu jest dostępna, ale każde założenie o kliencie ląduje w wyniku oznaczone jako `[NIEZWALIDOWANE]`.

Model, który nie spina się arytmetycznie – liczba klientów do progu razy godziny obsługi przekracza dostępny czas – wraca do poprawki zamiast iść dalej jako ładna tabelka.

## Różnica od sąsiednich skilli

`/od-zera-do-zlecenia` prowadzi kogoś bez doświadczenia do pierwszego płatnego zlecenia (nisza + roadmapa nauki). Ten skill jest dla kogoś, kto już coś potrafi i potrzebuje z tego modelu zarabiania.

Czyta output obu sąsiednich skilli, jeśli istnieje – `roadmapa.md` skraca wywiad, `wyroznik-marki.md` daje gotowy wsad do propozycji wartości.

## Zawartość folderu

| Plik | Co to |
|---|---|
| `SKILL.md` | Skill do Claude Code – pełny workflow (9 kroków, od wywiadu po plan 90 dni) |
| `references/canvas-9-blokow.md` | 9 bloków Business Model Canvas – definicje, testy, typowe błędy |
| `references/wzorce-modeli.md` | Katalog 18 wzorców monetyzacji (usługa 1:1, retainer, kurs, SaaS...) |
| `references/protokol-researchu.md` | Jak prowadzić rozmowy z rynkiem wg Mom Testa, gdzie szukać rozmówców |
| `references/kanaly-dotarcia.md` | 17 kanałów dotarcia – koszt, czas do sygnału, progi wyłączenia |
| `references/szablon-modelu.md` | Szablony plików wyjściowych `model-biznesowy.md` i `plan-b.md` |
| `prompt-model-biznesowy.md` | **Wersja standalone bez Claude Code** – jeden prompt do wklejenia w ChatGPT, Claude.ai albo Gemini |

## Instalacja skilla

```
cp -r model-biznesowy ~/.claude/skills/
```

Wymaga folderu `_shared` (walidator typografii) obok, w katalogu skilli.

## Prompt standalone

Jeśli nie masz Claude Code, użyj `prompt-model-biznesowy.md` – ta sama logika sprowadzona do jednego promptu, bez zależności od plików i narzędzi. Skopiuj całość i wklej w dowolny czat.
