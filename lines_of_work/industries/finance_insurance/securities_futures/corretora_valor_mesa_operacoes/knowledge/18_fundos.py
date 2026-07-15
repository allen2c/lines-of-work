title = "Operações com Fundos de Investimento"

content = """
- **Tipos**: Fundos de ações, multimercado, renda fixa, cambial, ETFs (negociados em bolsa). Fundos abertos (resgate em D+1 a D+30) e fundos fechados (negociados em bolsa).
- **Ordens de Aplicação/Resgate**: Para fundos abertos, o operador envia a ordem ao administrador do fundo (ex: Bradesco, Itaú) via sistema (CETIP ou plataforma). Prazo de cotização: D+0 (aplicação até 15h) ou D+1.
- **ETFs**: Negociados como ações na B3. Ordem de compra/venda normal. Liquidação D+2. O operador deve verificar o valor patrimonial (NAV) e o spread.
- **Fundos Fechados (FII, Fiagro)**: Negociados em bolsa com código. Preço de mercado pode diferir do valor patrimonial. Cuidado com liquidez.
- **Regras**: Aplicação mínima de R$ 1.000 para fundos abertos (padrão). Para ETFs, lote de 100 cotas. O cliente deve ter conta em corretora habilitada para fundos.
- **Compliance**: Verificar se o fundo está registrado na CVM e se o cliente tem perfil de risco adequado (suitability). Não recomendar fundos com taxa de performance acima de 20% sem aprovação.
"""

version = "0.0.1"
