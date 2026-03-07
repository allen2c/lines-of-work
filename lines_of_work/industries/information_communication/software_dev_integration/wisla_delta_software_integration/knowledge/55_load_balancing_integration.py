title = "Load balancing w integracjach"

content = """
Integracje wywołujące usługi z wieloma instancjami muszą rozkładać ruch w sposób
zapewniający dostępność i wydajność. Niewłaściwa konfiguracja może przeciążyć
pojedyncze instancje lub ignorować niezdrowe węzły.

**Strategie:** Round-robin, least connections, weighted distribution. Dla integracji
z zachowaniem stanu — sticky sessions (session affinity) gdy konieczne.

**Health checks:** Load balancer musi sprawdzać stan instancji. Integracje powinny
udostępniać endpoint /health zgodny z oczekiwaniami balancera. Unikać usuwania
instancji w trakcie aktywnych połączeń (graceful shutdown).

**Delta Wisła:** Dla integracji wewnętrznych używamy load balancera na poziomie
orchestracji (Kubernetes). Dla zewnętrznych — konfiguracja retry i failover na
poziomie klienta HTTP.
"""

version = "0.0.1"
