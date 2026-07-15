title = "Control y ajuste de audio en transmisión"

content = """
- Los niveles de audio deben cumplir con la norma ITU-R BS.1770: loudness integrado de -24 LKFS (±2 LU) para programas, y -23 LKFS para comerciales.
- Usar un medidor de loudness (Dolby LM100) en tiempo real. Si el loudness excede los límites, ajustar la ganancia en la consola o en el procesador de audio.
- Para contenido en vivo, coordinar con el estudio para que ajusten sus niveles. Si no es posible, aplicar compresión suave (ratio 2:1, threshold -20 dBFS).
- Monitorear la fase del audio: si hay cancelación de fase (sonido monoaural), insertar un filtro de corrección.
- Registrar cualquier ajuste manual de audio en el log con valores antes y después.
"""

version = "0.0.1"
