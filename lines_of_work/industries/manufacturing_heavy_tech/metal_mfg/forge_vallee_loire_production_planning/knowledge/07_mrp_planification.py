"""MRP : planification des besoins en composants."""

title = "MRP (Planification des besoins matières)"

content = """
Le MRP (Material Requirements Planning) calcule les besoins en matières et
composants à partir du plan de production et des nomenclatures. Il génère des
ordres d'achat ou de fabrication avec des dates de besoin et de lancement.

**Données** : PDP (Plan Directeur de Production), nomenclatures (BOM), stocks,
délais. Le MRP explosion éclate les besoins niveau par niveau et propose des
ordres planifiés.

**Limites** : Le MRP suppose des délais et des quantités fixes ; les aléas
nécessitent des ajustements manuels et des stocks de sécurité.
"""  # noqa: E501

version = "0.0.1"
