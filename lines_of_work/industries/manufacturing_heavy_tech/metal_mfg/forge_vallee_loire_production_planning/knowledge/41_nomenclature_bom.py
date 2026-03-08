"""Nomenclatures et structure des produits."""

title = "Nomenclatures (BOM)"

content = """
La nomenclature (Bill of Materials) définit la composition d'un produit : matières,
composants, quantités. Elle sert au MRP pour calculer les besoins et à la
planification pour dimensionner les OF.

**Structure** : Niveau 0 = produit fini ; niveaux inférieurs = sous-ensembles et
composants. Les nomenclatures erronées génèrent des ruptures ou des surstocks.

**Mise à jour** : Les modifications de conception ou de process doivent se
refléter dans les nomenclatures. Un processus de changement (ECN) assure la
cohérence.
"""  # noqa: E501

version = "0.0.1"
