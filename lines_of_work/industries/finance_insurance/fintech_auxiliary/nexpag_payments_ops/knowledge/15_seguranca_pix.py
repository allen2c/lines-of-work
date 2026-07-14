title = "Segurança em Transações PIX (QR Code e Token)"

content = """
- QR Code estático: pode ser copiado e usado repetidamente; risco de substituição (troca de QR). NexPay exige confirmação do valor antes de autorizar.
- QR Code dinâmico: gerado por transação, expira em 15 minutos; contém dados criptografados (chave, valor, timestamp).
- Token de autenticação: toda transação PIX exige token de 6 dígitos (via app) ou biometria; transações acima de R$ 500,00 exigem confirmação adicional (ex.: selfie).
- O analista deve verificar logs de token para identificar tentativas de reutilização (token já usado).
"""

version = "0.0.1"
