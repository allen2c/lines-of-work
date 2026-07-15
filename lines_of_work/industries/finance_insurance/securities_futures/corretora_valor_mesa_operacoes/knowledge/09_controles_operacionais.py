title = "Controles Operacionais da Mesa"

content = """
- **Dupla Checagem**: Toda ordem acima de R$ 1 milhão deve ser verificada por um segundo operador antes de ser enviada. Para ordens acima de R$ 5 milhões, aprovação do head de mesa.
- **Registro de Ordens**: Todas as ordens (verbais ou eletrônicas) devem ser registradas em sistema com timestamp. Ordens verbais devem ser confirmadas por e-mail em até 5 minutos.
- **Limite de Erro**: Cada operador tem limite de 3 erros operacionais por mês (ex: preço errado, quantidade errada). Após o terceiro, suspensão temporária e treinamento.
- **Segregação de Funções**: O operador que executa a ordem não pode fazer a conciliação. A conciliação é feita pelo backoffice.
- **Backup**: Sistemas de negociação devem ter backup em nuvem. Em caso de falha, usar terminal de contingência (Profit Web ou Bloomberg Anywhere).
- **Auditoria**: A mesa é auditada trimestralmente pela auditoria interna e anualmente pela CVM. Manter registros por 5 anos.
"""

version = "0.0.1"
