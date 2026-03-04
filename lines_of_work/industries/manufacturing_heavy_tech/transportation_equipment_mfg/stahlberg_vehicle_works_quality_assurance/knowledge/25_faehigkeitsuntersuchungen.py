"""Process capability studies."""  # noqa: E501

title = "Fähigkeitsuntersuchungen (Cpk, Ppk)"

content = """
Fähigkeitsuntersuchungen bewerten, ob ein Prozess in der Lage ist,
Spezifikationsgrenzen einzuhalten. Cpk (capability) und Ppk (performance)
sind die gebräuchlichsten Indizes.

**Cpk:** Langfristige Prozessfähigkeit unter Annahme statistischer Kontrolle.
Cpk = min((Oberes Limit - Mittelwert) / 3 sigma, (Mittelwert - Unteres Limit) / 3 sigma).
Mindestens 1,33 für neue Prozesse, 1,67 für sicherheitsrelevante Merkmale.

**Ppk:** Prozessleistung, weniger restriktive Annahmen. Oft für initiale
Bewertung. Ppk-Anforderungen kundenspezifisch.

**Voraussetzungen:** Prozess unter statistischer Kontrolle, ausreichend
Messwerte (typisch mindestens 100), Normalverteilung prüfen. Bei
Nichtnormalverteilung: andere Methoden oder Transformation.

**Revalidierung:** Bei Prozessänderung, Werkzeugwechsel, längeren Stills,
 regelmäßig (z.B. jährlich) für kritische Merkmale.
"""

version = "0.0.1"
