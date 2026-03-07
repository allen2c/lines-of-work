"""Documentation d'architecture pour Lyon Forge."""

title = "Documentation d'architecture"

content = """
La documentation d'architecture permet aux nouveaux et aux pairs de comprendre les décisions et
l'organisation du système. Lyon Forge utilise des ADR (Architecture Decision Records) et des
diagrammes à jour.

**ADR:** Chaque décision architecturale significative est documentée: contexte, options
envisagées, décision prise, conséquences. Format court et daté. Permet de comprendre le «pourquoi»
des années plus tard.

**Diagrammes:** C4 ou équivalent pour les niveaux système, conteneur, composant. Éviter les
diagrammes générés automatiquement non maintenus. Préférer le code comme source de vérité pour
les détails, les diagrammes pour la vue d'ensemble.

**Mise à jour:** La doc d'architecture est revue lors des changements majeurs. Une doc obsolète
est pire qu'aucune doc: elle induit en erreur.
"""

version = "0.0.1"
