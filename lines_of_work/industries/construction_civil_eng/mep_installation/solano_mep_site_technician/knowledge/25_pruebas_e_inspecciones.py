title = "Pruebas e Inspecciones de Sistemas MEP"

content = """
Las pruebas formales de los sistemas MEP son el paso previo a la entrega al cliente y
a la habilitación del edificio por parte de las autoridades. Cada sistema tiene sus
propias pruebas de aceptación definidas por normativa y por las especificaciones del proyecto.

**Prueba hidrostática de tuberías a presión:** Se aísla el segmento a probar, se llena
con agua, se purga el aire y se eleva la presión hasta 1,5 veces la presión de trabajo
(o el valor que indique la norma aplicable). La presión se mantiene durante 2 horas mínimo.
Se acepta si no hay caída de presión en manómetro calibrado ni humedad visible en uniones.

**Prueba de estanqueidad de drenaje:** Se tapan las salidas del ramal, se llena con agua
hasta el nivel de la boca más alta y se observa durante 15–30 minutos. Se verifica
ausencia de fugas en uniones y sellos de campana.

**Prueba de resistencia de aislamiento (megger):** Con el circuito sin tensión y los
extremos del conductor desconectados de equipos, se aplica una tensión CC de prueba
(500 V para sistemas de baja tensión) y se mide la resistencia de aislamiento. Valores
aceptables: mínimo 1 MΩ entre conductores y entre conductor y tierra. Valores inferiores
indican daño en el aislamiento que debe corregirse.

**Prueba de continuidad y tierra:** Con el multímetro en modo continuidad, se verifica
que cada conductor llegue al destino correcto y que la tierra de protección tenga
continuidad desde los equipos hasta la barra de tierra del tablero.

**Prueba funcional eléctrica:** Se energiza el sistema con el tablero y se verifica el
funcionamiento correcto de cada circuito: alumbrado, tomacorrientes, equipos de fuerza.
Se comprueba la actuación de los interruptores diferenciales con el botón de prueba.

**Prueba de balanceo de aire (TAB):** El equipo de Testing, Adjusting and Balancing
mide y ajusta los caudales de aire en cada terminal hasta alcanzar los valores de proyecto
con una tolerancia de ±10%. Los resultados se documentan en el informe TAB.

**Prueba de evacuación (smoke test/fire test):** Verificación funcional del sistema de
detección y alarma de incendio, incluyendo la respuesta de cada detector, las alarmas
audibles y visuales, y la señalización al panel.

**Registros de prueba:** Cada prueba genera un certificado firmado por el técnico
ejecutor y el supervisor de calidad. Estos documentos forman parte del dossier de obra
que se entrega al cliente junto con los manuales de operación y mantenimiento.
"""  # noqa: E501

version = "0.0.1"
