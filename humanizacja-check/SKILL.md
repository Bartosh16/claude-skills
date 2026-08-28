---
name: humanizacja-check
description: Waliduje wynik humanizacji - sprawdza deterministycznie, czy tekst po humanizacji faktycznie się zmienił i czy sygnały AI zniknęły, zamiast polegać na ocenie "wygląda lepiej". Porównuje wersję przed i po (zakres zmian, liczniki sygnałów per kategoria, rytm zdań, typografia, wierność wobec oryginału) i wystawia werdykt ZWALIDOWANE albo WRACA DO POPRAWEK z listą konkretów. ZAWSZE używaj tego skilla gdy użytkownik mówi "sprawdź czy humanizacja zadziałała", "zwaliduj humanizację", "czy te zmiany faktycznie weszły", "porównaj przed i po", "czy tekst dalej brzmi jak AI", "sprawdź output humanizacji", "check po humanizacji", "czy to na pewno shumanizowane" - albo podaje dwa pliki (przed/po) i pyta o różnicę. Używaj też automatycznie po każdym uruchomieniu skilla /humanizacja lub /humanize, zanim oddasz tekst. Działa dla polskiego i angielskiego.
---

# Walidacja humanizacji

Model, który właśnie przepisał tekst, jest najgorszym sędzią własnej roboty. Widzi swoje zmiany i domyślnie uznaje je za skuteczne. Ten skill zastępuje ocenę „wygląda lepiej" pomiarem.

Sprawdza dwie rzeczy, których nie da się ocenić na oko:

1. **Czy zmiany w ogóle zaszły** - czy to przepisanie, czy podmiana kilku przymiotników.
2. **Czy sygnały AI zniknęły** - per kategoria, z licznikiem przed i po, łącznie z regresją (naprawiłeś jedno, wstawiłeś drugie).

Skill jest kontrolny. Nie humanizuje - od tego są `/humanizacja` (polski) i `/humanize` (angielski).

## Workflow

### Krok 1: przygotuj dwa pliki

Walidator porównuje plik źródłowy z wynikiem. Jeśli tekst przed i po jest w kontekście rozmowy, a nie na dysku - zapisz oba do katalogu roboczego (scratchpad), zanim odpalisz skrypt.

Jeśli wersji źródłowej nie ma (użytkownik przyniósł sam wynik i pyta, czy brzmi jak AI) - uruchom tryb scan-only. Wtedy odpada sekcja zakresu zmian i wierności, zostaje skan sygnałów.

### Krok 2: odpal walidator

```bash
python ~/.claude/skills/humanizacja-check/walidator-humanizacji.py --before przed.md --after po.md --lang pl
```

Tryb scan-only (bez wersji źródłowej):

```bash
python ~/.claude/skills/humanizacja-check/walidator-humanizacji.py --after tekst.md --lang pl
```

Dla angielskiego `--lang en`. Skrypt korzysta wyłącznie ze stdlib, exit 0 = ZWALIDOWANE, exit 1 = WRACA DO POPRAWEK.

**Nie streszczaj outputu skryptu z pamięci.** Przeczytaj, co wypisał, i buduj raport na jego liczbach.

### Krok 3: warstwa jakościowa

Skrypt liczy wzorce. Nie umie ocenić sensu. Przejdź te sześć punktów sam, czytając oba teksty:

1. **Wierność faktów.** Czy liczby, nazwiska, daty i twierdzenia z oryginału przetrwały bez zmian? Walidator sygnalizuje nowe liczby, ale nie wie, czy „30%" zamienione na „jedną trzecią" to przeformułowanie, czy przekłamanie.
2. **Czy nic nie dorosło.** Humanizacja tnie i przebudowuje. Jeśli tekst po urósł o akapit z nową treścią, to nie humanizacja, tylko dopisywanie.
3. **Rejestr.** Czy formalny dokument nie zjechał w kolokwializmy? Humanizacja nie równa się rozluźnieniu. Raport ma zostać raportem.
4. **Czy naprawa jest realna.** Podmiana „kluczowy" na „istotny" to nie naprawa wzorca, tylko ominięcie listy. Sprawdź, czy zdanie mówi teraz coś konkretnego, czy dalej pompuje ważność innym słowem.
5. **Nowe AI-izmy spoza list.** Modele naprawiają jeden wzorzec, wstawiając drugi: w miejsce „nie tylko X, ale Y" wchodzi „to nie X, to Y", w miejsce wyciętej triady wchodzi zdanie-aforyzm. Czytaj wynik pod kątem katalogu z `/humanizacja` (19 kategorii) i `/humanize` (20 kategorii), nie tylko pod kątem tego, co skrypt umie zmierzyć.
6. **Głos.** Czy po pierwszym akapicie wiadomo, kto pisze? Czy jest tu coś, czego model by nie wygenerował - własna obserwacja, konkretna liczba, anegdota?

### Krok 4: werdykt

Werdykt to koniunkcja: skrypt musi dać exit 0 **i** sześć punktów jakościowych musi przejść. Jedno bez drugiego nie wystarcza - tekst może mieć czyste liczniki i zerową treść.

Przy WRACA DO POPRAWEK: wypisz ponumerowaną listę tego, co konkretnie ma zostać naprawione (kategoria + cytat + oczekiwana zmiana) i przekaż ją z powrotem do `/humanizacja` albo `/humanize`. Nie poprawiaj tekstu w tym skillu - walidator, który sam nanosi poprawki, przestaje być niezależną kontrolą.

Po poprawkach uruchom walidację ponownie na nowej parze plików.

## Co mierzy skrypt

| Sekcja | Co sprawdza | Kiedy blokuje |
|---|---|---|
| Zakres zmian | podobieństwo tekstów, odsetek zdań przepisanych bajt w bajt | podobieństwo ≥ 0,92 albo ≥ 50% zdań nietkniętych |
| Sygnały AI | licznik trafień per kategoria, przed i po | kategoria twarda nadal obecna albo licznik wzrósł (regresja) |
| Rytm zdań | średnia długość i współczynnik zmienności | zmienność < 0,25 (metronom) |
| Typografia | PL: em dash, cudzysłowy, kolejność interpunkcji, separatory. EN: limit em dashy, curly quotes | dowolne trafienie w kategorii twardej |
| Wierność | delta długości, nowe liczby nieobecne w oryginale | delta > 35% |

**Wyjątek od wierności - wsad autorski.** `/humanizacja` może wpleść do tekstu materiał dostarczony przez autora (case, liczby, opinie - krok 1.5 tamtego skilla) i deklaruje to w notce redaktorskiej. Nowe liczby i przyrost długości pokryte tą deklaracją to celowa rozbudowa, nie naruszenie wierności - odnotuj je w raporcie jako wsad autorski i nie blokuj werdyktu. Nowe fakty BEZ deklaracji w notce traktuj po staremu: podejrzenie halucynacji, blokada.

**Kategorie twarde** (mają zniknąć w całości, nie zmaleć): wata słowna, atrybucja bez źródła, fałszywa autentyczność, coachingowy bełkot, otwarcia „jako [rola]", generyczne zakończenia, triady anaforyczne, konstrukcje „nie tylko X, ale Y". Po angielsku dochodzą artefakty czatbota i throat-clearing.

**Kategorie miękkie** (mają zmaleć, nie muszą wyzerować): słownik AI, miękka komunikacja, unikanie „jest", bezosobowość, imiesłowy doklejone, nadużycie „bez". Wzrost licznika w którejkolwiek to regresja i blokada.

**Heurystyki** (tylko do wglądu, bez wpływu na werdykt): reguła trzech. Wzorzec „X, Y i Z" łapie też zwykłe wyliczenia, więc liczba służy do porównania przed i po, nie do wyroku.

## Czego skrypt nie zmierzy

Regex nie wie, czy tekst mówi prawdę i czy ma sens. Poza zasięgiem pomiaru zostają: wierność faktów, dodana treść, rejestr, jakość konkretów, obecność głosu i AI-izmy, których nie ma na listach. To jest dokładnie zawartość kroku 3 i dlatego kroku 3 nie wolno pominąć, nawet gdy skrypt świeci na zielono.

Odwrotna pułapka też istnieje: skrypt potrafi wyrzucić błąd na tekście, który jest dobry. Zdanie „bez wyjątku" trafi do licznika „nadużycie bez", cytat z cudzej wypowiedzi może zawierać watę słowną. Jeśli trafienie jest uzasadnione, napisz to w raporcie i uzasadnij, zamiast kaleczyć tekst pod walidator.

## Format raportu

```
## Walidacja humanizacji

### Pomiar
[output walidatora: zakres zmian, tabela sygnałów, rytm, typografia, wierność]

### Warstwa jakościowa
1. Wierność faktów - [ocena]
2. Brak dodanej treści - [ocena]
3. Rejestr - [ocena]
4. Realność napraw - [ocena]
5. Nowe AI-izmy - [ocena]
6. Głos - [ocena]

### Werdykt: ZWALIDOWANE | WRACA DO POPRAWEK

[Jeśli WRACA DO POPRAWEK - ponumerowana lista:]
1. [kategoria] „cytat" - [co ma się stać]
2. [kategoria] „cytat" - [co ma się stać]
```

## Powiązane skille

- `/humanizacja` - pełna przebudowa polskiego tekstu, 19 kategorii sygnałów,
- `/humanize` - to samo dla angielskiego, 20 kategorii,
- `/frazy-ai` - chirurgiczne cięcie fraz przy minimalnym diffie (gdy tekst nie wymaga przebudowy).
