"""Knowledge item: performance and load testing."""

title = "Performance- und Lasttests"

content = """
Performance-Tests messen Antwortzeiten, Durchsatz und Ressourcennutzung unter definierter Last.
Lasttests prüfen das Systemverhalten bei erwarteten und Spitzenlasten.

**Metriken:** Latenz (p50, p95, p99), RPS (Requests pro Sekunde), Fehlerrate,
CPU- und Speichernutzung. Baseline-Werte müssen vor Änderungen dokumentiert werden.

**Lastprofile:** Realistische Workloads modellieren (z. B. Tageszeiten, Saisonality).
Stress-Tests gehen über die erwartete Last hinaus, um Grenzen zu identifizieren.

**Regressionserkennung:** Performance-Tests in CI integrieren; signifikante Verschlechterungen
müssen vor Merge behoben oder explizit akzeptiert werden.
"""

version = "0.0.1"
