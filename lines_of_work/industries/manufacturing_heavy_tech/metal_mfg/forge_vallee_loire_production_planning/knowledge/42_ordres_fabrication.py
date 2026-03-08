"""Création et suivi des ordres de fabrication."""

title = "Ordres de fabrication"

content = """
Un ordre de fabrication (OF) autorise la production d'une quantité donnée d'une
référence. Il contient la gamme, les matières à consommer, les dates prévues et
le lien commande client si applicable.

**Cycle de vie** : Création (à partir du PDP/MRP ou manuelle), lancement, exécution,
confirmation des opérations, clôture. Les OF en retard ou bloqués doivent être
signalisés et traités.

**Traçabilité** : Chaque OF a un numéro unique ; les matières et produits sont
rattachés à ce numéro pour la traçabilité lot.
"""  # noqa: E501

version = "0.0.1"
