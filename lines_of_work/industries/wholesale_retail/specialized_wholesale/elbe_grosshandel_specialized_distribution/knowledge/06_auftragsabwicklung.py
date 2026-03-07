"""Order processing and fulfillment workflow."""

title = "Auftragsabwicklung und Fulfillment"

content = """
Die Auftragsabwicklung bei Elbe Großhandel folgt einem standardisierten Ablauf von der
Bestelleingabe bis zur Auslieferung. Jeder Auftrag wird im WMS erfasst und durchläuft
die Schritte Prüfung, Reservierung, Kommissionierung und Versand.

**Bestelleingang:** Kundenbestellungen erfolgen per E-Mail, Telefon oder EDI. Die
Bestelldaten werden in das WMS übertragen. Vollständigkeit der Artikelnummern,
Mengen und Lieferadressen wird geprüft.

**Verfügbarkeitsprüfung:** Das System prüft Lagerbestand und reserviert die
benötigten Mengen. Bei Unterdeckung wird der Kunde informiert; Alternativartikel
oder Lieferaufteilung werden angeboten.

**Kommissionierung:** Die Ware wird nach Pickliste aus dem Lager geholt. Schwere
Stahlprofile und Rohre werden mit Gabelstaplern bewegt. Die Kommissionierung
erfolgt nach Priorität (Express, Standard) und Liefertermin.

**Versandvorbereitung:** Verpackung, Lieferscheine, Gefahrgutdokumentation bei
bedarf. Selbstabholer erhalten die Ware am Schalter; Speditionsaufträge werden
an die Logistik übergeben.
"""  # noqa: E501

version = "0.0.1"
