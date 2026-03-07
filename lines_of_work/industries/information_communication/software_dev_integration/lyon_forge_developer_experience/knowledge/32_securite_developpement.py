"""Security in development knowledge for Lyon Forge developer experience."""

title = "Sécurité dans le développement"

content = """
La sécurité est intégrée dès la phase de développement. Les développeurs doivent connaître les
risques courants et les bonnes pratiques pour les éviter.

**Injection:** Toujours utiliser des requêtes paramétrées pour les bases de données. Valider et
assainir toutes les entrées utilisateur. Éviter l'exécution dynamique de code non fiable.

**Secrets:** Ne jamais committer de clés, mots de passe ou tokens. Utiliser des variables
d'environnement ou un gestionnaire de secrets. Les fichiers .env sont dans .gitignore.

**Dépendances:** Scanner régulièrement les vulnérabilités connues (npm audit, pip-audit).
Mettre à jour les dépendances critiques rapidement. Vérifier la réputation des paquets tiers.
"""

version = "0.0.1"
