title = "Monitoreo de señal en tiempo real"

content = """
- Verificar continuamente los parámetros de video: nivel de luminancia (100% blanco, 0% negro), crominancia, relación señal/ruido (>45 dB), y ausencia de artefactos de compresión.
- Monitorear audio: niveles PPM entre -18 dBFS y -10 dBFS para diálogos, picos máximos -6 dBFS; detectar silencios >2 segundos o clipping.
- Usar monitores de forma de onda y vectoscopio para validar la señal SDI o IP (SMPTE 2110). Registrar desviaciones en el log.
- Umbrales de alarma: pérdida de sincronía >1 cuadro, error de CRC en video, desbalance de audio >3 dB entre canales.
- Realizar barridos de frecuencia cada hora en los feeds satelitales para detectar interferencias.
"""

version = "0.0.1"
