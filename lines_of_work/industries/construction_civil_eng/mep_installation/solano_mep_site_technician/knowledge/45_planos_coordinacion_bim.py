title = "Planos de Coordinación MEP y Metodología BIM"

content = """
La metodología BIM (Building Information Modeling) ha transformado la planificación e
instalación de sistemas MEP en proyectos de mediana y gran escala. BIM permite crear un
modelo tridimensional de todos los sistemas de la edificación antes de instalar, detectar
colisiones virtualmente y optimizar las rutas de instalación con un alto nivel de precisión.

**¿Qué es BIM en contexto MEP?** El modelo BIM MEP es la representación digital de todos
los sistemas mecánicos, eléctricos y de plomería en su ubicación exacta dentro del edificio.
Incluye los diámetros reales de tuberías, las dimensiones de ductos, la ubicación de equipos
y los soportes. Permite medir longitudes, calcular interferencias y generar listas de
materiales (BOM, Bill of Materials) directamente del modelo.

**Niveles de desarrollo (LOD):** El nivel de detalle del modelo BIM evoluciona a lo largo
del proyecto. El LOD 300-350 es el habitual en diseño para construcción; el LOD 400 incluye
el nivel de fabricación (spools de tubería); el LOD 500 representa el as-built (conforme
a obra). El técnico MEP trabaja con modelos LOD 300-400 en obra.

**Detección de colisiones (clash detection):** Navisworks, Revit y otros softwares combinan
los modelos de estructura, arquitectura y MEP para identificar automáticamente interferencias
(hard clashes: dos objetos se interpenetran; soft clashes: distancia insuficiente para
mantenimiento; workflow clashes: secuencia incorrecta de instalación).

**Reuniones de coordinación BIM:** Los responsables de cada especialidad se reúnen para
resolver las colisiones detectadas, priorizar rutas y tomar decisiones de rediseño antes
de llegar a obra. Cada decisión se documenta en el modelo y en el registro de coordinación.

**Uso en campo:** Algunos proyectos dotan al técnico de tablet con acceso al modelo BIM
en el sitio, permitiéndole verificar dimensiones, ubicaciones exactas y detalles de
instalación en tiempo real. El escaneo láser 3D del edificio construido puede compararse
con el modelo BIM para verificar tolerancias.

**Transición al as-built:** Al finalizar la instalación, las modificaciones de campo
(cambios de ruta, diámetros diferentes, equipos sustituidos) se actualizan en el modelo
BIM para generar el as-built digital. Este modelo es entregado al cliente como parte
del dossier final de obra.
"""  # noqa: E501

version = "0.0.1"
