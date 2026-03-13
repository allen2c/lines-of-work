"""Knowledge item: classes marchandises dangereuses."""

title = "Classes de Marchandises Dangereuses (RID)"

content = """
Le RID reprend les 9 classes du systeme ONU : 1 Explosifs, 2 Gaz, 3 Liquides
inflammables, 4 Solides inflammables, 5 Matieres comburantes, 6 Matieres
toxiques/infectieuses, 7 Radioactifs, 8 Corrosifs, 9 Divers. Chaque matiere
a un numero UN et des dispositions specifiques.

**Compatibilite:** Certaines classes ne doivent pas etre chargees a proximite
(tableau de compatibilite RID). Les wagons et emballages doivent etre
homologues pour la classe concernee. Une erreur de clasement peut etre
grave en cas d'accident.

**Fiches de donnees de securite:** Les FDS fournissent les informations
pour le transport et l'intervention en cas d'incident. Elles doivent etre
disponibles dans le convoi.
"""  # noqa: E501

version = "0.0.1"
