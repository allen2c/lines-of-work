"""Conventions de nommage pour Lyon Forge."""

title = "Conventions de nommage"

content = """
Des noms cohérents améliorent la lisibilité et réduisent la charge cognitive. Lyon Forge suit
des conventions par type d'artefact.

**Variables et fonctions:** snake_case en Python, camelCase en JavaScript/TypeScript. Noms
descriptifs: `user_count` plutôt que `n` ou `x`. Éviter les abréviations sauf celles universelles
(id, url, api).

**Classes et types:** PascalCase. Suffixes explicites: `UserService`, `OrderRepository`,
`PaymentHandler`. Les interfaces peuvent préfixer par I dans les langages qui le supportent.

**Fichiers et modules:** Correspondre au nom de la classe principale ou décrire le contenu.
`user_service.py`, `order_repository.ts`. Éviter les noms génériques (`utils.py`) pour les
modules partagés; préférer des noms spécifiques.
"""

version = "0.0.1"
