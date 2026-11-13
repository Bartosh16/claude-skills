# /ocena-pomyslu-apki

Sprawdza pomysł na aplikację (mobilną, webową, SaaS, mikronarzędzie AI) na danych z sieci, nie na entuzjazmie. Wynik ma być na tyle twardy, żeby dało się na jego podstawie zrezygnować.

## Co robi, krok po kroku

1. **Konkurencja** – 5–10 istniejących produktów: wydawca, model cenowy, ocena, liczba ocen, data ostatniej aktualizacji.
2. **Kto jest martwy** – apki porzucone przez twórców i powód, dla którego padły.
3. **Co ludzie mówią** – negatywne opinie i miejsca, w których ludzie z tym problemem w ogóle rozmawiają.
4. **Luka** – którą dziurą da się wejść.
5. **Dowód popytu** – czy ktoś już płaci za rozwiązanie tego problemu.
6. **Rachunek** – ile kosztuje obsługa jednego użytkownika i ile osób musi zapłacić, żeby to się spięło.
7. **Werdykt** – z kryterium wyjścia: liczba i termin, po których projekt się zamyka.

Na starcie skill pyta o trzy rzeczy: pomysł, Twoją przewagę (do kogo masz dziś dostęp) i budżet z czasem. Bez przewagi nie da się ocenić dystrybucji, więc nie zaczyna z pustym punktem 2.

## Na czym stoi

Na badaniu 41 wywiadów z kanału Starter Story i danych RevenueCat (State of Subscription Apps 2026): nikt nie odpada na kodzie, wszyscy odpadają na dystrybucji, koszcie jednostkowym i braku płacącego klienta. Konwersja z darmowego na płatne w tej próbie: 0,7–2,5%.

## Wymagania

WebSearch i WebFetch (Claude Code albo Claude z dostępem do sieci).

## Instalacja skilla

```
cp -r ocena-pomyslu-apki ~/.claude/skills/
```

Na Windows: `C:\Users\<user>\.claude\skills\`.

Potem w Claude Code: „oceń mój pomysł na apkę” i opisz pomysł w dwóch zdaniach.

## Para z /model-biznesowy

Ten skill odpowiada na pytanie „czy na tę apkę jest miejsce na rynku”. `/model-biznesowy` odpowiada na „jak na tym zarabiać i co, jeśli nie wyjdzie”. Najpierw ocena pomysłu, potem model.
