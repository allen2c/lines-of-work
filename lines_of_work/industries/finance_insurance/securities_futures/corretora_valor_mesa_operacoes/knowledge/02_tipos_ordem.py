title = "Tipos de Ordem e Validade"

content = """
- **Ordem a Mercado (MKT)**: Executa imediatamente ao melhor preço disponível. Usar apenas quando a liquidez for alta e o spread for inferior a 0,3% do preço de referência. Risco de slippage em ativos ilíquidos.
- **Ordem Limitada (LMT)**: Especifica preço máximo (compra) ou mínimo (venda). Permanece no book até ser executada ou cancelada. Validade: Day (D) – válida até o fim do pregão; Good-till-cancel (GTC) – válida por até 30 dias corridos; Fill-or-kill (FOK) – executa total ou cancela; Immediate-or-cancel (IOC) – executa parcial e cancela o restante.
- **Ordem Stop (STP)**: Ativa uma ordem a mercado ou limitada quando o preço atinge um gatilho. Usar para stop loss ou stop gain. Exemplo: compra stop a R$ 15,00 ativa ordem a mercado quando o ativo tocar R$ 15,00.
- **Ordem Stop Limit (STL)**: Combina stop e limite. Ex: vender stop a R$ 14,50 com limite a R$ 14,30. Só executa entre esses preços.
- **Ordem de Financiamento (FIN)**: Usada em operações de day trade com margem. Exige garantia adicional.
- **Ordem de Bloco (BLK)**: Para grandes volumes (acima de 500.000 ações ou R$ 5 milhões). Negociada em leilão especial. Necessário autorização da mesa.
- **Validade**: Padrão é Day. Para GTC, o sistema cancela automaticamente após 30 dias. Nunca usar GTC em ativos com eventos corporativos iminentes.
"""

version = "0.0.1"
