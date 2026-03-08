"""Gammes opératoires et temps standards."""

title = "Gammes opératoires"

content = """
Une gamme définit la séquence des opérations (chauffage, forge, usinage, contrôle)
avec les temps unitaires et les ressources. Ces données alimentent le calcul de
charge et le délai prévisionnel des OF.

**Qualité des données** : Des gammes obsolètes ou imprécises faussent le planning.
Mettre à jour après changement de process, d'outillage ou de méthode. Les temps
réels (confirmations) permettent d'ajuster.

**Hiérarchie** : Gamme type par référence ou famille ; variantes pour options
spécifiques.
"""  # noqa: E501

version = "0.0.1"
