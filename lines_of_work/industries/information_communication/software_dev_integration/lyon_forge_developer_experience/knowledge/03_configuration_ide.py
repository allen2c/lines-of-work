"""IDE configuration knowledge for Lyon Forge."""

title = "Configuration de l'éditeur et de l'IDE"

content = """
Une configuration d'éditeur cohérente réduit les conflits de formatage et améliore la
lisibilité du code. Lyon Forge fournit des fichiers de configuration partagés par projet.

**EditorConfig :** .editorconfig à la racine impose indentation, fin de ligne et encodage.
Tous les éditeurs modernes le supportent nativement.

**Linters et formateurs :** ESLint, Prettier (JS/TS) ou Ruff, Black (Python) sont configurés
dans le dépôt. Les règles sont alignées sur le style guide interne. Pre-commit hooks
appliquent les vérifications avant chaque commit.

**Extensions recommandées :** Liste dans CONTRIBUTING.md — débogueur, support de tests,
snippets métier. Optionnel mais encouragé pour l'uniformité.

**Pas d'obligation :** Chaque développeur reste libre de son éditeur. Seules les sorties
(format, lint) doivent respecter les standards du projet.
"""

version = "0.0.1"
