"""
Requisitos de arquivo PDF para impressão profissional.
"""

title = "Requisitos de PDF para Impressão"

content = """
O PDF é o formato preferido para impressão por manter fontes, imagens
e cores encapsulados. Para melhor resultado, recomenda-se PDF/X-1a
ou PDF/X-4, que garantem conformidade com padrões gráficos.

**Resolução de Imagens:** Imagens em bitmap devem ter no mínimo 300 dpi
na dimensão final de impressão. Imagens de menor resolução ficam
pixeladas. Para fundos e elementos de apoio, 150 dpi pode ser aceito
em alguns casos.

**Fontes:** Devem estar incorporadas (embedded) no PDF. Fontes faltando
causam substituição por fontes padrão e quebra de layout. Converter
textos em curvas (outline) elimina dependência de fontes.

**Modo de Cor:** Trabalhos em CMYK são padrão para offset. RGB será
convertido; a conversão pode alterar cores. Cores especiais (Pantone)
exigem definição correta no arquivo.
"""  # noqa: E501

version = "0.0.1"
