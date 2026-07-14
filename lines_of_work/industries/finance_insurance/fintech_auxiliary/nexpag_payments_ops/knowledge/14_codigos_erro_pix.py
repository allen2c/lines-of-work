title = "Códigos de Erro Comuns em Transações PIX"

content = """
- ERRO_001: Chave PIX inválida (não encontrada no DICT). Ação: orientar cliente a verificar chave.
- ERRO_002: Saldo insuficiente na conta do pagador. Ação: recusar transação; cliente deve depositar fundos.
- ERRO_003: Limite diário excedido. Ação: informar cliente; sugerir aumento de limite via app.
- ERRO_004: Transação recusada por suspeita de fraude (score > 80). Ação: bloquear e notificar cliente.
- ERRO_005: Falha de liquidação (SPI indisponível). Ação: aguardar retorno; reenviar automaticamente após 30 segundos.
- ERRO_006: QR Code expirado (válido por 15 minutos). Ação: solicitar novo QR.
"""

version = "0.0.1"
