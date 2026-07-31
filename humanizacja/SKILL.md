---
name: humanizacja
description: Humanizuje polskie teksty AI - identyfikuje sygnały "stylu AI" (GPT-izmy, frazy-wytrychy, miękka komunikacja, bezosobowość, monotonny rytm zdań, błędna interpunkcja) i przepisuje tekst tak, by brzmiał jak napisany przez człowieka. ZAWSZE używaj tego skilla gdy użytkownik mówi "shumanizuj", "humanizuj", "ten tekst brzmi sztucznie", "to wygląda jak ChatGPT", "popraw styl AI", "wyczyść AI-izmy", "wyczyść GPT-izmy", "przepisz po ludzku", "anti-AI", "to brzmi jak robot", "to jest za bardzo encyklopedyczne", "to jest sztywne", "popraw na naturalny język", "ludzki ton", "naturalny tekst" - albo wkleja tekst i pyta czy brzmi jak AI, czy widać że to wygenerowane, jak go poprawić. Używaj też proaktywnie, gdy widzisz że user wkleił tekst i prosi o "ulepszenie" lub "polerkę" stylu - tekst AI w 95% przypadków potrzebuje humanizacji.
---

# Humanizacja tekstu AI

Celem jest przerobić wygenerowany tekst tak, żeby brzmiał jak napisany przez człowieka z opinią, doświadczeniem i charakterem - nie jak skompilowany przez algorytm.

**Ten skill jest do tekstów POLSKICH.** Jeśli tekst jest po angielsku, użyj skilla `/humanize` - warstwa strukturalna jest wspólna, ale słownictwo, typografia i obsługa fleksji już nie (w angielskim em dash nie jest błędem, kropka wchodzi do środka cudzysłowu, a proste cudzysłowy są normą, nie usterką).

Po humanizacji zweryfikuj wynik skillem `/humanizacja-check` - sprawdza deterministycznie, czy zmiany faktycznie zaszły i czy sygnały zniknęły, zamiast polegać na własnej ocenie „wygląda lepiej".

Praca przebiega w dwóch krokach:
1. **Audyt** - zidentyfikuj wszystkie sygnały AI w tekście (z cytatami i kategoriami).
2. **Przepisanie** - przebuduj tekst z zachowaniem sensu i długości, eliminując sygnały AI.

Nie dodawaj nic od siebie. Nie wymyślaj faktów, liczb, nazwisk. Twoje zadanie to **czyścić i przebudowywać**, nie rozbudowywać.

## Workflow

### Krok 1: audyt

Przeskanuj cały tekst pod kątem 19 kategorii sygnałów AI (sekcja "Katalog sygnałów AI" poniżej). Dla każdego znalezionego problemu wynotuj:

- kategorię (np. "Miękka komunikacja", "Słownik AI", "Zaimkoza"),
- dokładny cytat z tekstu,
- krótkie wyjaśnienie czemu to AI-izm,
- propozycję naprawy (zwięźle).

Format raportu:

```
## Audyt AI-izmów

### 1. [Kategoria]
- "cytat z tekstu" - [czemu to AI] - [jak naprawić]

### 2. [Kategoria]
- "cytat z tekstu" - [czemu to AI] - [jak naprawić]
```

Jeśli tekst jest czysty w jakiejś kategorii - pomiń ją w raporcie. Nie pisz "Zasada N: nic do poprawy". Po prostu omiń.

**Szukaj rdzeniami, nie formami podstawowymi.** Polska fleksja rozbraja listy słów: „kluczowy" ma siedem form (kluczowa, kluczowego, kluczowym, kluczowe, kluczowych...). Skanując tekst pod kątem słów z tabel, szukaj rdzenia (`kluczow-`, `dynamiczn-`, `innowacyjn-`, `kompleksow-`, `fundamentaln-`), inaczej przepuścisz sześć z siedmiu trafień.

### Krok 2: przepisanie

Po raporcie napisz nagłówek:

```
## Tekst po humanizacji
```

I podaj pełną przebudowaną wersję tekstu. Zachowaj:

- ten sam temat, fakty, sens,
- zbliżoną długość (±20%),
- strukturę nagłówków, jeśli były (ale popraw Title Case → sentence case),
- listy, jeśli były (ale popraw interpunkcję na końcach).

Wymień:

- styl AI na ludzki rytm,
- bezosobowe konstrukcje na czynne ze sprawcą,
- słownik-wytrychy na konkrety,
- miękką komunikację na twardą.

Po przepisanym tekście dodaj krótką notkę (1-3 zdania), jaki był główny problem stylistyczny i co najbardziej zmieniłeś.

## Katalog sygnałów AI

Poniższe 19 kategorii to checklist - przejdź każdą przy audycie.

**Priorytet: wzorce strukturalne przed listami słów.** Kategorie strukturalne (rytm, bezosobowość, reguła trzech, atrybucja bez źródła, napuszona ważność, unikanie „jest") są ponadczasowe - modele powielają je niezależnie od wersji. Listy słów (kat. 4, 11) przeterminowują się mniej więcej co rok, bo słownictwo modeli ewoluuje (GPT-4: „delve", „crucial"; GPT-4o: „align with", „enhance"; GPT-5: „showcasing", „emphasizing"). Wykreślenie słowa z listy nie robi tekstu ludzkim - robi go ubogim. Napraw wzorzec, nie poluj na pojedyncze wyrazy. Data ostatniej aktualizacji słownika: 2026-07.

### 1. Monotonny rytm zdań ("metronom")

AI pisze zdania o zbliżonej długości - jednostajnie. Człowiek pisze muzykę: krótkie zdanie. Średnie. I czasem długie, rozbudowane zdanie z trzema klauzulami, które niesie czytelnika przez akapit.

**Sygnał:** trzy lub więcej kolejnych zdań o podobnej długości. Akapity o tej samej długości.

**Naprawa:** wrzuć zdanie 2-3-wyrazowe. Albo zlej dwa zdania w jedno dłuższe. Zróżnicuj długość akapitów.

**Drugi biegun - staccato-sieczka.** Metronom to jeden wzorzec AI, karabin to drugi. Serie zdań-uderzeń („Serio. Tyle. To wszystko."), sztuczne cięcie powiązanych myśli na osobne krótkie zdania i dramatyczne fragmenty („Bez preferencji. Bez sentymentu. Bez nostalgii.") to ten sam szablon w drugą stronę. Jeśli dwie myśli należą do siebie - połącz je w jedno zdanie. Zdanie-cios działa, gdy jest jedno na sekcję, nie trzy na akapit.

> **ŹLE:** „Uczenie głębokie to zaawansowany rodzaj uczenia maszynowego. Wykorzystuje sieci algorytmów inspirowanych strukturą mózgu. Głęboka sieć neuronowa ma zagnieżdżone węzły neuronowe. Każde pytanie prowadzi do zestawu powiązanych pytań”.
>
> **DOBRZE:** „Uczenie głębokie naśladuje strukturę ludzkiego mózgu. Sieć neuronowa zagnieżdża węzły, a jedno pytanie rodzi kolejne. I kolejne. Aż system potrafi rozpoznać kota na zdjęciu albo przetłumaczyć zdanie z suahili”.

### 2. Brak sprawcy (bezosobowość, strona bierna)

AI ucieka w „zrobiono”, „pominięto”, „zostało wdrożone”, „uważa się”, „należy”. Każde zdanie powinno mieć podmiot: człowieka, firmę, narzędzie, dokument.

**Sygnał:** „się” + czasownik, strona bierna („został wdrożony”), konstrukcje typu „uważa się, że”.

**Naprawa:** dodaj sprawcę. Jeśli oczywisty - użyj go wprost.

> **ŹLE:** „Została podjęta decyzja o wdrożeniu systemu”. → **DOBRZE:** „Zarząd zdecydował o wdrożeniu systemu”.
> **ŹLE:** „Zaleca się stosowanie tego rozwiązania”. → **DOBRZE:** „Stosuj to rozwiązanie”. / „Producent zaleca to rozwiązanie”.

### 3. Miękka komunikacja („warto”, „należy”, „powinno się”)

AI asekuracyjnie pisze „warto”, „może pomóc”, „dobrze jest”, „zaleca się”, „należy rozważyć”. To robocza encyklopedyczność - nikogo nie obraża, niczego nie nakazuje.

**Sygnał:** lista słów-zmiękczeń.

**Naprawa:** zamień na korzyść, skutek albo tryb rozkazujący.

| Miękkie (AI) | Twarde (ludzkie) |
|---|---|
| Warto rozważyć | Rozważ / Zrób to, bo... |
| Może pomóc | Pomoże / Skróci / Zmniejszy |
| Należy pamiętać | Pamiętaj |
| Zaleca się | Rób tak / [Kto] zaleca |
| Powinno się | Musisz / [Kto] powinien |
| Dobrze jest | [Konkretna korzyść] |

### 4. Słownik AI (słowa-wytrychy)

| Słowo AI | Co zrobić |
|---|---|
| kluczowy | ważny, decydujący, niezbędny - albo wywal i napisz DLACZEGO |
| dynamiczny | usuń lub opisz co się zmienia |
| kompleksowy | całościowy, pełny - albo wywal |
| innowacyjny | opisz co jest nowego i czemu lepsze |
| synergia | współpraca, połączenie sił - albo wywal |
| fundamentalny | podstawowy, bazowy - albo wywal |
| niezwykły, fascynujący, wyjątkowy | wywal i POKAŻ czym się wyróżnia |
| potężne narzędzie | napisz CO to narzędzie robi |
| znacząco | podaj skalę (o 30%, dwukrotnie) |
| zmienia zasady gry / game changer | opisz CO zmienia i JAK |
| holistyczny | całościowy, pełny - albo wywal |
| dostarczać wartość | dawać korzyść, przynosić efekty |
| prezentuje / uwydatnia (showcasing) | pokazuje - albo napisz CO konkretnie widać |
| „co podkreśla" / „co uwypukla" (highlighting) | wywal dopowiedzenie, zostaw fakt (patrz kat. 16) |
| wzmacnia / usprawnia (enhance) | podaj CO się zmienia i o ile |
| wpisuje się w / jest zgodny z (align with) | pasuje do - albo pokaż związek konkretem |

**Frazy do całkowitego wyrzucenia (wata słowna):**

- „W dzisiejszym dynamicznie zmieniającym się świecie...”
- „W obecnych czasach...”
- „W tym artykule przyjrzymy się...”
- „Poniżej przedstawiamy...”
- „Należy pamiętać, że...”
- „Warto zauważyć, że...”
- „To nic innego, jak...”
- „Niezależnie od tego, czy...”
- „brzmi jak...”

Po prostu wywal. Zacznij od sedna. Czytelnik nie potrzebuje rozgrzewki.

**Konstrukcje do rozbicia:**

| Konstrukcja AI | Co zrobić |
|---|---|
| „Nie tylko X, ale przede wszystkim Y” | „X, a do tego Y” / „X, i co ważniejsze - Y” |
| „To nie jest X, to Y” | Połącz w jedno zdanie z uzasadnieniem |
| „Coś więcej niż...” | Napisz wprost czym to jest |

**Kalki z angielskiego:**

| Kalka | Polski |
|---|---|
| Adresować problem | Rozwiązywać problem |
| Na koniec dnia | Ostatecznie |
| Dedykowany (= dedicated to) | Przeznaczony dla |
| Dostarczać rezultaty | Dawać wyniki |
| Podjąć akcję | Działać |
| Zanurz się, zagłęb się (delve) | Sprawdź, przeanalizuj |
| Krajobraz technologiczny (landscape) | Branża, rynek |
| Tętniący życiem (vibrant) | Aktywny, prężny |
| Podnieść na wyższy poziom (elevate) | Popraw, ulepsz |
| Świadectwo (testament to) | Dowód |

### 5. Zaimkoza i rzeczowniki odczasownikowe

**Zaimkoza:** AI nadużywa „twój”, „swój”, „jego”, „tych”, „tego”. W polskim zaimek jest zbędny, gdy kontekst jasny.

> **ŹLE:** „On poszedł do swojego domu”. → **DOBRZE:** „Poszedł do domu”.
> **ŹLE:** „Zrozumienie tych podstawowych definicji jest kluczowe dla każdego, kto pragnie zgłębić tajemnice tego dynamicznego obszaru”.
> **DOBRZE:** „Znajomość podstawowych definicji otwiera drzwi do zrozumienia całej dziedziny”.

**Rzeczowniki odczasownikowe na początku zdania:** „Zrozumienie...”, „Wdrażanie...”, „Zapewnienie...”, „Monitorowanie...”. To kalka z angielskiego gerunda. Przebuduj na zdanie z podmiotem i czasownikiem.

> **ŹLE:** „Zrozumienie kultury organizacyjnej jest kluczowe w procesie fuzji”.
> **DOBRZE:** „Kto nie zrozumie kultury organizacyjnej przejmowanej firmy, ten przepali fuzję”.

**Imiesłowy „Rozumiejąc, wdrażając, analizując...”** - zamień na normalne zdanie.

> **ŹLE:** „Wdrażając nowe procesy, firma może zwiększyć efektywność”.
> **DOBRZE:** „Nowe procesy zwiększą efektywność firmy”.

### 6. Interpunkcja i formatowanie (polski standard)

#### Cudzysłowy — DOKŁADNE KODY ZNAKÓW

W polskim tekście używaj WYŁĄCZNIE dwóch znaków cudzysłowu:

- otwierający: U+201E (`„` DOUBLE LOW-9 QUOTATION MARK)
- zamykający: U+201D (`”` RIGHT DOUBLE QUOTATION MARK)

**Poprawnie:** U+201E na początku cytatu, U+201D na końcu.

**ZAKAZANE w treści (mogą być tylko w atrybutach HTML / Markdown typu id, class, href):**

- U+0022 — ASCII quote (`"`). Łamie typografię.
- U+201C — LEFT DOUBLE (`“`). To **angielski otwierający**, nie polski zamykający. Wygląda podobnie do U+201D, ale to inny znak.
- U+0027 — ASCII apostrof (`'`).

**Częsty błąd modeli LLM:** zamykanie polskiego cytatu znakiem U+201C zamiast U+201D. Renderowanie wygląda prawie tak samo, ale to różne znaki. Zawsze weryfikuj programowo (sekcja "Automatyczny check" niżej).

#### Kolejność interpunkcji w polskim — KRYTYCZNE

W polskim cudzysłów zamykający stoi **PRZED** znakiem interpunkcyjnym (kropka, przecinek, średnik, dwukropek). W angielskim odwrotnie. To dwa różne standardy i model LLM domyślnie idzie angielską drogą.

| Co piszemy | PL standard | EN standard |
|------------|-------------|-------------|
| Kropka | U+201E tekst U+201D **.**  → `„tekst”.` | `"text."` |
| Przecinek | U+201E tekst U+201D **,**  → `„tekst”,` | `"text,"` |
| Średnik | U+201E tekst U+201D **;**  → `„tekst”;` | `"text;"` |
| Dwukropek | U+201E tekst U+201D **:**  → `„tekst”:` | `"text:"` |

**Wyjątek:** znak zapytania (?) i wykrzyknik (!), jeśli są CZĘŚCIĄ cytowanej wypowiedzi, zostają WEWNĄTRZ cudzysłowu: `„Czy to działa?” – zapytał klient.`

Jeśli to zewnętrzne zdanie pyta o cytat: `Czy klient powiedział „działa”?`

#### Pozostałe zasady formatowania

- **Myślniki:** półpauza `–` (U+2013) ze spacjami po obu stronach (polski standard). Wywal em-dash `—` (U+2014).
- **Listy:** po dwukropku mała litera (chyba że nazwa własna). Każdy element listy zakończ znakiem (przecinek lub kropka, konsekwentnie). Ostatni element zawsze kropka.
- **Nagłówki:** sentence case (tylko pierwsze słowo wielką literą), nigdy Title Case.
- **Separatory poziome:** nigdy nie używaj `---` między sekcjami tekstu. To znak wodny AI. Sekcje rozdziela sam nagłówek.
- **Skrótowce w nawiasach:** wywal nawias jeśli skrót jest powszechnie znany (AI, SEO, KNF). Jeśli niezbędny - wprowadź naturalnie w kolejnym zdaniu.
- **Nadmiar pogrubień:** mechaniczne boldowanie fraz w środku zdań („łączy **OKR-y** z **KPI**") to sygnał AI. Pogrubienie zostaje tylko tam, gdzie czytelnik skanujący tekst ma się zatrzymać - kilka na cały tekst, nie kilka na akapit.
- **Listy z inline-headerami:** wzorzec „**Nagłówek:** wyjaśnienie..." powtórzony w każdym punkcie listy to szablon AI. Jeśli punkty są krótkie - zwykła lista bez pogrubień. Jeśli długie - akapity prozy.
- **Nagłówek + jednozdaniowy akapit-echo:** nagłówek, pod nim jedno zdanie powtarzające nagłówek innymi słowami, potem dopiero treść. Wywal zdanie-echo, przejdź do treści.
- **Generyczne optymistyczne zakończenia:** „Podsumowując...", „Przyszłość rysuje się obiecująco", „Przed nami ekscytujące czasy". Wywal. Tekst kończy się ostatnim konkretem, nie ceremonią.

#### Automatyczny check po humanizacji

Po zakończeniu humanizacji **zawsze** wykonaj weryfikację. Sprawdza zarówno kody znaków jak i kolejność interpunkcji:

```python
import re
# usun atrybuty HTML z analizy (id="x", class="y", href="z")
body_for_check = re.sub(r'\b\w+="[^"]*"', '', text)

n_open  = body_for_check.count(chr(0x201E))   # „
n_close = body_for_check.count(chr(0x201D))   # ”
n_bad1  = body_for_check.count(chr(0x201C))   # “ angielski otwierajacy - musi byc 0
n_bad2  = body_for_check.count(chr(0x0022))   # " ASCII - musi byc 0

# Kolejnosc PL: cudzyslow zamyk PRZED znakiem interp (nie wielokropek)
bad_order = len(re.findall(r'(?<!\.\.)\.' + re.escape(chr(0x201D)), body_for_check))
bad_order += len(re.findall(r'[,;:]' + re.escape(chr(0x201D)), body_for_check))

assert n_open == n_close, f"Niesparowane cudzyslowy: otw={n_open}, zam={n_close}"
assert n_bad1 == 0,       f"U+201C w tresci ({n_bad1}) - musi byc U+201D"
assert n_bad2 == 0,       f"ASCII quote w tresci ({n_bad2})"
assert bad_order == 0,    f"Zla kolejnosc PL: znak interp przed ” ({bad_order}). PL: tekst”. nie tekst.”"
```

Jeśli któraś asercja nie przechodzi — popraw i policz ponownie.

### 7. Emoji

Jeśli tekst jest naszpikowany emoji (w każdym zdaniu, w każdym bullet poincie) - wywal większość. Zostaw 1-3 w całym tekście, i tylko jeśli gatunek tego wymaga (social media). W artykułach, raportach, mailach - zero emoji.

### 8. Ogólniki bez konkretu

- Jeśli nie znasz konkretu - **wywal zdanie**. Lepiej krótszy tekst niż pompowany ogólnikami.
- Jeśli konkret jest dostępny - wstaw: nazwisko, firmę, datę, liczbę, miejsce.
- Wywal tautologie - jeśli dwa akapity mówią to samo innymi słowami, zostaw jeden.
- **Fałszywe zakresy:** „od X po Y", gdzie X i Y nie leżą na żadnej realnej skali („od strategii po emocje", „od startupów po korporacje i wszystko pomiędzy"). To poza udawanej kompletności. Zamień na konkretną listę albo wywal.

> **ŹLE:** „Wiele osób uważa, że AI zmienia rynek”.
> **DOBRZE:** „Raport McKinsey z 2024 roku szacuje, że AI zautomatyzuje 30% zadań w marketingu do 2030 roku”. (jeśli masz źródło) / [wywal zdanie, jeśli nie masz].

### 9. Otwarcia „Jako [rola]...”

AI uwielbia „Jako HR Business Partner z wieloletnim doświadczeniem...”. Wywal. Jeśli autor jest ekspertem - niech to wynika z treści, nie z deklaracji.

> **ŹLE:** „Jako ekspert SEO z 10-letnim doświadczeniem widzę, że...”
> **DOBRZE:** „W ostatnich trzech latach widziałem to w czterech firmach, z którymi pracowałem”.

### 10. Spójność interpunkcyjna

Jeśli tekst jest hybrydowy (część ludzka, część AI), ujednolić:

- jeden typ myślnika (półpauza ze spacjami),
- jeden typ cudzysłowu (polski),
- jedna zasada na listach (wszędzie przecinki albo wszędzie kropki),
- jedna konwencja nagłówków.

### 11. Anglicyzmy zbędne (gdy istnieje polski odpowiednik)

To inna kategoria niż kalki z angielskiego (zasada 4). Kalki to idiomy przetłumaczone dosłownie („adresować problem"). Anglicyzmy zbędne to gołe angielskie słowa wpadające do polskiego tekstu mimo że polski ma identycznie zwięzły odpowiednik.

**Reguła:** Mieszanie angielskiego z polskim (polglish, korpomowa) – wyrzucamy. Branżowe terminy techniczne – zostają. Linia podziału:

**Zostają w angielskim (branżowe terminy, których się nie tłumaczy):**
- Skróty marketingu/IT: SEO, AI, API, CRM, CRO, CTR, KPI, ROI, B2B, B2C, MVP, SaaS, LLM, RAG, MCP, EEAT, YMYL
- Branżowe pojęcia SEO/AIO/marketingu: **BLUF**, **Cost of Retrieval**, **Information Gain**, **Information Density**, **Effort Score**, **Fan-Out Coverage**, **Entity Salience**, **Quick Wins**, **AI Search**, **link juice**, **anchor text**, **canonical**
- Terminy techniczne bez polskiego: prompt, token, embedding, n8n workflow (jako nazwa obiektu)
- Nazwy własne narzędzi: Slack, Notion, Google Docs, GPT, Claude, Perplexity

Pierwsze wystąpienie branżowego terminu w artykule – wprowadź z krótkim wyjaśnieniem („BLUF, czyli najważniejsze zdanie na początku"). Potem używaj swobodnie.

**Zamieniamy zawsze (gdy używane jako rzeczownik pospolity):**

| Anglicyzm | Polski odpowiednik |
|---|---|
| generic / generyczny ton | generyczny ton, ogólnikowy, banalny, szablonowy |
| engagement | zaangażowanie |
| engagement rate | wskaźnik zaangażowania |
| reach | zasięg |
| conversion rate | współczynnik konwersji (konwersja przyjęta w PL) |
| churn | rezygnacja, odpływ |
| hook | otwarcie, haczyk, pierwsze zdanie |
| pillar content | treść filarowa, filar treści |
| key takeaways | najważniejsze wnioski, kluczowe wnioski |
| callout | ramka, wyróżnienie, blok wyróżniony |
| feature (funkcja) | funkcja, element |
| benchmark | punkt odniesienia, wzorzec |
| insight | spostrzeżenie, wniosek, wgląd |
| output | wynik, rezultat |
| input | dane wejściowe, wejście |
| brief (jako rzeczownik) | brief (przyjęty w marketingu) / opis zlecenia / wytyczne |
| stack (narzędzia) | zestaw narzędzi, narzędziownia |
| setup | konfiguracja, ustawienie |
| review | przegląd, recenzja, ocena |
| feedback | informacja zwrotna, opinie, uwagi |
| case study | studium przypadku |
| driven (data-driven) | oparty na, kierowany (oparty na danych) |
| based (cohort-based) | oparty na, w formie (np. grupowy) |
| core | sedno, rdzeń, istota |
| focus | koncentracja, nacisk |
| impact | wpływ, skutek |
| highlight (verb) | wyróżnić, podkreślić |
| boost | przyspieszyć, zwiększyć, wzmocnić |
| feature (verb, „featuring X") | z X, w obsadzie X (jeśli artykuł) |
| workflow (luźno) | przepływ pracy, proces |
| pipeline (luźno) | sekwencja, proces, potok |
| onboarding | wdrożenie (HR/produktowe), uruchomienie (klient) |
| recurring | powtarzający się, cykliczny |
| crucial | ważny, decydujący (ale to też wytrych – patrz zasada 4) |
| lock-in | blokada, uzależnienie od dostawcy |
| target (audience) | grupa docelowa |
| persona | profil odbiorcy (persona OK w branży marketingu) |
| pricing | cennik, polityka cenowa |
| funnel | lejek (sprzedażowy) – przyjęte |
| growth | wzrost |
| level up | podnieść poziom, awansować |
| ready-to-use | gotowe do użycia, od ręki |
| matching | dopasowanie, pasujący |
| approach | podejście |
| process (jako kalka) | proces (OK, ale nie używaj „processować") |

**Wyjątek dla branżowych terminów SEO/AIO/marketingu:** BLUF, Cost of Retrieval, Information Gain, Information Density, Effort Score, Fan-Out Coverage, Entity Salience, Quick Wins, EEAT, YMYL, link juice, anchor text, canonical – zostają w oryginale. Przy pierwszym wystąpieniu krótkie wyjaśnienie w nawiasie („BLUF, czyli najważniejsze zdanie na początku"), potem swobodnie.

**Featured image** – termin WordPressowy. W prozie artykułu pisz „obrazek wyróżniający" lub „grafika nagłówkowa". W kontekście technicznym WP (kod, REST API, panel administratora) zostaje „featured image".

**Polglish do wyrzucenia bezwzględnie** (mieszanie języków bez sensu):
- „Key Takeaways" jako H2 polskiego artykułu → „Najważniejsze wnioski"
- „Onboarding pracownika" jako pogrubiony nagłówek → „Wdrożenie pracownika"
- „pillar content" w narracji → „treść filarowa", „artykuł filarowy"
- „generic voice", „klepie generic" → „generyczny ton", „ogólnikowy"

**Test decyzyjny:**
1. Czy polski odpowiednik istnieje?
2. Czy brzmi naturalnie w tym zdaniu?
3. Czy nie wydłuża zdania o więcej niż 30%?

Trzy razy TAK → używaj polskiego.

### 12. Nadużycie „bez”

„Bez opłat”, „bez presji”, „bez ryzyka”, „bez obaw” - AI tego nadużywa. „Bez X” jest formą miękką: mówi co czegoś brakuje zamiast co jest.

**Limit:** maksymalnie raz na zdanie, maksymalnie raz na ~200 słów.

**Naprawa:** zamień na konkret.

| „Bez” (AI) | Konkretnie (ludzkie) |
|---|---|
| Bez ukrytych opłat | Wszystkie koszty znane od startu |
| Bez presji | Decydujesz w swoim tempie |
| Bez zobowiązań | Najpierw audyt, potem decyzja |
| Bez wysiłku | Automatycznie, z łatwością |
| Bez ryzyka | Gwarancja zwrotu / Testuj za darmo |

### 13. Trójki anaforyczne („bez X, bez Y, bez Z" / „zero X, zero Y, zero Z")

AI uwielbia rytm trzech z anaforą - powtarza ten sam wytrych na początku trzech kolejnych członów. Najczęstsze formy:

- „bez X, bez Y, bez Z"
- „zero X, zero Y, zero Z"
- „bez wciskania, bez urgency, bez sztuczek"
- „zero presji, zero zobowiązań, zero ryzyka"

To brzmi rytmicznie i przekonująco, ale jest natychmiast rozpoznawalne jako szablon AI/copy-coachowy. Trójka z anaforą to świetna figura retoryczna używana raz na dłuższy tekst - jako element kontrolny. AI używa jej co akapit, każdą obietnicę pakując w trzy bezy.

**Sygnał:** trzy lub więcej członów z tym samym słowem-anaforą rozdzielonych przecinkami w jednym zdaniu. Szczególnie z „bez" lub „zero".

**Naprawa:**

1. **Zostaw jeden człon i rozwiń.** Zamiast „bez wciskania, bez urgency, bez sztuczek" - „bez wciskania - nie sprzedaję tak, że potem żałujesz".
2. **Przerób na pełne zdanie z konkretem.** „Bez X, bez Y, bez Z" → „Po prostu rozmowa, nie sprzedaż przez ciśnienie".
3. **Zostaw dwa człony zamiast trzech** (dwójka brzmi celowo, trójka brzmi jak szablon). „Bez wciskania i bez urgency".
4. **Wywal całą konstrukcję** - jeżeli mówisz to samo, co kontekst już zakomunikował, to powtórzenie jest zbędne.

| Trójka anaforyczna (AI) | Naprawa (ludzkie) |
|---|---|
| „Bez presji, bez sztuczek, bez wciskania" | „Bez ciśnienia - sprzedaję tak, jak sama chciałabym, żeby mi sprzedawano" |
| „Zero opłat, zero ryzyka, zero zobowiązań" | „Pierwszy miesiąc bezpłatnie. Rezygnujesz, kiedy chcesz" |
| „Bez korpomowy, bez schematów, bez ściemy" | „Po polsku i konkretnie" |
| „Krótkie. Mocne. Bez wciskania." | „Krótkie i mocne - bez wciskania" (z dwóch zrobić jedno) |

**Limit:** maksymalnie jedna trójka anaforyczna na cały tekst, i to tylko jeżeli celowo budujesz figurę retoryczną. W każdym innym wypadku rozbij na dwójkę albo zdanie z konkretem.

### 14. Reguła trzech (ogólna triada)

Najbardziej uniwersalny wzorzec AI - potwierdzony we wszystkich znanych zestawach reguł (Wikipedia „Signs of AI writing", no-ai-slop i inne). Model pakuje wyliczenia w trójki dla pozoru kompletności: trzy przymiotniki („szybki, prosty i skuteczny"), trzy rzeczowniki („innowacje, inspiracje i wnioski"), trzy zdania o tej samej konstrukcji pod rząd. Kat. 13 łapie wariant z anaforą - ta kategoria łapie każdą triadę.

**Sygnał:** trzy elementy wyliczone razem, zwłaszcza gdy trzeci nic nie wnosi ponad dwa pierwsze. Więcej niż jedna triada w tekście = na pewno szablon.

**Naprawa:**

1. **Zostaw dwa człony.** Dwójka brzmi jak wybór, trójka jak szablon.
2. **Zostaw jeden i rozwiń go w konkret.** Zamiast „szybki, prosty i skuteczny" - „skuteczny: skraca proces z trzech dni do dwóch godzin".
3. **Rozbij na realną listę**, jeśli elementów naprawdę jest więcej i każdy niesie treść.

> **ŹLE:** „Narzędzie jest szybkie, intuicyjne i niezawodne".
> **DOBRZE:** „Narzędzie renderuje stronę w 2 sekundy i przez pół roku nie zaliczyło ani jednej awarii".

**Limit:** jedna triada na tekst - i tylko celowa, jako figura retoryczna.

### 15. Atrybucja bez źródła (weasel words)

AI przypisuje twierdzenia bytom, których nie da się sprawdzić: „badania pokazują", „eksperci są zgodni", „powszechnie uważa się", „obserwatorzy wskazują", „wiele osób twierdzi", „raporty branżowe sugerują", „niektórzy krytycy". To tworzy pozór autorytetu bez żadnego autorytetu.

**Sygnał:** twierdzenie z podmiotem-widmem. Kto konkretnie? Które badanie? Jaki ekspert?

**Naprawa:** nazwij źródło (autor, instytucja, rok) - albo wywal twierdzenie. Nie ma trzeciej opcji.

> **ŹLE:** „Eksperci są zgodni, że automatyzacja odgrywa kluczową rolę w content marketingu".
> **DOBRZE:** „Raport HubSpot z 2025 roku: 67% marketerów automatyzuje przynajmniej jeden etap produkcji treści". / [wywal, jeśli nie masz źródła].

### 16. Napuszona ważność i pseudogłębia

AI dopisuje wagę zamiast pokazać fakt. Trzy odmiany tego samego problemu:

**a) Pompowanie znaczenia:** „odgrywa kluczową rolę", „stanowi dowód na", „to przełomowy moment", „wpisuje się w szerszy trend", „ma fundamentalne znaczenie dla". Podaj fakt - czytelnik sam oceni, czy jest ważny.

> **ŹLE:** „Wdrożenie AI stanowi przełomowy moment w historii firmy".
> **DOBRZE:** „Po wdrożeniu AI firma skróciła produkcję artykułu z 6 godzin do 40 minut".

**b) Pseudoanaliza imiesłowowa na końcu zdania:** dopowiedzenia typu „..., podkreślając zaangażowanie zespołu", „..., co pokazuje, jak ważna jest elastyczność", „..., wpisując się w globalny trend". To kalka angielskiego „-ing" - udaje analizę, nie wnosi treści. Kat. 5 łapie imiesłowy na początku zdania; ta łapie doklejki na końcu. Utnij zdanie po fakcie. Jeśli wniosek jest wart osobnej myśli - daj mu osobne zdanie z konkretem.

> **ŹLE:** „Firma wdrożyła nowy proces onboardingu, co podkreśla jej zaangażowanie w rozwój pracowników".
> **DOBRZE:** „Firma wdrożyła nowy proces onboardingu. Nowi pracownicy wchodzą w projekty po tygodniu, nie po miesiącu".

**c) Aforyzm-puenta:** pseudogłębokie zdanie-kicker zamykające sekcję: „Symetria to język zaufania", „Bo content to tak naprawdę rozmowa". Brzmi jak mądrość, znaczy tyle co nic. Zakończ konkretem, nie sentencją.

### 17. Unikanie „jest" i „ma" (copula avoidance)

Model zastępuje najprostsze czasowniki zawijasami: „stanowi", „pełni funkcję", „służy jako", „oferuje", „wyróżnia się", „charakteryzuje się". W piśmiennictwie naukowym użycie „is/are" spadło po 2023 roku o ponad 10% - to mierzalny odcisk palca modeli. Po polsku ten sam mechanizm.

**Sygnał:** „stanowi", „pełni rolę", „służy jako", „oferuje możliwość", „charakteryzuje się" tam, gdzie wystarczy „jest", „ma", „daje".

**Naprawa:** wróć do prostego czasownika.

| Zawijas (AI) | Prosto (ludzkie) |
|---|---|
| Stanowi ważny element | Jest ważnym elementem / Jest ważny |
| Pełni funkcję centrum | Jest centrum |
| Służy jako punkt odniesienia | Jest punktem odniesienia |
| Oferuje możliwość eksportu | Ma eksport / Eksportuje |
| Charakteryzuje się wysoką jakością | Jest dobrej jakości / [pokaż czym] |

### 18. Karuzela synonimów

Model rotuje synonimy, żeby uniknąć powtórzeń (kara za powtórzenia w architekturze modeli): „bohater... główna postać... centralna figura... protagonista". Człowiek powtarza jasny termin i nikt tego nie zauważa - czytelnik zauważa dopiero karuzelę.

**Sygnał:** to samo pojęcie nazywane w tekście trzema lub więcej różnymi słowami bez powodu.

**Naprawa:** wybierz jedno słowo na jedno pojęcie i trzymaj się go. Synonim tylko wtedy, gdy wnosi nowy odcień znaczenia.

### 19. Fałszywa autentyczność i coachingowy bełkot

Wzorce specyficznie polskie - model generuje polski tekst od zera, więc te frazy nie występują na angielskich listach.

**a) Fałszywa autentyczność:** zmyślone sygnały doświadczenia - „Ostatnio coraz częściej słyszę, że...", „Moi klienci pytają mnie ostatnio...", „Znam to z autopsji", „Widzę to u każdego klienta". Udają anegdotę, nie zawierają żadnej. Prawdziwa anegdota ma konkret: kto, kiedy, co się stało.

> **ŹLE:** „Moi klienci pytają mnie ostatnio, czy AI zastąpi copywriterów".
> **DOBRZE:** „W marcu na warsztatach w agencji [X] padło pytanie: czy za rok będziecie nas jeszcze potrzebować?". / [wywal, jeśli nie masz prawdziwej historii].

**b) Coachingowy bełkot:** „Uwolnij swój potencjał", „Odkryj autentyczną wersję siebie", „Wejdź na wyższy poziom", „Turbodoładuj biznes". Obietnica bez treści. Zamień na mierzalną korzyść albo wywal.

**c) Sygnały pod algorytm:** wtręty pisane pod engagement, nie pod czytelnika - „I szczerze?", „Czytaj dalej, bo będzie ciekawie", „Zostań ze mną do końca". Wywal.

## Diagnostyka: szybki test

Po przepisaniu sprawdź:

1. Przeczytaj tekst na głos - miejsca, w których się potkniesz, to miejsca do przepisania.
2. Czy jest tu coś, czego AI nie wygeneruje? (własna obserwacja, konkretna liczba, anegdota)
3. Po pierwszym akapicie wiadomo, kto pisze? Czy to mógł napisać każdy?
4. Czy są wszystkie sygnały AI usunięte (sprawdź checklistę 19 kategorii)?
5. Czy tekst odpowiada na konkretne pytanie konkretnego człowieka, czy „komunikuje” w próżnię?
6. Czy tekst brzmi jak mówienie na żywo do publiki - zwraca się do czytelnika, angażuje go pytaniem, uprzedza jego reakcje? (sekcja „Tryb konwersacyjny”)

## Zasady, których trzymaj się przy przepisywaniu

1. **Nie dodawaj treści.** Twoje zadanie to czyścić, nie rozbudowywać. Jeśli AI wciskało wodę, wywal wodę i tekst będzie krótszy. To OK.
2. **Nie wymyślaj faktów.** Liczb, nazwisk, dat, miejsc - nie zmyślaj. Jeśli AI je wymyśliło, też je wywal albo oznacz w raporcie do weryfikacji.
3. **Zachowaj rejestr.** Jeśli tekst jest formalny (raport, dokument prawny) - nie wrzucaj kolokwializmów. Humanizacja ≠ kolokwializacja. Człowiek może pisać formalnie, ale żywo.
4. **Krótszy tekst to często lepszy tekst.** AI lubi rozbudowywać. Człowiek wycina.
5. **Pisz konwersacyjnie.** Domyślny tryb outputu to mówienie na żywo do publiki, nie esej do szuflady. Szczegóły w sekcji „Tryb konwersacyjny" niżej.

## Tryb konwersacyjny (domyślny styl outputu)

Przepisany tekst ma brzmieć jak mówienie na żywo do konkretnej publiki - jakby autor stał przed salą albo mówił do kamery. Nie jak referat czytany z kartki.

Techniki:

- **Mów do czytelnika wprost.** Druga osoba („Ty") i pytania skierowane do niego: „Znasz to?", „Ile razy Ci się to zdarzyło?".
- **Pytania retoryczne jako zawiasy.** Zamiast suchego przejścia między myślami wrzuć pytanie: „Efekt?", „Co z tego masz?", „I co dalej?". Jedno-dwa na sekcję, nie w każdym akapicie.
- **Uprzedzaj reakcje publiki.** „Wiem, co teraz myślisz...", „Brzmi banalnie? No właśnie nie do końca" - odpowiadaj na obiekcje czytelnika, nim je wypowie.
- **Zawieszenia i dopowiedzenia.** Krótkie zdanie-uderzenie po dłuższym wywodzie: „Serio.", „Tyle.", „I to działa". Działa jak pauza sceniczna. **Twardy limit: 1-2 na cały tekst.** Te konstrukcje same stały się rozpoznawalnym wzorcem AI (staccato drama, kat. 1) - nadużyte przestają być pauzą, a zaczynają być szablonem.
- **Język mówiony, nie pisany.** Konstrukcje, które naturalnie wychodzą z ust: „no dobra", „umówmy się", „patrz" - dawkuj według rejestru tekstu.

Granice:

- Rejestr nadal rządzi (zasada 3 wyżej): w raporcie czy dokumencie formalnym konwersacyjność ogranicza się do bezpośredniego zwrotu do czytelnika i żywego rytmu, bez kolokwializmów.
- Zwroty do publiki i pytania retoryczne to przyprawa, nie danie główne. Gdy są w każdym akapicie, tekst brzmi jak skrypt webinaru sprzedażowego - czyli znowu jak szablon.
- **Zakaz dwukropka dramatu.** Konstrukcja „fraza, dwukropek, dramatyczne ujawnienie" („Sedno: nikt tego nie czyta", „Efekt: podwoiliśmy sprzedaż") to rozpoznany wzorzec AI. Napisz zwykłe zdanie.
- **Zakaz pseudogłębokich puent.** Nie kończ sekcji aforyzmem-kickerem (kat. 16c). Konwersacyjnie znaczy: mówisz do ludzi normalnie, a nie rzucasz sentencjami jak mówca motywacyjny.
- Test: przeczytaj na głos. Jeśli nie powiedziałbyś tego zdania do żywego człowieka - przepisz.

## Format finalnego outputu

```
## Audyt AI-izmów

### 1. [Kategoria]
- „cytat” - [problem] - [proponowana naprawa]
- „cytat” - [problem] - [proponowana naprawa]

### 2. [Kategoria]
- „cytat” - [problem] - [proponowana naprawa]

[...kolejne kategorie...]

## Tekst po humanizacji

[Pełny przebudowany tekst.]

## Notka redaktorska

[1-3 zdania: co było głównym problemem, co najmocniej zmieniłeś.]
```


## Polska typografia (obowiązkowa)

Stosuj zasady z `~/.claude/skills/_shared/polska-typografia.md` (source of truth).

Skondensowane reguły:

- **Cudzysłowy:** otwierający U+201E (`„`), zamykający U+201D (`”`). Zakazane w treści: ASCII `"` (U+0022) i `“` U+201C (to angielski otwierający, nie polski zamykający).
- **Kolejność interpunkcji (krytyczne):** cudzysłów zamykający PRZED znakiem interp. PL: `„tekst”.`, EN (błędne w PL): `"text."`. Wyjątek: `?` i `!` zostają wewnątrz cudzysłowu, jeśli są częścią cytowanej wypowiedzi.
- **Myślniki:** półpauza `–` (U+2013) ze spacjami; em-dash `—` (U+2014) zakazany.
- **Separator `---`:** tylko w YAML frontmatter, nigdy między sekcjami treści.
- **Nagłówki:** sentence case (pierwsze słowo wielką literą + nazwy własne).

### Programowy check po edycji (obowiązkowy)

```
python ~/.claude/skills/_shared/walidator-typografii.py [twoj-plik.md]
```

Walidator zwróci exit 1 jeśli wykryje niesparowane cudzysłowy, U+201C/ASCII `"` w treści, złą kolejność interp lub em-dashy. Jeśli FAIL — popraw i uruchom ponownie. Nie oddawaj tekstu z błędami typografii.
