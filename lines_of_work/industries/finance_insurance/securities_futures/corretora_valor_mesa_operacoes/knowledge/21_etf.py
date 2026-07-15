title = "ETFs (Exchange Traded Funds)"

content = """
- **Definição**: Fundos negociados em bolsa que replicam índices (IBOV, IBrX, S&P500) ou setores. Código: 4 letras + 11 (ex: BOVA11). Lote de 100 cotas.
- **Vantagens**: Diversificação, baixa taxa de administração (0,2% a 0,5% a.a.), liquidez diária. Negociados como ações.
- **Ordens**: Mesmo procedimento de ações. O operador deve verificar o NAV (valor patrimonial) e o spread entre compra e venda. Se spread > 0,5%, alertar cliente.
- **Dividendos**: ETFs distribuem dividendos dos ativos subjacentes. O pagamento é feito pela B3, creditado na conta do cliente.
- **ETFs Internacionais**: Alguns ETFs negociados na B3 replicam índices dos EUA (ex: IVVB11). Sujeitos a variação cambial. O operador deve informar o risco cambial.
- **Limites**: Mesmos limites de concentração de ações. Para ETFs setoriais, considerar exposição setorial.
"""

version = "0.0.1"
