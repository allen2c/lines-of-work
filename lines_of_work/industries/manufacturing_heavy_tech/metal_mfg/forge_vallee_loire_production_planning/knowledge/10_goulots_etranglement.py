"""Identification et gestion des goulots d'étranglement."""

title = "Goulots d'étranglement"

content = """
Un goulot est une ressource dont la capacité limite le débit de l'ensemble de la
chaîne. En forge, ce sont souvent les fours ou les presses à forger. La production
totale ne peut dépasser celle du goulot.

**Stratégies** : Planifier en priorité le goulot ; éviter les temps morts sur cette
ressource ; découpler les autres postes pour qu'ils ne génèrent pas de surstock
avant le goulot. La théorie des contraintes (TOC) formalise ce pilotage.

**Surcapacité temporaire** : Heures supplémentaires, sous-traitance, report de
commandes non urgentes. Documenter les décisions pour l'analyse ultérieure.
"""  # noqa: E501

version = "0.0.1"
