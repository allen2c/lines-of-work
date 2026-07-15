title = "Gestão de Insumos e Reagentes"

content = """\
- Catálogo de insumos: mantido no sistema LabManager, com informações: nome, fabricante, número de catálogo, lote, validade, quantidade mínima de estoque (ponto de pedido), local de armazenamento.
- Ponto de pedido: calculado com base no consumo médio mensal e lead time do fornecedor. Exemplo: para anticorpo primário anti-CD4 (consumo 2 frascos/mês, lead time 20 dias), ponto de pedido = 3 frascos.
- Solicitação de compra: formulário eletrônico no sistema de compras (SIGCOMP). Aprovação do coordenador para valores até R$ 5.000,00; acima disso, aprovação do diretor.
- Recebimento: conferir quantidade, lote, validade e integridade da embalagem. Registrar entrada no LabManager em até 24h. Amostras de controle de qualidade (ex.: verificar atividade enzimática) antes de liberar para uso.
- Validade: reagentes vencidos são segregados e descartados conforme normas de resíduos químicos. Relatório mensal de vencimentos enviado ao coordenador.
"""  # noqa: E501

version = "0.0.1"
