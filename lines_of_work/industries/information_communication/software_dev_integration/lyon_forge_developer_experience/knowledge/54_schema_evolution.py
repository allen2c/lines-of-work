"""Schema evolution knowledge for Lyon Forge developer experience."""

title = "Évolution des schémas et rétrocompatibilité"

content = """
L'évolution des schémas (API, base de données, configuration) doit préserver la rétrocompatibilité
ou fournir des chemins de migration explicites. Lyon Forge applique des règles pour éviter les
casses en production.

**API:** Ajoutez des champs de manière additive ; ne supprimez pas sans période de dépréciation.
Utilisez des numéros de version ou des en-têtes pour les changements incompatibles. Documentez
les durées de support des anciennes versions.

**Base de données:** Les migrations doivent être réversibles lorsque possible. Les suppressions
de colonnes passent par une phase de dépréciation (colonnes nullable, non utilisées) avant
suppression. Testez les migrations sur des copies de production.

**Configuration:** Utilisez des valeurs par défaut pour les nouveaux paramètres. Les anciens
paramètres dépréciés doivent émettre des avertissements avant suppression. Maintenez une
matrice de compatibilité des versions.
"""

version = "0.0.1"
