---
name: formularz-apps-script
description: >
  Buduje kompletny, gotowy do wdrożenia formularz jako Google Apps Script Web App —
  trzy pliki do przeklejenia (Code.gs, Index.html, appsscript.json), backend na Apps Script,
  dane w Google Sheets, komunikacja przez google.script.run. Bezpieczeństwo backendu i deploymentu
  traktuje na równi z wyglądem: walidacja serwerowa, allowlisty pól zamkniętych, twarda neutralizacja
  formula injection, honeypot, LockService, minimalne oauthScopes, sekrety wyłącznie w Script Properties.
  Kończy własnym code review i werdyktem SECURITY REVIEW — PASS oraz dokładną instrukcją wdrożenia.
  ZAWSZE używaj tego skilla gdy użytkownik mówi: "zrób formularz w Apps Script", "formularz Google
  Apps Script", "Web App z formularzem", "formularz zapisujący do Google Sheets", "ankieta w Apps
  Script", "bezpieczny formularz firmowy", "formularz z Code.gs i Index.html", "google.script.run
  saveResponse", "formularz do arkusza bez Google Forms", "chcę własny formularz zamiast Google Forms",
  "formularz na intranet do Sheetsa", "appsscript.json z minimalnymi scope'ami". Używaj też gdy
  użytkownik wkleja listę pytań i branding i prosi o gotowy formularz zbierający odpowiedzi do arkusza.
---

# Formularz Google Apps Script Web App

Generujesz kompletny formularz-webapp na stacku Google Apps Script + Google Sheets. Odbiorca wypełnia stronę
serwowaną przez HTML Service, dane lecą przez `google.script.run` do backendu, backend waliduje i zapisuje do
arkusza. Respondent nigdy nie dotyka arkusza bezpośrednio.

To rozwiązanie ma trafiać do środowiska firmowego, więc bezpieczeństwo backendu i deploymentu jest równie
ważne jak wygląd. Nie oddajesz „ładnego formularza z dziurą" – oddajesz formularz, który przejdzie audyt.

## Zanim zaczniesz pisać kod

Zbierz od użytkownika dwie rzeczy, bez których nie ma sensu generować:

1. **Pytania** – lista pól. Sam dobierasz typy (radio, checkbox, select, textarea, input). Dla każdego pola
   zamkniętego ustalasz dozwolone wartości, dla otwartego – maksymalną długość.
2. **Branding** – kolory, logo, font, ton. Odwzorowujesz go w HTML/CSS w `Index.html`.

Dopytaj też o dwie decyzje wpływające na architekturę:

- **Publiczny czy wewnętrzny?** Publiczny anonimowy formularz w internecie → rozważ Cloudflare Turnstile.
  Wewnętrzny (domena Workspace) → nie dodawaj zewnętrznych usług, honeypot wystarczy.
- **Arkusz tworzony automatycznie czy istniejący?** `setup_()` może utworzyć arkusz i zapisać jego ID do
  Script Properties, albo użytkownik tworzy pusty arkusz ręcznie i raz wkleja ID do Script Properties.

Pełny szablon promptu z miejscami na pytania i branding leży obok: [`PROMPT.md`](PROMPT.md). To wersja do
wklejenia w czacie, gdy ktoś chce odpalić ten sam proces bez skilla.

## Kontrakt wyjścia

Zwracasz trzy kompletne pliki, gotowe do przeklejenia, bez pseudokodu, bez „...", bez pominiętych fragmentów:

- `Code.gs`
- `Index.html` (cały CSS i JS w środku, nie rozbijaj na dodatkowe pliki)
- `appsscript.json`

Po kodzie: dokładna instrukcja wdrożenia, potem własne code review, na końcu linijka `SECURITY REVIEW — PASS`.

## Model bezpieczeństwa – nienegocjowalny

Cały frontend i wszystko, co przychodzi z przeglądarki, traktuj jako dane niezaufane. Walidacja w JavaScript
służy tylko UX. Prawdziwa walidacja żyje w `Code.gs`. To nie paranoja: Web App z `Anyone` jako dostępem
przyjmuje request od kogokolwiek, a `google.script.run` woła nazwaną funkcję – więc powierzchnia ataku to
dokładnie to, co wystawisz publicznie.

### 1. Minimalna powierzchnia publiczna

Frontend potrzebuje tylko dwóch funkcji publicznych: `doGet()` i `saveResponse(data)`. Każdy helper kończy
nazwę podkreśleniem – `validateResponse_()`, `sanitizeText_()`, `safeCellText_()`, `getSpreadsheet_()`,
`getSheet_()`, `validateEnum_()`, `setup_()`. Funkcje z `_` na końcu nie są wywoływalne z `google.script.run`,
i to jest cała pointa: helper, którego nie da się zawołać z zewnątrz, nie jest wektorem.

Nie twórz `getSpreadsheetId()`, `getConfig()`, `getSecret()`, `runAnything()`, `execute()`, `debug()`,
`admin()` ani niczego, co wystawia backend „na wszelki wypadek".

### 2. Gdzie mieszka arkusz

ID arkusza żyje wyłącznie po stronie serwera, najlepiej w Script Properties pod kluczem `SPREADSHEET_ID`.
Frontend nie przekazuje ID arkusza, ID zakładki, nazwy arkusza, zakresu komórek, numeru wiersza, formuły ani
nazwy funkcji backendowej. Backend sam wie, gdzie zapisuje.

Nigdy nie rób `SpreadsheetApp.openById(data.spreadsheetId)` ani `sheet.getRange(data.range)` na podstawie
danych z formularza. To otwiera zapis do dowolnego arkusza, do którego ma dostęp konto wykonujące skrypt.

### 3. Formula injection – obowiązkowe

Tekst od respondenta nie może wpaść do arkusza jako formuła. Zbuduj jedną centralną funkcję `safeCellText_(value)`
i przepuść przez nią KAŻDĄ wartość od respondenta przed zapisem. Ma ona:

- skonwertować wartość na `String`,
- usunąć zbędne znaki kontrolne,
- przyciąć do limitu długości,
- sprawdzić pierwszy znaczący znak i zneutralizować tekst zaczynający się od `=`, `+`, `-`, `@`,
  najbezpieczniej prefiksując apostrofem, żeby Sheets zapisał to jako literalny tekst.

Test akceptacyjny: respondent wpisuje `=1+1`, w arkuszu ma być literalnie `=1+1`, a nie wynik `2`. Nie ufaj
samemu `setNumberFormat()` – neutralizacja idzie w backendzie.

### 4. Allowlisty pól zamkniętych

Każde pytanie zamknięte (radio, select, checkbox) ma jawną allowlistę po stronie backendu, np.
`AGE_VALUES = ['18–24', '25–34', ...]`. Jeśli frontend wyśle `age: 'administrator'`, backend odrzuca request.
Dla checkboxów: parametr musi być tablicą, każdy element należy do allowlisty, ogranicz maksymalną liczbę
elementów i usuń duplikaty.

### 5. Pola otwarte

Każdy `textarea`/`input` ma maksymalną długość (przykładowo: krótkie pole 200, standardowa odpowiedź 2000,
dłuższa 5000 znaków). Backend odrzuca albo bezpiecznie przycina wartości ponad limit. Nie przyjmujesz
nieskończenie długich stringów – to prosty wektor na wyczerpanie zasobów i rozdęcie arkusza.

### 6. Schema validation

Backend ma dokładny zestaw oczekiwanych kluczy. Pola spoza zestawu ignorujesz albo odrzucasz cały request.
Nie kopiujesz automatycznie wszystkich kluczy `data` do arkusza – żadnego `Object.values(data)` jako sposobu
budowania wiersza. Wiersz budujesz jawnie: `[ new Date(), safeCellText_(data.age), ... ]`. Dzięki temu nowe,
podrzucone pole nie przecieka do arkusza.

### 7. Timestamp z backendu

Znacznik czasu generuje backend przez `new Date()`. Nie ufasz czasowi z przeglądarki.

### 8. Współbieżność

Zapis obejmij `LockService.getScriptLock()` z rozsądnym `waitLock()`. Lock zwalniasz zawsze w `finally` –
inaczej jeden wyjątek zostawia skrypt z zablokowanym zapisem.

### 9. Podwójne wysłanie

Front: po kliknięciu Submit natychmiast disable przycisku i stan „Wysyłanie...". Odblokowujesz wyłącznie gdy
backend zwróci błąd. Po sukcesie nie da się wysłać tego samego formularza drugim kliknięciem.

### 10. Antyspam

Ukryty honeypot. Jeśli wypełniony – nie zapisujesz danych i nie ujawniasz botowi szczegółów błędu. Dla
formularza publicznego w internecie opisz opcjonalnie wariant z Cloudflare Turnstile: SECRET KEY tylko w
Script Properties, nigdy w `Index.html`, weryfikacja tokenu po stronie `Code.gs`, a scope `external_request`
dodajesz tylko wtedy, gdy faktycznie jest potrzebny. Wewnątrz organizacji nie dokładaj zewnętrznych usług.

### 11. XSS

Danych użytkownika nie wstawiasz do DOM przez `innerHTML`. Jeśli front musi wyświetlić tekst użytkownika –
`textContent`. Nie generujesz HTML-a z danych respondenta.

### 12. Sekrety

`Index.html` jest publiczny. Nie ma tam OAuth tokenów, API secrets, haseł, kluczy prywatnych, wartości Script
Properties ani Spreadsheet ID, jeśli front go nie potrzebuje (a nie potrzebuje). Nigdy nie przekazujesz do
klienta `ScriptApp.getOAuthToken()`. Sekret, jeśli w ogóle jest, siedzi w Script Properties i używa go tylko
`Code.gs`.

### 13. Logi

Żadnego `Logger.log(data)` dla całej odpowiedzi. Nie logujesz danych osobowych ani pełnych treści formularzy.
Logujesz tylko to, co potrzebne diagnostycznie: timestamp błędu, kod błędu, miejsce wystąpienia. Frontendowi
zwracasz ogólny komunikat „Nie udało się zapisać odpowiedzi. Spróbuj ponownie." Bez stack trace, bez wewnętrznych
szczegółów.

### 14. OAuth scopes

`appsscript.json` ma jawnie wypisane minimalne `oauthScopes`. Do zapisu do istniejącego arkusza przez
`SpreadsheetApp` wystarczy zakres Sheets – bez Gmail, Drive, Calendar, Contacts, Docs, Forms. Wyjaśnij, że
`https://www.googleapis.com/auth/spreadsheets` pozwala pracować z arkuszami, do których konto wykonujące ma
dostęp – i że ten scope NIE ogranicza automatycznie dostępu do jednego konkretnego Spreadsheet ID.

### 15. Konto wdrażające

Przy `Execute as → Me` kod działa z uprawnieniami konta wdrażającego. W firmie preferuj dedykowane konto
techniczne (np. `forms-automation@firma.pl`) z dostępem tylko do potrzebnego arkusza, bez normalnej skrzynki
Gmail, z MFA zgodnym z polityką organizacji. Jeśli użytkownik wdraża z głównego konta z szerokimi uprawnieniami
– wyraźnie ostrzeż, że blast radius jest większy.

### 16. Zero usług, których nie używasz

Bez `DriveApp`, `GmailApp`, `CalendarApp`, `ContactsApp` i Advanced Services, jeśli formularz ich nie potrzebuje.
Nie dodajesz usług „na przyszłość".

### 17. Zero eval

Bez `eval()`, `new Function()`, dynamicznego wykonywania kodu. Nie wybierasz funkcji backendowej na podstawie
stringa od użytkownika.

## Arkusz i setup_()

`setup_()` uruchamia ręcznie właściciel z edytora Apps Script – respondent nigdy go nie potrzebuje. `setup_()`:

- tworzy arkusz, jeśli projekt ma go tworzyć automatycznie,
- tworzy i stylizuje nagłówki, zamraża pierwszy wiersz, ustawia szerokości kolumn,
- zapisuje `SPREADSHEET_ID` do Script Properties,
- nie tworzy kolejnego arkusza, jeśli property już wskazuje poprawny arkusz (idempotencja),
- wypisuje właścicielowi URL arkusza.

Model prostszy: użytkownik tworzy pusty Google Sheet ręcznie i raz wpisuje jego ID do Script Properties.
W obu wariantach backend nigdy nie przyjmuje ID arkusza od respondenta.

## Formularz i UX

Sam dobierasz typy pól do pytań. Jeśli pytań jest sporo, podziel formularz na 2–4 logiczne etapy. Dodaj:
progress bar, przyciski Dalej/Wróć, walidację kroku, scroll do góry przy zmianie kroku, czytelne komunikaty
błędów, stan loading, ekran sukcesu, responsywność mobilną, focus states i podstawową obsługę klawiaturą.

## Instrukcja wdrożenia – dołączasz zawsze

Po kodzie podajesz dokładną instrukcję krok po kroku:

1. Utworzenie projektu Apps Script.
2. Wklejenie `Code.gs`, `Index.html`, `appsscript.json`.
3. Włączenie widoczności manifestu: Project Settings → „Show appsscript.json manifest file in editor".
4. Sprawdzenie Overview → Project OAuth Scopes. Jeśli pojawi się Gmail/Drive/Calendar bez powodu – STOP, nie
   wdrażaj, dopóki przyczyna nie zniknie.
5. Ręczne uruchomienie `setup_()`. Wyjaśnij, jakich zgód się spodziewać przy autoryzacji i że niespodziewana
   zgoda to sygnał do zatrzymania.
6. Test deployment: Deploy → Test deployments → Web app. Wyjaśnij różnicę: `/dev` to najnowszy kod dla osób z
   prawem edycji, `/exec` to konkretna opublikowana wersja produkcyjna.
7. Produkcja: Deploy → New deployment → Web app. Publiczny anonimowy: `Execute as → Me`, `Who has access → Anyone`
   (tylko gdy formularz naprawdę ma być publiczny). Wewnętrzny: ogranicz dostęp do użytkowników organizacji/domeny
   Workspace, jeśli konfiguracja na to pozwala.
8. Testy przed publikacją: normalna odpowiedź, brak wymaganego pola, niedozwolona wartość radio/select,
   niedozwolona wartość checkboxa, bardzo długi tekst, tekst `=1+1`, tekst od `+`/`-`/`@`, podwójny klik submit,
   test mobile, incognito, kilka szybkich odpowiedzi z rzędu. Test formula injection ma potwierdzić, że `=1+1`
   jest zapisane jako tekst.
9. Aktualizacja bez zmiany URL: Deploy → Manage deployments → Edit → New version → Deploy.
10. Checklista bezpieczeństwa do odhaczenia przed przekazaniem URL użytkownikom.

## Code review na końcu

Zanim oddasz finalny kod, zrób własny logiczny przegląd i sprawdź:

- każde pole frontu ma odpowiednik w backendzie,
- backend nie ufa frontowi,
- wszystkie dane użytkownika przechodzą przez sanitizację,
- żadna wartość użytkownika nie może zostać formułą,
- enumy mają allowlisty,
- helpery kończą się `_`,
- front nie zna Spreadsheet ID ani sekretów, w HTML nie ma sekretu,
- brak zbędnych funkcji publicznych,
- `appsscript.json` ma minimalne scope'y, kod nie używa usług, których nie potrzebuje,
- `LockService` zwalniany w `finally`,
- Submit nie pozwala wysłać formularza wielokrotnie,
- błędy nie ujawniają danych technicznych.

Na końcu wypisz `SECURITY REVIEW — PASS` i krótko, co zostało zabezpieczone. Jeśli któregoś wymagania nie da się
bezpiecznie spełnić w Google Apps Script – powiedz to wprost, zamiast udawać, że problem nie istnieje.
