title = "Correlação e Filtragem de Alarmes"

content = """
- Muitos alarmes podem ser consequência de uma única falha raiz. Exemplo: falha de energia em um site gera alarmes de todos os equipamentos daquele local.
- O operador deve identificar o alarme primário (ex: "Power Failure") e suprimir os secundários (ex: "Interface Down") no NMS, para evitar ruído.
- Regra: se mais de 5 alarmes do mesmo site em menos de 2 minutos, provável causa raiz única. Investigar o alarme de maior severidade.
- Utilizar a funcionalidade de "alarm correlation" do Zabbix (event correlation rules) para agrupar automaticamente.
"""

version = "0.0.1"
