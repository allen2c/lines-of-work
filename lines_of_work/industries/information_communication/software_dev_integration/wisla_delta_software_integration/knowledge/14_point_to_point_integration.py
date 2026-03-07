title = "Integracja point-to-point"

content = """
Integracja point-to-point łączy bezpośrednio dwa systemy. Każda para ma dedykowany
kanał (API, plik, kolejka). Proste przy małej liczbie systemów; nie skaluje się
przy wielu połączeniach.

**Kiedy stosować:** 2–3 systemy, proste przepływy, niska zmienność. Szybki czas
wdrożenia. Brak potrzeby centralnego huba.

**Wady:** N połączeń dla N systemów (N*(N-1)/2 par). Duplikacja logiki w każdym
konektorze. Trudna zmiana — każda nowa integracja wymaga modyfikacji wielu
punktów. Brak wspólnej widoczności i audytu.

**Przejście do huba:** Gdy liczba integracji rośnie, rozważ hub-and-spoke lub
event bus, aby uniknąć sieci połączeń.
"""  # noqa: E501

version = "0.0.1"
