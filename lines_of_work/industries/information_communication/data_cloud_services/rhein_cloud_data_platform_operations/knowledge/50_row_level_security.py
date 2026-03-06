title = "Zeilenebene-Sicherheit (Row-Level Security)"

content = """
Row-Level Security (RLS) filtert Zeilen basierend auf Benutzerattributen.
Beispiel: Ein Vertriebsmitarbeiter sieht nur Kundendaten seiner Region.
Implementierung über Policies, die eine Filterbedingung (z.B. region = current_user_region)
anwenden. RLS muss performant sein; schlecht definierte Policies können
Abfragen verlangsamen. Rhein Cloud nutzt RLS für mandantenfähige
Daten und bereichsbezogene Zugriffsbeschränkungen. Die Definition
erfolgt in Abstimmung mit dem Sicherheitsteam.
"""

version = "0.0.1"
