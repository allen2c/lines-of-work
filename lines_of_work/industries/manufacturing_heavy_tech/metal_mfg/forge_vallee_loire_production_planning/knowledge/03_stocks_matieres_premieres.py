"""Gestion des stocks de matières premières en métallurgie."""

title = "Stocks de matières premières"

content = """
Les matières premières en forge incluent billettes, barres, blooms et lingots selon
le procédé. Les niveaux de stock doivent couvrir le lead time d'approvisionnement
et absorber les variations de demande, sans immobiliser excessivement des capitaux.

**Point de commande** : Seuil déclenchant une commande fournisseur. Calcul : consommation
moyenne × (délai appro + sécurité). Ajuster selon saisonnalité et contrats cadre.

**Contrôles** : Réception avec numéro de lot, vérification certificateur (2.2, 3.1),
traçabilité jusqu'au produit fini. En cas de non-conformité, blocage du lot et
signalement qualité.
"""  # noqa: E501

version = "0.0.1"
