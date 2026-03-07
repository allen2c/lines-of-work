"""Internal API knowledge for Lyon Forge developer experience."""

title = "APIs internes et contrats"

content = """
Les APIs internes à Lyon Forge exposent des contrats stables entre services.
Chaque API documente ses endpoints, schémas de requête/réponse, et codes d'erreur.

**Documentation OpenAPI:** Toutes les APIs REST exposent une spec OpenAPI 3.x.
La spec est générée depuis le code ou maintenue à la main, selon le projet.

**Versioning:** Utiliser des préfixes de chemin (/v1/, /v2/) pour les versions majeures.
Les versions mineures restent rétrocompatibles. Déprécier avec un délai de 6 mois minimum.

**Erreurs et retry:** Codes HTTP cohérents (4xx client, 5xx serveur). Corps d'erreur structuré
avec code, message, et trace_id. Documenter les stratégies de retry et backoff.

**Tests de contrat:** Chaque consommateur exécute des tests de contrat contre la spec.
Les changements breaking sont détectés en CI avant merge.
"""

version = "0.0.1"
