"""Profiling and performance knowledge for Lyon Forge developer experience."""

title = "Profiling et optimisation des performances"

content = """
Avant d'optimiser, mesurer. Le profiling identifie les goulots d'étranglement réels plutôt que
les intuitions. Lyon Forge recommande une approche basée sur les données.

**Outils:** cProfile ou py-spy pour Python, Chrome DevTools pour le frontend, pprof pour Go.
Analyser les temps CPU, la mémoire, et les appels I/O. Comparer avant et après les changements.

**Méthodologie:** Établir un baseline avec des données représentatives. Isoler les changements.
Éviter les optimisations prématurées; la lisibilité prime sauf si les métriques le justifient.

**Cache et requêtes:** Vérifier les requêtes N+1, les index manquants, et les caches inutiles.
Documenter les optimisations significatives pour les futurs mainteneurs.
"""

version = "0.0.1"
