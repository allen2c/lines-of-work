title = "Ordonnancement à capacité finie"

content = """
L'ordonnancement à capacité finie (finite capacity scheduling) répartit les ordres de fabrication
sur les postes en ne dépassant pas les capacités réelles. Contrairement au MRP à capacité infinie,
les dates résultent du chargement des postes.

**Règles:** Les algorithmes utilisent des règles de priorité (date livraison, durée, charge
goulot). Le résultat est un planning réalisable, avec des dates de fin réalistes.

**Périmètre:** Postes de travail, main-d'œuvre, outillages critiques. Les replans sont
nécessaires quand des aléas (panne, absence, urgence client) surviennent.
"""  # noqa: E501

version = "0.0.1"
