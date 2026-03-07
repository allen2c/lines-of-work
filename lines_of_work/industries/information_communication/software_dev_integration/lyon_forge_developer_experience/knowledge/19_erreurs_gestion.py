"""Error handling knowledge for Lyon Forge developer experience."""

title = "Gestion des erreurs"

content = """
La gestion des erreurs à Lyon Forge suit des principes cohérents pour faciliter
le débogage et offrir une expérience utilisateur claire en cas de problème.

**Hiérarchie d'exceptions:** Définir des exceptions métier héritant de base.
Éviter les except génériques; capturer des types spécifiques. Toujours logger avant de raise.

**Messages utilisateur vs technique:** Les messages exposés à l'utilisateur sont génériques
et ne révèlent pas d'infos sensibles. Les logs contiennent le détail technique et le stack trace.

**Retry et circuit breaker:** Pour les appels externes, implémenter retry avec backoff.
Utiliser un circuit breaker pour éviter de saturer un service en panne.

**Propagation:** Remonter les erreurs avec contexte. Ne pas avaler les exceptions
sans les logger. Utiliser des error boundaries ou handlers globaux pour les cas non gérés.
"""

version = "0.0.1"
