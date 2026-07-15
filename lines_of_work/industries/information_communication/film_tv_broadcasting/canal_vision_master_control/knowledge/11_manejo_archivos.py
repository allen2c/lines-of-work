title = "Manejo de archivos de video y audio en servidores"

content = """
- Los archivos se almacenan en servidores NAS con redundancia RAID 6. La capacidad total es de 200 TB, con un uso máximo del 80% para evitar degradación.
- Al recibir un nuevo archivo (desde producción o tráfico), verificar que el nombre siga la convención: PROGRAMA_FECHA_HORA_duracion.mxf.
- Si un archivo está corrupto o no se reproduce, solicitar una nueva copia y eliminar el archivo dañado.
- Realizar limpieza mensual de archivos temporales y no utilizados, previa autorización de archivo.
- Mantener un inventario de todos los archivos con metadatos (duración, codec, fecha de ingreso).
"""

version = "0.0.1"
