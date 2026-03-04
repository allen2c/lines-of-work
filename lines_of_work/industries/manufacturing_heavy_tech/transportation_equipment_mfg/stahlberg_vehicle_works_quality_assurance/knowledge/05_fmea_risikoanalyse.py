"""FMEA failure mode and effects analysis."""  # noqa: E501

title = "FMEA — Fehlermöglichkeits- und Einflussanalyse"

content = """
FMEA identifiziert potenzielle Fehler, bewertet deren Risiko und leitet
Vermeidungs- und Erkennungsmaßnahmen ab. Design-FMEA (DFMEA) und
Prozess-FMEA (PFMEA) werden getrennt aber abgestimmt geführt.

**Bewertungskriterien:** Schweregrad (S), Eintrittswahrscheinlichkeit (O),
Entdeckungswahrscheinlichkeit (D). Risiko prioritätszahl RPN = S × O × D.
Maßnahmen zielen auf Reduktion von S, O oder D.

**Design-FMEA:** Fokus auf Produktfunktionen und Ausfallarten. Unterstützt
Robustheit und Fehlertoleranz in der Entwicklung. Muss vor Prozess-FMEA
vorliegen.

**Prozess-FMEA:** Fokus auf Fertigungs- und Montageprozesse. Identifiziert
Prozessrisiken und steuert Control Plan und Prüfpläne. Wird mit PFMEA
der Vorstufen abgestimmt.

**Aktualisierung:** FMEA ist lebendes Dokument. Bei Änderungen, Reklamationen
oder neuen Erkenntnissen aktualisieren. Regelmäßige Reviews sicherstellen.
"""

version = "0.0.1"
