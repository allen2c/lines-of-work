"""Debugging practices knowledge for Lyon Forge."""

title = "Pratiques de débogage"

content = """
Le débogage efficace repose sur des outils et une méthode. Lyon Forge encourage l'utilisation
du débogueur intégré et des logs structurés plutôt que des print.

**Logs :** Format JSON structuré (niveau, message, contexte). Éviter les données sensibles.
Les logs de debug sont désactivés en production ; utiliser le niveau approprié.

**Débogueur :** Breakpoints, inspection des variables, pas à pas. Pour les services
distribués, le tracing (OpenTelemetry) permet de suivre une requête à travers les composants.

**Reproductibilité :** Documenter les étapes pour reproduire un bug. Utiliser des fixtures
ou des enregistrements pour les cas complexes. Un bug non reproductible reste un ticket
ouvert avec hypothèses.
"""

version = "0.0.1"
