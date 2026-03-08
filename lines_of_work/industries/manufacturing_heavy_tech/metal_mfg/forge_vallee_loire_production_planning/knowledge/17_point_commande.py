"""Point de commande et quantité économique."""

title = "Point de commande"

content = """
Le point de commande est le niveau de stock qui déclenche une commande. Il doit
couvrir la demande pendant le délai de réapprovisionnement, plus une marge de
sécurité. Formule : PC = consommation moyenne × délai + stock de sécurité.

**Réapprovisionnement** : Commande à date fixe (périodique) ou à point de commande
(continu). En production, le point de commande s'applique aux matières ; pour les
produits finis, le PDP et le MRP pilotent souvent les lancements.

**Suivi** : Alerter quand le stock franchit le point de commande ; vérifier les
ordres d'achat ouverts.
"""  # noqa: E501

version = "0.0.1"
