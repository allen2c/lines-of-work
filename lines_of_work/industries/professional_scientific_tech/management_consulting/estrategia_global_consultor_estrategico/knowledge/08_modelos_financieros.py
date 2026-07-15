title = "Modelos Financieros en Excel"

content = """\
- Construye modelos financieros para evaluar proyectos de inversión, valoración de empresas o análisis de escenarios. Usa Excel con estructura modular: supuestos, cálculos, resultados.
- Hoja de supuestos: incluye tasas de crecimiento, márgenes, CAPEX, depreciación, tasa de descuento (WACC). Todos los supuestos deben estar en celdas de color amarillo y con comentarios explicativos.
- Hoja de cálculos: estado de resultados, balance general, flujo de caja libre proyectado a 5 años. Usa fórmulas consistentes (sin valores hardcodeados). Valida con comprobaciones de coherencia (ej. activo = pasivo + patrimonio).
- Hoja de resultados: VAN, TIR, Payback, ROI. Incluye análisis de sensibilidad (tabla de datos con variación de ±10% en ingresos y costos). Gráfico de tornado para identificar variables críticas.
- Escenarios: crea tres escenarios (optimista, base, pesimista) con diferentes supuestos de crecimiento y margen. Calcula probabilidades si el cliente las proporciona.
- Formato: usa formato de moneda (€ o $ según cliente), números con separadores de miles, y protección de celdas para evitar cambios accidentales.
- Entregable: archivo .xlsx con macros desactivadas, más un informe de 2 páginas explicando los resultados.
"""  # noqa: E501

version = "0.0.1"
