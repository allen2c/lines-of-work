title = "Explosión de BOM"

content = """
Explosionar la BOM significa multiplicar las cantidades de cada componente por las
necesidades del nivel superior, recursivamente hasta llegar a materias primas y
componentes comprados.

**Ejemplo:** Si el MPS exige 100 unidades del producto A, y A contiene 2 unidades del
submódulo B, y B contiene 3 resistencias, las necesidades brutas de resistencias
serán 100 × 2 × 3 = 600.

**Consideraciones:** Factores de desperdicio y rendimiento (yield) se aplican según
políticas. Los ítems con múltiples padres (donde un mismo componente se usa en varios
productos) se agregan en el MRP. La explosión puede ejecutarse por lote o por demanda
en tiempo real según el sistema.
"""  # noqa: E501

version = "0.0.1"
