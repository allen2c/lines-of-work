title = "Motores sin escobillas (BLDC)"

content = """
- Comunes en herramientas a batería de gama alta (Makita, DeWalt, Milwaukee). No tienen escobillas; el control electrónico conmuta las fases.
- Fallas típicas: controlador electrónico dañado, sensores Hall defectuosos, bobinados del estator en corto, imanes del rotor despegados.
- Diagnóstico: primero verifica la batería (voltaje y estado). Luego, con el motor desconectado, mide resistencia entre cada par de fases (U-V, V-W, W-U). Debe ser igual en las tres (típicamente 0.1-0.5 Ω). Si hay diferencia >10%, el bobinado está dañado.
- Prueba de sensores Hall: con alimentación de 5 V (de la herramienta), mide voltaje en las salidas de los sensores mientras giras el rotor manualmente. Deben alternar entre 0 y 5 V. Si uno no cambia, el sensor está muerto.
- No intentes reparar el controlador a nivel de componentes (microcontroladores, MOSFETs) a menos que tengas equipo de reflow y esquemas. Reemplaza la placa completa.
- Si el rotor tiene imanes sueltos, no lo repares; reemplaza el rotor completo. Los imanes son frágiles y pueden desprenderse a alta velocidad.
"""

version = "0.0.1"
