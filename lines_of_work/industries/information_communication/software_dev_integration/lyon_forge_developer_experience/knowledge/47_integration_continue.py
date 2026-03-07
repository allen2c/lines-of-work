"""Intégration continue pour Lyon Forge."""

title = "Intégration continue"

content = """
L'intégration continue (CI) exécute des vérifications automatiques à chaque commit ou pull request.
Lyon Forge exige que la CI soit verte avant merge.

**Stages typiques:** Lint et format. Tests unitaires. Tests d'intégration. Build. Déploiement
vers un environnement de test. Chaque stage doit être rapide pour un feedback court. Les tests
lents peuvent être déplacés en post-merge ou exécutés en parallèle.

**Parallélisation:** Diviser les suites de tests pour réduire le temps total. Utiliser des
matrices pour tester plusieurs versions (OS, runtime). Éviter les dépendances entre jobs quand
possible.

**Feedback:** Les résultats sont visibles dans l'interface du dépôt. Les notifications sont
configurées pour les échecs. Les développeurs corrigent avant de passer à autre chose.
"""

version = "0.0.1"
