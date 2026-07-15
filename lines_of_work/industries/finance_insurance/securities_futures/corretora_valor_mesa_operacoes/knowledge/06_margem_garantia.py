title = "Margem e Garantias"

content = """
- **Margem Inicial (MI)**: Exigida pela B3 para cada posição em futuros e opções. Calculada pelo modelo VaR (Value at Risk) com 99% de confiança e horizonte de 1 dia. Exemplo: para 1 contrato de WIN (índice), MI ≈ R$ 1.500 (varia conforme volatilidade).
- **Margem de Manutenção (MM)**: 80% da MI. Se o saldo da conta margem cair abaixo da MM, o cliente recebe chamada de margem (margin call). Deve depositar garantias em até 1 hora (intraday) ou até o próximo dia útil (overnight).
- **Garantias Aceitas**: Dinheiro (100% do valor), títulos públicos (Tesouro Selic, NTN-B) com deságio de 5% a 10%, ações de alta liquidez (deságio de 30%), fundos de investimento (deságio de 20%). Não aceitamos imóveis ou criptomoedas.
- **Chamada de Margem**: Se o cliente não atender, a mesa pode liquidar posições automaticamente. Prioridade: liquidar primeiro as posições com maior perda e menor liquidez.
- **Margem de Day Trade**: Para day trade, a margem é reduzida (ex: 20% da MI). Mas se a posição não for encerrada até o fim do dia, a margem integral é exigida.
- **Ajuste Diário**: Futuros têm ajuste diário (mark-to-market). O saldo é creditado/debitado na conta do cliente. Se o ajuste for negativo e reduzir a margem abaixo da MM, nova chamada.
"""

version = "0.0.1"
