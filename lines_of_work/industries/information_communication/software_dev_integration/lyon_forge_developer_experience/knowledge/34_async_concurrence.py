"""Async and concurrency knowledge for Lyon Forge developer experience."""

title = "Programmation asynchrone et concurrence"

content = """
L'asynchrone et la concurrence permettent de gérer plusieurs opérations I/O sans bloquer.
Comprendre quand et comment les utiliser évite les pièges courants.

**Async/await:** Pour les opérations I/O-bound (réseau, disque). Une seule boucle d'événements
par processus. Ne pas mélanger du code synchrone bloquant dans du code async.

**Threads vs processus:** Les threads partagent la mémoire (GIL en Python). Les processus sont
isolés. Choisir selon le type de charge (I/O vs CPU). Utiliser les pools pour limiter le nombre.

**Pièges:** Deadlocks, race conditions, fuites de ressources. Toujours libérer les connexions
et les locks. Tester la concurrence avec des scénarios réalistes.
"""

version = "0.0.1"
