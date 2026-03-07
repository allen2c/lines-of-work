"""Semantic versioning knowledge for Lyon Forge developer experience."""

title = "Versioning sémantique et politique de release"

content = """
Le versioning sémantique (SemVer) communique les types de changements entre les versions. Lyon
Forge l'applique aux bibliothèques, APIs et services pour permettre des mises à jour prévisibles.

**Format MAJOR.MINOR.PATCH:** MAJOR pour les changements incompatibles, MINOR pour les ajouts
rétrocompatibles, PATCH pour les corrections. Les pré-releases utilisent des suffixes
(1.0.0-alpha.1, 1.0.0-rc.2).

**Politique:** Définissez la durée de support des versions majeures (ex. 12 mois). Les correctifs
de sécurité peuvent justifier des patches sur des versions plus anciennes. Documentez la
matrice de compatibilité avec les dépendances et les clients.

**Automatisation:** Les tags Git et les artefacts de build doivent refléter la version.
Les outils de release (semantic-release, etc.) peuvent incrémenter automatiquement selon les
commits (Conventional Commits). Vérifiez que les numéros de version sont cohérents partout.
"""

version = "0.0.1"
