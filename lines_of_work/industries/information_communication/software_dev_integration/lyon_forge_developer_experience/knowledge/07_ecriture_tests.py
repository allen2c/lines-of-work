"""Test writing knowledge for Lyon Forge."""

title = "Écriture et exécution des tests"

content = """
Les tests sont la première ligne de défense contre les régressions. Lyon Forge exige des
tests unitaires pour toute logique métier nouvelle et des tests d'intégration pour les APIs.

**Structure :** Arrange-Act-Assert. Un test = un comportement. Noms explicites (test_xxx_quand_yyy).
Éviter les dépendances entre tests (ordre, état partagé).

**Couverture :** Objectif de 80 % sur le code métier. La couverture seule ne garantit pas la
qualité ; privilégier les cas limites et les chemins d'erreur.

**Mocks :** Utiliser avec parcimonie. Préférer les fakes ou stubs pour les dépendances
externes. Documenter les hypothèses des mocks.

**Exécution :** make test ou npm test en local. CI exécute la suite complète. Les tests
lents sont marqués et peuvent être exclus en développement rapide.
"""

version = "0.0.1"
