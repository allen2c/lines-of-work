title = "Tratamento Estatístico"

content = """
- Calcular média aritmética e mediana dos dados homogeneizados.
- Desvio-padrão amostral (s) e coeficiente de variação (CV = s / média * 100%).
- Identificar outliers: valores fora do intervalo [média – 2s ; média + 2s]. Excluir no máximo 20% da amostra.
- Após exclusão, recalcular média e intervalo de confiança (IC) a 80% de confiança (t de Student para amostras pequenas).
- O valor final do imóvel é a média do IC, arredondado para o milhar mais próximo.
- Exemplo: amostra de 10 dados, média R$ 9.500/m², s = R$ 800, IC 80% = [R$ 9.050; R$ 9.950] → valor unitário R$ 9.500/m².
"""  # noqa: E501

version = "0.0.1"
