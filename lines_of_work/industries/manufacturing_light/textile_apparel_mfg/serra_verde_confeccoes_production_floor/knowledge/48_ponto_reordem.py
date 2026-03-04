title = "Ponto de Reordem"

content = """
O ponto de reordem é o nível de estoque que dispara o pedido de ressuprimento.
Abaixo desse ponto, há risco de parada por falta de material.

**Cálculo:** Consumo médio diário × tempo de reposição + estoque de segurança.
Ex.: 100 unidades/dia × 3 dias + 50 = 350 unidades.

**Aplicação no chão:** Linhas e almoxarifado podem usar Kanban visual — quando
o estoque no chão atinge o nível mínimo, o cartão ou container é enviado para
resposto. O chão sinaliza quando o material está próximo do fim.

**Ajuste:** Revisar ponto de reordem quando o consumo ou o lead time mudar.
"""  # noqa: E501

version = "0.0.1"
