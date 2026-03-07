"""Safety stock and inventory levels."""

title = "Inventario de seguridad y niveles de stock"

content = """
El inventario de seguridad protege contra variabilidad de demanda y de suministro. En
alimentación, la vida útil limita cuánto se puede almacenar.

**Cálculo básico:** Stock de seguridad = factor de servicio × desviación típica de demanda
durante lead time. A mayor factor, menor riesgo de ruptura y mayor inventario.

**Vida útil:** Productos frescos o con fecha corta exigen rotación rápida. No tiene sentido
mantener meses de stock si la vida útil es de semanas.

**Punto de pedido:** Cuando el stock disponible cae por debajo del punto de pedido, se
lanza una orden de producción o de compra. Punto de pedido = demanda durante lead time +
stock de seguridad.
"""  # noqa: E501

version = "0.0.1"
