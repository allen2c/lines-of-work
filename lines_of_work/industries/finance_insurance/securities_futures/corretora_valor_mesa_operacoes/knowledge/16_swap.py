title = "Operações de Swap"

content = """
- **Definição**: Contrato de troca de fluxos financeiros entre duas partes, geralmente lastreado em taxa de juros, câmbio ou índice. Negociado no balcão (não na B3) mas registrado na CETIP (atual B3).
- **Tipos**: Swap de taxa de juros (prefixado vs CDI), swap cambial (dólar vs CDI), swap de inflação (IPCA vs CDI).
- **Registro**: Toda operação de swap deve ser registrada em até 1 hora após a negociação no sistema da B3 (antiga CETIP). O operador deve enviar os dados (contraparte, valor nocional, datas, taxas).
- **Margem**: Swap exige margem de garantia (colateral) calculada pelo VaR. Normalmente 5% a 10% do nocional, ajustado diariamente.
- **Liquidação**: No vencimento, as partes trocam o valor final. Pode ser liquidado financeiramente ou com entrega física (raro).
- **Risco**: Risco de contraparte (default). A corretora deve avaliar o crédito do cliente antes de executar. Swaps com clientes de alta renda exigem contrato ISDA.
"""

version = "0.0.1"
