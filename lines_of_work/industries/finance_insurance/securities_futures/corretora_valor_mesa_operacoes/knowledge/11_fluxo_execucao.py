title = "Fluxo de Execução de Ordens"

content = """
1. **Recepção**: Cliente envia ordem via telefone gravado, chat Bloomberg ou sistema eletrônico (FIX). O operador confirma: ativo, lado (compra/venda), quantidade, tipo de ordem, validade, preço (se limitada), conta.
2. **Pré-Trade Check**: Sistema verifica limites de risco, compliance (insider, concentração) e margem disponível. Se aprovado, segue; se não, ordem é bloqueada e operador informa o motivo ao cliente.
3. **Roteamento**: Ordem é enviada ao sistema de negociação (Profit, MetaTrader) que a encaminha para a B3 (via DMA ou corretora). Para grandes volumes, pode ser necessário leilão de bloco.
4. **Execução**: A ordem é executada total ou parcialmente. O operador monitora o fill e confirma ao cliente em tempo real (via chat ou telefone).
5. **Pós-Trade**: O sistema gera o ticket de negociação. O operador verifica se o preço e quantidade estão corretos. Em caso de erro, inicia procedimento de correção.
6. **Registro**: A ordem é registrada no sistema de risco e no livro de ordens. O backoffice recebe automaticamente para liquidação.
7. **Relatório**: Ao final do dia, o operador gera relatório de execução para o cliente (se solicitado) e para a mesa.
"""

version = "0.0.1"
