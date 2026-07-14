title = "Fluxo Completo de uma Transação PIX"

content = """
- Inicia com o pagador informando a chave PIX (CPF, CNPJ, e-mail, telefone ou chave aleatória) ou lendo QR Code estático/dinâmico.
- A NexPay (como PSP do pagador) envia a ordem de pagamento ao DICT (Diretório de Identificadores de Contas Transacionais) para validação da chave.
- Após confirmação, a ordem é encaminhada ao SPI (Sistema de Pagamentos Instantâneos) do BCB, que liquida em tempo real (até 10 segundos).
- O PSP do recebedor credita o valor na conta do beneficiário e envia confirmação (receipt) para ambos os lados.
- A transação gera um ID único (EndToEndId) de 32 caracteres, usado para rastreamento e conciliação.
"""

version = "0.0.1"
