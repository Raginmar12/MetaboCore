# ADR-0007: MetaboCore como generador de formatos imprimibles

## Estado
Aceptado

## Contexto
MetaboCore ya cuenta con documentación clínica, schemas y un visor Django de formatos. El objetivo inmediato del proyecto es probar y refinar formatos durante la consulta presencial antes de avanzar hacia captura electrónica o expediente clínico.

La prioridad sigue siendo validar el flujo humano de consulta y los formatos operativos antes de crear persistencia clínica, generación documental formal o expediente electrónico.

## Decisión
MetaboCore priorizará, en esta fase, la creación, visualización e impresión de formatos clínicos derivados de schemas.

El visor conservará sus vistas estructurales:

- Preview
- Ejemplo ficticio
- Schema
- UI schema
- JSON ejemplo

Y agregará una vista:

- Imprimible

La vista imprimible estará pensada para impresión en papel y llenado manual durante consulta presencial. La estructura imprimible debe derivarse de `schemas/forms/` y `schemas/ui/`, sin duplicar manualmente cada formato en templates.

## Límites
- No guarda datos.
- No procesa datos reales.
- No crea modelos clínicos.
- No genera PDF desde backend en esta fase.
- No implementa expediente clínico electrónico.
- No implementa login, usuarios ni permisos.
- No declara cumplimiento completo NOM-004.
- No sustituye la revisión normativa posterior.
- No modifica la fuente oficial de la NOM-004.

## Consecuencias
- MetaboCore puede usarse como taller de diseño de formatos clínicos.
- El equipo puede probar formularios en papel antes de digitalizar.
- Se reduce la fricción clínica al evitar capturas electrónicas prematuras.
- Se mantiene el camino para transición futura a captura digital, documentos generados y expediente electrónico, pero solo después de validar el flujo en consulta real.
- Cualquier evolución hacia persistencia, captura electrónica, PDF backend, documentos NOM generados, firma, confidencialidad o conservación requiere revisión arquitectónica posterior.
