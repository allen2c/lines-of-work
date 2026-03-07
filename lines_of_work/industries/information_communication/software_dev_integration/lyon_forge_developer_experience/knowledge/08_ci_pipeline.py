"""CI pipeline knowledge for Lyon Forge."""

title = "Pipeline CI et intégration continue"

content = """
La CI valide chaque commit avant merge. Lyon Forge utilise GitHub Actions ou GitLab CI selon
le dépôt. Le pipeline doit rester rapide (< 15 min) pour ne pas bloquer les développeurs.

**Étapes :** Lint, tests unitaires, tests d'intégration (si applicable), build. Les étapes
sont parallélisées quand possible. Les artefacts (images, binaires) sont publiés uniquement
sur main ou sur des tags.

**Secrets :** Jamais de secrets en clair. Utiliser les variables d'environnement du CI.
Les accès aux registries et APIs sont limités par scope.

**Échec :** En cas d'échec, la PR ne peut pas être mergée. Corriger ou désactiver temporairement
un test flaky avec un ticket de suivi. Les builds rouges sont prioritaires.
"""

version = "0.0.1"
