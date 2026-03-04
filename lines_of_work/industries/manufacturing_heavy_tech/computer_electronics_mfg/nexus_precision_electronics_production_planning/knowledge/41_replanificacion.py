title = "Replanificación y frecuencia"

content = """
Replanificar significa volver a ejecutar MRP (y en su caso MPS) con datos actualizados:
demandas, inventarios, órdenes abiertas, cambios en BOM o rutas.

**Frecuencia:** Puede ser diaria, semanal o según eventos (cambio significativo). Más
frecuente da más precisión pero genera nerviosismo si cada replan cambia muchas
órdenes; menos frecuente estabiliza pero puede retrasar la respuesta a problemas.

**Reglas:** Congelar el horizonte cercano (próximos días o semana) para no alterar
órdenes ya liberadas salvo excepción justificada. Documentar qué dispara una replan
y quién la autoriza si afecta compromisos con clientes.
"""  # noqa: E501

version = "0.0.1"
