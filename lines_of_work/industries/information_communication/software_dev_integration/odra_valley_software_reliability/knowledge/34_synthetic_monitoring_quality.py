"""Knowledge item: synthetic monitoring quality."""

title = "Jakość monitoringu syntetycznego"

content = """
Monitoring syntetyczny polega na symulowaniu transakcji użytkownika w regularnych
interwałach, aby wykrywać awarie i degradację z perspektywy użytkownika końcowego.
Jakość tych testów wpływa bezpośrednio na czas wykrycia incydentów.

**Kontekst:** Syntetyczne transakcje muszą odzwierciedlać krytyczne ścieżki biznesowe,
wykonywać się z realistyczną częstotliwością i geograficznie rozproszonych lokalizacji.
Słabo zaprojektowane testy syntetyczne dają fałszywe alarmy lub przeoczenia.

**Kluczowe działania:**
1) Mapuj krytyczne ścieżki użytkownika na scenariusze syntetyczne.
2) Ustal częstotliwość i lokalizacje zgodnie z profilem ruchu i SLA.
3) Zdefiniuj progi alertów (np. czas odpowiedzi, procent sukcesu) i powiąż z
   error budget.
4) Przeglądaj skuteczność: ile incydentów wykryto przez syntetykę vs. inne źródła.
5) Aktualizuj scenariusze przy zmianie funkcjonalności lub nowych ścieżkach.
"""

version = "0.0.1"
