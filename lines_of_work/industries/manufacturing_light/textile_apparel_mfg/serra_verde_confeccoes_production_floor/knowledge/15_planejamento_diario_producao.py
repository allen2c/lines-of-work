title = "Planejamento Diário de Produção"

content = """
O planejamento diário traduz a capacidade da linha e as prioridades de pedidos
em metas por turno e por operador.

**Entrada:** Lista de pedidos a produzir, quantidade, modelo e prazo. Capacidade
da linha em peças/hora ou minutos/peça. Disponibilidade de matéria-prima e
aviamentos.

**Saída:** Meta de produção do dia, distribuição por linha ou célula, sequência
de troca de modelo. Comunicar ao chão no início do turno.

**Acompanhamento:** Comparar produção real com meta ao longo do dia. Identificar
atrasos e causas — falta de material, quebra de máquina, retrabalho. Ajustar
quando possível; escalar quando o desvio comprometer o prazo.
"""  # noqa: E501

version = "0.0.1"
