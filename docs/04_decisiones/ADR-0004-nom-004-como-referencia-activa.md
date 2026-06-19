# ADR-0004: NOM-004 como referencia normativa activa

## Estado
Aceptado

## Contexto
MetaboCore está en una fase inicial centrada en documentar el flujo clínico-operativo de MetaboCare. Aunque el cumplimiento completo de la NOM-004 no se implementará todavía, la norma debe estar presente desde el inicio para orientar decisiones futuras y evitar deuda normativa.

La fuente oficial en Markdown fue incorporada manualmente dentro de `docs/03_capa_nom/nom_004/fuente_oficial/`.

## Decisión
Se incorporará una sección específica de referencia NOM-004 dentro de `docs/03_capa_nom/nom_004/`.

Esta sección no declara cumplimiento completo. Su función es servir como referencia, checklist inicial, matriz de requisitos y guía de revisión arquitectónica.

La carpeta `fuente_oficial/` contiene la fuente oficial convertida a Markdown y su README.

## Consecuencias
- Las decisiones futuras deberán considerar impacto normativo.
- Los agentes de IA tendrán una referencia explícita antes de proponer modelos, documentos o arquitectura clínica.
- La NOM-004 permanecerá como capa documental y de cumplimiento, sin reemplazar el flujo clínico de MetaboCare.
- El proyecto podrá avanzar por fases sin ignorar requisitos obligatorios.
- El texto completo de la norma no debe ser copiado, reemplazado ni reescrito automáticamente por agentes. La fuente oficial ya fue agregada manualmente y cualquier actualización futura debe hacerse de forma explícita y revisada.
