"""Production error handling knowledge for Lyon Forge developer experience."""

title = "Gestion des erreurs en production"

content = """
Les erreurs en production nécessitent une approche structurée pour le diagnostic et la
résolution. Lyon Forge définit des pratiques pour limiter l'impact et accélérer la résolution.

**Logging structuré:** Inclure request_id, user_id, et contexte pertinent dans chaque log
d'erreur. Utiliser des niveaux cohérents (ERROR pour les échecs, WARN pour les dégradations).

**Alerting:** Définir des seuils et des canaux d'escalade. Éviter l'alerte fatigue en
agrégeant les incidents similaires. Documenter les runbooks pour les alertes récurrentes.

**Post-mortem:** Analyser les incidents majeurs sans blame. Identifier les causes racines et
les actions correctives. Partager les apprentissages avec l'équipe.
"""

version = "0.0.1"
