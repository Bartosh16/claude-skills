# Szablon raportu ai-audit

Raport ma być czytelny dla kogoś, kto nie zna metodyki. Prowadź go od werdyktu do dowodów, nie odwrotnie — odbiorca chce najpierw wiedzieć, jak jest źle, potem dlaczego tak twierdzisz.

Zasada nadrzędna dla każdej sekcji: **żadnego zarzutu bez cytatu albo liczby**. Cytat podawaj dosłownie, w cudzysłowie, z nazwą pliku lub URL-a.

Raport zapisuj do pliku (`audyt-ai-[nazwa]-[RRRR-MM].md`) w folderze wskazanym przez użytkownika. Przy audycie własnych treści DBest Content miejscem domyślnym jest `09-BADANIA/`, przy analizie konkurencji też `09-BADANIA/` — nigdy root workspace'u.

## Układ

````markdown
# Audyt AI: [nazwa serwisu / zbioru]

**Zakres:** [ile tekstów, jakie, z jakiego okresu]
**Data audytu:** [RRRR-MM-DD]
**Tryb:** pojedynczy tekst / korpus / audyt zdalny

## Werdykt

**SLOP-score: [X]/100 — [etykieta werdyktu]**

[Dwa–trzy zdania streszczające, czym ta treść jest. Bez owijania, bez listy.
Wzór brzmienia: "Blog wygląda na produkcję liniową prowadzoną z jednego szablonu.
Artykuły są poprawne językowo i merytorycznie nieszkodliwe, ale nie zawierają
ani jednej informacji, której czytelnik nie dostałby zadając to samo pytanie modelowi."]

### Punktacja wymiarów

| Wymiar | Ocena 0–10 | Waga | Punkty | Dowód główny |
|---|---|---|---|---|
| Doświadczenie i głos autora | | 22 | | |
| Information gain | | 18 | | |
| Szablon strukturalny | | 15 | | |
| Język i jednostajność | | 15 | | |
| Źródła i weryfikowalność | | 10 | | |
| Ślady produkcji maszynowej | | 12 | | |
| Podporządkowanie monetyzacji | | 8 | | |
| **Razem** | | **100** | **[X]** | |

## Materiał

| # | Tekst / URL | Objętość | Data | Autor |
|---|---|---|---|---|

## Metryki

[Tabela ze skryptu. Pod nią 3–5 zdań interpretacji — które liczby są tu kluczowe i dlaczego.
Nie przepisuj tabeli słowami.]

## Dowody

### 1. Brak doświadczenia z pierwszej ręki

[Cytaty. Dla każdego: skąd pochodzi i co dowodzi. Wypisz osobno wszystkie
scenariusze hipotetyczne i zestaw je z liczbą realnych case'ów.]

### 2. Information gain

[Wypisz 3–5 głównych tez korpusu i przy każdej zaznacz, czy wymaga wiedzy
spoza modelu. Jeżeli występuje pętla samoreferencyjna — pokaż listę tytułów.]

### 3. Szablon strukturalny

[Szkielety obok siebie. Wskaż konkretne sekcje, których temat nie potrzebował,
i uzasadnij, dlaczego uważasz je za doklejone.]

### 4. Język i jednostajność

[Frazy z gęstością na 1000 słów. Potem — ważniejsze — lista sygnałów braku:
czego w tym tekście nie ma.]

### 5. Źródła

[Twierdzenia wymagające źródła vs twierdzenia mające źródło. Osobno odwołania mgliste.
Jeżeli weryfikowałeś liczby — wynik weryfikacji.]

### 6. Ślady produkcji maszynowej

[Wycieki, meta, kadencja z wyliczeniem. Kadencję podaj rachunkiem:
"N tekstów × M minut czytania ÷ K dni".]

### 7. Monetyzacja

[Liczba i rozmieszczenie CTA. Test: co zostaje po ich usunięciu.]

## Sygnały pozytywne

[Uczciwa lista. Zawsze niepusta, chyba że naprawdę nie ma czego wpisać —
wtedy napisz to wprost, zamiast wymyślać.]

## Konsekwencje

- **Google / Helpful Content i scaled content abuse:** [konkretnie, z uzasadnieniem]
- **E-E-A-T:** [które litery padają i przez co]
- **AI Search:** [czy jest tu cokolwiek cytowalnego]
- **Biznes:** [co to znaczy dla zaufania, konwersji, sprzedaży]

## Plan naprawy

[Tylko jeżeli zamawiający tego chciał. Priorytet = waga wymiaru × wykonalność.
Każda pozycja: co zrobić, na czym, jaki efekt, jakim skillem.]

| Priorytet | Działanie | Zakres | Efekt | Narzędzie |
|---|---|---|---|---|
````

## Uwagi redakcyjne

**Ton.** Rzeczowy i chłodny. Bez ironii pod adresem autorów — audyt ocenia treść, nie ludzi. Konkret zamiast przymiotnika: „zero liczb w trzech tekstach" zamiast „słaby merytorycznie".

**Formatowanie.** Polski cudzysłów „ ", półpauza – ze spacjami, zero em dashy, zero separatorów `---` między sekcjami.

**Skala raportu.** Jeden tekst: 400–700 słów. Korpus do 10 tekstów: 900–1500. Większy korpus: 1500–2500 plus załącznik z tabelą per tekst. Dłuższy raport nie jest lepszy — jest trudniejszy do wykorzystania.

**Czego nie robić.** Nie pisz „to napisało AI". Nie podawaj procentów prawdopodobieństwa autorstwa — to liczby bez pokrycia. Nie kończ raportu ogólnym akapitem podsumowującym; werdykt jest na górze i nie potrzebuje powtórki.
