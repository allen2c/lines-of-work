title = "Fatores de Homogeneização"

content = """
- Fator localização: ponderação por bairro, zoneamento, proximidade de comércio, transporte, escolas. Usar tabela interna da Precision com pesos de 0,8 a 1,2.
- Fator área: ajuste por metragem quadrada (imóveis muito grandes ou pequenos têm preço unitário diferente). Aplicar fator de escala (ex.: área do avaliando / área do comparativo) elevado a 0,2.
- Fator padrão construtivo: classificar como baixo (1,0), médio (1,1), alto (1,2), luxo (1,3) conforme tabela do IBAPE.
- Fator estado de conservação: ótimo (1,0), bom (0,9), regular (0,8), ruim (0,6), péssimo (0,4).
- Fator idade: depreciação linear com vida útil de 50 anos para estrutura.
"""  # noqa: E501

version = "0.0.1"
