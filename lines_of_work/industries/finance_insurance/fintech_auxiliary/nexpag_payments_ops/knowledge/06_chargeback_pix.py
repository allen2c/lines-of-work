title = "Processo de Chargeback (Contestação) no PIX"

content = """
- O recebedor pode contestar uma transação PIX em até 90 dias corridos após a data da transação, via MDR (Mecanismo de Devolução e Retorno).
- Motivos padronizados: M01 (fraude), M02 (coação), M03 (falha operacional), M04 (transação não autorizada), M05 (duplicidade), M06 (valor incorreto), M07 (serviço não prestado), M08 (produto não entregue), M09 (cancelamento), M10 (outros).
- A NexPay, como PSP do recebedor, recebe a notificação e tem 7 dias úteis para responder: aceitar (devolver valor) ou contestar (enviar evidências).
- Se contestar, o BCB analisa e decide; se aceitar, o valor é debitado da conta do recebedor e creditado ao pagador.
"""

version = "0.0.1"
