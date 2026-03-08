"""Construction et suivi du plan de charge."""

title = "Plan de charge et capacité"

content = """
Le plan de charge répartit les ordres de fabrication sur les ressources (presses,
fours, machines d'usinage) en fonction de leur capacité nominale et des disponibilités.
En forge, la capacité des fours limite souvent le débit.

**Étapes** : Charger les OF validés, appliquer les gammes pour calculer les temps
machine, vérifier les conflits de capacité et rééquilibrer. Anticiper les arrêts
maintenance en réduisant la capacité disponible sur les plages concernées.

**Ajustements** : Face aux urgences client, décaler les OF non prioritaires ou
ajuster les lots. Documenter tout changement pour la traçabilité.
"""  # noqa: E501

version = "0.0.1"
