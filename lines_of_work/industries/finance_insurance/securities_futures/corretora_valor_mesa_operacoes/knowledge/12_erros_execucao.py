title = "Tratamento de Erros de Execução"

content = """
- **Erro de Preço**: Se a ordem foi executada a um preço diferente do solicitado (ex: cliente pediu R$ 15,00 e executou R$ 15,50), o operador deve imediatamente:
   - Comunicar o head de mesa e o compliance.
   - Tentar reverter a operação (comprar/vender o mesmo ativo no mesmo dia) se possível, com autorização.
   - Se a reversão gerar perda, a corretora pode absorver até R$ 10.000 por erro; acima disso, o operador pode ser responsabilizado.
- **Erro de Quantidade**: Se executou 1.000 ações em vez de 100, proceder similar. Reverter o excesso no mesmo dia.
- **Erro de Ativo**: Ex: comprou PETR4 em vez de VALE3. Reverter imediatamente. Se o mercado já moveu, a diferença é registrada como perda operacional.
- **Ordem Duplicada**: Se o cliente enviou a mesma ordem duas vezes, cancelar a segunda execução (se possível) ou liquidar a posição extra.
- **Prazo**: Erros devem ser reportados em até 30 minutos. Após o fechamento do pregão, a correção é mais complexa (envolve leilão de reabertura no dia seguinte).
- **Registro**: Todo erro é documentado em formulário de não conformidade e revisado pelo comitê de operações.
"""

version = "0.0.1"
