title = "Circuit Breaker e Leilões"

content = """
- **Circuit Breaker**: Acionado quando o Ibovespa (IBOV) varia mais de 10% em relação ao fechamento anterior. Interrompe as negociações por 30 minutos (primeiro nível). Se após reabertura a variação atingir 15%, nova parada de 30 minutos. Se 20%, parada de 1 hora e encerramento do pregão.
- **Leilão de Abertura**: Das 09h45 às 10h00, ordens são acumuladas e o preço de abertura é definido pelo leilão. Ordens a mercado não são executadas antes do leilão.
- **Leilão de Fechamento**: Das 16h55 às 17h00, para definir o preço de fechamento. Ordens a mercado são executadas apenas no final do leilão.
- **Leilão por Volatilidade**: Acionado quando um ativo varia mais de 2% em 1 minuto (ações) ou 1% (futuros). Dura 5 minutos, permitindo que o book se estabilize. Durante o leilão, ordens são acumuladas e não executadas.
- **Leilão de Reabertura**: Após circuit breaker, há um leilão de 10 minutos para reabertura.
- **Procedimento**: Durante leilões, não é possível cancelar ordens. O operador deve aguardar o fim do leilão para ajustar posições.
"""

version = "0.0.1"
