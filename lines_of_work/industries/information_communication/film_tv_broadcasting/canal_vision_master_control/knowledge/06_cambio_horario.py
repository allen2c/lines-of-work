title = "Manejo de cambios de horario (horario de verano/invierno)"

content = """
- En México, el horario de verano inicia el primer domingo de abril a las 2:00 AM (adelantar 1 hora) y termina el último domingo de octubre a las 2:00 AM (retrasar 1 hora).
- El sistema de automatización debe actualizarse con la nueva zona horaria. Verificar que los eventos programados para la hora del cambio se ejecuten correctamente.
- Durante el cambio de primavera, la hora 2:00-3:00 no existe; los eventos programados en ese lapso deben omitirse o reprogramarse.
- Durante el cambio de otoño, la hora 1:00-2:00 se repite; asegurar que los eventos no se dupliquen. Coordinar con programación para ajustar la parrilla.
- Realizar una prueba de simulación 24 horas antes del cambio para detectar errores.
"""

version = "0.0.1"
