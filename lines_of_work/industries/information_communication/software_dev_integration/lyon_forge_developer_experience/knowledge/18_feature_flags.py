"""Feature flags knowledge for Lyon Forge developer experience."""

title = "Feature flags et déploiement progressif"

content = """
Les feature flags à Lyon Forge permettent de découpler le déploiement du release.
Les fonctionnalités peuvent être activées progressivement ou désactivées en cas de problème.

**Types de flags:** Release (activation progressive), experiment (A/B testing),
ops (kill switch pour désactiver une feature en prod). Chaque type a sa stratégie.

**Naming:** Préfixer par le nom de la feature ou du module. Ex: billing.new_checkout_flow.
Documenter chaque flag, sa raison, et sa date de suppression prévue.

**Cycle de vie:** Créer le flag, développer derrière le flag, activer progressivement,
supprimer le flag une fois la feature stabilisée. Ne pas laisser des flags orphelins.

**Performance:** Éviter les flags qui impactent chaque requête. Utiliser des caches
ou des évaluations asynchrones pour les flags à haute fréquence.
"""

version = "0.0.1"
