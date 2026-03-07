"""API documentation knowledge for Lyon Forge developer experience."""

title = "Documentation des APIs internes"

content = """
Les APIs internes de Lyon Forge doivent être documentées pour faciliter leur utilisation
par les autres équipes. La documentation est générée à partir du code quand possible.

**Format:** OpenAPI (Swagger) pour les APIs REST. Les schémas GraphQL sont auto-documentés
via l'introspection. Compléter avec des exemples de requêtes et de réponses typiques.

**Exemples:** Chaque endpoint critique doit avoir au moins un exemple fonctionnel.
Les exemples doivent être testés et mis à jour lors des changements de contrat.

**Découverte:** Un portail central liste toutes les APIs internes avec liens vers la
documentation et les dépôts. Les changements breaking sont annoncés à l'avance.
"""

version = "0.0.1"
