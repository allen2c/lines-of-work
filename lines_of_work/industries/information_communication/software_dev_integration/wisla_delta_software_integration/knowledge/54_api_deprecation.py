title = "Wycofywanie API (deprecation)"

content = """
Wycofywanie API musi być zarządzane tak, aby nie zaskoczyć konsumentów i dać im czas
na migrację. Nagłe usunięcie lub zmiana łamiąca kompatybilność wsteczną powoduje
awarie integracji.

**Proces:** Ogłoszenie deprecacji z datą końcową (minimum 6–12 miesięcy dla API
zewnętrznych). Nagłówek Deprecation lub X-API-Deprecated w odpowiedziach.
Dokumentacja alternatyw i przewodnik migracji.

**Wersjonowanie:** Stare wersje pozostają dostępne do daty końcowej. Nowe funkcje
tylko w bieżącej wersji. Komunikacja z konsumentami przez kanały ustalone przy
rejestracji integracji.

**Delta Wisła:** Wszystkie zmiany łamiące kompatybilność są ogłaszane z 12-miesięcznym
wyprzedzeniem. Konsumenci wewnętrzni — 6 miesięcy. Logowanie użycia zdeprecjonowanych
endpointów dla śledzenia migracji.
"""

version = "0.0.1"
