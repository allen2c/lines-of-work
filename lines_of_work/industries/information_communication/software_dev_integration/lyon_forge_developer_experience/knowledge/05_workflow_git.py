"""Git workflow knowledge for Lyon Forge."""

title = "Workflow Git et gestion des branches"

content = """
Lyon Forge utilise un workflow basé sur des branches de fonctionnalité et des pull requests.
La branche main est protégée ; tout changement passe par une PR et une revue.

**Création :** Brancher depuis main à jour. Nommer la branche : feature/xxx, fix/xxx, ou
docs/xxx. Un ticket (Jira, Linear) est référencé dans le titre de la PR.

**Commits :** Messages en impératif, préfixés par le type (feat, fix, docs, refactor).
Convention Conventional Commits pour le versioning automatique.

**Revue :** Au moins un approbateur. Les commentaires doivent être constructifs. Répondre
à chaque commentaire, même par un simple « fait » ou référence à un commit.

**Merge :** Squash ou merge selon la politique du dépôt. La branche est supprimée après
merge. En cas de conflit, rebase sur main avant de re-demander la revue.
"""

version = "0.0.1"
