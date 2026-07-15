title = "Uso do Sistema de Ticketing (ServiceNow)"

content = """
- Todo incidente deve ter um ticket único. Abertura pode ser manual ou automática via integração com Zabbix.
- Campos obrigatórios: severidade, equipamento afetado, data/hora, descrição, ação tomada, cliente impactado (se aplicável).
- O operador deve atualizar o status do ticket: Novo, Em Andamento, Escalonado, Resolvido, Fechado.
- Após resolução, o ticket deve ser fechado com a causa raiz e solução. Se não for possível determinar, marcar como "Causa desconhecida" e escalonar para engenharia.
"""

version = "0.0.1"
