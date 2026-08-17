# Bezpieczeństwo – kryteria YMYL według SQRG

Kategoria SQRG: YMYL Health or Safety (2.3) – „każda forma bezpieczeństwa, fizycznego i online”. Obejmuje sytuacje awaryjne, bezpieczeństwo produktów i czynności, cyberbezpieczeństwo konsumenckie, scamy.

## Kiedy ta branża jest YMYL, a kiedy nie

| Werdykt | Przykładowe tematy |
|---|---|
| Wyraźnie YMYL | co robić przy pożarze/trzęsieniu ziemi/tsunami, pierwsza pomoc, bezpieczeństwo dzieci (foteliki, baseny), praca z prądem i gazem, obsługa niebezpiecznych narzędzi, rozpoznawanie scamów i phishingu, hasła i ochrona kont, przemoc domowa – gdzie szukać pomocy |
| Może być YMYL | bezpieczna jazda zimą, dobór kasku, podstawy BHP w biurze, prywatność w social media |
| Raczej nie YMYL | recenzje sprzętu outdoor bez instrukcji ryzykownych czynności, ciekawostki o służbach ratunkowych |

Test dwuosiowy (SQRG 2.3): oś A – temat z natury niebezpieczny (instrukcje czynności grożących krzywdą); oś B – szkoda przy niedokładnej treści (błędna instrukcja ewakuacji). Treści z osi A wymagają ram ochronnych albo nie powinny powstać wcale.

## Wymagane sygnały

- **Zgodność z wytycznymi służb i norm**: procedury awaryjne zgodne z zaleceniami RCB, straży pożarnej, WOPR, producentów; cyberbezpieczeństwo zgodne z CERT Polska. Autorska „lepsza metoda” ewakuacji to czerwona flaga, nie oryginalność.
- **Typ ekspertyzy** (SQRG 3.4.1): instruktaż ratujący zdrowie/życie wymaga ekspertyzy (ratownik, strażak, elektryk z uprawnieniami); relacja „jak przeżyłem powódź” jest OK jako doświadczenie z zastrzeżeniem, że nie zastępuje procedur.
- **Pokazywanie ryzyka, nie tylko metody** (SQRG 4.2): treść o niebezpiecznej czynności ma opisywać zagrożenia, wymagane umiejętności i sprzęt – SQRG wprost chroni treści, które zniechęcają do powtarzania wyczynu.
- **Aktualność**: numery alarmowe, procedury, wersje standardów (np. wytyczne resuscytacji) z datą.
- **Priorytet informacji krytycznej** (SQRG 5.2.2): w treści awaryjnej instrukcja na górze, kontekst niżej – filler przed procedurą to realna szkoda, nie tylko UX.

## Typowe braki

1. Instrukcja czynności niebezpiecznej bez sekcji o ryzyku i wymaganych zabezpieczeniach (SQRG 4.2).
2. Brak numerów alarmowych i progu „kiedy przerwać i wezwać profesjonalistę”.
3. Procedury przeterminowane (stare wytyczne pierwszej pomocy) bez daty (SQRG 18.0).
4. Autor bez kwalifikacji przy treści instruktażowej wysokiego ryzyka (SQRG 5.1).
5. Clickbaitowy tytuł strasząca zagrożeniem, którego treść nie potwierdza (SQRG 5.2).
6. Porada cyberbezpieczeństwa zachęcająca do podania danych „w celu weryfikacji” – wzorzec phishingu (SQRG 4.5.5).

## Czerwone flagi Lowest

- Zachęcanie do niebezpiecznych zachowań lub bagatelizowanie ryzyka (SQRG 4.2) – wzorzec z wytycznych: challenge z kapsułkami do prania (2.3).
- Instrukcje przemocy lub krzywdy łatwe do odtworzenia (4.2) – przy takiej treści odmów proponowania poprawek, zgłoś problem wprost.
- Bagatelizowanie objawów alarmowych i sytuacji wymagających służb.
- Fałszywe „porady bezpieczeństwa” prowadzące do wyłudzenia danych (4.5.5).
- Treść podważająca sens procedur ochronnych niepopartymi teoriami (4.4).

## Przykłady z SQRG

- Trasy ewakuacji przy tsunami = wzorcowy clear YMYL w kategorii „informacja” (2.3).
- „Co robić przy trzęsieniu ziemi” wymienione wprost jako temat osi B (2.3).
- Challenge z kapsułkami do prania (śmiertelne skutki) = clear YMYL; challenge z ostrym sosem = may be (2.3).
- Pokazywanie niebezpiecznych wyczynów w sposób zniechęcający, z opisem ryzyka i sprzętu = NIE harmful (4.2).
- „Zachęcanie do spożywania środków czystości” jako przykład encouraging unsafe behavior (4.2).

## Granice

- Procedury i numery → `/fact-checker`. Głębokie E-E-A-T → `/eeat-analyzer`.
- Treści z osi A (instruktaż krzywdy) nie audytujesz „jak poprawić” – odmawiasz i wyjaśniasz dlaczego.
