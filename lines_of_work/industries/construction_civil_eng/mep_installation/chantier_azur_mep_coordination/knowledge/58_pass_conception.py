title = "Profil d'accès sécurisé (PASS) en conception"

content = """
Le PASS (Profil d'Accès Sécurisé aux Données) définit les droits
d'accès et de modification des maquettes BIM et des documents de
conception. Le coordinateur applique les règles du PASS : qui peut
modifier quel lot, quelles sont les procédures de validation, comment
sont gérées les versions. Une modification non autorisée peut corrompre
le modèle fédéré ou créer des incohérences.

**Rôles :** Propriétaire du lot (modifications), lecteur (consultation),
coordinateur (assemblage, clash, pas de modification directe des lots).
Le coordinateur travaille sur une copie assemblée et renvoie les
correctifs aux propriétaires.

**Traçabilité :** Les versions sont horodatées et attribuées. En cas
d'erreur, il est possible de revenir à une version antérieure. Le
coordinateur archive les versions utilisées pour chaque rapport de clash.
"""  # noqa: E501

version = "0.0.1"
