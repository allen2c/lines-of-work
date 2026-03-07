"""Safe refactoring knowledge for Lyon Forge developer experience."""

title = "Refactoring en toute sécurité"

content = """
Le refactoring améliore la structure du code sans changer son comportement observable.
À Lyon Forge, un refactoring réussi repose sur des tests existants et des changements
incrémentaux.

**Prérequis:** S'assurer que les tests passent avant de commencer. Si la couverture
est faible, ajouter des tests pour les zones à refactorer en priorité.

**Stratégie:** Petits commits, changements atomiques. Un refactoring mécanique (renommage,
extraction) dans un commit, les changements logiques dans un autre. Facilite la revue
et le rollback.

**Validation:** Les tests doivent passer après chaque étape. En cas d'échec, corriger
avant de continuer. Les outils de refactoring automatique de l'IDE réduisent les erreurs
humaines.
"""

version = "0.0.1"
