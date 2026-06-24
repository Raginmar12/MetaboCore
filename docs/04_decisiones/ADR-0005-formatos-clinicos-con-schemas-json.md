# ADR-0005: Formatos clínicos con schemas JSON

## Estado
Aceptado

## Contexto
MetaboCore busca crear formatos clínicos útiles durante la consulta, sin convertir la NOM-004 en el flujo principal ni construir todavía un expediente electrónico completo.

El primer formato estructurado será `ficha_inicial`, que contiene datos personales y clínicos mínimos para iniciar la consulta y alimentar documentos clínicos posteriores.

## Decisión
Cada formato clínico podrá tener varias capas:

1. Formato humano en Markdown dentro de `docs/02_formatos/`.
2. Schema de datos en JSON Schema dentro de `schemas/forms/`.
3. Schema de presentación o UI dentro de `schemas/ui/`.
4. Ejemplo ficticio dentro de `schemas/examples/`.

Los campos propios de MetaboCore se escribirán en español, usando `snake_case`, sin acentos, sin ñ y sin espacios.

Las keywords estándar de JSON Schema permanecerán en inglés por compatibilidad técnica.

Los ejemplos deberán ser ficticios y marcarse explícitamente como tales.

Los schemas no declaran cumplimiento completo de la NOM-004. Solo estructuran datos que podrán alimentar la capa documental futura.

## Consecuencias
- Los formatos podrán leerse por humanos y también validarse/renderizarse por sistemas futuros.
- Se reduce el riesgo de construir un expediente genérico desconectado del flujo clínico.
- Se introduce una responsabilidad de mantener sincronía entre Markdown, schema de datos, UI schema y ejemplos.
- Los datos personales deberán tratarse como sensibles desde el diseño.
- Cualquier generación documental NOM futura requerirá revisión específica.
