"""Process capability indices Cpk and Ppk details."""  # noqa: E501

title = "Prozessfähigkeitsindizes im Detail"

content = """
Prozessfähigkeitsindizes fassen die Lage und Streuung eines Prozesses
relativ zu den Spezifikationsgrenzen in einer Zahl zusammen. Sie ermöglichen
Vergleiche und Zielvorgaben.

**Cp:** Verhältnis Toleranz zu Prozessstreuung (6 sigma). Misst Potenzial,
berücksichtigt keine Lageabweichung. Cp = (OSG - USG) / (6 * sigma).

**Cpk:** Berücksichtigt auch Lage. Nimmt den ungünstigeren Abstand zum
nächsten Grenzwert. Cpk <= Cp. Cpk 1,0 bedeutet: Prozess gerade noch im
Toleranzfeld bei zentrierter Verteilung.

**Ppk:** Verwendet Gesamt-Standardabweichung statt geschätztem sigma.
Für kurze Serien oder initiale Bewertung. Strenger zu interpretieren.

**Interpretation:** Cpk unter 1,0: Prozess erzeugt Ausschuss. Über 1,33:
guter Prozess. Kontinuierliche Verbesserung auch bei gutem Cpk anstreben.
"""

version = "0.0.1"
