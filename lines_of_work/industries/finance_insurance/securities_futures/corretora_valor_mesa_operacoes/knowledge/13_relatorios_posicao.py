title = "Relatórios de Posição e Exposição"

content = """
- **Relatório Diário de Posição**: Gerado automaticamente ao final do pregão. Contém: ativo, quantidade comprada/vendida, preço médio, valor de mercado, P&L do dia, P&L acumulado, margem utilizada, margem disponível.
- **Relatório de Exposição por Cliente**: Soma de todas as posições (incluindo derivativos) com valor nocional. Mostra percentual de alocação por ativo, setor e classe.
- **Relatório de Risco**: Inclui VaR (99%, 1 dia), stress test (cenários de queda de 10%, 20%), e limites de concentração. Enviado diariamente ao risk manager.
- **Relatório de Execução**: Para clientes que solicitam: detalha cada ordem executada, horário, preço, volume, e comparação com preço médio do dia (VWAP).
- **Relatório de Compliance**: Lista de ordens bloqueadas, alertas de insider, e erros operacionais. Revisado semanalmente.
- **Frequência**: Relatórios diários até 8h do dia seguinte. Relatórios mensais consolidados até o 5º dia útil do mês seguinte.
"""

version = "0.0.1"
