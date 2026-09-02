Chcę zbudować kompletny formularz jako Google Apps Script Web App.

To ma być rozwiązanie możliwe do użycia w środowisku firmowym, więc bezpieczeństwo backendu i deploymentu jest równie ważne jak wygląd formularza.

Wygeneruj kompletne, gotowe do przeklejenia pliki:

- Code.gs
- Index.html
- appsscript.json

Nie używaj pseudokodu, „...” ani pominiętych fragmentów.

============================================================
ARCHITEKTURA
============================================================

Frontend:

HTML + CSS + JavaScript działające przez Apps Script HTML Service.

Backend:

Google Apps Script.

Dane:

Google Sheets.

Komunikacja:

google.script.run.

Przepływ:

respondent
→ Index.html
→ google.script.run
→ saveResponse(data)
→ walidacja backendowa
→ bezpieczny zapis
→ Google Sheets

Respondent nie powinien mieć bezpośredniego dostępu do Google Sheets.

============================================================
BEZPIECZEŃSTWO — BARDZO WAŻNE
============================================================

Traktuj cały frontend i wszystko, co przychodzi z przeglądarki, jako niezaufane dane.

Walidacja JavaScript służy UX.
Prawdziwa walidacja ma odbywać się po stronie Code.gs.

1. PUBLICZNE FUNKCJE BACKENDU

Ogranicz publiczne funkcje Apps Script do absolutnego minimum.

Docelowo frontend powinien potrzebować jedynie:

- doGet()
- saveResponse(data)

Wszystkie funkcje pomocnicze mają kończyć nazwę podkreśleniem, np.:

- validateResponse_()
- sanitizeText_()
- safeCellText_()
- getSpreadsheet_()
- getSheet_()
- validateEnum_()
- setup_()

Funkcje kończące się "_" mają być prywatnymi helperami i nie powinny być możliwe do wywołania z frontendowego google.script.run.

Nie twórz publicznych funkcji typu:

- getSpreadsheetId()
- getConfig()
- getSecret()
- runAnything()
- execute()
- debug()
- admin()

Nie wystawiaj przez frontend żadnych niepotrzebnych możliwości backendu.

2. GOOGLE SHEETS

ID arkusza ma znajdować się wyłącznie po stronie serwera.

Najlepiej:

Script Properties:
SPREADSHEET_ID

Frontend NIE może przekazywać:

- spreadsheet ID
- sheet ID
- nazwy arkusza
- zakresu komórek
- numeru wiersza
- formuły
- nazwy funkcji backendowej

Backend sam ma wiedzieć, gdzie zapisuje dane.

Nigdy nie wykonuj czegoś w rodzaju:

SpreadsheetApp.openById(data.spreadsheetId)

ani:

sheet.getRange(data.range)

na podstawie danych pochodzących z formularza.

3. FORMULA INJECTION

To jest obowiązkowe.

Dane tekstowe pochodzące od respondenta nie mogą zostać zapisane do Google Sheets jako formuła.

Stwórz centralną funkcję np.:

safeCellText_(value)

która:

- konwertuje wartość na String
- usuwa niepotrzebne znaki kontrolne
- ogranicza długość
- sprawdza pierwszy znaczący znak
- neutralizuje tekst zaczynający się od:
  =
  +
  -
  @

Najbezpieczniej prefiksując taki tekst apostrofem, aby Google Sheets zapisał go jako literalny tekst.

Ta funkcja ma być stosowana do KAŻDEJ wartości pochodzącej od respondenta przed zapisem do Sheets.

Przykład testu:

Respondent wpisuje:

=1+1

W arkuszu ma znaleźć się literalnie:

=1+1

a NIE wynik:

2

Nie ufaj samemu setNumberFormat().
Neutralizacja ma być wykonana w backendzie.

4. ALLOWLISTY

Dla wszystkich pytań zamkniętych backend ma mieć jawne allowlisty.

Przykładowo:

AGE_VALUES = [
  '18–24',
  '25–34',
  ...
]

Jeżeli frontend wyśle:

age: 'administrator'

backend ma odrzucić request.

Dotyczy to:

- radio
- select
- checkbox
- wszelkich pól zamkniętych

Dla checkboxów:

- parametr musi być tablicą
- każdy element tablicy musi należeć do allowlisty
- ogranicz maksymalną liczbę elementów
- usuń duplikaty

5. POLA OTWARTE

Dla każdego textarea/input określ maksymalną długość.

Przykładowo:

krótkie pole:
200 znaków

standardowa odpowiedź:
2000 znaków

dłuższa odpowiedź:
5000 znaków

Backend ma odrzucać lub bezpiecznie ograniczać wartości przekraczające limit.

Nie przyjmuj nieskończenie długich stringów.

6. SCHEMA VALIDATION

Backend ma mieć dokładny zestaw oczekiwanych kluczy.

Przykład:

[
  'age',
  'gender',
  'roles',
  'frustration'
]

Jeśli obiekt zawiera nieoczekiwane pola, możesz je ignorować albo odrzucić request.

Nie kopiuj automatycznie wszystkich kluczy obiektu data do arkusza.

Nie używaj:

Object.values(data)

jako sposobu budowania wiersza.

Zbuduj wiersz jawnie:

[
  new Date(),
  safeCellText_(data.age),
  ...
]

7. TIMESTAMP

Timestamp ma być generowany przez backend:

new Date()

Nie ufaj timestampowi przesłanemu przez przeglądarkę.

8. CONCURRENCY

Do zapisu użyj:

LockService.getScriptLock()

i rozsądnego waitLock().

Lock ma być zawsze zwalniany w finally.

9. DOUBLE SUBMIT

Po stronie frontendu:

- po kliknięciu Submit natychmiast disable button
- pokaż stan "Wysyłanie..."
- ponownie odblokuj przycisk wyłącznie jeśli backend zwróci błąd

Po sukcesie nie pozwalaj ponownie wysłać tego samego formularza jednym kliknięciem.

10. ANTYSPAM

Dodaj ukryty honeypot.

Jeżeli honeypot jest wypełniony:

- nie zapisuj danych
- nie ujawniaj botowi szczegółowego błędu

Jeżeli formularz ma być publiczny w internecie, opisz dodatkowo opcjonalny wariant z Cloudflare Turnstile/CAPTCHA.

Jeśli używasz Turnstile:

- SECRET KEY wyłącznie w Script Properties
- secret nigdy nie trafia do Index.html
- weryfikacja tokenu po stronie Code.gs
- dodaj scope external_request tylko wtedy, gdy faktycznie jest wymagany

Nie dodawaj zewnętrznych usług, jeśli formularz ma działać tylko wewnątrz organizacji i nie są potrzebne.

11. XSS

Nie wstawiaj danych użytkownika do DOM poprzez:

innerHTML

Jeżeli frontend musi wyświetlić tekst użytkownika, korzystaj z:

textContent

Nie generuj HTML-a na podstawie danych respondenta.

12. SEKRETY

Index.html traktuj jako publiczny.

Nie umieszczaj tam:

- OAuth tokenów
- API secrets
- haseł
- private keys
- Spreadsheet ID, jeśli nie jest potrzebne frontendowi
- wartości Script Properties

Nigdy nie przekazuj do klienta:

ScriptApp.getOAuthToken()

Jeśli jakikolwiek sekret jest potrzebny, przechowuj go w Script Properties i używaj tylko w Code.gs.

13. LOGI

Nie rób:

Logger.log(data)

dla całej odpowiedzi użytkownika.

Nie loguj niepotrzebnie danych osobowych ani pełnych treści formularzy.

Loguj jedynie informacje potrzebne diagnostycznie, np.:

- timestamp błędu
- kod błędu
- miejsce wystąpienia

Frontendowi zwracaj ogólny komunikat:

"Nie udało się zapisać odpowiedzi. Spróbuj ponownie."

Nie pokazuj respondentowi stack trace ani wewnętrznych informacji.

14. OAUTH SCOPES

Wygeneruj appsscript.json z JAWNIE określonymi minimalnymi oauthScopes.

Jeżeli aplikacja korzysta tylko z Google Sheets, nie dodawaj:

- Gmail
- Calendar
- Contacts
- Drive
- Docs
- Forms

ani innych usług.

Dla standardowego zapisu do istniejącego arkusza przez SpreadsheetApp użyj tylko zakresu niezbędnego do pracy z Sheets.

Wyjaśnij, że scope:

https://www.googleapis.com/auth/spreadsheets

umożliwia skryptowi pracę z arkuszami, do których konto wykonujące skrypt ma dostęp.

Nie sugeruj, że ten scope automatycznie ogranicza dostęp wyłącznie do jednego Spreadsheet ID.

15. KONTO WDRAŻAJĄCE

Jeżeli Web App ma działać jako:

Execute as → Me

wyjaśnij, że kod działa z uprawnieniami konta wdrażającego.

W środowisku firmowym preferuj:

DEDYKOWANE KONTO TECHNICZNE

np.:

forms-automation@firma.pl

które:

- ma dostęp tylko do potrzebnego arkusza / folderu
- nie korzysta z Gmaila jako normalnej skrzynki pracownika
- nie ma dostępu do poufnych zasobów, których aplikacja nie potrzebuje
- jest kontrolowane przez organizację
- ma MFA zgodne z polityką organizacji

Jeśli użytkownik korzysta ze swojego głównego konta z szerokimi uprawnieniami, wyraźnie ostrzeż, że blast radius jest większy.

16. NIE UŻYWAJ NIEPOTRZEBNYCH USŁUG

Nie używaj:

DriveApp
GmailApp
CalendarApp
ContactsApp

ani Advanced Services, jeżeli formularz ich nie potrzebuje.

Nie dodawaj usług "na przyszłość".

17. NIE UŻYWAJ EVAL

Nie używaj:

eval()
new Function()
dynamicznego wykonywania kodu

Nie wybieraj funkcji backendowej na podstawie stringa przesłanego przez użytkownika.

============================================================
ARKUSZ
============================================================

Funkcja setup_() ma być uruchamiana ręcznie przez właściciela z edytora Apps Script.

Nie może być potrzebna respondentowi.

setup_() ma:

- utworzyć arkusz, jeśli projekt ma go tworzyć automatycznie
- utworzyć nagłówki
- ostylować arkusz
- zamrozić pierwszy wiersz
- ustawić szerokości kolumn
- zapisać SPREADSHEET_ID w Script Properties
- nie tworzyć kolejnego arkusza, jeżeli property już wskazuje poprawny arkusz
- wypisać właścicielowi URL arkusza

Jeśli preferujesz jeszcze prostszy model, możesz zamiast automatycznego tworzenia arkusza poprosić użytkownika o ręczne utworzenie pustego Google Sheeta i jednorazowe wpisanie jego ID do Script Properties.

Backend nigdy nie ma przyjmować ID arkusza od respondenta.

============================================================
FORMULARZ / UX
============================================================

Pytania:

[TUTAJ WKLEJ PYTANIA]

Sam dobierz odpowiednie typy pól:

- radio
- checkbox
- textarea
- input
- select

Jeśli liczba pytań tego wymaga, podziel formularz na 2–4 logiczne etapy.

Dodaj:

- progress bar
- Dalej
- Wróć
- walidację kroku
- scroll do góry
- czytelne komunikaty błędów
- stan loading
- ekran sukcesu
- mobile responsive
- focus states
- podstawową dostępność klawiaturą

============================================================
BRANDING
============================================================

[TUTAJ WKLEJ BRANDING]

Odwzoruj branding możliwie dokładnie w HTML/CSS.

Cały CSS i JS mogą znajdować się w Index.html.

Nie rozbijaj frontendu na dodatkowe pliki, chyba że wyraźnie o to poproszę.

============================================================
DEPLOYMENT — INSTRUKCJA BEZPIECZNA
============================================================

Po wygenerowaniu kodu podaj BARDZO DOKŁADNĄ instrukcję wdrożenia.

Ma zawierać:

KROK 1

Utworzenie projektu Apps Script.

KROK 2

Wklejenie:

- Code.gs
- Index.html
- appsscript.json

KROK 3

Jak włączyć widoczność pliku appsscript.json:

Project Settings
→ Show "appsscript.json" manifest file in editor

KROK 4

Jak sprawdzić:

Overview
→ Project OAuth Scopes

i upewnić się, że nie pojawiły się niepotrzebne scope'y.

Jeśli pojawi się Gmail/Drive/Calendar bez powodu:
STOP.
Nie wdrażaj aplikacji, dopóki przyczyna nie zostanie usunięta.

KROK 5

Ręczne uruchomienie setup_().

Wyjaśnij dokładnie:

- jakie zgody pojawią się podczas autoryzacji
- których zgód się spodziewamy
- że niespodziewane zgody są sygnałem do zatrzymania procesu

KROK 6

Test deployment:

Deploy
→ Test deployments
→ Web app

Wyjaśnij różnicę między:

/dev
/exec

/dev służy do testowania najnowszego kodu przez osoby z prawem edycji.

/exec to konkretna opublikowana wersja produkcyjna.

KROK 7

Produkcja:

Deploy
→ New deployment
→ Web app

Dla PUBLICZNEGO anonimowego formularza:

Execute as → Me

Who has access → Anyone

ALE wyraźnie zaznacz, że "Anyone" wybieramy tylko wtedy, kiedy formularz faktycznie ma być publiczny.

Dla formularza WEWNĘTRZNEGO:

preferuj ograniczenie dostępu do użytkowników organizacji / domeny Workspace, jeśli dostępna konfiguracja na to pozwala.

KROK 8

Przed publikacją wykonaj testy:

- normalna odpowiedź
- brak wymaganego pola
- zmodyfikowana niedozwolona wartość
- checkbox z niedozwoloną wartością
- bardzo długi tekst
- tekst zaczynający się od =1+1
- tekst zaczynający się od +, -, @
- podwójne kliknięcie submit
- test mobile
- test incognito
- test kilku szybkich odpowiedzi

Test formula injection ma potwierdzić, że:

=1+1

jest zapisane jako tekst, a nie jako formuła dająca wynik 2.

KROK 9

Po wdrożeniu wyjaśnij:

Deploy
→ Manage deployments
→ Edit
→ New version
→ Deploy

aby aktualizować aplikację bez zmiany publicznego URL.

KROK 10

Podaj checklistę bezpieczeństwa do odhaczenia przed przekazaniem URL użytkownikom.

============================================================
CODE REVIEW
============================================================

Przed podaniem finalnego kodu wykonaj własny logiczny review i sprawdź:

- czy każde pole frontendowe odpowiada backendowi
- czy backend nie ufa frontendowi
- czy wszystkie dane użytkownika przechodzą przez sanitizację
- czy żadne dane użytkownika nie mogą zostać formułą
- czy enumy mają allowlisty
- czy helpery kończą się "_"
- czy frontend nie zna spreadsheet ID/sekretów
- czy żaden sekret nie występuje w HTML
- czy nie ma niepotrzebnych publicznych funkcji
- czy appsscript.json ma minimalne scope'y
- czy kod nie korzysta z usług Google, których nie potrzebuje
- czy LockService jest poprawnie zwalniany w finally
- czy przycisk Submit nie pozwala przypadkiem wysłać formularza wielokrotnie
- czy błędy nie ujawniają danych technicznych

Na samym końcu wypisz:

SECURITY REVIEW — PASS

i krótko napisz, co zostało zabezpieczone.

Jeżeli któregoś wymagania nie można bezpiecznie spełnić w Google Apps Script, powiedz to wprost zamiast udawać, że problem nie istnieje.
