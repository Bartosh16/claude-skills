# Ubezpieczenia – kryteria YMYL według SQRG

Kategoria SQRG: YMYL Financial Security (2.3). Osobny plik obok finansów, bo to specjalizacja Daniela i branża z własnym nadzorem (KNF) oraz własnym typem decyzji konsumenckich: kupujesz obietnicę wypłaty na wypadek szkody, której nie możesz przetestować przed zakupem.

## Kiedy ta branża jest YMYL, a kiedy nie

| Werdykt | Przykładowe tematy |
|---|---|
| Wyraźnie YMYL | wybór i zakup polisy (OC/AC, mieszkanie, życie, NNW, turystyczne, zdrowotne), zakres ochrony i wyłączenia, ubezpieczenia inwestycyjne (unit-linked), zgłaszanie i likwidacja szkody, odmowa wypłaty i odwołania, rezygnacja z polisy |
| Może być YMYL | edukacja „jak działa ubezpieczenie”, trendy rynku ubezpieczeń, treści B2B o marketingu i sprzedaży ubezpieczeń, kariera agenta |
| Raczej nie YMYL | historia ubezpieczeń, ciekawostki branżowe, treści rekrutacyjne bez porad finansowych |

Test: czy czytelnik może na podstawie tekstu kupić, zmienić, wypowiedzieć polisę albo poprowadzić sprawę szkodową? Jeśli tak – wyraźnie YMYL. Uwaga na treści B2B: artykuł o content marketingu ubezpieczeń jest zwykle „może być YMYL” – pisze o branży YMYL, ale nie doradza konsumentowi.

## Wymagane sygnały

- **Typ ekspertyzy** (SQRG 3.4.1): rekomendacja polisy lub interpretacja zakresu ochrony wymaga ekspertyzy (agent, broker, praktyk likwidacji szkód) albo oparcia w źródłach pierwotnych. Relacja klienta „jak przebiegła moja likwidacja szkody” jest wartościowa jako doświadczenie, dopóki nie przechodzi w poradę.
- **OWU jako źródło pierwotne**: twierdzenia o zakresie, wyłączeniach i sumach z ogólnych warunków ubezpieczenia konkretnego produktu, nie z materiałów sprzedażowych. Przy porównaniach – data i wersja OWU.
- **Kto pisze i w jakiej roli** (SQRG 2.5.2, 3.4): agent na prowizji, broker, porównywarka z afiliacją, towarzystwo – każda z tych ról ma konflikt interesów do ujawnienia. Brak ujawnienia = podważony Trust.
- **Rozdzielenie opisu od rekomendacji**: „polisa X obejmuje Y” vs „wybierz polisę X”. Rekomendacja wymaga kontekstu: dla kogo, przy jakich potrzebach, z jakimi wyłączeniami.
- **Aktualność** (SQRG 18.0): stawki, taryfy, przepisy (np. kary za brak OC) zmieniają się co roku – data przy liczbach.
- **Odpowiedzialność** (SQRG 4.5.1): formularze zbierające dane do wyceny (PESEL, adres, majątek) wymagają pełnej informacji o administratorze i kontaktu.

## Typowe braki

1. Porównanie polis bez wersji i daty OWU – tabela wygląda konkretnie, ale nie wiadomo, co porównano.
2. Autor bez roli: nie wiadomo, czy pisze agent, marketer czy anonim (SQRG 2.5.2, 5.5).
3. Nieujawniona afiliacja przy linkach do porównywarek i wniosków (SQRG 3.4).
4. „Najlepsze ubezpieczenie na życie” bez określenia, dla kogo najlepsze i wg jakich kryteriów.
5. Pominięcie wyłączeń odpowiedzialności przy opisie zalet produktu – jednostronny obraz to problem Trust.
6. Nieaktualne kwoty (kary za brak OC, sumy gwarancyjne) podane jako obowiązujące (SQRG 5.2, 18.0).
7. Straszenie szkodą jako jedyny argument sprzedażowy zamiast rzetelnego opisu ryzyka.

## Czerwone flagi Lowest

- Wprowadzanie w błąd co do ochrony: sugerowanie, że polisa pokrywa coś, czego OWU wyłącza (SQRG 4.4 – harmfully misleading w decyzji finansowej).
- Strona udająca niezależny ranking, w rzeczywistości sprzedająca jedno towarzystwo (4.5.3 – zwodniczy cel).
- Zbieranie danych osobowych „do wyceny” bez administratora i celu (4.5.1, 4.5.5).
- Fikcyjny „ekspert ubezpieczeniowy” w biogramie, zmyślone kwalifikacje (4.5.3).
- Namawianie do rezygnacji z ochrony (np. wypowiedzenia OC) wbrew przepisom lub interesowi konsumenta.

## Przykłady z SQRG

- Ubezpieczenia nie mają w SQRG dedykowanych przykładów – klasyfikuj przez YMYL Financial Security (2.3): decyzja o polisie to decyzja o stabilności finansowej rodziny.
- Analogia z 3.4.1 (emerytura): recenzja usługi z pierwszej ręki OK, porada „którą polisę wybrać” wymaga ekspertyzy.
- Analogia z 2.3 (e-commerce): zakup polisy przez internet bliżej „leków na receptę” niż „ołówków” – produkt o poważnych konsekwencjach.
- Wymogi informacyjne dla witryn transakcyjnych (4.5.1, 5.5) obejmują kalkulatory i formularze wycen.

## Granice

- **Zgodność prawna (UDU, Zasady KNF) to nie ten skill.** Compliance treści ubezpieczeniowych sprawdza skill `anthropic-skills:insurance-content` – w raporcie odeślij do niego, nie powtarzaj jego reguł. Ten plik pokrywa wyłącznie warstwę jakościową Google.
- Liczby i stawki → `/fact-checker`. Głębokie E-E-A-T → `/eeat-analyzer`.
