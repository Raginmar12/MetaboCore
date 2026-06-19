# Revisión arquitectónica NOM-004

## Propósito

Esta guía ayuda a evaluar si un cambio arquitectónico, documental o de sistema puede tener impacto sobre la capa normativa NOM-004.

No reemplaza la revisión jurídica ni declara cumplimiento completo.

## Regla de revisión

Todo cambio arquitectónico que afecte pacientes, consultas, documentos clínicos, almacenamiento, confidencialidad, exportación, impresión, firma o conservación debe revisar esta guía antes de implementarse.

## Preguntas de revisión

- ¿Este cambio introduce captura de datos personales o clínicos?
- ¿Este cambio modifica cómo se documenta una consulta?
- ¿Este cambio afecta la generación de historia clínica, nota de evolución, receta, solicitud de estudios o consentimiento?
- ¿Este cambio afecta almacenamiento, conservación, confidencialidad o acceso a datos?
- ¿Este cambio requiere trazabilidad, autoría, fecha, hora o firma?
- ¿Este cambio debe reflejarse en `mapeo_nom_004.md`?
- ¿Este cambio requiere actualizar algún formato operativo?
- ¿Este cambio requiere crear o modificar un documento generado?
- ¿Este cambio requiere actualizar la matriz de requisitos NOM-004?
- ¿Este cambio depende de un numeral específico de la fuente oficial?

## Resultado esperado de la revisión

Al finalizar la revisión, documentar una de estas decisiones:

- Sin impacto NOM-004.
- Impacto NOM-004 identificado, documentación actualizada.
- Impacto NOM-004 identificado, requiere análisis posterior.
- Cambio pospuesto por incertidumbre normativa.

## Archivos relacionados

- `docs/03_capa_nom/mapeo_nom_004.md`
- `docs/03_capa_nom/nom_004/referencia_normativa.md`
- `docs/03_capa_nom/nom_004/checklist_inicial.md`
- `docs/03_capa_nom/nom_004/matriz_requisitos.md`
- `docs/03_capa_nom/nom_004/fuente_oficial/`
