title = "Gestión del sistema de automatización de playout"

content = """
- El sistema principal es Harmonic MediaGrid con servidores Spectrum. La lista de reproducción (playlist) se carga desde el sistema de tráfico (Broadcast Traffic) cada 24 horas.
- Verificar que todos los eventos tengan duración correcta y archivos asociados. Si un archivo falta, el sistema muestra "missing media" – debo reemplazar con un clip de relleno o solicitar el archivo a archivo.
- Supervisar la ejecución: cada evento debe iniciar en el segundo exacto (NTP sincronizado). Tolerancia de ±1 segundo; si excede, intervenir manualmente.
- Conocer atajos de teclado para pausar, saltar, o insertar eventos en vivo. No usar la interfaz táctil en emergencias.
- Realizar copia de seguridad de la playlist cada 6 horas en un servidor externo.
"""

version = "0.0.1"
