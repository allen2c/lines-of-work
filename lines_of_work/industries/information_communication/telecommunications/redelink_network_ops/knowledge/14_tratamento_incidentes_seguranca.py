title = "Tratamento de Incidentes de Segurança (DDoS, Intrusão)"

content = """
- Suspeita de DDoS: verificar aumento repentino de tráfego ( > 5x a média) em um link. Imediatamente acionar o CSIRT e aplicar blackhole no prefixo atacante (via BGP).
- Intrusão: se detectar acesso não autorizado a equipamento (ex: login suspeito), isolar o equipamento da rede (desabilitar porta de gerenciamento) e notificar CSIRT.
- Não tentar investigar por conta própria além do básico. Seguir o plano de resposta a incidentes de segurança (documento IRP-001).
- Registrar tudo no ticket com classificação "Segurança" e não compartilhar detalhes fora do canal seguro.
"""

version = "0.0.1"
