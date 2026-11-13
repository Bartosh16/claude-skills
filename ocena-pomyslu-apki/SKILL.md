---
name: ocena-pomyslu-apki
description: Ocenia pomysł na aplikację (mobilną, webową, SaaS, mikronarzędzie AI) na twardych danych z sieci, nie na entuzjazmie – sprawdza, czy taka apka już istnieje, kto ją wydaje, jakie ma oceny, kiedy dostała ostatnią aktualizację, co użytkownicy wypisują w negatywnych opiniach, gdzie ci ludzie w ogóle rozmawiają o problemie, ile kosztuje obsługa jednego użytkownika i którą luką da się wejść. Kończy werdyktem z kryterium wyjścia. ZAWSZE używaj gdy użytkownik mówi „oceń pomysł na apkę”, „czy taka apka już jest”, „sprawdź konkurencję dla tego pomysłu”, „czy warto to budować”, „zwaliduj mi pomysł na aplikację”, „mam pomysł na apkę, sprawdź to”, „analiza rynku pod apkę”, „czy ten pomysł ma sens”, albo gdy wkleja opis produktu i pyta, czy jest na to miejsce. Używaj też, gdy pyta o lukę rynkową albo unikatowy kąt wejścia dla istniejącej kategorii apek. Wymaga WebSearch i WebFetch.
---

# Ocena pomysłu na apkę

Sprawdzasz pomysł danymi, nie opinią. Wynik ma być na tyle brutalny, żeby użytkownik mógł na jego podstawie zrezygnować.

Podstawa metodyczna: badanie 41 wywiadów z kanału Starter Story (zrobione na kanale YouTube Content i Automatyzacja, 81 apek w katalogu, druga próba ~20 głośnych historii vibe codingu). Wnioski, na których stoi ten skill:

- nikt nie odpada na kodzie, wszyscy odpadają na dystrybucji, koszcie jednostkowym i braku płacącego klienta,
- 4,6 procent nowych aplikacji subskrypcyjnych dochodzi do 10 tys. USD MRR w dwa lata, 17,3 procent do 1 tys. (RevenueCat, State of Subscription Apps 2026),
- data ostatniej aktualizacji jest mocniejszym sygnałem niż ocena, bo ocena to średnia z całej historii i nigdy się nie starzeje,
- konwersja z darmowego na płatne w tym zestawie wyszła od 0,7 do 2,5 procenta.

## Wsad

Potrzebujesz trzech rzeczy. Jeżeli użytkownik nie podał którejś, dopytaj **przed** startem, jednym pytaniem zbiorczym:

1. **Pomysł** – jedno albo dwa zdania: co robi apka, dla kogo, jaki problem znika.
2. **Przewaga** – co użytkownik wie o tej niszy lepiej niż inni, do jakich ludzi ma dziś dostęp i ilu ich jest.
3. **Budżet i czas** – ile pieniędzy, ile godzin tygodniowo.

Bez punktu 2 nie da się zrobić kroku 7, więc nie zaczynaj z pustą przewagą.

## Procedura, siedem kroków

Wykonuj po kolei i pokazuj wynik każdego kroku. Nie skracaj, nie łącz kroków.

### 1. Konkurencja

Znajdź od pięciu do dziesięciu istniejących produktów rozwiązujących ten problem. Źródła: App Store (iTunes Search API działa bez klucza), Google Play, Product Hunt, G2, Capterra, zwykłe wyszukiwanie.

Tabela: nazwa, wydawca, platforma, model cenowy, ocena, liczba ocen, data ostatniej aktualizacji, dni od aktualizacji.

Wydawcę sprawdzaj zawsze. Apka o tej samej nazwie z innym wydawcą to inna apka – w badaniu wyszło to trzy razy.

### 2. Kto jest martwy

Oznacz każdą pozycję z ponad 365 dniami bez aktualizacji oraz każdą z mniej niż 50 ocenami. Podaj, ile pozycji odpada.

To najczęściej pomijany krok i najbardziej wartościowy: rynek pełen konkurentów, z których połowa nie dostała aktualizacji od dwóch lat, jest rynkiem porzuconym, a nie zajętym.

### 3. Co ludzie mówią

Po dziesięć najnowszych negatywnych opinii o trzech największych konkurentach. Wypisz powtarzające się skargi w kolejności od najczęstszej.

Osobno wypisz to, co użytkownicy chwalą – to jest koszt wejścia, czyli minimum, które trzeba dowieźć, żeby w ogóle wejść do gry.

Sprawdź szczególnie skargi na anulowanie subskrypcji, automatyczne odnowienia i odmowy zwrotów. W badaniu to jedyna kategoria poważnych zarzutów i najtańsza rzecz do zrobienia lepiej.

### 4. Luka

Trzy różne kąty wejścia:

- ta sama funkcja, inna grupa odbiorców,
- ta sama grupa, jedna funkcja wycięta wąsko i zrobiona lepiej,
- inny model płatności albo inny moment użycia.

Przy każdym napisz, którą skargę z kroku 3 naprawia. Kąt bez przypisanej skargi wykreśl – to zgadywanie.

### 5. Dowód popytu

Znajdź miejsca, w których ci ludzie już rozmawiają o problemie: wątki na Reddicie, grupy, fora, komentarze pod filmami, zapytania w wyszukiwarce. Linki plus przybliżona wielkość każdego miejsca.

**Ten krok rozstrzyga całą analizę.** Brak takich miejsc to odpowiedź sama w sobie i wtedy powiedz to wprost, zamiast dopisywać pozostałe kroki na pocieszenie.

### 6. Rachunek

Miesięczny koszt obsługi jednego aktywnego użytkownika: wywołania modelu, hosting, przechowywanie danych, prowizja sklepu. Zestaw z cenami konkurentów z kroku 1.

Podaj marżę na użytkownika i liczbę płacących potrzebną do wyjścia na zero. Reguła kciuka z badania: cena ma pokrywać koszt jednostkowy co najmniej trzykrotnie.

### 7. Werdykt

W tej kolejności:

- trzy najmocniejsze argumenty za,
- trzy najmocniejsze argumenty przeciw,
- jeden kanał dystrybucji, który przy przewadze z wsadu ma sens, i dlaczego akurat ten,
- jedno zdanie opisujące apkę na stronie sklepu,
- kryterium wyjścia: ilu płacących po 90 dniach oznacza „ciągnę”, a ile „zamykam”,
- czy pomysł nadaje się do przedsprzedaży, a jeżeli tak, to co da się sprzedać przed premierą (pre-order, founders pack, limitowany dostęp dożywotni) i za ile,
- ocena od 1 do 10 z jednym zdaniem uzasadnienia.

## Zasady

- Przy każdej liczbie źródło i data sprawdzenia.
- Rozdzielaj to, co znalazłeś, od tego, co szacujesz. Szacunki oznaczaj słowem „szacunek”.
- Nie zaokrąglaj w górę.
- Czego nie znalazłeś, opisz jako „nie ustalono”. Nie wypełniaj luk prawdopodobieństwem.
- Jeżeli któryś konkurent jest po prostu lepszy od pomysłu, napisz to wprost.
- Nie proponuj kanału dystrybucji, do którego użytkownik nie ma dziś dostępu. Kanał, który wymaga najpierw zbudowania publiczności, to nie jest plan dystrybucji, tylko odroczenie problemu.

## Wynik

Zapisz raport jako `ocena-[slug-pomyslu].md` w folderze, w którym pracujesz. Struktura raportu odpowiada siedmiu krokom, na końcu werdykt. Bez podsumowania po werdykcie.

Typografia polska wg `~/.claude/skills/_shared/polska-typografia.md`: cudzysłów „ ”, półpauza – ze spacjami, zero em dashy, zero separatorów `---` poza frontmatterem.
