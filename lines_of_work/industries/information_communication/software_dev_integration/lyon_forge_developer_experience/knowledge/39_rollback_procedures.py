"""Rollback procedures knowledge for Lyon Forge developer experience."""

title = "Procédures de rollback"

content = """
Un rollback rapide limite les dommages lors d'un déploiement problématique. Chaque release
doit avoir une procédure de rollback testée et documentée.

**Préparation:** Identifier les dépendances (base de données, services externes). Les migrations
de schéma nécessitent des scripts de rollback compatibles. Tester le rollback en staging.

**Exécution:** Définir qui peut décider et exécuter. Garder les artefacts de l'ancienne version
disponibles. Communiquer le rollback aux parties prenantes.

**Post-rollback:** Analyser la cause. Mettre à jour les tests et les procédures pour éviter la
récurrence. Documenter les leçons apprises.
"""

version = "0.0.1"
