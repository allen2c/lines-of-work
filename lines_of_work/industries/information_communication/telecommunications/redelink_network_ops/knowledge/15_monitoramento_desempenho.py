title = "Monitoramento de Desempenho (Latência, Jitter, Perda)"

content = """
- Métricas de QoS são monitoradas para links de clientes corporativos: latência < 50ms, jitter < 10ms, perda < 0,1%.
- Se os thresholds forem excedidos por mais de 5 minutos, gerar alarme Médio. Se persistir por 30 min, escalonar para engenharia.
- Utilizar o Grafana para analisar tendências: se a latência vem aumentando gradualmente, pode indicar congestionamento – abrir ticket de capacidade.
- Realizar testes de throughput (iPerf) em links suspeitos, com autorização do cliente.
"""

version = "0.0.1"
