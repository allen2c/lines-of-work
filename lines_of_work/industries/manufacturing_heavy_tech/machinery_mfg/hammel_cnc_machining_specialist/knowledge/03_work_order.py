title = "Arbeitsplan und Auftragsdokumente"

content = """
- Auftragsnummer 8-stellig, Format JJ-NNNNNN, z. B. 24-100875; Stempelzeiten (Start, Rüsten, Hauptzeit, Nacharbeit, Ende) im MES.
- Arbeitsplanfelder: Material/Werkstoff, Rohteilmaße, Spannmittel, Werkzeuge, Schnittdaten, Messschritte, Stückzahl, Vorgabezeit, Programmlink.
- Zeichnung lesen in fester Reihenfolge: Toleranzrahmen → Maßtoleranzen → Form- und Lagetoleranzen → Oberflächensymbole → Allgemeintoleranz → Stücklistennummer → Werkstoff → Stückzahl.
- Bei fehlender Oberflächenangabe oder Radiusangabe: zuerst Rückfrage an die Arbeitsvorbereitung, kein Raten.
- Materialabruf per Barcode-Scan am Lagerfach, ERP-Buchung automatisch.
- Programmfreigabe für Serie erst nach dokumentierter Erstmusterfreigabe (siehe 12_quality_inspection).
- Mehrere gleiche Aufträge (z. B. Sammelcharge) als ein Auftrag behandeln, sofern AV es vorsieht.
- Kein Bearbeitungsbeginn ohne freigegebenen, unterschriebenen Arbeitsplan.
"""  # noqa: E501

version = "0.0.1"
