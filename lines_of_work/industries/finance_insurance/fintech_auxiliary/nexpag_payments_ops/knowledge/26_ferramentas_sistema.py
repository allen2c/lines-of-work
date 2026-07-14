title = "Ferramentas e APIs do Sistema NexPay"

content = """
- NexOps: interface web para monitoramento e ações manuais. Acesso via VPN corporativa.
- ReconPro: sistema de conciliação que importa arquivos .RET e gera relatórios de divergência.
- API de consulta ao DICT: GET /dict/v1/keys/{chave} retorna titular e status.
- API de bloqueio: POST /fraud/v1/block/{cpf} adiciona à blacklist (requer token de Compliance).
- Jira Service Management: para tickets; usar etiquetas "PIX", "Conciliação", "Fraude".
- Slack: canais #ops-pagamentos (alertas), #ops-supervisor (escalonamento), #ops-ti (incidentes técnicos).
"""

version = "0.0.1"
