"""
Knowledge item 75: production smoke verification. Ensures post-deployment smoke
checks validate critical paths and fail fast when core functionality breaks.
"""

title = "production smoke verification"

content = """
La verificación de smoke en producción confirma que los caminos críticos del
sistema responden correctamente inmediatamente después de un despliegue. Sin
estas comprobaciones, los fallos en funcionalidad básica pueden pasar
desapercibidos hasta que los usuarios o el monitoreo los detecten.

**Contexto:** En servicios de alto tráfico con APIs distribuidas, un despliegue
exitoso no garantiza que el sistema funcione. Cambios en configuración,
dependencias o datos pueden provocar fallos silenciosos. Los smoke tests en
producción deben ser rápidos, no invasivos y centrados en los flujos que
impactan directamente a los usuarios y al negocio.

**Procedimientos principales:**
1) Definir un conjunto mínimo de endpoints y flujos que representen el camino
   crítico: autenticación, lectura/escritura principal, y puntos de integración
   externa esenciales.
2) Ejecutar smoke tests automáticamente tras cada despliegue, antes de marcar
   el release como estable. Los tests deben completarse en segundos, no minutos.
3) Integrar los resultados con el pipeline de CI/CD: un smoke fallido debe
   disparar alertas y, según política, considerar rollback automático o
   bloqueo de tráfico hacia la nueva versión.
4) Evitar tests que modifiquen datos reales o generen carga significativa;
   usar lecturas idempotentes y datos de prueba aislados cuando sea posible.
5) Documentar los criterios de éxito y el tiempo máximo de ejecución esperado
   para cada smoke test, y revisarlos cuando cambien los flujos críticos.

**Criterios de aceptación:** Los smoke tests en producción se consideran
verificados si se ejecutan en cada despliegue, cubren al menos los flujos
críticos acordados, fallan de forma clara y auditable, y están integrados
con el proceso de release y monitoreo.

**Fallos comunes:** Smoke tests demasiado lentos que retrasan el feedback;
cobertura insuficiente que deja pasar regresiones; tests que alteran datos
de producción. Mitigación: mantener el conjunto de smoke pequeño y estable,
revisar periódicamente su relevancia, y aislar cualquier operación de escritura.
"""  # noqa: E501

version = "0.0.1"
