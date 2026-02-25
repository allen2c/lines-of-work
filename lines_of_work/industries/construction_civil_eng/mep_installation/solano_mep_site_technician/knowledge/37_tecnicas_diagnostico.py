title = "Técnicas de Diagnóstico y Solución de Problemas MEP"

content = """
El diagnóstico eficaz de problemas en sistemas MEP requiere un enfoque metódico: recopilar
síntomas, formular hipótesis, probar y confirmar. La experiencia y el conocimiento de los
sistemas permiten reducir el tiempo de diagnóstico y minimizar la interrupción del servicio.

**Metodología general de diagnóstico:**
1. Recopilar información del problema: ¿Cuándo comenzó? ¿En qué condiciones? ¿Qué cambios
   se hicieron recientemente? ¿Es intermitente o continuo?
2. Revisar el sistema sin intervenir: lecturas de presión, temperatura, tensión, corriente,
   caudal de aire. Comparar con los valores de diseño o commissioning.
3. Formular hipótesis ordenadas de más probable a menos probable, basándose en los síntomas.
4. Probar cada hipótesis de la manera menos invasiva posible, comenzando por verificaciones
   sin desconectar.
5. Confirmar la causa raíz y corregir.
6. Verificar que el sistema funciona normalmente tras la corrección.
7. Documentar el problema, la causa y la solución para referencia futura.

**Herramientas de diagnóstico:**
- *Termografía infrarroja:* Cámara termográfica que detecta puntos calientes en tableros
  eléctricos (conexiones flojas, sobrecargas), condensadores sucios en chillers y pérdidas
  de calor en aislamiento deficiente.
- *Analizador de redes:* Registra parámetros eléctricos durante el tiempo (tensión, corriente,
  THD armónico, factor de potencia, interrupciones). Identifica distorsiones y desequilibrios.
- *Medidor de ultrasonido:* Detecta fugas en tuberías a presión, fugas de refrigerante,
  arcos eléctricos en tableros (emiten ultrasonido en frecuencias que no se oyen).
- *Manómetro diferencial digital:* Para diagnóstico de caída de presión en filtros, válvulas
  y serpentines de HVAC.
- *Registrador de datos (data logger):* Registra temperaturas, presiones o corrientes en
  el tiempo para detectar patrones intermitentes no visibles en mediciones instantáneas.

**Diagnóstico en plomería:** Ante una pérdida de presión en el sistema: verificar si hay
válvulas cerradas inadvertidamente antes de asumir una fuga. Usar el manómetro de presión
aguas arriba y aguas abajo de cada sección para aislar el segmento con pérdida.

**Diagnóstico en electricidad:** Ante un interruptor que dispara repetidamente: medir la
corriente real del circuito antes de cambiar el interruptor por uno de mayor capacidad.
El disparo puede indicar sobrecarga real, cortocircuito o falla de aislamiento —cada
causa tiene solución distinta.
"""  # noqa: E501

version = "0.0.1"
