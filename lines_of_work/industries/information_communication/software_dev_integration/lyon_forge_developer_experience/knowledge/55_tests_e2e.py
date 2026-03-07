"""End-to-end testing knowledge for Lyon Forge developer experience."""

title = "Tests end-to-end et scénarios critiques"

content = """
Les tests E2E valident les parcours utilisateur complets à travers plusieurs composants. Lyon Forge
les réserve aux scénarios critiques et aux régressions de haut niveau pour limiter la fragilité.

**Scope:** Couvrez les parcours d'inscription, de connexion, de commande ou de flux métier
principal. Évitez de dupliquer la couverture des tests unitaires et d'intégration. Un petit
ensemble de scénarios stables vaut mieux qu'une suite exhaustive et flaky.

**Environnement:** Utilisez un environnement dédié (staging ou équivalent) avec des données
de test reproductibles. Les tests doivent être idempotents et isolés. Docker ou des fixtures
permettent de recréer l'état initial rapidement.

**Maintenance:** Les sélecteurs doivent être stables (data-testid, rôles ARIA). Évitez les
timeouts arbitraires ; préférez les attentes explicites. Documentez les scénarios et les
prérequis pour faciliter le débogage.
"""

version = "0.0.1"
