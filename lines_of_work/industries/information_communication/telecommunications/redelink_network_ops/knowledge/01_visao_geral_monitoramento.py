title = "Visão Geral do Monitoramento de Rede"

content = """
- O NOC utiliza o sistema Zabbix como principal ferramenta de monitoramento, com dashboards personalizados por região (Norte, Nordeste, Centro-Oeste, Sudeste, Sul).
- Alarmes são classificados em: Crítico (vermelho), Alto (laranja), Médio (amarelo), Baixo (azul). Cada tipo tem tempo de resposta definido no SLA.
- O painel exibe métricas em tempo real: utilização de banda, latência, perda de pacotes, uptime de equipamentos, temperatura de racks.
- A cada turno (8h), o operador deve verificar a integridade dos backups de configuração dos roteadores core (realizados automaticamente às 02h).
- Exemplo de threshold: latência > 150ms para links de clientes corporativos gera alarme Médio; > 300ms gera Alto.
"""

version = "0.0.1"
