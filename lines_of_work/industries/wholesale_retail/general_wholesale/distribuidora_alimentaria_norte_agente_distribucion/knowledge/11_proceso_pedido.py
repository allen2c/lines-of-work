title = "Proceso de recepción y validación de pedidos"

content = """
- El pedido puede llegar por: portal web, correo electrónico (formato estándar), llamada telefónica o integración EDI.
- El agente verifica: datos del cliente (código, dirección, RFC), productos solicitados (código, cantidad), precio unitario según categoría, y condiciones de entrega.
- Se valida disponibilidad de inventario en el almacén asignado; si no hay suficiente, se consulta disponibilidad en otros almacenes (con costo de flete adicional).
- Se verifica el límite de crédito y el saldo de la cuenta; si todo está correcto, se genera un número de pedido (formato P-2025-XXXXX) y se envía confirmación al cliente.
- El pedido pasa a estado "En preparación" y se asigna a la ruta de entrega correspondiente.
"""

version = "0.0.1"
