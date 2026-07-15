title = "Limites de Risco por Cliente"

content = """
- **Exposição Máxima**: Cada cliente institucional tem limite de exposição total (soma de posições compradas e vendidas) definido em contrato. Padrão: 30% do patrimônio líquido do cliente. Para clientes de alta renda, limite de R$ 5 milhões por ativo.
- **Margem Inicial**: Exigida para operações a prazo (futuros, opções, aluguel). Calculada diariamente pela B3. O cliente deve manter margem disponível (dinheiro + títulos) igual a 100% da margem exigida. Se cair abaixo de 120%, alerta é gerado. Abaixo de 100%, liquidação forçada.
- **Limite de Day Trade**: Para day trade, a margem é reduzida (ex: 20% do valor do contrato para futuros). Mas o número máximo de day trades por dia é limitado a 20 por cliente (salvo autorização).
- **Limite de Concentração**: Um único ativo não pode representar mais de 25% da carteira do cliente. Para derivativos, a exposição nocional não pode exceder 3x o patrimônio.
- **Limite de Perda (Stop Loss)**: Clientes podem definir stop loss automático. Se a perda acumulada no dia ultrapassar 5% do patrimônio, a mesa pode intervir e liquidar posições.
- **Alavancagem**: Máximo de 2x para ações, 5x para futuros (com margem). Acima disso, requer aprovação do comitê de risco.
"""

version = "0.0.1"
