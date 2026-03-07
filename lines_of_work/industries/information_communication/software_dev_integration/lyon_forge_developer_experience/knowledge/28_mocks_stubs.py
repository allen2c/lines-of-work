"""Mocks and stubs knowledge for Lyon Forge developer experience."""

title = "Mocks et stubs en développement"

content = """
Les mocks et stubs permettent d'isoler les composants sous test et de simuler des
comportements externes. Lyon Forge recommande leur usage ciblé pour accélérer les
tests et éviter les dépendances flaky.

**Stubs:** Fournissent des réponses prédéfinies. Utiliser pour les dépendances simples
dont le comportement exact n'est pas critique pour le test.

**Mocks:** Vérifient les interactions (appels, arguments). Utiliser quand le test
doit confirmer qu'une méthode a été appelée avec les bons paramètres.

**Bonnes pratiques:** Ne pas sur-mocker. Un test qui mock tout perd sa valeur. Préférer
les vrais composants en tests d'intégration. Documenter les raisons des mocks complexes.
"""

version = "0.0.1"
