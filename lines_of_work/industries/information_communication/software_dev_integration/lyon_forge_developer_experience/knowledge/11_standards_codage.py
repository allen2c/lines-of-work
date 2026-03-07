"""Coding standards knowledge for Lyon Forge developer experience."""

title = "Standards de codage"

content = """
Les standards de codage garantissent la cohérence et la maintenabilité du code à Lyon Forge.
Chaque projet suit un style guide défini, appliqué via des outils de lint et de formatage.

**Conventions de nommage:** Les variables et fonctions en snake_case, les classes en PascalCase.
Les constantes en MAJUSCULES. Les noms doivent être explicites et éviter les abréviations obscures.

**Longueur et complexité:** Limiter les fonctions à 50 lignes, les fichiers à 400 lignes.
La complexité cyclomatique ne doit pas dépasser 10 par fonction. Extraire les blocs complexes.

**Commentaires et docstrings:** Documenter les fonctions publiques avec des docstrings.
Les commentaires expliquent le « pourquoi », pas le « quoi ». Éviter le code commenté.

**Imports et structure:** Imports groupés (stdlib, tiers, local), triés alphabétiquement.
Une seule instruction par ligne. Pas d'imports circulaires.
"""

version = "0.0.1"
