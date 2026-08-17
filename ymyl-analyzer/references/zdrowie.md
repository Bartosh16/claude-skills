# Zdrowie – kryteria YMYL według SQRG

Kategoria SQRG: YMYL Health or Safety (2.3). Obejmuje zdrowie fizyczne, psychiczne i emocjonalne, leki i suplementy, dietę w kontekście zdrowotnym, ciążę, choroby, pierwszą pomoc.

## Kiedy ta branża jest YMYL, a kiedy nie

| Werdykt | Przykładowe tematy |
|---|---|
| Wyraźnie YMYL | objawy chorób i kiedy jechać na SOR, dawkowanie i interakcje leków, leczenie nowotworów, szczepienia, zdrowie psychiczne i kryzysy, dieta przy chorobie (cukrzyca, nadciśnienie), ciąża i leki w ciąży, suplementy o działaniu farmakologicznym, pierwsza pomoc |
| Może być YMYL | ogólny fitness i plany treningowe, „zdrowe nawyki”, odchudzanie bez chorób współistniejących, kosmetyki o działaniu pielęgnacyjnym, jak często wymieniać szczoteczkę |
| Raczej nie YMYL | lifestyle wellness bez twierdzeń zdrowotnych, relacje z treningów, moda sportowa, przepisy kulinarne bez claimów leczniczych |

Test: czy zła informacja może opóźnić leczenie, zmienić dawkowanie, odwieść od lekarza albo zachęcić do ryzykownej praktyki? Jeśli tak – wyraźnie YMYL.

## Wymagane sygnały

- **Typ ekspertyzy** (SQRG 3.4.1): informacja i porada medyczna wymagają formalnej ekspertyzy – autor z kwalifikacjami medycznymi, konsultacja merytoryczna lub treść w całości oparta na źródłach eksperckich i z nimi zgodna. Relacja z własnej choroby („jak żyję z cukrzycą”) może mieć wysokie E-E-A-T bez lekarza, o ile nie doradza i nie przeczy konsensusowi.
- **Zgodność z konsensusem** (SQRG 3.2, 4.4): twierdzenia zgodne ze stanowiskami towarzystw naukowych, WHO, agencji leków (w Polsce: URPL, NIZP PZH-PIB, konsultanci krajowi). Każde odstępstwo od konsensusu wymaga wyraźnego oznaczenia jako hipoteza lub badanie wstępne.
- **Źródła pierwotne**: badania, wytyczne kliniczne, charakterystyki produktów leczniczych – nie blogi i agregatory.
- **Świeżość** (SQRG 18.0): zalecenia medyczne się zmieniają; data publikacji i przeglądu treści, aktualizacja przy zmianie wytycznych.
- **Rozdzielenie informacji od porady**: opis choroby to co innego niż „co masz zrobić”. Porada indywidualna wymaga zastrzeżenia o konsultacji z lekarzem.
- **Bezpieczne ramy**: przy tematach kryzysowych (depresja, samookaleczenia) numer wsparcia i zachęta do pomocy profesjonalnej.

## Typowe braki

1. Brak autora lub autor-widmo bez kwalifikacji przy treści doradczej (SQRG 4.5.2, 5.1).
2. Twierdzenia zdrowotne bez źródła albo ze źródłem wtórnym (portal o zdrowiu cytuje portal o zdrowiu).
3. Brak daty publikacji i aktualizacji przy zaleceniach, które mogły się zmienić.
4. Mieszanie relacji z doświadczenia z poradą medyczną bez oznaczenia granicy (SQRG 3.4.1).
5. Suplement lub zabieg opisany językiem skuteczności leku, bez zastrzeżeń.
6. Brak disclaimera „treść nie zastępuje konsultacji lekarskiej” przy treści doradczej.
7. Tytuł obiecujący więcej niż treść („najzdrowsze jedzenie ŚWIATA przedłuży Ci życie!”) – SQRG 5.2.

## Czerwone flagi Lowest

- Porady sprzeczne z konsensusem medycznym, mogące poważnie zaszkodzić lub odwieść od leczenia ratującego życie (SQRG 4.2) – np. „cytryny leczą raka” (4.4).
- Zachęcanie do samoleczenia w stanach wymagających lekarza, bagatelizowanie objawów alarmowych.
- Treści pro-ana, promocja samobójstw, instrukcje samookaleczeń (4.2).
- Fałszywe kwalifikacje medyczne twórcy, fikcyjny „lekarz” w biogramie (4.5.3).
- Sprzedaż „cudownych” terapii pod pozorem treści informacyjnej (4.5.3 – zwodniczy cel).

## Przykłady z SQRG

- Objawy zawału serca jako wzorcowy temat osi B – szkoda przy niedokładności (2.3).
- „Kiedy jechać na SOR” = clear YMYL; „jak często wymieniać szczoteczkę” = may be YMYL (2.3, tabela).
- Sen w ciąży: triki z poduszkami od matek OK, leki nasenne w ciąży tylko od ekspertów (3.4.1).
- Q&A o bólu w klatce piersiowej z poradą „weź aspirynę i pal dalej” = Lowest (9.3).
- Q&A „ile żyją chorzy na raka” oparte na doświadczeniach rodzin = Highest, bo fokus na doświadczenie, nie poradę (9.3).
- Strona o objawach odwodnienia bez śladów ekspertyzy medycznej = niewiarygodna (14.0).
- Zakup leków na receptę = clear YMYL w e-commerce (2.3).

## Granice

- Weryfikację konkretnych liczb i twierdzeń medycznych rób skillem `/fact-checker` – ten audyt ocenia obecność i jakość sygnałów, nie prawdziwość każdej liczby.
- Głęboki audyt sygnałów E-E-A-T (information gain, encje, autorytet tematyczny) → `/eeat-analyzer`.
