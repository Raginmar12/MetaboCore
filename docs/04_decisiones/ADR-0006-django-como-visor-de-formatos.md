# ADR-0006: Django como visor de formatos clínicos

## Estado
Aceptado

## Contexto
MetaboCore ya documenta flujos, formatos y schemas clínicos. Se necesita una forma de visualizar los formatos para evaluar si se adaptan al flujo real de consulta.

La prioridad sigue siendo flujo clínico primero, formatos operativos después, capa documental NOM como salida y sistema digital al final.

## Decisión
Se introduce Django inicialmente como visor/prototipo de formatos clínicos.

El visor renderiza formatos desde:

- `schemas/forms/`
- `schemas/ui/`
- `schemas/examples/`

El visor no guarda datos, no crea modelos clínicos, no implementa expediente electrónico y no declara cumplimiento completo NOM-004.

El visor no implementa login, usuarios, permisos, recetas, PDFs ni generación documental NOM en esta fase.

## Consecuencias
- Se podrán revisar formatos en navegador antes de implementar persistencia.
- Se reduce el riesgo de diseñar pantallas desconectadas del flujo de consulta.
- Se introduce código Python/Django al repositorio, pero aislado dentro de `metabocore_app/`.
- Los schemas siguen siendo la fuente de estructura para el renderizado.
- Cualquier evolución hacia captura persistente, pacientes, expedientes, consultas, autenticación o generación documental requerirá una decisión posterior y revisión NOM-004.
- El visor debe mostrar advertencias visibles de que no se deben introducir datos reales de pacientes, no guarda información y no declara cumplimiento NOM-004.
