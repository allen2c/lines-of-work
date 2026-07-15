title = "Detecção e Classificação de Incidentes"

content = """
- Incidentes são detectados por alarmes no NMS, chamados de clientes (via portal ou telefone) ou varreduras proativas de desempenho.
- Classificação de severidade segue a matriz: Crítico = indisponibilidade total de serviço para >100 clientes ou falha de backbone; Alto = indisponibilidade parcial (>50 clientes) ou degradação severa; Médio = falha em equipamento único sem impacto imediato; Baixo = alarmes informativos (ex: temperatura elevada mas dentro do limite).
- O operador deve confirmar o alarme no NMS antes de abrir o ticket. Se falso alarme, registrar como "alarme espúrio" e fechar.
- Para cada incidente, registrar: ID do ticket, horário de início, equipamento afetado, clientes impactados (se possível), ação tomada.
"""

version = "0.0.1"
