title = "Tableros de Distribución Eléctrica"

content = """
El tablero de distribución es el nodo central donde la energía se divide en circuitos
secundarios protegidos individualmente. Su correcto dimensionamiento, instalación y
documentación es crítico para la seguridad y operabilidad del sistema eléctrico.

**Tipos de tableros:**
- *Tablero principal (main panel):* Recibe la acometida del transformador o de la red
  pública y alimenta los subtableros. Contiene el interruptor general y protecciones
  de los circuitos derivados de mayor capacidad.
- *Subtablero o tablero de distribución secundaria:* Instalado en cada planta o zona;
  protege los circuitos de iluminación, tomacorrientes y equipos del área.
- *Tablero de control motor (MCC):* Agrupa arrancadores, variadores de frecuencia y
  protecciones de motores eléctricos en proyectos industriales o grandes instalaciones HVAC.
- *Tablero de transferencia automática (ATS):* Conmuta automáticamente entre la red
  comercial y el generador de emergencia cuando se detecta ausencia de tensión.

**Componentes internos:**
- *Interruptores termomagnéticos (breakers):* Protegen contra sobrecarga y cortocircuito.
  Se seleccionan según la corriente nominal del circuito y la corriente de cortocircuito
  máxima del punto de instalación.
- *Interruptores diferenciales (GFCI/RCD):* Detectan corrientes de fuga hacia tierra
  (>5 mA para protección de personas, 30 mA general). Obligatorios en baños, cocinas,
  áreas húmedas y exteriores.
- *Barras de distribución (bus bars):* Conductores de cobre desnudo o estañado que
  distribuyen la corriente a todos los interruptores del tablero.
- *Bloque de neutros y barra de tierra:* El neutro y la tierra están separados en
  subtableros; sólo se unen en el punto de servicio (tablero principal o transformador).

**Instalación y montaje:** Los tableros se instalan en superficies sólidas, a altura de
trabajo ergonómica (centro del tablero entre 1,2 y 1,8 m del piso). Deben tener espacio
libre de trabajo de al menos 0,9 m frente al tablero según NEC. Las entradas de conduit
deben sellarse para evitar el ingreso de insectos, polvo y humedad.

**Etiquetado:** Cada interruptor debe identificarse claramente con el circuito o equipo
que protege, el calibre del conductor y la corriente nominal. El diagrama unifilar del
tablero debe mantenerse actualizado y visible en la tapa interna.
"""  # noqa: E501

version = "0.0.1"
