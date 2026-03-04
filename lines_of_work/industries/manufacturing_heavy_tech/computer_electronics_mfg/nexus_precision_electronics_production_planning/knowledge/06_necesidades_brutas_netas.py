title = "Necesidades brutas y netas"

content = """
**Necesidades brutas:** Cantidad total requerida en cada periodo según la explosión de
BOM y el MPS. No tienen en cuenta lo que ya existe en stock o en tránsito.

**Necesidades netas:** Necesidades brutas menos inventario disponible, menos recibos
planificados (órdenes abiertas). Si el resultado es positivo, se genera una orden de
fabricación o compra; si es cero o negativo, no se requiere acción.

**Plazo:** Las necesidades netas se desplazan en el tiempo según el lead time del ítem.
Un componente con lead time de 2 semanas y necesidad neta en la semana 10 debe liberarse
en la semana 8. El MRP realiza este desplazamiento automáticamente para todos los ítems.
"""  # noqa: E501

version = "0.0.1"
