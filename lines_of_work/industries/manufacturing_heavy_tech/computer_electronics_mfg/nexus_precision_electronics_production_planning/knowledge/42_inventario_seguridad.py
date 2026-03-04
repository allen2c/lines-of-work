title = "Cálculo y revisión de inventario de seguridad"

content = """
El inventario de seguridad se calcula para cubrir la variabilidad. Fórmula común:
SS = Z × √(σ_d² × L + σ_L² × d²), donde Z es el factor de nivel de servicio, σ_d
desviación de demanda, σ_L de lead time, L y d valores medios.

**Revisión:** Recalcular periódicamente con datos recientes. Si la demanda o los
plazos cambian, los niveles deben ajustarse. Exceso de seguridad encubre problemas
de suministro o previsión; insuficiente genera rupturas.

**Por ítem:** No todos los ítems necesitan el mismo nivel. Clasificar por criticidad
(impacto de ruptura) y variabilidad. Ítems de alto valor o largo plazo de reaprovisionamiento
pueden justificar más stock; los de bajo valor, menos.
"""  # noqa: E501

version = "0.0.1"
