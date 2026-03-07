"""Local development environment knowledge for Lyon Forge."""

title = "Environnement de développement local"

content = """
L'environnement local doit refléter la production autant que possible pour éviter les écarts
« ça marche sur ma machine ». Lyon Forge recommande Docker Compose pour les services dépendants.

**Prérequis :** Docker, Node.js ou Python selon le projet, Git, un éditeur configuré (voir
03_configuration_ide). Les versions sont figées dans .nvmrc ou pyproject.toml.

**Services :** Base de données, cache, file d'attente et APIs internes sont lancés via
docker-compose up. Les secrets de dev sont dans un fichier .env.example (jamais commité).

**Données :** Des fixtures ou seeds permettent de démarrer avec un jeu de données cohérent.
Les migrations sont appliquées automatiquement au démarrage.

**Dépannage :** En cas d'échec, consulter le runbook « Local setup » sur le wiki. Les
problèmes récurrents (ports, permissions, chemins) sont documentés avec solutions.
"""

version = "0.0.1"
