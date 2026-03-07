"""Production lines and bottleneck management."""

title = "Líneas de producción y cuellos de botella"

content = """
Una línea de producción tiene una capacidad máxima determinada por su etapa más lenta
(cuello de botella). En alimentos y bebidas, típicamente es la etapa de envasado o
llenado.

**Identificación del cuello:** Medir el throughput por etapa (kg/h, unidades/h). La etapa
con menor capacidad limita el resto. Aumentar capacidad en otras etapas no mejora el
output total si el cuello no se alivia.

**Planificación:** La capacidad efectiva es la del cuello menos paradas planificadas
(mantenimiento, cambios de formato) y pérdidas por arranques y ajustes.

**Sierra Negra:** Cada línea tiene una ficha de capacidad por SKU. La planificación
agrupa órdenes por línea y evita sobrecargar el cuello; si hay exceso de demanda,
se prioriza o se desplaza a otra ventana.
"""  # noqa: E501

version = "0.0.1"
