# ADR-0008: Visor del flujo de consulta

## Estado
Aceptado

## Contexto
MetaboCore ya cuenta con documentación de flujo de consulta, formatos clínicos, schemas y un visor Django read-only de formatos. Se necesita conectar los formatos con el momento del flujo en que se usan.

La prioridad sigue siendo flujo antes que expediente: primero se entiende la consulta, después se ubican los formatos operativos y finalmente la capa documental NOM organiza la salida documental cuando corresponda.

## Decisión
MetaboCore tendrá un visor read-only del flujo de consulta.

El visor mostrará el flujo como mapa operativo y no como expediente clínico electrónico ni checklist obligatoria.

Los bloques del flujo podrán enlazar a formatos clínicos y a sus vistas disponibles.

Los flujos podrán representarse en `schemas/flows/*.flow.json` como mapa operativo estructurado, derivado de la documentación Markdown.

La documentación Markdown en `docs/01_flujo_consulta/` seguirá siendo la fuente humana principal del flujo clínico. Los JSON de flujo serán una capa navegable mínima para el visor.

## Límites
- No guarda datos.
- No procesa POST.
- No crea modelos clínicos.
- No implementa pacientes, expedientes ni consultas.
- No implementa login, usuarios ni permisos.
- No genera PDF desde backend.
- No declara cumplimiento completo NOM-004.
- No usa la NOM-004 como orden conversacional.
- No reemplaza la documentación clínica humana en Markdown.
- No modifica la fuente oficial NOM.

## Consecuencias
- Se podrá navegar la consulta como mapa operativo.
- Se podrá ubicar cada formato en su momento del flujo.
- Se reduce el riesgo de crear formatos aislados del proceso real de consulta.
- Habrá que mantener sincronía entre Markdown humano y `schemas/flows/` estructurado.
- Los formatos sin schema podrán mostrarse como documentos existentes sin generar enlaces rotos a vistas técnicas no disponibles.
- Los formatos futuros podrán aparecer como intención de diseño sin implicar captura, persistencia ni expediente electrónico.
