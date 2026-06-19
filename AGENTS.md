# Instrucciones para agentes de IA

Este repositorio contiene la documentación clínica-operativa inicial de MetaboCore. Antes de modificarlo, respete estas reglas:

## Reglas clínicas y de arquitectura

- Antes de crear código, lea `docs/01_flujo_consulta/`.
- No cree modelos de expediente clínico genérico antes de entender el flujo MetaboCare.
- No trate la NOM como el flujo principal de consulta.
- La NOM es una capa documental de cumplimiento, no el orden conversacional de la consulta.
- MetaboCore debe mantenerse como proyecto independiente.
- Si se agregan integraciones externas en el futuro, deben documentarse como APIs o interfaces explícitas.
- Si se agrega código en el futuro, debe derivarse de los formatos y flujos documentados.

## Privacidad y datos clínicos

- No use datos reales de pacientes en ejemplos, pruebas, documentación ni fixtures.
- Los ejemplos clínicos deben ser ficticios y estar claramente marcados como ficticios.
- No agregue carpetas, archivos, semillas, fixtures o bases de datos con información identificable o potencialmente identificable.

## Estilo documental

- Mantenga los documentos en español.
- Use un estilo claro, clínico, ordenado y operativo.
- Priorice el flujo real de consulta antes que plantillas normativas o modelos técnicos.
