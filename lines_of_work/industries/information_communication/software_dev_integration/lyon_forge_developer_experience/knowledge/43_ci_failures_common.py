"""Échecs CI courants pour Lyon Forge."""

title = "Échecs CI courants"

content = """
Les pipelines CI échouent pour des raisons récurrentes. Connaître les causes fréquentes accélère
le diagnostic et évite les retours inutiles.

**Tests flaky:** Tests dont le résultat varie sans changement de code. Causes: timing, ordre
d'exécution, état partagé, dépendances externes. Solution: isoler les tests, utiliser des timeouts
réalistes, mocker les I/O, réécrire les tests non déterministes.

**Dépendances:** Versions divergentes entre local et CI, résolution npm/pip instable. Solution:
lockfile strict, image Docker figée pour CI, pas de `latest` en production.

**Environnement:** Variables manquantes, chemins différents, permissions. Solution: documenter
toutes les variables requises, utiliser des valeurs par défaut sûres pour les tests, valider au
démarrage du job.

**Ressources:** Mémoire, disque, timeout. Solution: augmenter les limites, paralléliser, réduire
la surface des tests en CI.
"""

version = "0.0.1"
