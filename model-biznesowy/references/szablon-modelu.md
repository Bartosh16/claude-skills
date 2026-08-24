# Szablony plików wyjściowych

Dwa pliki: `model-biznesowy.md` i `plan-b.md`. Każde założenie niepoparte rozmową albo danymi dostaje znacznik `[NIEZWALIDOWANE]` bezpośrednio w miejscu, w którym stoi – nie zbiorczo na końcu.

Sekcje wypełnia się treścią, nie parafrazą pytań. Nagłówki zostają, instrukcje w nawiasach kwadratowych znikają.

## Szablon `model-biznesowy.md`

```markdown
# Model biznesowy – [imię lub nazwa]

**Data:** [data]
**Podstawa dowodowa:** [ile rozmów, z kim, w jakim okresie; albo jawnie: brak researchu]

## Streszczenie w pięciu zdaniach

[Kto jest klientem, jaki problem rozwiązujesz, jak za to płaci, ile potrzeba klientów do progu, jakimi dwoma kanałami do nich docierasz. Bez przymiotników.]

## Model w skrócie

| Element | Treść |
|---|---|
| Segment | |
| Problem | |
| Rozwiązanie | |
| Model płatności | |
| Cena | |
| Kanał główny | |
| Kanał wspierający | |
| Próg rentowności | [ilu klientów miesięcznie] |

## Business Model Canvas

### 1. Segment klientów
[Opis segmentu. Kto płaci, kto używa, jeżeli to różne osoby. Gdzie ci ludzie fizycznie są – trzy konkretne miejsca. Kogo segment wyklucza.]

**Dowód:** [z których rozmów to wynika]

### 2. Propozycja wartości
[Zmiana w sytuacji klienta, nie lista cech. Co robi dzisiaj zamiast tego. O ile lepiej.]

**Wynik testu podstawienia:** [co się dzieje, gdy wstawisz nazwę konkurenta]
**Dowód:** [cytaty z rozmów, dosłowne]

### 3. Strumienie przychodu

| Strumień | Model płatności | Cena | Częstotliwość | Klientów miesięcznie | Przychód |
|---|---|---|---|---|---|

[Uzasadnienie ceny: od czego wyszła. Czy ktoś z segmentu już zapłacił komuś za rozwiązanie tego problemu – ile.]

### 4. Kanały
[Dotarcie, sprzedaż, dostawa – rozdzielone. Szczegóły kanałów dotarcia w sekcji „Plan dotarcia” niżej.]

### 5. Relacje z klientami
[Rodzaj relacji. Koszt obsługi jednego klienta w godzinach miesięcznie. Co sprawia, że klient zostaje.]

### 6. Zasoby kluczowe
[Co masz. Czego brakuje – z kosztem i czasem zdobycia. Pojedynczy punkt awarii.]

### 7. Działania kluczowe

| Koszyk | Co konkretnie | Godzin tygodniowo |
|---|---|---|
| Zdobywanie | | |
| Dowożenie | | |
| Utrzymanie | | |
| **Razem** | | |

[Suma zestawiona z dostępnym czasem z wywiadu.]

### 8. Partnerzy kluczowi
[Kto, po co, co się dzieje, gdy zniknie.]

### 9. Struktura kosztów

| Koszt | Typ | Kwota miesięcznie |
|---|---|---|

**Miesięczny koszt minimalny:** [kwota]
**Koszt alternatywny twojego czasu:** [kwota, jeżeli rezygnujesz z innego dochodu]
**Runway:** [ile miesięcy wytrzymasz bez przychodu]

## Arytmetyka

| Pozycja | Wartość |
|---|---|
| Próg przeżycia (miesięcznie) | |
| Koszty stałe | |
| Potrzebny przychód | |
| Marża na kliencie | |
| **Klientów miesięcznie do progu** | |
| Godzin na obsługę jednego klienta | |
| **Godzin miesięcznie przy tej liczbie klientów** | |
| Godzin dostępnych | |

**Werdykt:** [Wychodzi albo nie wychodzi. Jeżeli nie – co konkretnie trzeba zmienić: cena w górę, zakres w dół, inny model.]

## Plan dotarcia

### Kanał główny: [nazwa]
- Dlaczego ten: [wynika z rozmów – gdzie segment szuka informacji]
- Nakład: [ile czasu tygodniowo, ile pieniędzy miesięcznie]
- Pierwszy sygnał spodziewany: [kiedy]
- Metryka: [co mierzysz – rozmowy, zapisy, sprzedaż; nie wyświetlenia]
- **Próg wyłączenia:** jeżeli do [data] przy [nakład] nie będzie [liczba i metryka], wyłączam i przechodzę na [co].

### Kanał wspierający: [nazwa]
[Ta sama struktura.]

## Pierwsze 90 dni

### Dni 1–30
- Cel: [jeden]
- Deliverable: [co fizycznie powstaje]
- Metryka: [liczba]
- Czego NIE robisz: [lista rzeczy odłożonych]

### Dni 31–60
[Ta sama struktura.]

### Dni 61–90
[Ta sama struktura. Ostatnia faza kończy się mierzalnym wynikiem – pierwszy klient, pierwsze X zł, N rozmów.]

## Ryzyka

| Ryzyko | Prawdopodobieństwo | Skutek | Co robisz zawczasu |
|---|---|---|---|

[Minimum trzy. Obowiązkowo: pojedynczy punkt awarii z bloku 6 i zależność od platformy z bloku 8.]

## Co jest niezwalidowane

[Lista wszystkich założeń oznaczonych [NIEZWALIDOWANE] w dokumencie, z jednym zdaniem, jak każde sprawdzić i ile to zajmie. Jeżeli lista jest pusta, bo research się odbył – napisz to wprost.]
```

## Szablon `plan-b.md`

```markdown
# Plan B – [imię lub nazwa]

Plan B nie jest innym pomysłem na biznes. Jest zwrotem wykonanym w momencie, gdy dane mówią, że model A nie działa – z zachowaniem tego, co model A zdążył zbudować.

## Warunki wyzwalające

Przełączasz się, gdy zajdzie którykolwiek z tych warunków. Każdy z liczbą i datą.

| # | Warunek | Termin sprawdzenia | Co go potwierdza |
|---|---|---|---|
| 1 | [np. mniej niż 3 klientów płacących] | [data] | [skąd wiesz] |
| 2 | | | |
| 3 | | | |

[Warunek bez liczby i daty nie jest warunkiem. „Jeżeli nie będzie szło” nie wyzwoli niczego, bo zawsze da się powiedzieć, że jeszcze chwilę.]

## Co przechodzi z modelu A

[Aktywa, które zostają niezależnie od zwrotu. Zwykle: lista mailowa, opublikowane treści, relacje z rozmówcami z researchu, wypracowane kompetencje, rozpoznawalność, narzędzia. To jest powód, dla którego plan B nie jest startem od zera.]

## Zwrot

**Co się zmienia:** [zwykle jedna rzecz – segment, model płatności albo kanał. Nie wszystko naraz.]

**Nowy model w skrócie:**

| Element | Model A | Model B |
|---|---|---|
| Segment | | |
| Propozycja wartości | | |
| Model płatności | | |
| Kanał główny | | |

**Dlaczego to ma szansę zadziałać tam, gdzie A nie zadziałał:** [konkretnie, na podstawie tego, co pokazał nieudany model A]

## Pierwsze 30 dni po przełączeniu

[Trzy do pięciu kroków. Konkretnie, z terminami.]

## Punkt bez powrotu

[Kiedy przestajesz próbować w ogóle i co wtedy robisz. Może to być powrót na etat, zmiana branży albo odłożenie tematu na rok. Nazwanie tego z góry jest tańsze niż dowiadywanie się o tym po fakcie, na dnie oszczędności.]
```
