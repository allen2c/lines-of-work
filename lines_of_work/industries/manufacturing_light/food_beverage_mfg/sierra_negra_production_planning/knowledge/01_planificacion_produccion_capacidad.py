"""Production planning and capacity management."""

title = "Planificación de producción y gestión de capacidad"

content = """
La planificación de producción equilibra la demanda prevista con la capacidad disponible de las
líneas. Sierra Negra opera líneas de envasado, procesamiento térmico y embotellado; cada una
tiene un ritmo nominal y tiempos de cambio de formato.

**Capacidad nominal:** Se expresa en unidades/hora o toneladas/día. Incluye paradas planificadas
para limpieza y mantenimiento. La capacidad efectiva es menor que la teórica por pérdidas y
ajustes.

**Cuellos de botella:** La línea más lenta limita el output global. La planificación debe
priorizar que el cuello de botella no quede ocioso por falta de materia prima o por colas
en líneas aguas abajo.

**Niveles de utilización:** Objetivo típico 75–85%. Por debajo se desperdicia capacidad; por
encima aumenta el riesgo de retrasos ante incidencias.
"""  # noqa: E501

version = "0.0.1"
