title = "Ciclos de Liquidação PIX (D0, D1, D+1)"

content = """
- O SPI liquida as transações em tempo real, mas a compensação financeira entre PSPs ocorre em ciclos predefinidos pelo BCB.
- Ciclo D0: liquidação no mesmo dia útil, até as 17h (horário de Brasília). Transações após esse horário entram no ciclo D1.
- Ciclo D1: liquidação no próximo dia útil, com processamento às 10h.
- A NexPay mantém conta de liquidação no BCB (Reserva Bancária) e precisa ter saldo suficiente para cobrir as obrigações líquidas de cada ciclo.
- O analista deve verificar o saldo da conta de liquidação 30 minutos antes do fechamento de cada ciclo e acionar a tesouraria se houver déficit.
"""

version = "0.0.1"
