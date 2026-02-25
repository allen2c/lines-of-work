title = "Puesta a Tierra y Equipotencialización"

content = """
El sistema de puesta a tierra (PAT) es un componente de seguridad fundamental en toda
instalación eléctrica. Su función es proporcionar un camino de baja impedancia para
las corrientes de falla, de modo que los dispositivos de protección actúen rápidamente
antes de que el usuario reciba una descarga peligrosa.

**Conceptos clave:**
- *Tierra de protección (PE):* Conductor verde o verde/amarillo que conecta las carcasas
  metálicas de los equipos con la tierra. En caso de falla de aislamiento, la corriente
  fluye hacia tierra y activa el interruptor de protección.
- *Tierra de servicio (neutro solidamente puesto a tierra):* En sistemas TN (norma IEC)
  o en sistemas con neutro aterrizado (NEC), el neutro se conecta a tierra en el punto
  de servicio para estabilizar la tensión de fase y facilitar la actuación de protecciones.
- *Tierra de referencia (tierra funcional):* Para equipos electrónicos sensibles que
  necesitan una referencia de tierra limpia (sin ruido), separada del circuito de protección.

**Electrodos de tierra:** Los sistemas de PAT usan electrodos enterrados para establecer
contacto eléctrico con la tierra física:
- *Varilla de copperweld:* Varilla de acero recubierta de cobre (longitud estándar 2,4 m),
  enterrada verticalmente. Resistencia típica < 25 Ω (NEC) o < 10 Ω (instalaciones críticas).
- *Malla de tierra:* Red de conductores de cobre enterrados en cuadrícula, usada cuando
  el suelo es de alta resistividad o se requiere baja resistencia (< 1 Ω en subestaciones).
- *Anillo de tierra:* Conductor de cobre que rodea la cimentación del edificio a cierta
  profundidad; método habitual en edificios nuevos durante la fase de excavación.

**Equipotencialización (bonding):** Todos los elementos metálicos de la instalación
(tuberías, ductos, estructuras, marcos de ventanas en zonas húmedas) deben conectarse
entre sí y al sistema de tierra para eliminar diferencias de potencial que podrían causar
descarga al tocarlos simultáneamente.

**Verificación:** La resistencia de tierra se mide con un telurómetro (earth tester)
usando el método de los tres puntos. Los resultados se registran y se comparan con los
valores máximos especificados en el proyecto y la normativa. Si el valor medido supera
el máximo, se agregan electrodos adicionales o se trata el suelo con sales de tierra.
"""  # noqa: E501

version = "0.0.1"
