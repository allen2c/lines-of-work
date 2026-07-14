title = "Devolução (Refund) de Transações PIX"

content = """
- O pagador pode solicitar devolução voluntária (sem chargeback) em até 90 dias, desde que o recebedor concorde.
- Fluxo: pagador abre solicitação no app; NexPay envia notificação ao recebedor; se aceito, o valor é debitado da conta do recebedor e creditado ao pagador.
- A devolução é processada via SPI como uma nova transação PIX, com identificador de devolução (ReturnIdentification).
- O analista deve verificar se a conta do recebedor tem saldo suficiente; caso contrário, a devolução é recusada.
- Devoluções acima de R$ 5.000,00 exigem aprovação do supervisor.
"""

version = "0.0.1"
