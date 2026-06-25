# Formato técnico interno de entrevista motivacional breve

> Estado: Borrador operativo.
>
> Uso: Formato técnico interno para personal clínico.
>
> Relacionado con: Conexión clínica, primera consulta y entrevista motivacional breve.
>
> Referencia clínica base: `docs/05_guias_clinicas/entrevista_motivacional_metabocare.md`.
>
> Manual operativo relacionado: `docs/01_flujo_consulta/entrevista_motivacional_operativa.md`.
>
> Este documento no es un formato para paciente y no debe entregarse para llenado autónomo por la persona atendida.

Este formato orienta al médico o personal clínico durante una entrevista motivacional breve dentro del flujo MetaboCare. Su función es guiar y registrar de forma breve los elementos clínicamente útiles de la conversación, sin convertir la consulta en interrogatorio, expediente clínico completo, checklist rígida ni protocolo normativo.

En este repositorio no deben guardarse datos reales de pacientes. Cualquier ejemplo futuro deberá ser ficticio y estar claramente identificado como tal.

---

## Propósito

El formato ayuda a documentar, de manera breve y operativa:

- El permiso para hablar de peso, hábitos, metabolismo u otros temas sensibles.
- El motivo personal de consulta y las expectativas expresadas por el paciente.
- La ambivalencia normal frente al cambio.
- Las escalas de importancia, confianza y disposición.
- Las barreras principales y los recursos disponibles.
- El lenguaje de cambio y el lenguaje de mantenimiento.
- La información médica dada con permiso y la respuesta del paciente.
- Un primer paso posible, pequeño y revisable.
- El acuerdo de seguimiento y los temas a retomar.

Su intención es sostener una conversación clínica colaborativa, centrada en la persona y no estigmatizante.

---

## Alcance y límites

Este documento:

- No es una guía oficial.
- No es psicoterapia.
- No es un formato para paciente.
- No es expediente clínico.
- No es JSON Schema ni define validaciones técnicas.
- No es UI schema.
- No es NOM ni declaración de cumplimiento normativo.
- No es un protocolo rígido ni una lista obligatoria de preguntas.
- No debe usarse para guardar datos reales de pacientes dentro del repositorio.

La guía clínica base orienta el criterio, el lenguaje y el enfoque operativo, pero no sustituye el juicio clínico ni las guías oficiales aplicables.

---

## Momento de uso

### Primera consulta

Se utiliza dentro de la macro-etapa de **Conexión clínica**, después de explorar motivo de consulta, expectativas y rapport. En ese punto ayuda a comprender qué cambio tiene sentido para la persona, qué tan preparada se siente y qué barreras deben considerarse antes de proponer un plan.

### Seguimiento

Puede usarse como herramienta breve para revisar:

- Barreras nuevas o persistentes.
- Confianza actual.
- Lenguaje de cambio.
- Ajuste del primer paso acordado.
- Necesidad de simplificar, pausar o reformular el plan.

---

## Estructura del formato

Las siguientes secciones describen los campos sugeridos para una versión técnica interna. No todas las secciones deben completarse en cada consulta; el personal clínico debe adaptar su uso al contexto, tiempo disponible, seguridad clínica y prioridades de la persona.

### A. Datos del encuentro

Campos sugeridos:

- `fecha`
- `tipo_de_consulta`
- `nombre_o_referencia`
- `profesional`

Uso interno: ubicar el momento clínico de la conversación sin convertir este formato en expediente clínico completo.

### B. Encuadre y permiso

Campos sugeridos:

- `permiso_para_hablar_de_peso_y_metabolismo`
- `tema_autorizado`
- `tema_preferido_por_el_paciente`
- `observaciones_de_permiso`

Ayuda interna:

- “Pedir permiso antes de hablar de peso, hábitos o metabolismo.”

### C. Motivo personal y expectativas

Campos sugeridos:

- `motivo_principal_en_palabras_del_paciente`
- `expectativas_de_la_consulta`
- `preocupacion_principal`
- `objetivo_sentido_por_el_paciente`

Preguntas guía:

- “¿Qué le hizo venir hoy?”
- “¿Qué espera de esta consulta?”
- “¿Qué le gustaría que fuera diferente?”

### D. Valores e impacto en vida diaria

Campos sugeridos:

- `impacto_actual_en_la_vida`
- `valor_o_area_importante`
- `beneficio_esperado`

Pregunta guía:

- “Si esto mejora, ¿dónde lo notaría primero?”

### E. Ambivalencia

Campos sugeridos:

- `razones_para_cambiar`
- `razones_para_no_cambiar`
- `frase_de_ambivalencia`
- `reflexion_doble_usada`

Ayudas internas:

- “No discutir. Reflejar ambos lados.”
- “Por un lado..., y por otro...”

### F. Escalas de cambio

Campos sugeridos:

- `importancia_0_10`
- `confianza_0_10`
- `disposicion_0_10`
- `por_que_no_mas_bajo`
- `que_subiria_un_punto`

Ayudas internas:

- “¿Por qué ese número y no uno más bajo?”
- “¿Qué ayudaría a subir un punto?”

### G. Barreras y recursos

Campos sugeridos:

- `barrera_principal`
- `otras_barreras`
- `recursos_personales`
- `apoyo_familiar_social`
- `estrategia_para_barrera_principal`

Ayuda interna:

- “La barrera modifica el plan; no define al paciente.”

### H. Lenguaje de cambio

Campos sugeridos:

- `frases_de_cambio`
- `frases_de_mantenimiento`
- `senal_de_preparacion`

Ayuda interna:

- “Anotar una frase textual breve del paciente.”

### I. Información médica dada con permiso

Campos sugeridos:

- `permiso_para_explicar`
- `informacion_medica_explicada`
- `respuesta_del_paciente`
- `duda_principal`

Ayuda interna:

- “Preguntar → explicar breve → preguntar qué piensa.”

### J. Primer paso posible

Campos sugeridos:

- `area_elegida`
- `primer_paso_posible`
- `frecuencia`
- `momento_del_dia`
- `barrera_anticipada`
- `plan_si_falla`
- `compromiso_0_10`

Ayuda interna:

- “Debe ser pequeño, concreto y revisable.”

### K. Acuerdo de seguimiento

Campos sugeridos:

- `acuerdo_de_seguimiento`
- `plazo_de_revision`
- `tema_a_retomar`
- `observaciones_para_siguiente_consulta`

Uso interno: dejar claro qué se revisará después, sin prometer resultados ni convertir el acuerdo en una obligación punitiva.

### L. Notas internas del clínico

Campos sugeridos:

- `impresion_motivacional`
- `riesgo_de_plan_irrealista`
- `ajuste_recomendado_del_estilo_de_plan`
- `observaciones_clinicas_internas`

Uso interno: registrar hipótesis operativas útiles para adaptar el estilo de comunicación, la educación y el plan. Estas notas deben mantener lenguaje respetuoso y no estigmatizante.

---

## Núcleo mínimo del formato

Si se usa una versión abreviada, los campos indispensables son:

- `motivo_principal_en_palabras_del_paciente`
- `razones_para_cambiar`
- `razones_para_no_cambiar`
- `importancia_0_10`
- `confianza_0_10`
- `barrera_principal`
- `frases_de_cambio`
- `primer_paso_posible`
- `plan_si_falla`
- `acuerdo_de_seguimiento`

Este núcleo mínimo permite conservar la lógica clínica de la entrevista motivacional breve aun cuando el tiempo sea limitado.

---

## Qué no debe documentar

El formato no debe registrar etiquetas culpabilizantes o estigmatizantes como:

- “paciente no cooperador”
- “mala adherencia”
- “falta de voluntad”
- “paciente difícil”
- “resistente”
- “no quiere cambiar”
- “no entiende”
- “fracaso”

Alternativas recomendadas:

- “confianza baja”
- “ambivalencia presente”
- “barrera identificada”
- “requiere plan más simple”
- “requiere educación gradual”
- “prefiere no hablar del tema”
- “priorizar seguridad clínica”

Estas alternativas describen el estado de la conversación o del plan sin definir negativamente a la persona.

---

## Relación futura con schema

Este documento será fuente documental para versiones futuras de:

- `schemas/forms/entrevista_motivacional.schema.json`
- `schemas/ui/entrevista_motivacional.ui.json`
- `schemas/examples/entrevista_motivacional.example.json`

Esos archivos no se crean en esta versión. La conversión a schema, UI schema o ejemplo JSON deberá hacerse en una tarea posterior, cuidando que el resultado siga siendo una herramienta clínica interna y no un expediente clínico electrónico.
