"""API contracts knowledge for Lyon Forge developer experience."""

title = "Contrats d'API et évolution"

content = """
Les contrats d'API définissent l'interface entre les services. Une évolution mal gérée casse
les clients. Lyon Forge applique le versioning et la rétrocompatibilité.

**Versioning:** URL (/v1/), header (Accept-Version), ou paramètre. Choisir une stratégie et
la documenter. Déprécier progressivement les anciennes versions avec des délais annoncés.

**Schémas:** OpenAPI ou JSON Schema pour documenter les requêtes et réponses. Valider les
payloads côté serveur. Les tests de contrat (Pact, etc.) vérifient la compatibilité.

**Changements breaking:** Ajouter des champs optionnels plutôt que modifier les existants.
Ne pas supprimer de champs sans période de transition. Communiquer les changements aux consommateurs.
"""

version = "0.0.1"
