"""Local performance knowledge for Lyon Forge developer experience."""

title = "Performance en développement local"

content = """
Les performances en environnement local impactent directement la productivité des
développeurs à Lyon Forge. Optimiser le temps de build, de test, et de démarrage.

**Build incrémental:** Configurer les builds pour ne recompiler que ce qui change.
Utiliser des caches (Gradle, Maven, npm) et éviter les clean complets inutiles.

**Tests ciblés:** Exécuter uniquement les tests impactés par les changements.
Utiliser des tags ou des filtres pour distinguer tests unitaires rapides et tests d'intégration lents.

**Démarrage rapide:** Réduire le temps de démarrage de l'application en dev.
Utiliser des profils légers, des mocks pour les services externes, du lazy loading.

**Outils:** Profiler occasionnellement pour identifier les goulots d'étranglement.
Partager les optimisations découvertes dans la doc interne.
"""

version = "0.0.1"
