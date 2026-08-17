# Finanse – kryteria YMYL według SQRG

Kategoria SQRG: YMYL Financial Security (2.3) – tematy mogące uderzyć w zdolność człowieka do utrzymania siebie i rodziny. Obejmuje inwestowanie, kredyty i pożyczki, podatki, emerytury, oszczędzanie, kryptowaluty, upadłość konsumencką. Ubezpieczenia mają osobny plik (`ubezpieczenia.md`).

## Kiedy ta branża jest YMYL, a kiedy nie

| Werdykt | Przykładowe tematy |
|---|---|
| Wyraźnie YMYL | jak i w co inwestować, wybór kredytu hipotecznego, instrukcje podatkowe (PIT, ulgi), planowanie emerytalne, konsolidacja długów, kryptowaluty jako inwestycja, upadłość konsumencka |
| Może być YMYL | ogólna edukacja ekonomiczna (co to inflacja), budżet domowy i oszczędzanie na co dzień, porównania kont bankowych bez rekomendacji, historia rynków |
| Raczej nie YMYL | ciekawostki ekonomiczne, biografie inwestorów, felietony o gospodarce bez porad |

Test: czy czytelnik może na podstawie tekstu podjąć decyzję angażującą jego pieniądze? Jeśli tak – wyraźnie YMYL.

## Wymagane sygnały

- **Typ ekspertyzy** (SQRG 3.4.1): porada finansowa (ile odkładać, w co inwestować, który kredyt) wymaga ekspertyzy; recenzja usługi finansowej z pierwszej ręki jest OK jako doświadczenie, dopóki nie przechodzi w doradztwo.
- **Aktualność danych** (SQRG 18.0): stopy procentowe, progi podatkowe, ulgi, limity zmieniają się co najmniej raz w roku. Data przy każdej liczbie wrażliwej na czas; rok podatkowy nazwany wprost.
- **Źródła instytucjonalne**: NBP, KNF, Ministerstwo Finansów, GUS, ustawy z Dz.U. – nie „eksperci twierdzą”.
- **Rozdzielenie informacji od rekomendacji**: opis produktu finansowego vs „weź ten produkt”. Rekomendacja wymaga wskazania, dla kogo jest, i zastrzeżenia o ryzyku.
- **Transparentność zarobku** (SQRG 3.4 – konflikt interesów): linki afiliacyjne, prowizje i współprace oznaczone; ranking kredytów bez ujawnienia prowizji to konflikt interesów podważający Trust.
- **Odpowiedzialność** (SQRG 4.5.1, 5.5): autor lub odpowiedzialna organizacja z kontaktem; witryna przyjmująca dane do wniosków finansowych musi mieć rozbudowaną obsługę klienta.

## Typowe braki

1. Kwoty i progi bez roku, którego dotyczą – tekst wygląda aktualnie, a cytuje stare limity (SQRG 18.0, 5.2).
2. Porada inwestycyjna bez słowa o ryzyku i bez profilu odbiorcy.
3. Ranking produktów finansowych bez ujawnienia afiliacji (SQRG 3.4).
4. „Ekspert finansowy” bez nazwiska, kwalifikacji i śladu w sieci (SQRG 5.6).
5. Mieszanie edukacji z ukrytą sprzedażą produktu jednej instytucji.
6. Brak rozróżnienia: informacja o produkcie vs porada dopasowana do sytuacji czytelnika (SQRG 3.4.1).
7. Kopiowanie tabel oprocentowania z porównywarek bez własnej weryfikacji i daty (SQRG 4.6.6/5.2.1).

## Czerwone flagi Lowest

- Obietnice zysku bez ryzyka, „gwarantowane” stopy zwrotu – twierdzenia sprzeczne z konsensusem, np. „loteria to sposób oszczędzania na emeryturę” (SQRG 4.4).
- Namawianie do decyzji finansowych pod presją czasu w treści udającej poradnik (4.5.3 – zwodniczy cel).
- Piramidy, schematy HYIP, „systemy” na pewny zarobek (4.5.5 – podejrzenie scamu).
- Strona zbierająca dane finansowe (PESEL, numery kont) bez informacji o administratorze (4.5.1).
- Fałszywe wyniki inwestycyjne, zmyślone testimoniale zysków (4.5.3).

## Przykłady z SQRG

- „Jak inwestować pieniądze” jako wzorcowy temat osi B – szkoda przy niedokładności (2.3).
- Podatki: humorystyczne wideo o frustracji OK, instrukcja wypełniania formularzy tylko od ekspertów (3.4.1).
- Emerytura: recenzje usług oszczędzania z pierwszej ręki OK, „ile odkładać i w co inwestować” tylko od ekspertów (3.4.1).
- „Loteria jako gwarantowany sposób na emeryturę” = harmfully misleading (4.4).
- annualcreditreport.com: reputacja potwierdzona niezależnie (jedyne federalnie umocowane źródło darmowych raportów) jako wzór pozytywnej reputacji w finansach (3.3.3).
- Oszust finansowy z dużym doświadczeniem = i tak niskie E-E-A-T, bo Trust zerowy (3.4).

## Granice

- Skill nie orzeka o zgodności z regulacjami (doradztwo inwestycyjne wg MiFID II, licencje KNF) – zaznacz ryzyko i odeślij do prawnika.
- Liczby i stawki → `/fact-checker`. Głębokie E-E-A-T → `/eeat-analyzer`.
