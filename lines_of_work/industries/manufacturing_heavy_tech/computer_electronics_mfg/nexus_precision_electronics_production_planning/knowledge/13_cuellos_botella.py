title = "Cuellos de botella"

content = """
Un cuello de botella es un recurso cuya capacidad limita el output total del sistema.
Aumentar la capacidad en otros centros no mejora el throughput si el cuello no se
alivia.

**Identificación:** Centros con utilización sostenida cerca o por encima del 100%,
colas de trabajo crecientes, órdenes retrasadas que pasan por ese centro.

**Gestión:** Priorizar el trabajo en el cuello, evitar paradas innecesarias, reducir
setups, externalizar si es posible. Las decisiones de nivelación o cambios de mix
deben considerar explícitamente el impacto en el cuello. Escalar si se requieren
inversiones o cambios estructurales.
"""  # noqa: E501

version = "0.0.1"
