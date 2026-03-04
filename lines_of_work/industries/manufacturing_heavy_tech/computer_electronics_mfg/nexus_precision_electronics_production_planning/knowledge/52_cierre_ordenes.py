title = "Cierre de órdenes de fabricación"

content = """
Una OF se cierra cuando la producción está completa, los consumos registrados y el
producto entregado a almacén o al siguiente proceso. El cierre actualiza inventario
y libera capacidad en el plan.

**Proceso:** Verificar cantidades producidas y consumidas, registrar scrap o
desviaciones, cerrar la OF en el sistema. Las cantidades no completadas (parciales)
se gestionan según política: cerrar y crear nueva OF para el resto, o mantener abierta.

**Importancia:** OF abiertas obsoletas distorsionan el MRP y los reportes. Establecer
procedimiento de cierre periódico y revisar órdenes huérfanas (sin avance significativo).
"""  # noqa: E501

version = "0.0.1"
