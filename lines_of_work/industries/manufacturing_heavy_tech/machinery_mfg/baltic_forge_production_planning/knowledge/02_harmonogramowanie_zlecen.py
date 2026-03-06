title = "Harmonogramowanie zleceń produkcyjnych"

content = """
Harmonogramowanie przypisuje zlecenia do maszyn i czasu w sposób optymalizujący
terminy dostaw i wykorzystanie zasobów.

**Reguły szeregowania:** FIFO (pierwsze przyszło — pierwsze wyszło), priorytet
terminu dostawy (EDD), priorytet krytyczny (najpilniejsze pierwsze). Bałtycka Kuźnia
stosuje hybrydę: EDD dla klientów zewnętrznych, FIFO wewnętrznie przy braku presji.

**Wąskie gardła:** Maszyny krytyczne (np. obrabiarki CNC) decydują o przepływie.
Planowanie od wąskiego gardła wstecz (Theory of Constraints) minimalizuje zapasy
i skraca czas realizacji.

**Bufor czasowy:** Zawsze uwzględniać czas przezbrojenia, kontroli jakości i
potencjalne opóźnienia. Plan „na styk” jest ryzykowny.
"""

version = "0.0.1"
