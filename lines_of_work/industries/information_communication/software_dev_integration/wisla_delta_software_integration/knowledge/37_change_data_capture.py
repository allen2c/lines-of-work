title = "Change Data Capture (CDC)"

content = """
CDC wykrywa zmiany w bazie źródłowej i propaguje je do systemów docelowych w czasie
zbliżonym do rzeczywistego. Alternatywa dla pełnych dumpów i polling.

**Mechanizmy:** Logi transakcyjne (WAL), triggers, timestamps. Preferowane są logi —
mniej obciążenia, pełna historia. Wymaga dostępu do logów bazy.

**Użycie:** Replikacja, synchronizacja do cache, data lake, event sourcing. Kluczowe
dla integracji legacy z nowoczesnymi systemami.
"""  # noqa: E501

version = "0.0.1"
