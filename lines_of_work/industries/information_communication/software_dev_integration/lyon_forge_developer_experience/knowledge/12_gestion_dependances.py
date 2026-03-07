"""Dependency management knowledge for Lyon Forge developer experience."""

title = "Gestion des dépendances"

content = """
La gestion des dépendances à Lyon Forge repose sur des fichiers de lock et des versions
pinnées pour garantir des builds reproductibles et éviter les régressions inattendues.

**Fichiers de lock:** Toujours commiter le lockfile (package-lock.json, Pipfile.lock, etc.).
Ne pas mettre à jour les dépendances majeures sans revue d'impact et tests de régression.

**Politique de mise à jour:** Mises à jour mineures et patch mensuelles via Dependabot ou Renovate.
Mises à jour majeures planifiées par trimestre avec revue de breaking changes.

**Vulnérabilités:** Scanner régulièrement avec npm audit, pip-audit, ou équivalent.
Corriger les vulnérabilités critiques sous 7 jours, les majeures sous 30 jours.

**Dépendances internes:** Utiliser des versions sémantiques pour les packages internes.
Éviter les dépendances circulaires entre modules partagés.
"""

version = "0.0.1"
