"""Stratégies de cache pour Lyon Forge."""

title = "Stratégies de cache"

content = """
Le cache améliore les performances mais introduit des risques de cohérence. Lyon Forge applique des
stratégies explicites selon le type de données et la tolérance à la fraîcheur.

**Cache applicatif:** Pour des données peu volatiles, utiliser TTL court (minutes) et invalidation
explicite à l'écriture. Documenter la politique de chaque cache. Éviter le cache pour les données
transactionnelles critiques.

**Cache HTTP:** Respecter les en-têtes Cache-Control et ETag. Pour les APIs internes, définir des
max-age cohérents avec le cycle de mise à jour des données. Utiliser le cache navigateur pour les
assets statiques avec hash dans l'URL.

**Cache distribué:** Redis ou équivalent pour le partage entre instances. Définir des clés préfixées
par contexte (ex: `user:123:profile`). Planifier l'éviction et la capacité. Surveiller le hit ratio.
"""

version = "0.0.1"
