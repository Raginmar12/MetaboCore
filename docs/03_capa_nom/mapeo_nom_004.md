# Mapeo inicial NOM-004

## Objetivo

Explicar que la NOM-004 se implementará como capa documental y no como flujo principal de la consulta MetaboCare.

## Principios

- La consulta MetaboCare genera datos clínicos durante un flujo humano, conversacional y operativo.
- La capa NOM organiza esos datos en documentos requeridos.
- La NOM no debe imponer el orden conversacional de la consulta.
- El expediente clínico conforme a norma se construye a partir de los datos capturados, sin convertir la consulta en una plantilla rígida.

## Tabla inicial de mapeo

| Dato capturado en flujo MetaboCare | Formato operativo fuente | Documento NOM que alimenta | Observaciones |
| --- | --- | --- | --- |
| Motivo de consulta | `docs/01_flujo_consulta/primera_consulta.md` / `docs/02_formatos/entrevista_motivacional.md` | Historia clínica / nota médica | Debe conservar el lenguaje principal del paciente cuando sea útil. |
| Antecedentes | Historia metabólica futura | Historia clínica | Se desarrollará un formato específico para antecedentes metabólicos. |
| Mediciones | `docs/02_formatos/analisis_corporal.md` | Exploración física | Incluye signos vitales, antropometría y análisis corporal cuando aplique. |
| Integración clínica | `docs/01_flujo_consulta/primera_consulta.md` | Diagnósticos/problemas clínicos | Debe reflejar problemas priorizados, no solo etiquetas diagnósticas aisladas. |
| Plan inicial | `docs/02_formatos/objetivos_y_plan.md` | Plan terapéutico / receta / indicaciones | Debe distinguir indicaciones clínicas, estudios y medicamentos si aplica. |
| Seguimiento | `docs/01_flujo_consulta/seguimiento.md` | Nota de evolución | Registra evolución, adherencia, barreras, efectos adversos y ajustes. |

## Pendientes

- Detallar campos mínimos por documento NOM.
- Definir plantillas documentales derivadas del flujo MetaboCare.
- Revisar requisitos normativos aplicables antes de implementar software.
