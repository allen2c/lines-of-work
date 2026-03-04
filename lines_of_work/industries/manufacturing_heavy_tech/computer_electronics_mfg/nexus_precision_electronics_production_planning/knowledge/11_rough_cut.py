title = "Rough-cut capacity planning"

content = """
Rough-cut es una verificación rápida de capacidad antes de ejecutar el MRP completo.
Usa factores de carga por familia de productos (horas por unidad) aplicados al MPS.

**Proceso:** Multiplicar las cantidades del MPS por los factores de cada familia,
agregar por centro crítico o recurso clave, comparar con horas disponibles. Si hay
sobrecarga, ajustar el MPS (mover producción, reducir cantidades) o identificar
necesidad de overtime/capacidad extra.

**Ventaja:** Rápido y suficiente para decisiones a nivel agregado. No sustituye el
CRP detallado cuando hay muchos centros y rutas complejas, pero evita planes
evidentemente infactibles.
"""  # noqa: E501

version = "0.0.1"
