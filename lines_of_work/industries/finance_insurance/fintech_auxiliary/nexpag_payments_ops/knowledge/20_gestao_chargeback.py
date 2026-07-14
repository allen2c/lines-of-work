title = "Gestão de Chargebacks: Análise e Decisão"

content = """
- Ao receber notificação de chargeback, o analista tem 7 dias úteis para responder. Passos:
  1. Verificar motivo (M01-M10) e valor.
  2. Coletar evidências: logs de autenticação, IP, geolocalização, comprovante de entrega (se aplicável).
  3. Decidir: aceitar (devolver) ou contestar (enviar evidências ao BCB).
- Se aceitar, o valor é debitado da conta do recebedor; se contestar, o BCB tem 30 dias para julgar.
- Chargebacks acima de R$ 5.000,00 devem ser revisados pelo supervisor antes da resposta.
- Histórico de chargebacks é usado para calcular taxa de contestação (deve ser < 2% para evitar penalidades do BCB).
"""

version = "0.0.1"
