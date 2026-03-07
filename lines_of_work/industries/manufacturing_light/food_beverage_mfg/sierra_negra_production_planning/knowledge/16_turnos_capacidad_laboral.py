"""Shifts and labor capacity for production."""

title = "Turnos y capacidad laboral"

content = """
La capacidad de producción depende de la disponibilidad de operarios y turnos.
Sierra Negra opera en turnos que deben alinearse con el plan de producción.

**Configuración de turnos:** Mañana, tarde, noche. Algunas líneas pueden operar
en uno o dos turnos según demanda y coste. La planificación conoce la capacidad
por turno y por línea.

**Ausencias y variabilidad:** Las bajas por enfermedad o vacaciones reducen la
capacidad efectiva. Se usa un factor de utilización histórica para ajustar.

**Formación:** Los operarios polivalentes permiten flexibilidad. La planificación
considera las restricciones de cualificación cuando asigna órdenes a líneas.
"""  # noqa: E501

version = "0.0.1"
