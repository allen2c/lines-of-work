"""Scripts d'automatisation pour Lyon Forge."""

title = "Scripts d'automatisation"

content = """
Les scripts d'automatisation réduisent la charge cognitive et les erreurs manuelles pour les tâches
répétitives. Lyon Forge privilégie des scripts versionnés, documentés et réutilisables.

**Principes:** Un script doit faire une chose bien. Éviter les scripts monolithiques. Préférer des
commandes composables. Documenter les prérequis et les effets de bord. Tester les scripts critiques
dans un environnement isolé avant exécution en production.

**Emplacement:** Les scripts partagés vivent dans un dépôt dédié ou un dossier `scripts/` à la racine.
Les scripts personnels restent hors du dépôt. Nommer clairement: `deploy_staging.sh`, `seed_data.py`.

**Sécurité:** Ne jamais hardcoder des secrets. Utiliser des variables d'environnement ou un gestionnaire
de secrets. Valider les entrées. Limiter les permissions d'exécution. Auditer les scripts qui modifient
des données sensibles.
"""

version = "0.0.1"
