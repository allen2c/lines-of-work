"""Calcul et pilotage du stock de sécurité."""

title = "Stock de sécurité"

content = """
Le stock de sécurité compense les variations de demande et de délai d'approvisionnement.
Formule courante : k × écart-type de la demande sur (délai + période de révision),
où k dépend du taux de service souhaité.

**Ajustements** : Augmenter pour les références critiques ou à forte variabilité ;
réduire pour les pièces à faible valeur ou à rotation rapide. Réviser périodiquement
selon les données réelles.

**Coût** : Le stock de sécurité immobilise des capitaux ; le dimensionnement est
un arbitrage entre risque de rupture et coût de possession.
"""  # noqa: E501

version = "0.0.1"
