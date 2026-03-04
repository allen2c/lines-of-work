"""SPC statistical process control for automotive."""  # noqa: E501

title = "SPC — Statistische Prozesslenkung"

content = """
SPC nutzt statistische Methoden zur Überwachung von Fertigungsprozessen.
Ziel ist die Erkennung von Prozessveränderungen, bevor Ausschuss entsteht,
und die Sicherung stabiler Prozesse.

**Regelkarten:** Shewhart-Karten für Einzelwerte, X-bar-R, X-bar-s je nach
Stichprobenumfang und Datenart. Regelkarten zeigen Prozessverlauf über Zeit
und signalisieren außer Kontrolle geratene Prozesse.

**Regeln für Eingriffe:** Western Electric Rules oder vergleichbare Regeln
für Out-of-Control-Signale. Beispiele: Punkt außerhalb Kontrollgrenzen,
sieben aufeinanderfolgende Punkte auf einer Seite der Mittellinie.

**Prozessfähigkeit:** Cpk und Ppk beschreiben, ob der Prozess die
Spezifikationen einhalten kann. Cpk mindestens 1,33 für neue Prozesse,
1,67 für sicherheitsrelevante Merkmale. Regelmäßige Revalidierung.

**Anwendung:** Für alle im Control Plan als SPC-pflichtig gekennzeichneten
Merkmale. Daten zeitnah erfassen, Auswertung durch geschulte Mitarbeiter.
"""

version = "0.0.1"
