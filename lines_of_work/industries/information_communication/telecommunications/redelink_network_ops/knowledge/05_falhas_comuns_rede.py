title = "Falhas Comuns de Rede e Primeiras Ações"

content = """
- Fibra óptica rompida: verificar alarme de perda de sinal (LOS) no OLT/roteador. Acionar equipe de campo imediatamente. Se houver rota redundante, ativar failover automático (verificar se funcionou).
- Queda de energia em site: verificar status do nobreak e gerador. Se bateria crítica (<20%), acionar equipe local. Registrar no ticket.
- Sobrecarga de CPU em roteador: verificar tráfego anômalo (possível ataque DDoS). Se confirmado, seguir procedimento de mitigação (blackhole).
- Erro de configuração: comparar configuração atual com backup. Se divergência, restaurar backup e notificar engenharia.
"""

version = "0.0.1"
