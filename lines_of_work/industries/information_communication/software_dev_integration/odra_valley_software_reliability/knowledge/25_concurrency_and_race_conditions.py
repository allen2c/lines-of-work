"""Knowledge item: concurrency and race conditions."""

title = "Współbieżność i warunki wyścigu"

content = """
Warunki wyścigu występują, gdy wiele wątków lub procesów modyfikuje współdzielony stan
bez odpowiedniej synchronizacji. Prowadzą do nieprzewidywalnych błędów trudnych do
odtworzenia.

**Kontekst:** W systemach wysokiej przepustowości współbieżność jest nieunikniona. Należy
identyfikować krytyczne sekcje i stosować mechanizmy blokowania lub lock-free algorytmy.

**Kluczowe działania:**
1) Zmapuj współdzielony stan i punkty dostępu.
2) Zidentyfikuj potencjalne race conditions (np. double-spend, lost update).
3) Testuj pod obciążeniem z wieloma równoległymi żądaniami.
4) Weryfikuj użycie mutexów, semaforów lub transakcji bazodanowych.
5) Rozważ wzorce optymistycznej blokady lub wersjonowania.
"""

version = "0.0.1"
