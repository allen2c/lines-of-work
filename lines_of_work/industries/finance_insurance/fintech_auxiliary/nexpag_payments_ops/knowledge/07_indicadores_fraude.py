title = "Indicadores de Fraude em Transações PIX"

content = """
- Transações com valor acima de 3 desvios padrão da média do cliente nos últimos 30 dias.
- Dispositivo novo (primeira transação) com valor > R$ 1.000,00.
- Mais de 3 tentativas de PIX para chaves diferentes em menos de 5 minutos.
- Geolocalização incompatível com o endereço cadastrado (ex.: transação de outro estado em horário atípico).
- Chave PIX recém-cadastrada (menos de 24h) sendo usada para receber valor alto (> R$ 5.000,00).
- Score de risco calculado pelo modelo de machine learning (0-100); acima de 80 bloqueio automático.
"""

version = "0.0.1"
