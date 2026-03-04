"""MSA measurement system analysis for automotive QA."""  # noqa: E501

title = "MSA — Messsystemanalyse"

content = """
MSA bewertet die Eignung von Messsystemen für den vorgesehenen Einsatzzweck.
Ein ungeeignetes Messsystem kann gute Teile als fehlerhaft oder fehlerhafte
als gut einstufen und verfälscht damit alle darauf basierenden Entscheidungen.

**Kernfragen:** Ist das Messsystem genau genug (Bias, Linearität)? Ist es
präzise genug (Wiederholbarkeit, Reproduzierbarkeit)? Geeignet für
Toleranzbreite und Prozessstreuung?

**Gage R&R:** Wiederholbarkeit (E-Varianz) misst Streuung bei gleichem
Prüfer, gleichem Teil. Reproduzierbarkeit (A-Varianz) misst Streuung zwischen
Prüfern. %GRR unter 30 Prozent gilt als akzeptabel, unter 10 Prozent als gut.

**Durchführung:** Typischerweise 10 Teile, 3 Prüfer, 3 Wiederholungen.
ANOVA oder Range-Methode. Vor Beginn: Prüfer schulen, Teile aus Prozess
auswählen, Prozedur standardisieren.

**Maßnahmen bei schlechtem Ergebnis:** Prüfmittel kalibrieren oder ersetzen,
Prüfer schulen, Messmethode vereinheitlichen, Stichprobenumfang anpassen.
"""

version = "0.0.1"
