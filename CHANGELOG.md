# Changelog

## v0.1.15 - Historia metabólica dirigida

- Agrega documento operativo inicial de historia metabólica dirigida.

## v0.1.14 - Permiso y variante interna de entrevista motivacional

- Incluye permiso en el núcleo mínimo del formato de entrevista motivacional y evita variante paciente para formatos técnicos internos.

## v0.1.13 - Schema de entrevista motivacional

- Agrega schema, UI schema y ejemplo ficticio del formato técnico interno de entrevista motivacional.

## v0.1.12 - Formato técnico interno de entrevista motivacional

- Define la primera versión documental del formato técnico interno de entrevista motivacional.

## v0.1.11 - Guías clínicas base

- Integra `docs/05_guias_clinicas/` como biblioteca de referencia clínica para MetaboCare.
- Agrega README de guías clínicas base y delimita que no son formatos, schemas, capa normativa, expediente ni protocolo rígido.
- Referencia la guía de entrevista motivacional desde el flujo de primera consulta y el formato de entrevista motivacional.
- Crea el placeholder `docs/01_flujo_consulta/entrevista_motivacional_operativa.md` para el futuro manual operativo interno de entrevista motivacional breve.
- Actualiza instrucciones para agentes para revisar guías clínicas relevantes antes de modificar flujos, formatos o schemas relacionados.

## v0.1.10 - Macro-etapas del flujo de primera consulta

- Agrupa la primera consulta en macro-etapas clínicas.
- Reordena antecedentes clínicos relevantes antes de hábitos actuales.
- Renombra antecedentes relevantes como antecedentes clínicos relevantes y seguridad.
- Actualiza el visor de flujo para mostrar etapas y bloques.

## v0.1.9 - Visor del flujo de consulta

- Agrega `schemas/flows/` como mapa operativo estructurado de flujos de consulta.
- Agrega visor read-only de flujos en Django.
- Agrega rutas `/flujos/`, `/flujos/primera-consulta/` y vista de bloque.
- Conecta bloques del flujo con formatos clínicos y sus vistas disponibles.
- Agrega ADR-0008 sobre visor del flujo de consulta.

## v0.1.8 - Variantes imprimibles para pacientes y técnica

- Separa la impresión en vista para pacientes y vista técnica.
- Mantiene `/formatos/<formato_id>/imprimir/` como alias de la vista para pacientes.
- Simplifica la vista para pacientes para uso en sala de espera.
- Conserva una vista técnica para revisión interna del formato.
- Mantiene ambas variantes derivadas de schema + UI schema.

## v0.1.7 - Vista imprimible de formatos clínicos

- Agrega vista imprimible al visor Django de formatos.
- Permite generar formatos en papel desde schema y UI schema.
- Agrega ruta `/formatos/<formato_id>/imprimir/`.
- Conserva vistas de Preview, Ejemplo ficticio, Schema, UI schema y JSON ejemplo.
- Agrega ADR-0007 sobre MetaboCore como generador de formatos imprimibles.
- Actualiza documentación del visor y reglas para agentes.

## v0.1.6 - Visor Django de formatos clínicos

- Agrega Django como visor local/prototipo de formatos clínicos.
- Renderiza formatos desde JSON Schema, UI schema y ejemplos ficticios.
- Agrega vistas para lista, preview, ejemplo ficticio, schema, UI schema y JSON de ejemplo.
- Agrega pruebas mínimas para carga, validación y rutas del visor.
- Agrega ADR-0006 sobre Django como visor sin persistencia clínica.

## v0.1.5 - Alineación de ficha inicial

- Alinea campos mínimos operativos de `ficha_inicial` con los requeridos técnicos del schema.
- Requiere `contacto`, `telefono_principal` y `municipio_o_localidad` en el schema de ficha inicial.
- Agrega `preferencia_comunicacion` como campo opcional de contacto.
- Agrega `observaciones` como campo opcional de contexto inicial.
- Actualiza UI schema, ejemplo ficticio y documentación relacionada.

## v0.1.4 - Ficha inicial y schemas clínicos base

- Agrega `ficha_inicial` como primer formato clínico estructurado.
- Agrega arquitectura base de schemas para formularios clínicos.
- Agrega schema de datos, UI schema y ejemplo ficticio para `ficha_inicial`.
- Agrega ADR-0005 sobre formatos clínicos con schemas JSON.
- Actualiza flujo de primera consulta y mapeo NOM-004 para usar `ficha_inicial`.

## v0.1.3 - Checklist NOM-004 actualizado

- Actualiza la checklist inicial NOM-004 para reflejar que la fuente oficial ya fue integrada manualmente.
- Retira referencia obsoleta a la incorporación pendiente de la fuente oficial.

## v0.1.2 - Fuente oficial NOM-004 integrada

- Registra la incorporación manual de la fuente oficial de la NOM-004-SSA3-2012 en Markdown.
- Actualiza referencias que describían la fuente oficial como pendiente.
- Actualiza instrucciones para agentes de IA sobre el manejo de la fuente oficial normativa.
- Mantiene la aclaración de que MetaboCore no declara cumplimiento completo de la NOM-004.

## v0.1.1 - Referencia normativa NOM-004

- Prepara estructura documental para integrar la NOM-004-SSA3-2012 como referencia normativa activa.
- Agrega referencia normativa resumida.
- Agrega checklist inicial NOM-004.
- Agrega matriz inicial de requisitos NOM-004 contra flujo MetaboCare.
- Agrega guía de revisión arquitectónica NOM-004.
- Prepara carpeta `fuente_oficial/` para incorporar manualmente el texto oficial en Markdown.
- Actualiza instrucciones para agentes de IA.
- Agrega ADR-0004 sobre NOM-004 como referencia normativa activa.

## v0.1.0 - Manual operativo inicial

- Crea estructura inicial de MetaboCore.
- Agrega documentación base de identidad clínica.
- Define MetaboCore como núcleo independiente de MetaboCare.
- Agrega flujo inicial de primera consulta.
- Agrega formato de entrevista motivacional.
- Agrega formato de análisis corporal.
- Agrega formato de objetivos y plan.
- Agrega mapeo inicial de capa NOM.
- Agrega ADRs iniciales.
