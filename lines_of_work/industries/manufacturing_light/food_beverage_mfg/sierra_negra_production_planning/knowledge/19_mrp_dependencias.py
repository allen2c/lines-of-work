"""MRP and material dependencies in food manufacturing."""

title = "MRP y dependencias de materiales"

content = """
El MRP (Planificación de Requerimientos de Materiales) calcula las necesidades
de materias primas y componentes a partir del plan de producción y las listas
de materiales (BOM).

**Explosión de materiales:** Por cada unidad de producto terminado, la BOM
define cantidades de ingredientes y envases. El plan de producción genera
requisiciones netas considerando stock disponible y pedidos en curso.

**Dependencias:** Algunos productos comparten ingredientes. Un retraso en un
lote puede afectar otros. La planificación debe priorizar según urgencia y
disponibilidad.

**Lotes y caducidad:** En alimentación, los materiales tienen vida útil.
El MRP considera fechas de caducidad para evitar usar materiales obsoletos.
"""  # noqa: E501

version = "0.0.1"
