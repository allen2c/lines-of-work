"""Database schema design knowledge for Lyon Forge developer experience."""

title = "Conception du schéma de base de données"

content = """
Un bon schéma facilite les requêtes, les migrations et l'évolution du système. Lyon Forge suit
des principes de normalisation et de nommage cohérent.

**Normalisation:** Éviter la redondance excessive. La 3NF est un bon point de départ. Dénormaliser
volontairement uniquement pour des raisons de performance documentées.

**Nommage:** snake_case pour les tables et colonnes. Noms explicites (users, order_items).
Éviter les abréviations obscures. Les clés étrangères référencent clairement la table cible.

**Évolution:** Prévoir les migrations réversibles. Ne pas supprimer de colonnes sans période de
dépréciation. Documenter les contraintes et index pour les requêtes critiques.
"""

version = "0.0.1"
