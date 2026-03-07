"""Aggregate vs detailed production planning."""

title = "Plan agregado vs plan detallado"

content = """
La planificación opera en dos niveles: agregado (mensual/semanal por familia de
productos) y detallado (órdenes de fabricación por lote y línea).

**Plan agregado:** Asigna capacidad a familias de productos. Equilibra demanda
y capacidad, identifica cuellos de botella y guía decisiones de inventario o
subcontratación. Horizonte: 3–12 meses.

**Plan detallado:** Convierte el plan agregado en órdenes concretas con fechas,
líneas y secuencias. Considera lotes mínimos, cambios de formato y disponibilidad
de materiales. Horizonte: 1–4 semanas.

**Consistencia:** El plan detallado debe ser coherente con el agregado. Las
desviaciones se comunican y el plan agregado se revisa si es necesario.
"""  # noqa: E501

version = "0.0.1"
