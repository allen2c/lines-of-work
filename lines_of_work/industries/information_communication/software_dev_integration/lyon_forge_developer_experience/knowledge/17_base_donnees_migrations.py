"""Database migrations knowledge for Lyon Forge developer experience."""

title = "Migrations de base de données"

content = """
Les migrations de schéma à Lyon Forge sont versionnées, réversibles, et testées
avant déploiement. Chaque changement de schéma passe par une migration dédiée.

**Outils:** Alembic (Python), Flyway (Java), ou équivalent selon la stack.
Les migrations sont des fichiers SQL ou du code déclaratif, jamais des scripts ad-hoc.

**Rétrocompatibilité:** Les migrations doivent être déployables sans downtime.
Éviter les suppressions de colonnes directes; procéder en plusieurs étapes (déprécier, migrer, supprimer).

**Environnements:** Tester les migrations en staging avant production.
Garder un backup avant toute migration destructive. Documenter le rollback.

**Conflits:** En cas de conflit de migrations (branches parallèles), fusionner manuellement
et tester l'ordre d'exécution. Ne pas réécrire l'historique des migrations appliquées.
"""

version = "0.0.1"
