"""Lead times and delivery deadlines for production planning."""

title = "Plazos de entrega y lead times"

content = """
El lead time es el tiempo transcurrido desde la emisión de la orden hasta la disponibilidad
del producto. En alimentos y bebidas incluye: preparación de materias primas, procesamiento,
envasado, cuarentena de calidad y liberación.

**Lead time interno:** Tiempo de fabricación en planta. Varía según producto, tamaño de lote
y disponibilidad de línea. Los cambios de formato (cambio de SKU en la misma línea) añaden
tiempo de parada.

**Lead time de aprovisionamiento:** Tiempo desde el pedido al proveedor hasta la recepción.
Las materias primas agrícolas suelen tener estacionalidad; los envases y aditivos suelen ser
más predecibles.

**Buffer:** En planificación se añade margen para incertidumbre. Un lead time de 5 días
puede planificarse como 7 para absorber retrasos menores sin afectar al cliente.
"""  # noqa: E501

version = "0.0.1"
