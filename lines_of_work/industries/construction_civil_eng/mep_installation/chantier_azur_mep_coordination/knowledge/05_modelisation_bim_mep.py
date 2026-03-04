title = "Modélisation BIM pour les réseaux MEP"

content = """
Le BIM (Building Information Modeling) permet de représenter les réseaux MEP en 3D
dans un modèle partagé. Chaque corps de métier produit un modèle de son lot ; le
coordinateur assemble et analyse ces modèles pour détecter les conflits spatiaux
et vérifier la cohérence des interfaces.

**LOD (Level of Development) :** En phase études, le LOD 300 ou 350 est courant :
les réseaux sont modélisés avec des dimensions et des tracés détaillés. Le LOD 400
correspond aux études d'exécution. Le coordinateur s'assure que tous les lots
utilisent un LOD compatible pour permettre des clash tests pertinents.

**Formats et logiciels :** L'IFC (Industry Foundation Classes) est le format
d'échange standard. Revit, Navisworks et Solibri sont couramment utilisés pour la
conception et la détection de conflits. Le coordinateur définit les conventions
de nommage et les règles d'export pour garantir l'interopérabilité.
"""  # noqa: E501

version = "0.0.1"
