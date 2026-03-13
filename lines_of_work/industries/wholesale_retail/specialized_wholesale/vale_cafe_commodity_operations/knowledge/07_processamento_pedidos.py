"""Fluxo de processamento de pedidos de commodities."""

title: str = "Processamento de Pedidos"

content: str = """
O processamento de pedidos na Vale do Café segue um fluxo padronizado para
garantir precisão e rastreabilidade.

**Recebimento:** O pedido pode chegar por e-mail, telefone ou sistema. Registre
imediatamente: cliente, produto, quantidade, especificações (tipo, bebida,
ICUMSA), prazo de entrega e condição de pagamento.

**Validação:** Confira disponibilidade de estoque no sistema. Se o lote
especificado estiver reservado ou insuficiente, consulte alternativas ou
informe prazo para reposição. Valide limite de crédito antes de confirmar.

**Reserva:** Reserve o lote ou quantidade no estoque assim que o pedido for
confirmado. Evite overselling — vendas além do disponível geram atrito com
clientes.

**Documentação:** Emita nota fiscal e ordem de carregamento. A NF deve conter
dados corretos do produto, quantidade e valor. Erros em NF geram retrabalho
fiscal e atrasos na entrega.
"""

version: str = "0.0.1"
