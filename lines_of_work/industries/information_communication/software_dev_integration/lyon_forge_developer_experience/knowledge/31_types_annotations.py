"""Type annotations knowledge for Lyon Forge developer experience."""

title = "Annotations de types et typage statique"

content = """
Les annotations de types améliorent la lisibilité et permettent l'analyse statique. Lyon Forge
encourage le typage explicite pour les signatures publiques et les structures de données partagées.

**Signatures de fonctions:** Annoter les paramètres et le type de retour. Utiliser Optional pour
les valeurs nulles et Union pour les types multiples. Les génériques (List, Dict) précisent la
structure des données.

**Structures de données:** Les dataclasses ou Pydantic modèles documentent le schéma attendu.
Éviter Any sauf pour l'interopérabilité avec des bibliothèques non typées.

**Outils:** mypy ou pyright pour l'analyse statique. Intégrer dans le CI pour bloquer les
régressions de typage. Les éditeurs modernes offrent l'autocomplétion et la détection d'erreurs.
"""

version = "0.0.1"
