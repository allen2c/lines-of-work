"""Knowledge item: chaos experiments design."""

title = "Projektowanie eksperymentów chaosu"

content = """
Chaos engineering polega na celowym wprowadzaniu awarii w systemie, aby
zweryfikować odporność i zdolność do odzyskania. Eksperymenty muszą być
starannie zaprojektowane, aby nie powodować niepotrzebnych szkód.

**Kontekst:** Narzędzia takie jak Chaos Monkey, Gremlin lub własne skrypty
symulują awarie sieci, zatrzymanie węzłów, opóźnienia. Eksperymenty wykonuje
się w środowiskach stage lub wyizolowanych fragmentach produkcji.

**Kluczowe działania:**
1) Zdefiniuj hipotezę: co chcesz zweryfikować (np. „system przeżyje utratę
   jednego węzła”).
2) Wybierz scope: które komponenty, w jakim środowisku.
3) Ustal kryteria sukcesu i abort (np. automatyczne wyłączenie przy wzroście
   error rate powyżej X%).
4) Udokumentuj wyniki i włącz wnioski do planów naprawczych.
"""

version = "0.0.1"
