title = "Wzorzec Saga"

content = """
Saga to wzorzec zarządzania transakcjami rozproszonymi przez sekwencję lokalnych
transakcji z kompensacją. Gdy jedna transakcja się nie powiedzie, wykonuje się
operacje kompensujące dla już wykonanych kroków.

**Choreografia vs orkiestracja:** W choreografii każda usługa reaguje na zdarzenia
i decyduje o następnym kroku. W orkiestracji centralny koordynator wywołuje usługi
i zarządza kompensacją.

**Kompensacja:** Każdy krok musi mieć zdefiniowaną operację odwrotną. Kompensacja
może być trudna (np. anulowanie płatności) — wymaga starannego projektowania.

**Delta Wisła:** Stosujemy Sagę dla przepływów wielosystemowych (np. zamówienie–
płatność–wysyłka). Preferujemy orkiestrację dla lepszej obserwowalności i kontroli.
"""

version = "0.0.1"
