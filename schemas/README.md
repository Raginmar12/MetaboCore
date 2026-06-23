# Schemas MetaboCore

## Propósito

La carpeta `schemas/` contiene definiciones estructuradas para formatos clínicos de MetaboCore. Su objetivo es facilitar validación futura de datos, renderizado HTML y generación documental posterior.

Los schemas no implementan backend, frontend, base de datos ni expediente electrónico completo.

## Organización

- Los formatos humanos viven en `docs/02_formatos/`.
- Los schemas de datos viven en `schemas/forms/`.
- Los schemas de presentación viven en `schemas/ui/`.
- Los ejemplos viven en `schemas/examples/`.

## Alcance normativo

Los schemas pueden estructurar datos que alimenten la capa documental NOM-004, pero no declaran cumplimiento completo de la NOM-004.

La generación de documentos NOM requerirá revisión específica posterior.

## Privacidad y ejemplos

Los ejemplos deben ser ficticios y estar claramente marcados como ficticios.

Nunca se deben guardar datos reales de pacientes en `schemas/examples/` ni en ningún otro archivo del repositorio.


## Requerimientos y presentación

Los campos `required` de los schemas representan requeridos técnicos para validar una estructura digital mínima. Los requeridos visuales del UI schema orientan la captura en pantalla. Los campos clínicamente recomendados en Markdown pueden incluir información útil que se mantenga opcional o diferible para evitar fricción en consulta.

## Convención de nombres

Los campos propios de MetaboCore deben escribirse:

- En español.
- En `snake_case`.
- Sin acentos.
- Sin `ñ`.
- Sin espacios.

Las keywords estándar de JSON Schema permanecen en inglés por compatibilidad técnica, por ejemplo: `$schema`, `$id`, `title`, `description`, `type`, `properties`, `required`, `enum`, `format` y `additionalProperties`.

Los metadatos propios de MetaboCore pueden vivir en `x-metabocore`.
