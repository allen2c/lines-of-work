"""Polyglot repositories knowledge for Lyon Forge developer experience."""

title = "Repositories polyglottes et monorepos"

content = """
Lyon Forge utilise des monorepos pour certains projets multi-langages. La cohérence des conventions
et des outils facilite la navigation et la contribution.

**Structure:** Organisez par domaine ou par couche (frontend, backend, shared). Chaque package
doit avoir son propre fichier de configuration (package.json, pyproject.toml, Cargo.toml). Les
dépendances partagées sont versionnées et documentées dans un fichier racine.

**Outils:** Utilisez des gestionnaires de monorepo (Nx, Turborepo, Lerna pour JS; uv ou poetry
pour Python) pour les builds incrémentaux et le cache. Les scripts de build doivent être
déterministes et reproductibles.

**CI:** Configurez des jobs parallèles par package ou par langue. Les tests et le lint ne
s'exécutent que sur les fichiers modifiés lorsque c'est possible. Documentez les commandes
racine pour build, test et lint de l'ensemble du repo.
"""

version = "0.0.1"
