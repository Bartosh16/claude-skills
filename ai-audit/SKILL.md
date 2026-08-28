---
name: ai-audit
description: >
  Audytuje tekst, artykuł, bloga, landing albo cały korpus treści pod kątem sygnałów "AI slop" —
  produkcji liniowej z jednego master promptu: powtarzalny szablon, brak głosu autora i doświadczenia
  z pierwszej ręki, zerowy information gain, wzorce językowe LLM, ślady maszynowej produkcji,
  treść podporządkowana lejkowi sprzedażowemu. Zwraca SLOP-score 0–100, werdykt, dowody z cytatami
  i plan naprawy. ZAWSZE używaj tego skilla gdy użytkownik mówi: "zrób audyt AI", "ai-audit",
  "sprawdź czy to slop", "czy ten blog jest pisany przez AI", "audyt bloga konkurencji",
  "przeanalizuj te artykuły pod kątem AI", "czy ta treść to content farm", "oceń jakość tych tekstów",
  "sprawdź czy nasze artykuły nie wyglądają jak generowane", "audyt treści pod Helpful Content",
  "czy Google to zdegraduje", "sprawdź te URL-e", "przeanalizuj konkurencję contentowo".
  Używaj też proaktywnie, gdy użytkownik wkleja kilka artykułów lub linki do bloga i pyta o ich jakość,
  oryginalność, wiarygodność albo o to, czy widać w nich rękę AI — nawet bez słowa "audyt".
---

# AI Audit — audyt sygnałów AI slop

Ten audyt odpowiada na jedno pytanie: **czy ta treść powstała jako produkcja liniowa, czy jako czyjaś praca?**

Nie jest to detektor autorstwa. Nie orzekasz „to napisał GPT" — bo tego nie da się orzec z tekstu, a klasyfikatory AI mają fatalną skuteczność na polszczyźnie i regularnie palą ludzi za dobrą redakcję. Orzekasz co innego, co da się udowodnić cytatem: **czy tekst wnosi coś, czego nie da się dostać zadając to samo pytanie modelowi**. Tekst może być w 100% wygenerowany i wartościowy (bo autor wsadził do niego swoje dane, decyzje i wnioski). Może być w 100% napisany ręcznie i być slopem (bo jest pustą parafrazą tego, co już jest w indeksie). Rozdzielenie tych dwóch rzeczy jest sednem tego skilla — jeżeli je pomylisz, cały raport jest bezwartościowy.

Konsekwencja praktyczna: każdy zarzut musi mieć **dowód** — cytat, liczbę, nazwę sekcji. Zarzut bez dowodu wypada z raportu. Lepiej oddać krótszy raport z pięcioma twardymi zarzutami niż długi z dwudziestoma wrażeniami.

## Tryby pracy

| Tryb | Kiedy | Co się zmienia |
|---|---|---|
| **Pojedynczy tekst** | jeden artykuł, landing, opis | wymiary 1, 2, 4, 5, 7 pełne; wymiar 3 (szablon) i 6 (kadencja) tylko z zastrzeżeniem „na jednym tekście nierozstrzygalne" |
| **Korpus** (3+ tekstów) | blog, konkurencja, własne archiwum | pełne 7 wymiarów; szablon i kadencja stają się najmocniejszymi dowodami |
| **Audyt zdalny** | użytkownik daje URL-e | pobierz treść (WebFetch), a przy tym zbierz warstwę techniczną: daty publikacji, meta tagi, autor/byline, kanoniczne linki |

Domyślnie celuj w tryb korpusu. Jeden tekst prawie nigdy nie wystarcza do mocnego werdyktu — powtarzalność to najtrudniejszy do podrobienia dowód i zarazem najłatwiejszy do wykazania.

## Przebieg audytu

### Krok 0 — ustal zakres i zbierz materiał

Zapytaj tylko o to, czego naprawdę nie wiesz. Potrzebujesz: co audytujemy (pliki / folder / URL-e), po co (własna kontrola jakości, analiza konkurencji, due diligence przed zakupem serwisu, obrona przed spadkiem w Google) i czy raport ma zawierać plan naprawy, czy tylko diagnozę. Cel zmienia ton: przy własnych tekstach piszesz z myślą o naprawie, przy konkurencji — o luce, którą można wykorzystać.

Przy URL-ach zapisz oprócz treści: datę publikacji, autora, meta description, meta keywords, tytuł. To materiał do wymiaru 6, którego nie da się odtworzyć z samego tekstu.

### Krok 1 — policz, zanim ocenisz

Uruchom skrypt. Daje liczby, których nie da się rzetelnie oszacować okiem, i chroni przed najczęstszym błędem audytu: potwierdzaniem pierwszego wrażenia.

```bash
python ~/.claude/skills/ai-audit/scripts/metryki.py <folder-albo-pliki>
# Windows: python "C:\Users\[twoja-nazwa]\.claude\skills\ai-audit\scripts\metryki.py" <folder-albo-pliki>
```

Co zwraca i jak to czytać:

- **burstiness** (odchylenie / średnia długości zdania) — miara falowania rytmu. Poniżej 0,55 tekst jest podejrzanie równy; ludzka publicystyka trzyma zwykle 0,7–1,2. Bardzo wysoka wartość przy zerze konkretów to nie dowód człowieczeństwa, tylko sztuczka stylistyczna nałożona na pustą treść.
- **konkr/1k** (liczby z jednostką + daty na 1000 słów) — najmocniejszy pojedynczy wskaźnik. Poniżej 3 tekst prawie na pewno nie zawiera własnych danych.
- **1os/1k** — gęstość pierwszej osoby. Zero oznacza tekst bez autora. Uwaga: wysoka wartość nie dowodzi doświadczenia — „moim zdaniem" to nadal nie jest dane.
- **hipot/1k** — gęstość ram hipotetycznych („załóżmy", „wyobraź sobie"). Wysoka wartość przy niskim konkr/1k to podpis pod wymiarem 1: autor nie ma czego opowiedzieć, więc zmyśla scenariusz.
- **frazy/1k** — konstrukcje przejściowe typowe dla wyjścia LLM. Traktuj jako poszlakę, nigdy jako dowód główny.
- **cta/1k**, **link/1k** — proporcja sprzedaży do źródeł.
- **podobieństwo szkieletu** (tryb korpusu) — jaccard i zgodność kolejności sekcji funkcjonalnych. Zgodność kolejności ≥0,7 przy szkieletach 5+ sekcji to twardy dowód na master prompt.

Liczby są wsadem, nie werdyktem. Skrypt nie czyta treści — nie odróżni cytatu z badania od zmyślonej statystyki. Weryfikuj każdą liczbę, na którą się powołasz w raporcie.

### Krok 2 — przeczytaj i zbierz dowody na siedmiu wymiarach

Przeczytaj teksty w całości. Podczas czytania zbieraj cytaty do każdego wymiaru — raport buduje się z cytatów, nie z ocen.

Każdy wymiar oceniasz w skali **0–10**, gdzie 0 = objaw nieobecny, 10 = objaw pełny. Punkty do wyniku końcowego: `ocena × waga / 10`.

#### 1. Brak doświadczenia z pierwszej ręki i głosu autora — waga 22

Najcięższy wymiar, bo to jedyna rzecz, której model nie ma i mieć nie może. Sprawdzasz, czy w tekście jest coś, co mogło powstać wyłącznie dlatego, że ktoś to zrobił.

Szukasz: konkretnych klientów lub projektów (choćby zanonimizowanych), liczb z własnych wdrożeń, zrzutów ekranu, opisów rzeczy, które poszły źle, decyzji z uzasadnieniem („wybraliśmy X, bo Y nas wtopił"), opinii, na którą można się nie zgodzić, bylinu i bio autora.

Sygnały objawu: wszystkie przykłady w trybie hipotetycznym; brak jakiegokolwiek podmiotu wykonującego („można", „warto", „należy" zamiast „zrobiłem"); zero porażek — tylko historie sukcesu bez kosztu; brak autora na stronie; opinie tak wyważone, że nikt nie mógłby się z nimi spierać.

- 0–2: własne dane i rozstrzygnięte case'y, autor podpisany, obecne opinie kontrowersyjne
- 3–5: głos autora jest, ale doświadczenie ilustracyjne, nie dowodowe
- 6–8: pojedyncze „ja" bez pokrycia w faktach, przykłady w większości hipotetyczne
- 9–10: zero autorstwa, zero danych, wszystkie scenariusze zmyślone

#### 2. Zerowy information gain i pętla samoreferencyjna — waga 18

Test jednym zdaniem: **czy czytelnik dostałby to samo, wklejając tytuł artykułu do modelu?** Jeżeli tak — information gain wynosi zero, niezależnie od tego, jak ładnie jest napisane.

Praktyczna procedura: weź 3–5 głównych tez tekstu i sprawdź, czy któraś wymaga wiedzy niedostępnej w wagach modelu — świeżych danych, cen, wyników testu, wiedzy o lokalnym rynku, cudzych wypowiedzi. Jeżeli żadna nie wymaga, to jest parafraza konsensusu.

Osobny objaw, który wyszedł w audycie źródłowym: **pętla samoreferencyjna** — blog o tworzeniu treści z AI, pisany przez AI, sprzedający kurs o tworzeniu treści z AI. Sam temat nie jest winą; winą jest to, że treść nie zawiera dowodu, że autor kiedykolwiek zastosował to, o czym pisze. Wykrywasz to, patrząc na listę tytułów w korpusie: jeżeli wszystkie krążą wokół tego samego rdzenia i żaden nie raportuje wyniku, masz pętlę.

- 0–2: przynajmniej połowa tekstów wnosi dane, których model nie ma
- 3–5: jest oryginalne ujęcie albo zestawienie, ale bez nowych faktów
- 6–8: parafraza konsensusu z pojedynczymi wtrętami własnymi
- 9–10: pełna parafraza, żadna teza nie wymaga wiedzy spoza modelu

#### 3. Powtarzalny szablon strukturalny — waga 15

Tu decyduje skrypt plus twoje oko. Wypisz szkielet funkcjonalny każdego tekstu (hook → TL;DR → spis treści → kroki → prompty → porównanie → scenariusz → błędy → checklista → FAQ → CTA) i połóż je obok siebie.

Uwaga na fałszywy alarm: powtarzalna struktura sama w sobie **nie jest wadą**. Dobre serie poradnikowe i szablony redakcyjne też mają stały układ, a formaty typu FAQ czy Key Takeaways bywają wymogiem SEO. Objawem jest dopiero powtarzalność **mechaniczna** — ta sama sekwencja niezależnie od tego, czy temat jej potrzebuje: checklista przy temacie, który nie ma kroków; FAQ będące parafrazą akapitów wyżej; „porównanie słaby vs lepszy" doklejone tam, gdzie nie ma czego porównywać. Zapytaj przy każdej sekcji: czy ta sekcja istnieje dlatego, że temat jej wymagał, czy dlatego, że była w szablonie?

- 0–2: struktura wynika z tematu, teksty różnią się układem
- 3–5: wspólny szkielet redakcyjny, ale wypełniany po tematowi
- 6–8: stała sekwencja z 1–2 sekcjami widocznie doklejonymi
- 9–10: identyczna sekwencja we wszystkich tekstach, sekcje puste znaczeniowo

#### 4. Wzorce językowe i jednostajność — waga 15

Dwie rzeczy naraz: katalog fraz (patrz `references/wzorce-jezykowe.md`) i **równość jakości**. Ta druga jest ważniejsza i trudniejsza do podrobienia. Ludzki tekst faluje: gdzieś autor się rozpędza, gdzieś skraca, gdzieś wtrąca dygresję albo żart, gdzieś napisze zdanie gorsze, bo mu się spieszyło. Wyjście modelu jest równe — każdy akapit tej samej temperatury.

Szukasz braków, nie obecności: brak dygresji, brak humoru, brak zdania, które można by wyciąć jako „autorskie", brak nierówności rejestru, brak zdań, przy których widać, że ktoś się zawahał.

Frazy z katalogu traktuj jako poszlakę drugiego rzędu. Pojedyncze „warto pamiętać" nic nie znaczy — dopiero gęstość plus regularne rozmieszczenie (jedna konstrukcja przejściowa otwierająca prawie każdy akapit) coś mówi.

- 0–2: wyraźny idiolekt, dygresje, nierówny rytm, autorskie zdania
- 3–5: styl czysty i poprawny, ale bezosobowy; pojedyncze frazy z katalogu
- 6–8: gęstość fraz przejściowych, rytm równy, zero dygresji
- 9–10: styl idealnie płaski, akapity o identycznej budowie, burstiness poniżej 0,55

#### 5. Źródła i weryfikowalność — waga 10

Liczysz twierdzenia wymagające źródła i sprawdzasz, ile ma link, cytat albo nazwany dokument. Osobno oznaczasz **mgliste odwołania** — „według badań", „oficjalne materiały OpenAI", „eksperci wskazują" bez linku. To gorsze niż brak źródła, bo pozoruje weryfikowalność.

Sprawdź też, czy liczby w tekście są prawdziwe — przy najbardziej nośnych odpal wyszukiwanie. Zmyślona statystyka w tekście o zerowym information gain to przejście z kategorii „bezwartościowe" do „szkodliwe" i musi trafić do raportu osobno.

- 0–2: twierdzenia ryzykowne mają źródła, linki prowadzą do konkretów
- 3–5: część twierdzeń bez pokrycia, źródła istnieją ale ogólne
- 6–8: dominują odwołania mgliste, brak linków wychodzących
- 9–10: zero źródeł przy twierdzeniach wymagających źródła albo źródła fałszywe

#### 6. Ślady produkcji maszynowej — waga 12

Twarde poszlaki spoza warstwy stylu — najbardziej przekonujące dla kogoś, kto nie ufa analizie językowej:

- **wycieki promptu i resztki outputu**: sekcje typu „Propozycje linkowania wewnętrznego" widoczne dla czytelnika, `[wstaw]`, „Oto artykuł na temat…", instrukcje meta zostawione w treści, placeholdery;
- **meta jak z pętli**: identyczne meta keywords albo meta description na wszystkich podstronach, tytuły z tym samym schematem liczbowym („10 błędów…", „20 promptów…", „9 sposobów…");
- **kadencja niemożliwa**: policz objętość podzieloną przez czas. 9 tekstów po 10–17 minut czytania w 15 dni przy jednoosobowej redakcji to fizyczna niemożliwość bez masowej generacji. Liczbę podaj wprost — działa mocniej niż każdy argument stylistyczny;
- **brak śladów redakcji**: żadnych aktualizacji, sprostowań, dat modyfikacji, komentarzy.

- 0–2: brak śladów, kadencja realistyczna, meta unikalne
- 3–5: pojedyncza poszlaka (np. schematyczne tytuły)
- 6–8: dwie poszlaki, w tym kadencja albo meta
- 9–10: wyciek promptu w opublikowanym tekście lub trzy poszlaki naraz

#### 7. Treść podporządkowana monetyzacji — waga 8

Sprawdzasz, czy artykuł istnieje po to, żeby odpowiedzieć na pytanie, czy po to, żeby dowieźć kliknięcie. Objawy: 2–3 bloki CTA wstawione w środek treści niezależnie od kontekstu; produkt jako odpowiedź na każdy problem; brak wariantu „w tym przypadku nie kupuj"; architektura fraza SEO → tekst → produkt bez etapu, w którym czytelnik dostaje coś za darmo o realnej wartości.

Sam CTA nie jest wadą — każdy komercyjny blog sprzedaje. Objawem jest **dysproporcja**: gęstość CTA wyższa niż gęstość konkretów.

- 0–2: jedno wezwanie, na końcu, wynikające z treści
- 3–5: CTA obecne w treści, ale tekst broni się bez nich
- 6–8: wiele bloków w środku, produkt jako domyślna odpowiedź
- 9–10: treść jest opakowaniem lejka, po usunięciu CTA nic nie zostaje

### Krok 3 — wypisz sygnały pozytywne

Zrób to zawsze i uczciwie, nawet przy najgorszym wyniku. Trzy powody: raport bez plusów czyta się jak wyrok i traci wiarygodność; odbiorca musi wiedzieć, czego **nie** psuć przy naprawie; a rozróżnienie „bezwartościowe" od „szkodliwe" jest realne i ważne — treść może nie mieć information gain i jednocześnie nie zawierać halucynacji, spamu ani manipulacji.

Typowe pozytywy do sprawdzenia: poprawność językowa, brak halucynacji, sensowna hierarchia nagłówków, użyteczność praktycznych fragmentów, brak spamu linkowego i cloakingu, uczciwe podejście procesowe w pojedynczych tekstach.

### Krok 4 — policz wynik i wystaw werdykt

`SLOP-score = Σ (ocena_wymiaru × waga / 10)`, zakres 0–100. Im wyżej, tym gorzej.

| Wynik | Werdykt | Co to znaczy |
|---|---|---|
| 0–19 | **Treść autorska** | AI mogło uczestniczyć, ale wsad jest ludzki |
| 20–39 | **Wspomagana AI, w normie** | Widać narzędzie, ale treść wnosi wartość |
| 40–59 | **Ryzykowna** | Wartość szczątkowa, realne ryzyko degradacji w Google |
| 60–79 | **AI slop** | Produkcja liniowa, zerowy information gain |
| 80–100 | **Farma treści** | Skala plus brak wartości — profil scaled content abuse |

Do werdyktu dopisz zawsze **konsekwencję**, a nie samą etykietę: ryzyko z Helpful Content i polityki scaled content abuse, luki w E-E-A-T (które litery padają i dlaczego), zerowy information gain jako powód, dla którego treść nie będzie cytowana przez modele w AI Search. Jeżeli oceniasz treść cudzą pod kątem konkurencji — dopisz, gdzie jest luka do zajęcia.

Nie zaokrąglaj werdyktu w górę dla efektu. Jeżeli wynik wychodzi 44, napisz „ryzykowna", nie „slop" — bo od rzetelności tej granicy zależy, czy ktokolwiek potraktuje raport poważnie.

### Krok 5 — napisz raport

Format i przykładowe brzmienie sekcji: `references/szablon-raportu.md`. Trzymaj się go — raport ma być porównywalny między audytami.

Jeżeli użytkownik prosił o plan naprawy, priorytetyzuj według wagi wymiaru razy wykonalność. Prawie zawsze pierwszą pozycją jest wymiar 1, bo bez niego reszta poprawek to kosmetyka: jeden tekst z realnym case'em i własnymi liczbami robi dla wiarygodności serwisu więcej niż dziesięć przeredagowanych.

## Zasady rzetelności

Te reguły istnieją, bo bez nich audyt zamienia się w konfirmację pierwszego wrażenia — a wtedy krzywdzi ludzi, którzy po prostu piszą schludnie.

**Nie orzekaj autorstwa.** Pisz „sygnały produkcji liniowej", „profil treści generowanej masowo", nie „to napisał ChatGPT". Jeżeli użytkownik pyta wprost „czy to AI?", odpowiedz uczciwie: tego nie da się stwierdzić, ale da się stwierdzić, czy treść ma wartość — i to jest pytanie, które realnie ma konsekwencje.

**Nie karz za dobry warsztat.** Poprawna polszczyzna, spójne formatowanie, brak literówek, bogata struktura nagłówków — to sygnały redakcji, nie maszyny. Wiele fraz z katalogu to normalna polszczyzna publicystyczna. Objawem jest gęstość i regularność, nie obecność.

**Uważaj na teksty humanizowane.** Tekst po świadomej humanizacji ma wysokie burstiness, dużo zdań krótkich i wyrazisty rytm, a mimo to może mieć zerowy information gain. Odwrotnie: gęsty raport branżowy z własnymi danymi bywa monotonny rytmicznie. Dlatego wymiary 1 i 2 ważą 40 punktów, a język tylko 15 — rytm jest najłatwiejszy do podrobienia, dane najtrudniejsze.

**Jeden objaw to nie diagnoza.** Werdykt „slop" wymaga objawów w co najmniej trzech wymiarach, w tym obowiązkowo w 1 albo 2. Sam katalog fraz nigdy nie wystarcza.

**Rozdziel „nie ma wartości" od „szkodzi".** Halucynacje, zmyślone statystyki i porady mogące komuś zaszkodzić (zdrowie, finanse, prawo) to osobna kategoria i osobna sekcja raportu. Przy treściach z tych obszarów rozważ dodatkowo `/ymyl-analyzer`.

## Skille pokrewne

Ten audyt **diagnozuje**. Naprawą zajmują się inne:

- `/humanizacja` — przepisanie tekstu, gdy problemem jest wymiar 4 (język i rytm)
- `/frazy-ai` — punktowe wycięcie fraz bez ruszania reszty
- `/eeat-analyzer` — pogłębienie wymiarów 1 i 5 pod sygnały autorytetu Google
- `/ai-search-optimizer` — gdy celem jest cytowalność w AI Search
- `/fact-checker` — weryfikacja twierdzeń wyłapanych w wymiarze 5
- `/ymyl-analyzer` — treści wrażliwe

Jeżeli po audycie użytkownik chce naprawy, zaproponuj konkretny skill zamiast poprawiać tekst w miejscu — inaczej gubisz pipeline i kontrolę jakości.

## Pliki

- `scripts/metryki.py` — liczby: rytm, gęstość konkretów, katalogi fraz, podobieństwo szkieletów w korpusie
- `references/wzorce-jezykowe.md` — katalog konstrukcji LLM w polszczyźnie wraz z kontrprzykładami (kiedy to normalny język)
- `references/szablon-raportu.md` — obowiązkowy układ raportu
