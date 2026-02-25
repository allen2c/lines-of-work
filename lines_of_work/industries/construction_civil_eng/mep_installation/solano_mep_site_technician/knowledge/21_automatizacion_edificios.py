title = "Automatización de Edificios (BMS/BAS)"

content = """
El Sistema de Gestión de Edificios (BMS, Building Management System; también llamado BAS,
Building Automation System) integra el monitoreo y control de todos los sistemas MEP de
un edificio desde una plataforma centralizada. Permite optimizar el consumo energético,
detectar fallas de forma proactiva y mantener registros operativos completos.

**Alcance del BMS:** Un BMS típico supervisa y controla:
- Sistemas HVAC: arranque/paro de UMAs, chillers, torres y bombas; control de temperatura
  y humedad por zona; control de presión en ductos.
- Iluminación: encendido programado, atenuación por sensores de presencia y luminosidad.
- Sistemas eléctricos: monitoreo de consumo por tablero, detección de demanda máxima,
  gestión de transferencia automática.
- Plomería: control de bombas de presión, detección de fugas, monitoreo de nivel en cisternas.
- Elevadores, acceso y CCTV en sistemas integrados avanzados.

**Protocolos de comunicación:** Los dispositivos de campo (controladores, sensores,
actuadores) se comunican con el BMS mediante protocolos estandarizados:
- *BACnet (ASHRAE 135):* El protocolo más extendido en HVAC/BAS.
- *Modbus RTU/TCP:* Ampliamente usado en equipos industriales y medidores eléctricos.
- *KNX:* Popular en automatización residencial y pequeños edificios en Europa.
- *LonWorks:* Usado en sistemas legados de algunos fabricantes.

**Controladores de campo (DDC):** Los Direct Digital Controllers (DDC) ejecutan localmente
los algoritmos de control (PID, encendido/apagado, secuencias de arranque) y reportan al
servidor del BMS. Un DDC correctamente programado puede operar de forma autónoma si se
pierde comunicación con el servidor.

**Integración durante la instalación MEP:** El técnico MEP debe dejar previsto el cableado
de señal (par trenzado, RS-485, Ethernet) para cada punto de campo indicado en el plano
de control. Los sensores de temperatura (PT100, NTC, 4-20 mA) deben instalarse en
ubicaciones representativas, alejados de fuentes de calor o corrientes de aire locales.

**Comisionamiento del BMS:** La puesta en marcha del BMS incluye la verificación punto
a punto de cada señal, la programación de setpoints y secuencias, y la capacitación del
equipo de mantenimiento del cliente.
"""  # noqa: E501

version = "0.0.1"
