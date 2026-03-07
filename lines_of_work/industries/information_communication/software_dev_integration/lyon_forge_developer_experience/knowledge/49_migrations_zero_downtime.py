"""Migrations sans interruption pour Lyon Forge."""

title = "Migrations sans interruption"

content = """
Les migrations de schéma ou de données en production doivent éviter les interruptions de service.
Lyon Forge applique des stratégies de déploiement progressif pour les changements de base de données.

**Schéma:** Ajouter des colonnes en nullable d'abord, remplir les données, puis rendre non-null si
nécessaire. Supprimer une colonne en plusieurs étapes: cesser de l'utiliser, déployer, puis
supprimer. Éviter les renommages directs; ajouter une nouvelle colonne et migrer.

**Données:** Les migrations volumineuses se font par lots (batching) pour éviter les locks longs.
Utiliser des transactions courtes. Planifier une fenêtre de maintenance si la migration est
inévitablement bloquante.

**Rollback:** Chaque migration doit avoir un plan de rollback. Les migrations destructives
(suppression de colonne) sont irréversibles sans backup; les éviter en production si possible.
"""

version = "0.0.1"
