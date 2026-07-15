title = "Inserción y verificación de pauta comercial"

content = """
- La pauta comercial se recibe del sistema de tráfico con códigos de spot (ISCI). Cada spot tiene duración exacta (15, 30, 60 segundos) y debe coincidir con el archivo en el servidor.
- Antes de cada corte, verificar que el bloque de comerciales esté completo y sin duplicados. Si falta un spot, insertar un filler institucional de la misma duración.
- Monitorear la reproducción: si un spot se salta o se repite, detener la automatización y corregir manualmente. Reportar a tráfico.
- Los cortes comerciales tienen duración fija (por ejemplo, 2 minutos 30 segundos). Ajustar la programación si un programa termina antes o después.
- No modificar la pauta sin autorización de tráfico, excepto en emergencias (ej. noticia de último momento que requiere interrupción).
"""

version = "0.0.1"
