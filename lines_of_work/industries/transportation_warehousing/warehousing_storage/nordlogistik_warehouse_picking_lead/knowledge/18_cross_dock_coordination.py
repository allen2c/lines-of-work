title = "Cross‑Dock‑Abstimmung mit Wareneingang/Versand"

content = """
- Täglicher Abgleich 07:30 Uhr: erwartete Cross‑Dock‑Sendungen (ca. 15 % der Tagesmenge).
- Zeitfenster: Wareneingang bis 10:00 Uhr, Kommissionierung bis 12:00 Uhr, Versandbereitstellung 14:00 Uhr.
- Schnittstelle: EDI‑ASN (DESADV) → EWM‑Cross‑Dock‑Wave.
- Abweichungen (Verspätung > 30 Min, Mengenabweichung > 5 %) → sofortige Info an Versandleiter, Neuberechnung Wave.
- KPI: Cross‑Dock‑Throughput ≥ 95 % termingerecht, Fehlmenge ≤ 0,5 %.
"""  # noqa: E501

version = "0.0.1"
