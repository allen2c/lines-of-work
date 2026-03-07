"""CLI tools knowledge for Lyon Forge developer experience."""

title = "Outils en ligne de commande"

content = """
Lyon Forge fournit une suite d'outils CLI pour automatiser les tâches courantes et garantir
la cohérence entre les environnements. Ces outils sont documentés dans le dépôt principal.

**Scripts disponibles:** Chaque projet expose des commandes via un Makefile ou un script wrapper.
Les commandes standard incluent build, test, lint, format, et run. Consultez la documentation
du projet pour la liste exacte.

**Conventions:** Les commandes doivent être idempotentes quand possible. Les scripts d'initialisation
doivent vérifier les prérequis et fournir des messages d'erreur explicites en cas d'échec.

**Intégration:** Les outils CLI s'intègrent avec le pipeline CI. Les mêmes commandes exécutées
localement doivent produire des résultats cohérents en CI pour éviter les surprises au merge.
"""

version = "0.0.1"
