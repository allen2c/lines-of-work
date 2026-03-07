"""Query optimization knowledge for Lyon Forge developer experience."""

title = "Optimisation des requêtes et bases de données"

content = """
L'optimisation des requêtes réduit la latence et la charge sur les bases de données. À Lyon Forge,
les développeurs doivent comprendre les index, les plans d'exécution et les anti-patterns courants.

**Index et couverture:** Créez des index sur les colonnes utilisées dans les clauses WHERE, JOIN et ORDER BY.
Un index couvrant évite les accès à la table. Évitez les index redondants qui ralentissent les écritures.

**Plans d'exécution:** Utilisez EXPLAIN (ou équivalent) pour analyser les requêtes lentes. Repérez les
full table scans, les nested loops coûteux et les mauvais choix d'index. Les outils de profiling
intégrés aux ORM aident à identifier les requêtes N+1.

**Anti-patterns:** Évitez SELECT *, les requêtes dans les boucles, et les jointures excessives.
Préférez le chargement paresseux contrôlé ou le batch loading pour les relations. Limitez les
résultats avec pagination ou cursor-based navigation pour les grands ensembles.
"""

version = "0.0.1"
