title = "Prevenção a Fraude: Impressão Digital do Dispositivo (Device Fingerprinting)"

content = """
- Cada transação coleta dados do dispositivo: modelo, sistema operacional, IP, resolução de tela, plugins, idioma.
- O fingerprint é comparado com o histórico do cliente; se for novo (nunca visto), a transação recebe score de risco +20.
- Se o mesmo fingerprint for usado por mais de 3 contas diferentes em 24h, todas as transações desse dispositivo são bloqueadas.
- O analista pode consultar o histórico de fingerprints no painel de fraude e liberar manualmente se identificar uso legítimo (ex.: familiar).
"""

version = "0.0.1"
