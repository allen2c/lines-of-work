title = "Architektura hub-and-spoke"

content = """
W hub-and-spoke wszystkie systemy łączą się z centralnym hubem. Hub tłumaczy
protokoły, transformuje dane i kieruje przepływy. Systemy peryferyjne nie
komunikują się bezpośrednio.

**Zalety:** Jedna integracja per system z hubem. Centralna transformacja,
routing, audyt. Łatwiejsze dodawanie nowych systemów — tylko nowy spoke.

**Implementacje:** ESB (Enterprise Service Bus), platformy iPaaS (MuleSoft,
Boomi, Azure Integration Services). Hub może być monolityczny lub rozproszony
(mikroserwisy integracyjne).

**Kompromisy:** Hub to single point of failure — wymaga HA. Opóźnienie i koszt
przejścia przez hub. Możliwy bottleneck przy dużym ruchu.
"""  # noqa: E501

version = "0.0.1"
