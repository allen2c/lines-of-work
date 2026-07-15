title = "Operações com Derivativos (Futuros e Opções)"

content = """
- **Futuros**: Contratos padronizados negociados na B3. Principais: Índice (WIN, WDO), Dólar (DOL), Taxa de Juros (DI1), Soja (SOJ), Milho (CMM), Boi Gordo (BGI), Café (ICF). Cada contrato tem tamanho, vencimento e ajuste diário.
- **Opções**: Direito de comprar (call) ou vender (put) um ativo-objeto a um preço fixo até o vencimento. Opções de ações (lote 100), opções de índice (IBOV), opções de futuros (ex: opção sobre DI1). Prêmio pago no ato.
- **Vencimentos**: Opções de ações: terceira segunda-feira do mês. Futuros: quarta-feira mais próxima do dia 15 (exceto DI1 que tem vencimento no primeiro dia útil do mês).
- **Margem para Opções**: Vendedor de opções (lançador) precisa depositar margem. Comprador paga prêmio e não precisa de margem adicional.
- **Estratégias Comuns**: Covered call, protective put, straddle, spread. O operador deve verificar se a estratégia é adequada ao perfil do cliente.
- **Riscos**: Alavancagem elevada, risco de gap, risco de liquidez em opções fora do dinheiro. Nunca recomendar estratégias complexas sem aprovação do compliance.
"""

version = "0.0.1"
