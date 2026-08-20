# Benchmarki, progi decyzyjne i anty-wzorce

## Metryki hooków per platforma

| Platforma | Metryka | Definicja | Słabo | Dobrze | Elita |
|---|---|---|---|---|---|
| Meta (wideo) | hook rate | 3-sekundowe odtworzenia / wyświetlenia | <15% | 25–30% | >40% |
| TikTok | hook rate | próg 2 s (wyniki naturalnie wyższe) | <20% | ~30% | 40–45% |
| TikTok | retencja 3 s | % widzów po 3 sekundach | <40% | ~70% | >85% |
| Meta/TikTok | hold rate | ThruPlays / 3-sekundowe odtworzenia | – | – | – |
| Short-form | rewatch rate | powtórne odtworzenia | – | – | >15–20% |
| LinkedIn | długość posta | znaki | <400 | 1301–2500 | – |

Zasady porównywania:

- Meta (3 s) i TikTok (2 s) NIEPORÓWNYWALNE wprost. Najlepszy benchmark = mediana własnego konta.
- Cold vs warm: prospecting thumbstop 18–28% (mediana ~22%), retargeting 30–45% (mediana ~36%).
  ~14 p.p. różnicy robi audytorium, nie kreacja. Porównuj w tej samej temperaturze.
- Reels zwykle 5–10 p.p. niżej niż Feed.

## Progi decyzyjne

- Retencja <50% po 3 s → przepisz hook (samo otwarcie).
- Hook rate <25% (Meta) / <30% (TikTok) na sensownej próbce → NOWA kreacja, nie optymalizacja.
- Checkpointy retencji do re-hooków: 3 s (~70%), 15 s (~60%), 30 s (~50%).
- Testuj 3 warianty hooka na treść; minimum 30 dni albo do istotności statystycznej.
- Po Andromedzie (Meta) silny hook = tańsze CPM – jakość kreacji liczy się w aukcji.

## Anty-wzorce – każdy hook przepuść przez tę listę

1. **Engagement bait** – „LIKE if…", „Tag 3 friends", „Comment YES", vote/share-baiting.
   Meta demotuje od XII 2017, w 25+ językach, modelem ML; recydywa = systemowa utrata zasięgu.
   Wyjątki chronione: zbiórki, zaginione osoby, prośby o poradę.
2. **Clickbait / luka bez payoffu** – hook obiecuje, treść nie domyka. Różnica: dobry curiosity
   gap DOMYKA pętlę wartością; clickbait otwiera lukę i zostawia. Jeśli wsad nie zawiera payoffu
   dla hooka – hook odpada.
3. **Wypalone formuły** – „You won't believe…", nadużyte „POV:", nadmiar „Stop scrolling",
   „Unpopular opinion" jako rytuał. Habituacja wygasza orienting response.
4. **Przesadne obietnice** – niszczą zaufanie i podnoszą churn; persuazja to mnożnik
   (słaba oferta × mocna persuazja = szybszy churn). Stosuj regułę Caplesa: liczba wiarygodna
   bije liczbę imponującą.
5. **Dark patterns** – fałszywe liczniki, fikcyjna dostępność, presja bez pokrycia.
   DSA art. 25 (od 17.02.2024) zakazuje interfejsów manipulujących decyzją; UOKiK ukarał
   Amazon kwotą 31,85 mln zł m.in. za licznik odliczający bez gwarancji dostawy.
   Scarcity/FOMO proponuj wyłącznie z prawdziwym ograniczeniem.
6. **Mit „8 sekund uwagi"** – zdyskredytowany; nie używaj go w uzasadnieniach hooków.

Zasada nadrzędna: otwieraj luki, które domykasz wartością. Manipulacja odbierająca świadomy
wybór to ryzyko zasięgowe (algorytm) i prawne (DSA, UOKiK) – nie proponuj jej nigdy.
