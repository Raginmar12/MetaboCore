# NOM-004-SSA3-2012 en MetaboCore

## Propósito

Esta carpeta prepara la referencia normativa activa de la **NOM-004-SSA3-2012, Del expediente clínico**, dentro de MetaboCore.

En el contexto de MetaboCore, la NOM-004 es una referencia obligatoria para el diseño futuro de la capa documental del expediente clínico. Su incorporación temprana busca orientar decisiones, prevenir deuda normativa y mantener trazabilidad entre el flujo clínico-operativo de MetaboCare y los documentos clínicos que deberán generarse posteriormente.

## Alcance actual

MetaboCore aún no declara cumplimiento completo de la NOM-004. En esta fase, la carpeta funciona como referencia normativa inicial para diseño, revisión y futuras implementaciones.

La NOM-004 se implementará como una capa documental encima del flujo humano de MetaboCare. No debe reemplazar el orden conversacional de la consulta ni convertir el flujo clínico en una plantilla normativa rígida.

## Cambios que deben revisar esta carpeta

Cualquier cambio arquitectónico relacionado con pacientes, consultas, documentos clínicos, almacenamiento, exportación, firma, consentimiento, confidencialidad o conservación debe revisar esta carpeta antes de implementarse.

También deben revisarse estos documentos antes de proponer modelos de datos, generación de documentos, expediente electrónico, mecanismos de firma, exportación, impresión o políticas de resguardo.

## Fuente oficial pendiente de incorporación manual

La fuente oficial en Markdown se agregará manualmente después en:

- `docs/03_capa_nom/nom_004/fuente_oficial/NOM-004-SSA3-2012_DOF.md`
- `docs/03_capa_nom/nom_004/fuente_oficial/README.md`

Los agentes de IA no deben copiar automáticamente el texto completo de la norma en esta carpeta.

## Estado actual

Referencia normativa inicial.

## Uso esperado

- Consulta para diseño documental y clínico-operativo.
- Revisión de impacto normativo antes de cambios arquitectónicos.
- Base para mapear requisitos contra flujos y formatos MetaboCare.
- Preparación para futuras implementaciones digitales sin afirmar cumplimiento completo.
