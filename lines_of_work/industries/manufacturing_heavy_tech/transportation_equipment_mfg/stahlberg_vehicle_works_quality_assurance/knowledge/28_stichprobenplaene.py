"""Sampling plans for inspection."""  # noqa: E501

title = "Stichprobenpläne und -umfänge"

content = """
Stichprobenpläne legen Umfang und Bewertung von Stichprobenprüfungen fest.
Sie balancieren Aufwand und Risiko: zu kleine Stichproben erkennen Fehler
nicht, zu große sind unwirtschaftlich.

**AQL-basiert:** Acceptable Quality Level. DIN ISO 2859-1 (z.B. Normalprüfung,
Losgröße, AQL 1,0) liefert Stichprobenumfang n und Annahme-/Ablehnungszahl.
Historisch weit verbreitet.

**Zero-Acceptance-Number:** c=0-Pläne. Jedes Fehlteil führt zu Ablehnung.
Strenger, manchmal kundenspezifisch gefordert.

**Statistische Grundlagen:** Operating Characteristic (OC)-Kurve zeigt
Annahme-Wahrscheinlichkeit in Abhängigkeit von Fehleranteil. Risiken
alpha (Hersteller) und beta (Verbraucher) bewusst wählen.

**Kritische Merkmale:** Oft 100-Prozent-Prüfung oder sehr strenge Stichprobe.
Im Control Plan definiert.
"""

version = "0.0.1"
