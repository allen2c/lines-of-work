title = "Operações de Câmbio (Dólar Futuro e Spot)"

content = """
- **Dólar Futuro (DOL)**: Contrato futuro de taxa de câmbio (R$/US$). Negociado na B3. Tamanho: US$ 10.000 por contrato. Vencimentos: todos os meses (primeiro dia útil). Ajuste diário.
- **Dólar Spot (Pronto)**: Operação de câmbio à vista, liquidada em D+2. Negociada no mercado de balcão (corretoras de câmbio). A corretora Valor não opera spot diretamente; encaminha para parceiro.
- **Procedimento**: Para cliente que deseja hedge cambial, recomendar Dólar Futuro. O operador verifica margem e executa a ordem. Para entrega física, usar contrato de câmbio (taxa PTAX).
- **Limites**: Exposição cambial máxima de 30% do patrimônio do cliente (salvo hedge comprovado). Para day trade, margem de 20% do valor do contrato.
- **PTAX**: Taxa de câmbio de referência divulgada pelo Banco Central. Usada para liquidação de contratos futuros no vencimento.
- **Risco**: Volatilidade alta em momentos de crise. Usar stop loss. Não permitir alavancagem acima de 5x para câmbio.
"""

version = "0.0.1"
