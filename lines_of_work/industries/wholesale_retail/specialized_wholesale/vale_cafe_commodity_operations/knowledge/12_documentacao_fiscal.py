"""Documentação fiscal e NF-e."""

title: str = "Documentação Fiscal e NF-e"

content: str = """
A emissão de notas fiscais eletrônicas (NF-e) é obrigatória para operações de
atacado no Brasil. Erros geram retrabalho e multas.

**Dados obrigatórios:** Emitente, destinatário (com CNPJ/CPF e inscrição
estadual válidos), descrição do produto (NCM correto), quantidade, valor
unitário e total, CFOP, CST/CSOSN e demais campos exigidos pela legislação.

**CFOP:** O Código Fiscal de Operações e Prestações indica a natureza da
operação (venda no estado, interestadual, exportação, etc.). Use o CFOP
adequado para evitar rejeição pela SEFAZ.

**Prazo de emissão:** A NF-e deve ser emitida até a data da saída da mercadoria
ou, no máximo, no dia seguinte, conforme legislação estadual.

**Arquivamento:** Mantenha cópia da NF-e e do XML por pelo menos 5 anos.
Clientes exigem NF-e para crédito de ICMS e contabilização.
"""

version: str = "0.0.1"
