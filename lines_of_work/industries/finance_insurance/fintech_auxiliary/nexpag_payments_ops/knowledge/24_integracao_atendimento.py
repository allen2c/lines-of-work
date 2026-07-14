title = "Integração com Atendimento ao Cliente (Tickets)"

content = """
- Quando um cliente reporta problema com PIX (não recebeu, valor errado), o atendimento abre um ticket no Jira com categoria "PIX".
- O analista recebe o ticket e investiga: consulta EndToEndId, verifica status no SPI, confirma se houve liquidação.
- Respostas devem ser dadas em até 4 horas úteis; se for necessário contato com outro PSP, o prazo sobe para 24h.
- Tickets com evidência de fraude são reclassificados para "Fraude" e tratados prioritariamente.
"""

version = "0.0.1"
