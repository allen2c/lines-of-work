"""Secrets management knowledge for Lyon Forge developer experience."""

title = "Gestion des secrets"

content = """
La gestion des secrets à Lyon Forge évite l'exposition de credentials dans le code,
les commits, ou les logs. Les secrets sont injectés au runtime ou via des variables d'environnement.

**Jamais dans le code:** Aucun mot de passe, clé API, ou token dans le dépôt.
Utiliser des placeholders ou des fichiers .env.example sans valeurs réelles.

**Outils:** Vault, AWS Secrets Manager, ou variables d'environnement selon l'infra.
En local, utiliser un fichier .env ignoré par Git, documenté dans .env.example.

**Rotation:** Les secrets sont rotés régulièrement. Documenter la procédure de rotation
et les impacts sur les services. Prévoir un délai de grâce pour les mises à jour.

**Audit:** Les accès aux secrets sont audités. Chaque développeur utilise ses propres
credentials de dev, jamais les credentials de production.
"""

version = "0.0.1"
