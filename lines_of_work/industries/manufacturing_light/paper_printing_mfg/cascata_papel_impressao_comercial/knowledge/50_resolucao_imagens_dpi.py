"""
Resolução de imagens e requisitos de DPI.
"""

title = "Resolução de Imagens (DPI)"

content = """
DPI (dots per inch) indica a densidade de pontos na impressão.
Para impressão offset e digital de qualidade, imagens devem
ter 300 dpi na dimensão final de impressão. Abaixo disso,
a imagem pode ficar pixelada ou com bordas serrilhadas.

**Dimensão Final:** Uma imagem 3×4 cm no impresso final
deve ter pelo menos 354×472 pixels (3×39,37×300 e 4×39,37×300,
aproximadamente). Imagens ampliadas do tamanho original
perdem qualidade.

**Imagens da Internet:** Muitas imagens de sites têm 72
ou 96 dpi e tamanho pequeno. Não são adequadas para
impressão. Avisar o cliente quando o arquivo contiver
imagens de baixa resolução.

**Vectorial:** Logos e ilustrações em vetor (AI, SVG,
EPS) não dependem de DPI e escalam sem perda.
"""  # noqa: E501

version = "0.0.1"
