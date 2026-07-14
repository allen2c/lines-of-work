title = "Prevenção a Fraude: Análise Comportamental"

content = """
- Modelo de machine learning analisa padrões: horário típico de transações, valor médio, frequência, tipo de chave usada.
- Desvios significativos (ex.: cliente que só faz PIX de manhã e de repente faz à 1h da madrugada) geram alerta.
- O analista revisa alertas comportamentais no painel "Comportamento" e pode aprovar ou bloquear a transação.
- Se o cliente for aprovado em 3 alertas consecutivos, o modelo reduz o score para esse perfil.
"""

version = "0.0.1"
