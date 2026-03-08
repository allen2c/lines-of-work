"""Kanban et flux tirés en production."""

title = "Kanban et flux tirés"

content = """
Le Kanban pilote les flux par la consommation réelle : un poste aval « tire » ce
dont il a besoin chez l'amont via des étiquettes ou signaux. Évite la surproduction
et aligne la production sur la demande réelle.

**Types** : Kanban de production (trigger fabrication), Kanban de transport (trigger
livraison). Taille du Kanban = consommation pendant le délai de réapprovisionnement.

**Usage en forge** : Adapté aux pièces à flux régulier ; moins adapté aux pièces
spécifiques à longue gamme. Combiner avec ordonnancement classique selon le produit.
"""  # noqa: E501

version = "0.0.1"
