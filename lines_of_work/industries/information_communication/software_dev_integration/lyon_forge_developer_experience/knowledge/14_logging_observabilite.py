"""Logging and observability knowledge for Lyon Forge developer experience."""

title = "Logging et observabilité"

content = """
Le logging et l'observabilité à Lyon Forge suivent des conventions structurées pour
faciliter le débogage et le monitoring en production.

**Format structuré:** Logs en JSON avec timestamp, level, message, et champs contextuels.
Inclure correlation_id ou request_id pour tracer les requêtes à travers les services.

**Niveaux de log:** ERROR pour les échecs, WARN pour les situations dégradées,
INFO pour les événements métier significatifs, DEBUG uniquement en développement.

**Métriques et traces:** Exposer des métriques Prometheus (compteurs, histogrammes).
Utiliser OpenTelemetry pour le tracing distribué. Ne pas logger de données sensibles.

**Corrélation:** Propager les headers de trace (traceparent, tracestate) entre services.
Les logs doivent permettre de reconstituer le flux d'une requête de bout en bout.
"""

version = "0.0.1"
