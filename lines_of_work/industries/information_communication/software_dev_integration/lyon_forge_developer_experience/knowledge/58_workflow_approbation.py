"""Approval workflow knowledge for Lyon Forge developer experience."""

title = "Workflow d'approbation et qualité des PR"

content = """
Le workflow d'approbation assure que les changements respectent les standards avant fusion. Lyon
Forge utilise des règles de review et des checks automatisés pour maintenir la qualité.

**Règles de review:** Au moins un approbateur pour les changements de code, deux pour les
zones sensibles (sécurité, données). Les reviewers doivent être différents de l'auteur. Les
commentaires doivent être constructifs et orientés amélioration.

**Checks obligatoires:** CI vert (build, tests, lint), couverture minimale, pas de vulnérabilités
connues. Les PR qui modifient des schémas ou des APIs peuvent exiger des approbations
supplémentaires. Les dépendances ajoutées sont vérifiées (licence, maintenance).

**Délais:** Définissez des attentes de temps de review (ex. 24–48 h). Les PR volumineux
doivent être découpées. Utilisez les draft PR pour les travaux en cours et évitez de bloquer
les reviewers avec des changements incomplets.
"""

version = "0.0.1"
