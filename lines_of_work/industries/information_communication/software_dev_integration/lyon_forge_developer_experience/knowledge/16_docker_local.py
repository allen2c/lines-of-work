"""Docker for local development knowledge for Lyon Forge developer experience."""

title = "Docker en développement local"

content = """
Docker permet de reproduire l'environnement de production en local à Lyon Forge.
Les développeurs utilisent docker-compose pour lancer les services dépendants.

**Compose par projet:** Chaque projet a un docker-compose.yml pour les dépendances
(base de données, cache, message queue). Le code applicatif tourne en local ou en container.

**Volumes et hot-reload:** Monter le code en volume pour éviter les rebuilds.
Configurer le hot-reload du langage pour une boucle de développement rapide.

**Ressources:** Limiter la mémoire et CPU des containers en dev pour éviter la saturation.
Documenter les ports exposés et les variables d'environnement requises.

**Nettoyage:** Utiliser docker system prune périodiquement. Éviter d'accumuler
des images et volumes inutilisés.
"""

version = "0.0.1"
