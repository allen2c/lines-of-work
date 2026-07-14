title = "Método Comparativo Direto de Dados de Mercado"

content = """
- Método preferencial para imóveis urbanos com mercado ativo.
- Coletar dados de ofertas e transações recentes (até 6 meses) de imóveis semelhantes na mesma região.
- Homogeneizar por fatores: localização (bairro, zoneamento), área privativa (m²), padrão construtivo (baixo, médio, alto), estado de conservação (ótimo, bom, regular, ruim), idade (anos), número de vagas, andar (para apartamentos).
- Aplicar tratamento estatístico: calcular média, mediana, desvio-padrão, coeficiente de variação (CV). CV < 15% indica amostra homogênea.
- Definir valor unitário (R$/m²) e multiplicar pela área do avaliando.
- Exemplo: imóvel de 100 m², amostra com R$ 8.000/m² a R$ 10.000/m², média R$ 9.000/m² → valor estimado R$ 900.000.
"""  # noqa: E501

version = "0.0.1"
