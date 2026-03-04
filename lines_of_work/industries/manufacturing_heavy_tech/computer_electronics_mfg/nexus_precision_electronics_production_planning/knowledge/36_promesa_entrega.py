title = "Promesa de entrega (ATP)"

content = """
ATP (Available to Promise) indica qué cantidades están disponibles para comprometer
en fechas concretas. Combina inventario disponible, recepciones planificadas y
órdenes en fabricación, menos demandas ya comprometidas.

**Uso:** Cuando ventas recibe una solicitud, consulta ATP para ofrecer fecha realista.
Planificación mantiene los datos actualizados y define las reglas (horizonte, agrupación
por familia).

**CTP (Capable to Promise):** Extiende ATP considerando capacidad y materiales no
aún liberados. Da mayor flexibilidad pero requiere cálculos más complejos. En muchos
casos un ATP bien gestionado es suficiente; CTP se reserva para situaciones especiales.
"""  # noqa: E501

version = "0.0.1"
