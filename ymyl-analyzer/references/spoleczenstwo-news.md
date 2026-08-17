# Społeczeństwo i news – kryteria YMYL według SQRG

Kategoria SQRG: YMYL Government, Civics & Society (2.3; do września 2025 „YMYL Society”) – tematy wpływające na grupy ludzi, sprawy interesu publicznego, zaufanie do instytucji, informacje wyborcze. Obejmuje newsy o bieżących wydarzeniach, tematy obywatelskie i treści o grupach społecznych.

## Kiedy ta branża jest YMYL, a kiedy nie

| Werdykt | Przykładowe tematy |
|---|---|
| Wyraźnie YMYL | informacje wyborcze (kto może głosować, jak, kiedy), newsy o trwającej przemocy/katastrofie, programy rządowe i świadczenia (800+, dopłaty), zmiany prawa dotykające ogółu, treści o grupach społecznych (imigranci, mniejszości), zaufanie do instytucji publicznych |
| Może być YMYL | news o wypadku samochodowym, komentarz polityczny z tezą, analizy społeczne |
| Raczej nie YMYL | sport lokalny, kultura i rozrywka, lifestyle, plotki o celebrytach (o ile nie krzywdzą) |

Test: czy temat wpływa na decyzje obywatelskie, bezpieczeństwo publiczne albo traktowanie grup ludzi? Wzorzec z SQRG 2.3: trwająca przemoc = clear YMYL (ludzie podejmują decyzje o bezpieczeństwie), wypadek samochodowy = may be, mecz licealny = nie.

## Wymagane sygnały

- **Datowanie**: data publikacji i aktualizacji obowiązkowa – news bez daty nie pozwala ocenić aktualności (SQRG 18.0); dla trwających wydarzeń znacznik „stan na”.
- **Fakt oddzielony od opinii**: relacja vs komentarz oznaczone; tekst opiniotwórczy może mieć tezę, ale nie może przeinaczać faktów (SQRG 4.4 – wyłączenie dla kwestii zasadnie dyskusyjnych).
- **Źródła weryfikowalne**: agencje, dokumenty, wypowiedzi z imienia; anonimowe „źródła zbliżone” tylko jako uzupełnienie.
- **Standardy dla najwyższej jakości** (SQRG 8.1): oryginalne dziennikarstwo, opis źródeł pierwotnych, standardy zawodowe – to odróżnia High od Highest w newsach.
- **Odpowiedzialność redakcyjna** (SQRG 2.5.2): wydawca i autor jawni; serwis informacyjny bez stopki redakcyjnej to sygnał ostrzegawczy (4.5.3 zna wzorzec „strona udająca serwis informacyjny”).
- **Język o grupach ludzi** (SQRG 4.3): krytyka idei i polityk jest dozwolona; generalizacje o ludziach z grupy chronionej – nie.

## Typowe braki

1. Brak daty publikacji/aktualizacji przy treści o zmieniającym się stanie (świadczenia, terminy wyborcze).
2. Tytuł ostrzejszy niż treść – „szok”, „skandal” bez pokrycia (SQRG 5.2 – tytuły przesadzone).
3. Opinia ubrana w formę relacji informacyjnej bez oznaczenia.
4. Przepisane depesze bez wartości dodanej i bez wskazania źródła pierwotnego (SQRG 5.2.1).
5. Dane o programach rządowych bez linku do źródła urzędowego.
6. Cytaty bez kontekstu zmieniające wydźwięk wypowiedzi.
7. Brak autora i stopki redakcyjnej w serwisie publikującym newsy (SQRG 5.5).

## Czerwone flagi Lowest

- Fałszywe informacje wyborcze (daty, zasady, uprawnieni) – wzorcowy przykład harmfully misleading (SQRG 4.4: „fałszywe daty wyborów”).
- Niepotwierdzone teorie podkopujące zaufanie do instytucji publicznych (4.4 – typ 3).
- Treści promujące nienawiść wobec grup chronionych, dehumanizujące stereotypy, sugerowanie wyższości/niższości grup (4.3; wzorzec z 2.3: „opinia, dlaczego grupa rasowa jest gorsza”).
- Strona udająca niezależny serwis informacyjny, w rzeczywistości manipulująca na rzecz organizacji lub polityka (4.5.3).
- Fałszywa informacja o śmierci osoby publicznej (4.4 – typ 1).

## Przykłady z SQRG

- News o trwającej przemocy = clear YMYL; o wypadku = may be; o meczu licealnym = nie (2.3, tabela).
- „Kto może głosować, jak się zarejestrować” tylko ze źródeł eksperckich/urzędowych; osobisty post „dlaczego głosuję” OK (3.4.1).
- Wyłączenia z 4.3: dokument historyczny z przemówieniami nazistów, artykuł o organizacji szerzącej nienawiść, definicja słownikowa obelgi – to NIE jest harmful.
- Wyłączenia z 4.4: satyra i parodia bez twardych twierdzeń, kwestie zasadnie dyskusyjne (porównania systemów ochrony zdrowia).
- Highest dla newsów = oryginalne dziennikarstwo ujawniające nieznane fakty, ze źródłami pierwotnymi (8.1).

## Granice

- Fakty, daty i liczby → `/fact-checker` (dla newsów to niemal zawsze obowiązkowy krok po audycie).
- Głębokie E-E-A-T → `/eeat-analyzer`.
