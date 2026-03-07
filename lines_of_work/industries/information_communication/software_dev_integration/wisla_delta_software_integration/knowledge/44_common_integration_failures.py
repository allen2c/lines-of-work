title = "Typowe awarie integracji"

content = """
**Timeouty:** Zewnętrzny system odpowiada zbyt wolno — skonfiguruj timeouty,
użyj circuit breakera. **Niespójność schematu:** API zmieniło format — wersjonuj,
waliduj wejście, obsługuj brakujące pola. **Duplikaty:** Wiadomość przetworzona
dwukrotnie — stosuj idempotencję, klucze deduplikacji. **Utrata wiadomości:**
Brak potwierdzenia — używaj persistent queues, at-least-once delivery.

**Eskalacja:** Powtarzające się błędy, naruszenie SLA, awaria krytycznego
systemu — zgłoś zespołowi operacyjnemu i właścicielowi integracji.
"""  # noqa: E501

version = "0.0.1"
