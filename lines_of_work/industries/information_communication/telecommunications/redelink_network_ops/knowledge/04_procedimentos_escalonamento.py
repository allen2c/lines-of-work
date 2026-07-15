title = "Procedimentos de Escalonamento"

content = """
- Escalonamento automático: se incidente Crítico não for resolvido em 30 min, o sistema envia alerta para supervisor L2. Em 60 min, para gerente de operações.
- O operador pode escalonar manualmente a qualquer momento se julgar que o problema está além de sua capacidade.
- Template de escalonamento: "Incidente #12345 – Crítico – 14:32 – Roteador RTR-SP-01 – Reinicialização não resolveu – Necessário suporte L2 para substituição de hardware."
- Para escalonamento a fornecedor (ex: Huawei, Cisco), abrir chamado no portal do fabricante com número de série do equipamento e logs.
"""

version = "0.0.1"
