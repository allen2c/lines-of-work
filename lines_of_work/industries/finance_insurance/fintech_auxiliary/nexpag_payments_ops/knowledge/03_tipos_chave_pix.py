title = "Tipos de Chave PIX e Validações"

content = """
- CPF (11 dígitos) e CNPJ (14 dígitos): validar com dígito verificador e consultar situação na Receita Federal (ativa/regular).
- E-mail: formato padrão (user@dominio.com), sem caracteres especiais proibidos; verificar se já está cadastrado em outra conta.
- Telefone: +55 (DDD) + número (8 ou 9 dígitos) – aceitar apenas celular; validar com operadora via SMS de confirmação.
- Chave aleatória: UUID v4 gerado pelo sistema; não pode ser alterada pelo usuário; única por conta.
- Cada chave pode ser vinculada a apenas uma conta; se o usuário tentar cadastrar chave já existente, o DICT rejeita.
"""

version = "0.0.1"
