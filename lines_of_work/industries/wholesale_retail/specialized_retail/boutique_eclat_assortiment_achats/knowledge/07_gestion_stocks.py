title = "Gestion des stocks et réassorts"

content = """
- Stock de sécurité : 15 jours de vente pour les références permanentes, 30 jours pour les saisonnières (pour couvrir le délai de réapprovisionnement).
- Réassort automatique déclenché quand le stock atteint le seuil de réapprovisionnement (calculé comme : délai de livraison × vente quotidienne moyenne + stock de sécurité).
- Inventaire tournant : tous les mois pour les 100 meilleures ventes, inventaire complet tous les 6 mois (janvier et juillet).
- Gestion des invendus : après 6 mois sans vente, démarque progressive (10% par mois jusqu'à 40% max). Si toujours invendu après 9 mois, don à une association ou destruction.
"""

version = "0.0.1"
