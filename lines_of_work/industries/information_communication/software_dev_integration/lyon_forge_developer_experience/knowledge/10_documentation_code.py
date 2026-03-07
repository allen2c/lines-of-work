"""Code documentation knowledge for Lyon Forge."""

title = "Documentation du code"

content = """
La documentation du code aide les futurs lecteurs, y compris soi-même. Lyon Forge privilégie
le code lisible ; la doc complète ce qui n'est pas évident.

**Commentaires :** Expliquer le « pourquoi », pas le « quoi ». Éviter les commentaires
redondants avec le code. Supprimer le code commenté ; Git conserve l'historique.

**Docstrings :** Pour les fonctions et classes publiques. Format standard (Google, NumPy ou
Sphinx selon le langage). Décrire paramètres, retour, et exceptions éventuelles.

**README :** À la racine du dépôt : objectif, prérequis, installation, commandes principales.
Les détails vont dans docs/ ou le wiki. Tenir à jour à chaque changement structurel.
"""

version = "0.0.1"
