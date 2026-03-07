"""Health checks knowledge for Lyon Forge developer experience."""

title = "Health checks et liveness"

content = """
Les health checks permettent aux orchestrateurs et load balancers de détecter les instances
défaillantes. Lyon Forge définit des endpoints standardisés pour le monitoring.

**Liveness:** Indique si l'application répond. Simple et rapide. Un échec déclenche un restart.
Ne pas inclure de dépendances externes pour éviter les restarts en cascade.

**Readiness:** Indique si l'instance peut recevoir du trafic. Vérifier les connexions DB,
cache, et services critiques. Retirer du pool si non prêt.

**Implémentation:** Endpoints /health/live et /health/ready. Temps de réponse < 100ms. Loguer
les échecs pour le diagnostic.
"""

version = "0.0.1"
