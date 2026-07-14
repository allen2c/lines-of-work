title = "Ferramentas de Monitoramento em Tempo Real"

content = """
- Painel NexOps: exibe todas as transações PIX em andamento, com filtros por valor, chave, status (autorizada, recusada, pendente).
- Alertas configuráveis: notificações no Slack para transações acima de R$ 3.000,00, tentativas de fraude, erros de liquidação.
- API de consulta ao DICT: verificar titularidade de chave PIX em tempo real.
- Logs de transação: armazenados por 5 anos (exigência BCB); acessíveis via consulta por EndToEndId.
- Dashboard de conciliação: mostra divergências entre extratos do BCB e registros internos, atualizado a cada 15 minutos.
"""

version = "0.0.1"
