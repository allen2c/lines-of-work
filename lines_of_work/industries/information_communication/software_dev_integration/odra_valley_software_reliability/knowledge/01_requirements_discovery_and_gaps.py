"""Knowledge item: requirements discovery and gaps."""

title = "Odkrywanie wymagań i luki"

content = """
Odkrywanie wymagań i identyfikacja luk stanowi fundament planowania niezawodności oprogramowania.
Zespół musi zrozumieć, co system ma osiągać, jakie są granice akceptowalnego ryzyka oraz gdzie
mogą występować niejasności między interesariuszami a implementacją.

**Kontekst:** W środowiskach wysokiej dostępności i dużego obciążenia niejednoznaczne wymagania
prowadzą do błędów w produkcji. Należy ustalić mierzalne kryteria sukcesu (np. czas wykrycia
awarii, czas odtworzenia) oraz powiązać je z celami biznesowymi.

**Kluczowe działania:**
1) Zdefiniuj kryteria sukcesu za pomocą wskaźników ilościowych.
2) Ustal workflow dla planowania, testowania, monitorowania i weryfikacji.
3) Stwórz checklistę powtarzalnych testów oraz procedury śledzenia defektów.
4) Wykorzystuj logi, metryki i trace do potwierdzenia, że zmiany redukują ryzyko.
5) Kończ każdą iterację jasną oceną: system spełnia kryteria czy wymaga dalszej pracy.

**Kryteria akceptacji:** Praca jest uznana za zakończoną, gdy istnieje dokumentacja założeń,
skrypty testowe, powtarzalne wyniki z co najmniej dwóch źródeł dowodów oraz wyznaczony owner.
"""

version = "0.0.1"
