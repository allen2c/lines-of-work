"""Knowledge item: wagon isole."""

title = "Transport de Wagons Isoles"

content = """
Le wagon isole (WU) designe un ou quelques wagons acheminés dans un train
composite qui dessert plusieurs destinations. Les wagons sont regroupes en
gares de triage ou en cours de route, puis achemines vers leur destination.

**Complexite:** Plus lent et moins previsible que le train block. Les
correspondances entre trains et les manoeuvres en gare generent des delais.
La planification est plus difficile car dependante du graphique global.

**Usage:** Trafic diffus, petits volumes, destinations multiples. Vallee Rhone
Fret utilise le WU pour les flux qui ne justifient pas un train block.
La communication avec le client sur les delais realistes est importante.
"""  # noqa: E501

version = "0.0.1"
