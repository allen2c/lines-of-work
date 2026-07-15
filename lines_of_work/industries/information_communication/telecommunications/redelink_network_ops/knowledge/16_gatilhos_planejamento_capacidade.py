title = "Gatilhos para Planejamento de Capacidade"

content = """
- Quando a utilização de um link atingir 80% da capacidade por mais de 1 hora em horário de pico, gerar alerta para engenharia de capacidade.
- Se a utilização média semanal ultrapassar 70%, o operador deve abrir um ticket de "Capacity Planning" no ServiceNow.
- Para equipamentos (roteadores, switches), monitorar uso de CPU e memória: CPU > 90% por 10 min gera alarme Alto.
- O operador não realiza o planejamento, apenas aciona a equipe responsável.
"""

version = "0.0.1"
