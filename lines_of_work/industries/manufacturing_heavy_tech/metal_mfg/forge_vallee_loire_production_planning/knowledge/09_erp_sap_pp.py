"""Utilisation de SAP PP pour la planification."""

title = "SAP PP et modules production"

content = """
Le module SAP PP (Production Planning) gère les ordres de fabrication, les gammes,
les nomenclatures et le MRP. Les écrans principaux : création OF, planification
des capacités (CM01), suivi des coûts, confirmation des opérations.

**Flux typique** : Créer OF à partir de la demande planning, lancer le MRP,
vérifier les ordres planifiés, valider et transmettre en exécution. Les confirmations
saisies par les opérateurs mettent à jour stocks et coûts.

**Bonnes pratiques** : Maintenir les données maîtres (gammes, nomenclatures) à jour ;
saisir les confirmations en temps réel pour un pilotage fiable.
"""  # noqa: E501

version = "0.0.1"
