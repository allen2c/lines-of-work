title = "Outils de clash detection"

content = """
Les logiciels de clash detection (Navisworks, Solibri, BIM Collab, etc.)
comparent les modèles IFC ou natifs pour identifier les conflits. Le
coordinateur maîtrise au moins un de ces outils et définit les règles
de clash (tolérances, types d'éléments à comparer, exclusions).

**Paramétrage :** Définition des règles de clash par paire de lots
(structure vs électricité, plomberie vs CTA, etc.). Tolérance de
séparation minimale (ex. 50 mm entre gaine et conduite). Exclusion
des clashes connus et acceptés (documentés).

**Workflow :** Import des modèles, exécution des règles, revue des
résultats, export du rapport, attribution des correctifs. Le cycle
se répète jusqu'à clôture des conflits. Le coordinateur archive les
rapports et les versions de modèles pour traçabilité.
"""  # noqa: E501

version = "0.0.1"
