title = "Troubleshooting de Conectividade para Clientes"

content = """
- Para reclamação de cliente sem internet: verificar status do CPE (modem/ONT) no NMS. Se offline, tentar reinicialização remota via comando SNMP.
- Se CPE online mas sem tráfego: testar ping para gateway e servidor DNS. Se falha, verificar VLAN e configuração de porta no switch de acesso.
- Se problema persistir, verificar se há manutenção programada na região. Se não, abrir incidente e escalonar para L2.
- Documentar cada passo no ticket: "Teste de ping para 8.8.8.8 falhou; reinicialização remota do CPE não restaurou; verificado que porta do switch está down – acionado L2."
"""

version = "0.0.1"
