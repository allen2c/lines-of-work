title = "Sistema eléctrico en herramientas con cable"

content = """
- Componentes: cable de alimentación, interruptor, motor (bobinados), condensador (en motores monofásicos), escobillas (en motores universales), protección térmica.
- Prueba de continuidad del cable: con multímetro en modo resistencia (Ω), mide entre el enchufe y el terminal del motor. Debe haber continuidad en ambos conductores (fase y neutro). Si no, el cable está roto internamente.
- Prueba de aislamiento: mide resistencia entre cada conductor y la carcasa metálica. Debe ser >1 MΩ (ideal >10 MΩ). Si es menor, hay fuga a tierra; reemplaza el cable o el motor.
- Interruptor: mide continuidad entre terminales cuando está en posición ON. Debe ser 0 Ω. En OFF debe ser infinito. Si está defectuoso, reemplázalo.
- Condensador de arranque (en motores de inducción): mide capacitancia con un capacímetro. El valor debe estar dentro del ±10% del nominal (ej. 20 µF). Si está abierto o en corto, reemplázalo.
- Protección térmica: algunos motores tienen un termostato que abre el circuito si se sobrecalienta. Mide continuidad en frío; debe ser 0 Ω. Si está abierto, espera a que se enfríe o reemplázalo.
"""

version = "0.0.1"
