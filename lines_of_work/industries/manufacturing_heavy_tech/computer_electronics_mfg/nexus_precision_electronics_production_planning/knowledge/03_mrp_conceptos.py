title = "Material Requirements Planning (MRP)"

content = """
MRP calcula las cantidades y fechas de materiales y componentes necesarios para cumplir
el plan maestro. A partir del MPS y de las listas de materiales (BOM), determina qué
fabricar o comprar, en qué cantidad y para cuándo.

**Proceso:** Explosión de BOM multinivel, cálculo de necesidades brutas, descuento de
inventario disponible y en tránsito, aplicación de lead times y políticas de lote.
Resultado: órdenes de fabricación (OF) y órdenes de compra (OC) planificadas.

**Limitaciones:** MRP asume capacidad infinita; no resuelve cuellos de botella. La
planificación de capacidad debe validar el resultado. Los lead times y BOM deben estar
actualizados para que el cálculo sea fiable.
"""  # noqa: E501

version = "0.0.1"
