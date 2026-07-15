title = "Niveles de reorden"

content = """
- Cada SKU tiene un punto de reorden calculado como: (demanda diaria promedio × lead time del proveedor en días) + inventario de seguridad.
- Ejemplo: para el producto "Arroz 10kg" con demanda diaria 50 unidades, lead time 3 días, inventario seguridad 15% → punto de reorden = (50×3) + (0.15×50×3) = 150 + 22.5 = 173 unidades (redondeado a 175).
- Los niveles se revisan mensualmente y se ajustan según estacionalidad (ej. aumento en diciembre para bebidas y conservas).
- Si un SKU tiene punto de reorden pero el proveedor no puede surtir, se activa una alerta al comprador para buscar sustituto o ajustar inventario de seguridad al 25%.
- Los pedidos de reabastecimiento se generan automáticamente cada lunes y jueves, consolidando todos los SKU que han alcanzado su punto de reorden.
"""

version = "0.0.1"
