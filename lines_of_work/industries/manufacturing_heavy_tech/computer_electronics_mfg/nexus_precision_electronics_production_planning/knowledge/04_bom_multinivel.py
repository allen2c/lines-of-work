title = "BOM multinivel"

content = """
La lista de materiales (BOM) describe la estructura de un producto: qué componentes
entran en cada nivel. En electrónica es habitual tener varios niveles: producto
terminado → submódulos → componentes y materias primas.

**Estructura:** Cada nivel indica cantidades por unidad del padre. Un módulo óptico
puede contener 2 conectores, 1 PCB y 4 tornillos. El MRP recorre la BOM de arriba
abajo (explosión) para obtener las necesidades totales de cada ítem.

**Precisión:** Un BOM incorrecto genera pedidos erróneos, retrasos y scrap. Los ECO
(Engineering Change Orders) deben reflejarse en la BOM antes de planificar. Rev y
efectividad de fechas deben estar documentadas.
"""  # noqa: E501

version = "0.0.1"
