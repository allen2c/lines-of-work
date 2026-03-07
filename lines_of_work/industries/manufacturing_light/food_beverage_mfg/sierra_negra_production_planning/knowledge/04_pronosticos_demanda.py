"""Demand forecasting for production planning."""

title = "Pronósticos de demanda y planificación agregada"

content = """
El plan de producción se basa en pronósticos de demanda. Sierra Negra recibe pronósticos de
ventas (mensuales, semanales) y los desagrega por referencia y por canal.

**Horizonte:** Plan agregado a 3–12 meses; plan detallado a 2–4 semanas. Los pronósticos
más lejanos tienen mayor incertidumbre.

**Estacionalidad:** Productos de temporada (refrescos en verano, conservas en invierno) generan
picos. La planificación debe anticipar capacidad y stock para esos picos.

**Ajustes:** Ventas reales vs pronóstico se revisan semanalmente. Desviaciones importantes
generan replanificación y posible expedición de pedidos urgentes.
"""  # noqa: E501

version = "0.0.1"
