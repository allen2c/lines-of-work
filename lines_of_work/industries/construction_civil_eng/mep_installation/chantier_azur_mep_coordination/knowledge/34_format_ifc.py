title = "Format IFC (Industry Foundation Classes)"

content = """
L'IFC est un format d'échange ouvert pour les maquettes BIM. Il permet
l'interopérabilité entre logiciels (Revit, ArchiCAD, Navisworks, etc.)
et la conservation à long terme des données. Le coordinateur vérifie que
les modèles exportés en IFC sont complets et exploitables pour la
coordination et la clash detection.

**Structure IFC :** Fichiers .ifc contenant la géométrie, les propriétés
et les relations entre objets. Les versions courantes sont IFC2x3 et
IFC4. Le projet définit une version cible et un schéma de nommage.

**Qualité des exports :** Modèles filtrés (LOD cohérent), propriétés
conservées, géométrie valide. Un export dégradé peut fausser les
résultats du clash test. Le coordinateur valide les exports avant
leur intégration dans le modèle fédéré.
"""  # noqa: E501

version = "0.0.1"
