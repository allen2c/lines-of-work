"""
Requisitos de sangria e margem de corte para arquivos.
"""

title = "Sangria e Margem de Corte"

content = """
A sangria é a extensão do elemento gráfico além da linha de corte para
evitar filetes brancos em caso de pequeno desvio no corte. O padrão
recomendado é 3 mm além da área final.

**Linha de Corte:** Define o formato final do impresso. Elementos
importantes (texto, logos) devem ficar a pelo menos 3–5 mm da linha de
corte para não serem cortados. A margem de segurança interna evita
que o corte “coma” o conteúdo.

**Arquivo Fechado:** O cliente deve fornecer arquivo com sangria já
aplicada, ou a gráfica pode aplicar em pré-impressão (pode haver
custo adicional). Arquivos sem sangria adequada podem gerar filetes
brancos e reclamações.

**Formatos Fechados:** Para cartazes A3, o arquivo deve ter A3 + sangria;
o formato fechado é maior que o aberto. Para encartes e catálogos, cada
página é preparada com sangria na borda externa.
"""  # noqa: E501

version = "0.0.1"
