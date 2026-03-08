"""Spécificités des fours de chauffe en forge."""

title = "Fours de chauffe"

content = """
En forge, les billettes ou blooms sont chauffés avant mise en forme. Les fours
(à gaz, induction) ont une capacité (tonnage/heure), un temps de chauffe et des
contraintes de montée en température. Le planificateur doit respecter ces paramètres.

**Séquençage** : Grouper les pièces de même nuance et format pour optimiser les
changements de régime. Éviter les arrêts répétés qui dégradent le rendement.

**Limites** : Temps de séjour maximum (risque de brûlure) ; compatibilité nuance /
température. Les gammes définissent les paliers de chauffe.
"""  # noqa: E501

version = "0.0.1"
