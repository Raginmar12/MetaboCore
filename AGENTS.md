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

## Revisión normativa NOM-004

Antes de realizar cambios arquitectónicos relacionados con pacientes, consultas, documentos clínicos, almacenamiento, exportación, impresión, firma, confidencialidad o conservación, revisar:

- `docs/03_capa_nom/nom_004/README.md`
- `docs/03_capa_nom/nom_004/referencia_normativa.md`
- `docs/03_capa_nom/nom_004/revision_arquitectonica.md`
- `docs/03_capa_nom/nom_004/matriz_requisitos.md`
- `docs/03_capa_nom/mapeo_nom_004.md`

La fuente oficial en Markdown ya fue incorporada manualmente y está disponible en:

- `docs/03_capa_nom/nom_004/fuente_oficial/NOM-004-SSA3-2012_DOF.md`
- `docs/03_capa_nom/nom_004/fuente_oficial/README.md`

Los agentes no deben reemplazar ni reescribir automáticamente la fuente oficial completa. Cualquier actualización de la fuente normativa debe hacerse de forma explícita y revisada.

No declarar cumplimiento completo de la NOM-004 hasta que exista una revisión específica y documentada.

La NOM-004 debe guiar la capa documental y de cumplimiento, pero no debe reemplazar el flujo clínico humano de MetaboCare.

## Reglas para el visor Django

- El visor Django en `metabocore_app/` es un prototipo de visualización de formatos clínicos, no un expediente clínico electrónico.
- No crear modelos clínicos sin ADR y revisión arquitectónica previa.
- No crear modelos `Paciente`, `Expediente` ni `Consulta` sin revisión NOM-004 documentada.
- No agregar persistencia de datos de pacientes sin revisión NOM-004.
- El visor no debe guardar datos reales de pacientes.
- Cualquier evolución hacia pacientes, expedientes, consultas, autenticación, persistencia o generación documental requiere revisión arquitectónica y NOM-004.
