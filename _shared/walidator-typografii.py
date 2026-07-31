#!/usr/bin/env python3
"""
Walidator typografii polskiej dla skilli pisarskich.

Uruchomienie:
    python walidator-typografii.py <plik.md> [plik2.md ...]

Sprawdza:
    1. Sparowane cudzyslowy (U+201E otwierajacy = U+201D zamykajacy)
    2. Brak U+201C w tresci (poza atrybutami HTML)
    3. Brak ASCII " w tresci (poza atrybutami HTML)
    4. Brak zlej kolejnosci interp: .” ,” ;” :” (powinno byc ”. ”, ”; ”:)
    5. Brak em-dash — w tresci (powinna byc polpauza –)
    6. Brak separatora --- miedzy sekcjami (tylko YAML frontmatter)

Zwraca exit code 0 jesli OK, 1 jesli sa bledy.
"""
import re
import sys
from pathlib import Path

PL_OPEN  = chr(0x201E)  # „
PL_CLOSE = chr(0x201D)  # ”
EN_LEFT  = chr(0x201C)  # “
ASCII_Q  = chr(0x0022)  # "
EM_DASH  = chr(0x2014)  # —


def split_yaml(text):
    """Wydziel YAML frontmatter (jesli istnieje) z body."""
    if text.startswith("---\n") or text.startswith("---\r\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return text[:end + 4], text[end + 4:]
    return "", text


def split_code_blocks(text):
    """Podziel na (typ, fragment) gdzie typ to 'code' (```...```) lub 'text'."""
    parts, pos = [], 0
    for m in re.finditer(r'```.*?```', text, re.DOTALL):
        if m.start() > pos:
            parts.append(('text', text[pos:m.start()]))
        parts.append(('code', m.group(0)))
        pos = m.end()
    if pos < len(text):
        parts.append(('text', text[pos:]))
    return parts


def check_file(path: Path):
    """Zwraca liste komunikatow bledow (pusta = OK)."""
    errors = []
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        return [f"Nie mozna odczytac pliku: {e}"]

    yaml_part, body = split_yaml(text)

    # Usun bloki kodu z analizy
    text_only = "".join(frag for typ, frag in split_code_blocks(body) if typ == "text")
    # Usun atrybuty HTML id="...", class="..." itp.
    text_only = re.sub(r'\b\w+="[^"]*"', '', text_only)
    # Usun linki/url w nawiasach ()
    text_only = re.sub(r'\(https?://[^)]*\)', '', text_only)

    # 1. Sparowane cudzyslowy
    n_open = text_only.count(PL_OPEN)
    n_close = text_only.count(PL_CLOSE)
    if n_open != n_close:
        errors.append(f"Niesparowane cudzyslowy: U+201E={n_open}, U+201D={n_close}")

    # 2. U+201C w tresci
    n_bad1 = text_only.count(EN_LEFT)
    if n_bad1 > 0:
        examples = []
        for m in re.finditer(re.escape(EN_LEFT) + r'[^\n]{0,40}', text_only):
            examples.append(m.group(0)[:50])
            if len(examples) >= 3:
                break
        errors.append(f"U+201C w tresci ({n_bad1}x). Przyklady: {examples}")

    # 3. ASCII " w tresci
    n_bad2 = text_only.count(ASCII_Q)
    if n_bad2 > 0:
        errors.append(f"ASCII quote (U+0022) w tresci ({n_bad2}x)")

    # 4. Zla kolejnosc interp
    bad_dot = re.findall(r'(?<!\.\.)\.' + re.escape(PL_CLOSE), text_only)
    bad_other = re.findall(r'[,;:]' + re.escape(PL_CLOSE), text_only)
    if bad_dot or bad_other:
        examples = []
        for m in re.finditer(r'(?<!\.\.)[\.,;:]' + re.escape(PL_CLOSE), text_only):
            ctx = text_only[max(0, m.start()-15):m.end()+5]
            examples.append(ctx.replace('\n', ' '))
            if len(examples) >= 3:
                break
        errors.append(
            f"Zla kolejnosc interp ({len(bad_dot) + len(bad_other)}x). "
            f"PL: tekst-zamyk-znak (\".), nie tekst-znak-zamyk (.\"). Przyklady: {examples}"
        )

    # 5. Em-dash
    n_em = text_only.count(EM_DASH)
    if n_em > 0:
        errors.append(f"Em-dash (U+2014) w tresci ({n_em}x). Uzyj polpauzy U+2013 (–) ze spacjami.")

    # 6. Separator --- (tylko YAML, nie miedzy sekcjami)
    body_lines = body.split("\n")
    for i, line in enumerate(body_lines):
        if line.strip() == "---":
            errors.append(f"Separator --- w linii {i+1} body (poza YAML frontmatter). Sekcje rozdziela naglowek H2/H3.")
            break

    return errors


def main():
    if len(sys.argv) < 2:
        print("Uzycie: walidator-typografii.py <plik.md> [plik2.md ...]")
        sys.exit(2)

    any_errors = False
    for arg in sys.argv[1:]:
        path = Path(arg)
        if not path.exists():
            print(f"[BRAK PLIKU] {path}")
            any_errors = True
            continue

        errors = check_file(path)
        if errors:
            any_errors = True
            print(f"[FAIL] {path}")
            for e in errors:
                print(f"  - {e}")
        else:
            print(f"[OK]   {path}")

    sys.exit(1 if any_errors else 0)


if __name__ == "__main__":
    main()
