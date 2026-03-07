"""Knowledge item: integration point mapping."""

title = "Mapowanie punktów integracji"

content = """
Mapowanie punktów integracji to inwentaryzacja wszystkich połączeń między komponentami systemu
oraz z systemami zewnętrznymi. Pozwala na planowanie testów integracyjnych i identyfikację
pojedynczych punktów awarii.

**Kontekst:** Każdy punkt integracji może być źródłem opóźnień, błędów lub awarii. Należy
udokumentować protokoły, timeouts, retry policy oraz fallback dla każdego połączenia.

**Kluczowe działania:**
1) Stwórz diagram lub listę wszystkich punktów integracji.
2) Dla każdego punktu udokumentuj: protokół, SLA, mechanizmy retry i circuit breaker.
3) Zidentyfikuj zależności krytyczne i ich wpływ na dostępność.
4) Zaplanuj testy integracyjne i chaos dla każdego krytycznego punktu.
5) Aktualizuj mapę przy zmianach architektury.
"""

version = "0.0.1"
