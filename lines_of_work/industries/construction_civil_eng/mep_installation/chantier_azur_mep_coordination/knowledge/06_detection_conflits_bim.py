title = "Détection des conflits (clash) dans le BIM"

content = """
La clash detection consiste à comparer les modèles 3D de différents lots pour identifier
les intersections indésirables entre éléments. Un conflit survient lorsque deux objets
se chevauchent ou ne respectent pas la tolérance minimale de séparation définie dans
le référentiel de coordination.

**Types de conflits :** Conflits directs (chevauchement physique), conflits de
réservation (empiètement sur une zone réservée), conflits de tolérance (distance
insuffisante pour la maintenance ou la réglementation). Le coordinateur classe les
conflits par criticité : bloquant, majeur, mineur.

**Processus :** Exécuter le clash test, exporter le rapport, prioriser les conflits,
attribuer les correctifs aux lots concernés, vérifier les corrections lors du
cycle suivant. Les conflits non résolus sont escaladés au chef de projet et
documentés dans la synthèse de coordination.
"""  # noqa: E501

version = "0.0.1"
