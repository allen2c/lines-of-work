title = "ERP y módulos de producción"

content = """
Los ERP integran ventas, compras, inventario, fabricación y finanzas. Los módulos de
producción gestionan BOM, rutas, MPS, MRP, OF y seguimiento. Planificación opera
principalmente dentro de estos módulos.

**Flujo típico:** MPS se introduce o calcula desde demandas; MRP explota BOM y genera
recomendaciones; planificación libera OF, ajusta fechas y monitoriza. Los datos maestros
(BOM, rutas, lead times, políticas) deben estar correctos.

**Integración:** Cambios en ventas (nuevos pedidos, cancelaciones) deben reflejarse
en el plan. Consumos y entregas en planta actualizan el inventario y alimentan el
siguiente ciclo MRP.
"""  # noqa: E501

version = "0.0.1"
