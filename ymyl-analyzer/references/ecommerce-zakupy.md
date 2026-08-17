# E-commerce i zakupy – kryteria YMYL według SQRG

Kategoria SQRG: zależnie od produktu i etapu – YMYL Financial Security (transakcje, dane płatnicze) lub YMYL Health or Safety (produkty mogące zaszkodzić). Obejmuje sklepy, strony produktowe, recenzje i rankingi zakupowe.

## Kiedy ta branża jest YMYL, a kiedy nie

| Werdykt | Przykładowe tematy |
|---|---|
| Wyraźnie YMYL | checkout i dane płatnicze (zawsze), zakup leków i suplementów, foteliki dziecięce i produkty bezpieczeństwa, elektronarzędzia i chemia, drogie zakupy angażujące oszczędności, recenzje produktów zdrowotnych |
| Może być YMYL | recenzja auta, sprzętu AGD, elektroniki – duże zakupy, ale ludzie radzą się też znajomych (SQRG 2.3) |
| Raczej nie YMYL | zakup ołówków i innych przedmiotów codziennych, recenzje gadżetów, ubrań, dekoracji |

Test z SQRG 2.3 (wiersz e-commerce): „rozważ produkt – czy może wyrządzić istotną szkodę?”. Leki na receptę = clear, auto = may be, ołówki = nie. Niezależnie od produktu: sama transakcja (płatność, dane osobowe) zawsze podnosi wymagania Trust (SQRG 3.4, 4.5.1).

## Wymagane sygnały

- **Trust transakcyjny** (SQRG 3.4): bezpieczne płatności, rzetelna obsługa klienta. Strona z płatnościami bez satysfakcjonującej obsługi klienta = Low (5.5); bez żadnych informacji o właścicielu = Lowest (4.5.1).
- **Dane sklepu**: pełne dane podmiotu, kontakt, polityka zwrotów i reklamacji – łatwe do znalezienia, nie ukryte w stopce regulaminu.
- **Uczciwość recenzji** (SQRG 3.4): recenzja ma pomagać w decyzji, nie tylko sprzedawać. Recenzent z doświadczeniem z produktem = wartość (Experience); recenzja od producenta lub opłaconego influencera bez oznaczenia = konflikt interesów podważający Trust.
- **Realne testowanie** (SQRG 4.5.3): deklaracja „testowaliśmy” musi być prawdziwa – fałszywe twierdzenie o niezależnych testach to zwodniczy cel = Lowest. Ranking z parafraz cudzych recenzji bez własnego wkładu = Low (5.2.1: „listy najlepszych z istniejących recenzji”).
- **Afiliacja ujawniona**: linki prowizyjne oznaczone; użycie afiliacji samo w sobie jest OK (SQRG 4.6.4 wprost dopuszcza właściwie oznaczone linki afiliacyjne).
- **Aktualność ofert** (SQRG 18.0): ceny i dostępność z datą; nieaktualne ceny podane jako bieżące wprowadzają w błąd.

## Typowe braki

1. Ranking „top 10” sklejony z cudzych recenzji, bez śladu kontaktu z produktem (SQRG 5.2.1).
2. Nieoznaczona afiliacja przy każdym linku „sprawdź cenę”.
3. Recenzja bez wad produktu – jednostronność podważa uczciwość (SQRG 3.4).
4. Strona produktowa suplementu z twierdzeniami zdrowotnymi bez źródeł (krzyżuje się ze `zdrowie.md` – załaduj oba pliki).
5. Brak polityki zwrotów i danych podmiotu przy sklepie (SQRG 5.5).
6. Ceny bez daty ważności w treściach porównawczych.
7. Opinie klientów bez śladu weryfikacji, podejrzanie jednorodne (SQRG 3.3.2 – liczy się treść recenzji, nie liczba gwiazdek).

## Czerwone flagi Lowest

- Sklep bez możliwości kontaktu przy transakcjach finansowych (SQRG 4.5.1).
- Fałszywe recenzje i testimoniale, fałszywa deklaracja testowania produktów (4.5.3).
- Fałszywy sklep stacjonarny (zmyślony adres, zdjęcia) dla uwiarygodnienia (4.5.3).
- Wiarygodne doniesienia o oszustwach: klienci płacą i nie dostają towaru (3.3.2, 4.5.2 – skrajnie negatywna reputacja).
- Strona „recenzencka” istniejąca wyłącznie dla kliknięć w monetyzowane linki, z celowo mylącymi informacjami (4.5.3).
- Sprzedaż produktów niebezpiecznych lub obchodzących regulacje (np. leki na receptę bez recepty) – 2.3 + 4.2.

## Przykłady z SQRG

- Wiersz e-commerce tabeli 2.3: leki na receptę / recenzja auta / ołówki.
- Sklep z placem zabaw dla dzieci: wygląda porządnie, ale reputacja ujawnia oszustwa finansowe = Lowest dla całej witryny (3.3.3, 4.5.2).
- Q&A „czy Roomba poradzi sobie z sierścią” z doświadczeniami wielu użytkowników = High (9.3) – wzór wartościowej treści zakupowej z Experience.
- Recenzje produktów wymagają „przynajmniej pewnego poziomu Trust” nawet poza YMYL (7.3).
- Test funkcjonalności: rater ma włożyć produkt do koszyka i sprawdzić, czy sklep działa (3.2) – audytując sklep, sprawdź działanie ścieżki zakupowej, jeśli masz dostęp.

## Granice

- Deklarowane parametry produktów → `/fact-checker`.
- Produkty zdrowotne: załaduj równolegle `zdrowie.md`; produkty finansowe → `finanse.md`; polisy → `ubezpieczenia.md`.
- Głębokie E-E-A-T → `/eeat-analyzer`.
