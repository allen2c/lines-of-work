"""
Amostragem e AQL em inspeção de lotes.
"""

title = "Amostragem e AQL"

content = """
O AQL (Acceptable Quality Level) define o nível de qualidade aceitável e
o plano de amostragem. Normas como ISO 2859 estabelecem tamanho da amostra
e critérios de aceitação/rejeição conforme o tamanho do lote.

**Níveis de defeito**: Crítico (inutiliza o produto), Maior (afeta função
ou aparência de forma significativa), Menor (cosmético, aceitável em
alguns contextos). Cada tipo tem seu AQL e contagem separada.

**Tamanho do lote**: Define a letra de código e o tamanho da amostra.
Para lotes grandes, inspecionar uma fração; para lotes pequenos, 100%
pode ser exigido em trabalhos críticos.

**Decisão**: Se defeitos na amostra excedem o número de aceitação do plano,
o lote é rejeitado. Reinspeção ou triagem podem ser acordados.
"""  # noqa: E501

version = "0.0.1"
