title = "Políticas de lote"

content = """
Las políticas de lote definen cómo agrupar las necesidades en órdenes. Opciones comunes:
lote a lote (lot-for-lot), tamaño fijo, múltiplo, mínimo/máximo, período fijo.

**Lote a lote:** Ordenar exactamente lo necesario en cada periodo. Minimiza inventario
pero puede aumentar costes de setup y número de órdenes.

**Tamaño fijo:** Siempre pedir una cantidad determinada (ej. 500 unidades). Útil cuando
hay restricciones de proveedor o equipos con setup costoso.

**Mínimo/máximo:** Mantener stock entre umbrales; cuando baja del mínimo, pedir hasta
el máximo. Adecuado para ítems de bajo valor o consumo estable.
"""  # noqa: E501

version = "0.0.1"
