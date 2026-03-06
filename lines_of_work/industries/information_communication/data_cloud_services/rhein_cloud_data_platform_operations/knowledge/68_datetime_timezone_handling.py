title = "Datums- und Zeitzonenbehandlung"

content = """
Konsistente Zeitzonenbehandlung ist kritisch für korrekte Analysen. Standard: UTC
intern speichern, Konvertierung bei Anzeige. Bei Rhein Cloud: DACH-Zeitzonen (CET/CEST)
für Business-Logik. Timestamp-Typen (TIMESTAMP vs. TIMESTAMP_TZ) bewusst wählen.
Dokumentation der Zeitzone pro Feld. Bei Schedulern: Cron in definierter Zeitzone.
"""

version = "0.0.1"
