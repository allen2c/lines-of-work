"""Integration tests knowledge for Lyon Forge developer experience."""

title = "Tests d'intégration"

content = """
Les tests d'intégration vérifient le comportement de plusieurs composants ensemble.
À Lyon Forge, ils s'exécutent dans le pipeline CI et peuvent être lancés localement
via Docker Compose.

**Scope:** Tester les interactions entre services, bases de données, et APIs externes.
Éviter de dupliquer la couverture des tests unitaires. Se concentrer sur les chemins
critiques et les contrats entre composants.

**Environnement:** Utiliser des données de test déterministes. Isoler les tests pour
éviter les interférences. Nettoyer les ressources après chaque exécution.

**Performance:** Les tests d'intégration sont plus lents que les tests unitaires.
Limiter leur nombre et optimiser leur exécution. En CI, les exécuter en parallèle
quand possible.
"""

version = "0.0.1"
