title = "Prevenção a Fraude: Controles de Velocidade (Velocity Checks)"

content = """
- Regra 1: Máximo de 5 transações PIX por minuto para o mesmo CPF/CNPJ. Acima disso, bloqueio temporário de 30 minutos.
- Regra 2: Máximo de 10 transações recebidas em 1 hora para a mesma chave PIX (suspeita de "mula").
- Regra 3: Máximo de 3 tentativas de PIX para chaves diferentes em 5 minutos (ataque de força bruta).
- Regra 4: Máximo de 2 transações com mesmo valor exato (ex.: R$ 1.999,99) em 1 hora (tentativa de burlar limite).
- Essas regras são configuráveis no NexOps; o analista pode ajustar temporariamente com aprovação do supervisor.
"""

version = "0.0.1"
