# Historia metabólica dirigida

> Estado: Borrador operativo.
>
> Uso: Formato técnico interno para personal clínico.
>
> Relacionado con: Primera consulta, bloque 5, historial clínico y antecedentes, integración clínica.
>
> ID técnico futuro: `historia_metabolica_dirigida`.
>
> No sustituye: juicio clínico, historia clínica completa, antecedentes clínicos, análisis corporal, plan terapéutico, nota NOM-004 ni valoración individual.
>
> No es formato para paciente.

Este formato orienta al personal clínico durante la exploración dirigida del eje cardiometabólico dentro del flujo MetaboCare. Su función es ordenar hallazgos, síntomas, estudios previos, problemas activos y patrón de progresión sin convertir la consulta en interrogatorio rígido, expediente clínico completo, diagnóstico automático ni nota normativa.

En este repositorio no deben guardarse datos reales de pacientes. Cualquier ejemplo futuro deberá ser ficticio y estar claramente identificado como tal.

---

## 1. Propósito

Este formato ayuda a explorar el eje cardiometabólico y sus manifestaciones principales:

- Glucosa, insulina y diabetes.
- Presión arterial y riesgo vascular.
- Lípidos y riesgo aterogénico.
- Hígado graso metabólico.
- Ácido úrico, hiperuricemia y gota.
- Sueño con impacto metabólico o sospecha de apnea.
- Estudios previos disponibles.
- Patrón de progresión cardiometabólica.
- Problemas metabólicos activos.
- Banderas rojas.

El objetivo es construir un mapa clínico inicial que alimente la integración clínica posterior. No busca formular todavía un plan terapéutico, indicar estudios, definir tratamiento ni cerrar diagnósticos sin valoración individual.

---

## 2. Alcance y límites

Este formato:

- No es historia clínica completa.
- No sustituye ficha inicial.
- No sustituye entrevista motivacional.
- No sustituye historia de peso y tratamientos previos.
- No sustituye antecedentes clínicos relevantes y seguridad.
- No sustituye hábitos actuales.
- No sustituye análisis corporal.
- No sustituye plan inicial.
- No es nota NOM-004 completa.
- No es formato para paciente.
- No es diagnóstico automático.
- No debe usarse para guardar datos reales de pacientes en la repo.

Temas como medicamentos actuales, antecedentes familiares, alergias, cirugías, salud reproductiva amplia y seguridad terapéutica completa pertenecen principalmente al futuro formato de `antecedentes_clinicos`. En esta historia metabólica dirigida solo deben mencionarse de forma breve cuando sean necesarios para interpretar un eje metabólico o priorizar datos para la integración clínica.

---

## 3. Momento de uso en el flujo

Se utiliza en la primera consulta, dentro del bloque 5: **Historia metabólica dirigida**.

Se ubica después de:

- Motivo de consulta y expectativas.
- Rapport.
- Entrevista motivacional breve.

Se ubica antes de:

- Historia de peso y tratamientos previos.
- Antecedentes clínicos relevantes y seguridad.
- Hábitos actuales.
- Mediciones y análisis corporal.
- Integración clínica.
- Plan inicial.

Su uso principal es la primera consulta. En seguimiento puede usarse solo como referencia breve si aparecen nuevos síntomas, estudios, diagnósticos o cambios cardiometabólicos relevantes.

---

## 4. Estructura del formato

Las siguientes secciones describen campos sugeridos, ayudas internas y preguntas guía para una versión técnica interna. No todas las secciones deben completarse en cada consulta; el personal clínico debe priorizar motivo de consulta, seguridad clínica, relevancia cardiometabólica y tiempo disponible.

### A. Datos del encuentro

Campos sugeridos:

- `fecha`
- `tipo_de_consulta`
- `nombre_o_referencia`
- `profesional`

Uso interno: ubicar el momento clínico de la exploración sin convertir este formato en expediente clínico completo ni en ficha de identificación.

### B. Motivo metabólico y contexto de detección

Campos sugeridos:

- `motivo_metabolico_principal`
- `preocupacion_metabolica_principal`
- `diagnosticos_o_hallazgos_referidos`
- `como_se_detecto_el_problema`
- `tiempo_de_evolucion_referido`
- `cambio_reciente_relevante`

Preguntas guía:

- “¿Qué le han dicho sobre su glucosa, presión, colesterol, triglicéridos, hígado graso o ácido úrico?”
- “¿Cuándo se detectó por primera vez?”
- “¿Fue por síntomas, revisión, laboratorio o consulta previa?”

### C. Eje glucosa, insulina y diabetes

Campos sugeridos:

- `glucosa_alta_referida`
- `prediabetes_referida`
- `diabetes_tipo_2_referida`
- `fecha_aproximada_deteccion_glucosa`
- `ultimo_valor_glucosa_referido`
- `ultima_hba1c_referida`
- `sintomas_hiperglucemia`
- `sintomas_hipoglucemia_o_bajones`
- `somnolencia_postprandial`
- `antojos_o_hambre_intensa`
- `infecciones_recurrentes`
- `cicatrizacion_lenta`
- `observaciones_glucosa_insulina`

Preguntas guía:

- “¿Ha notado mucha sed, mucha orina o visión borrosa?”
- “¿Le da mucho sueño después de comer?”
- “¿Se siente mal si pasa muchas horas sin comer?”
- “¿Ha tenido infecciones frecuentes o heridas que tardan en cerrar?”

### D. Eje presión arterial y riesgo vascular

Campos sugeridos:

- `presion_alta_referida`
- `fecha_aproximada_deteccion_presion`
- `mediciones_previas_presion`
- `cefalea_frecuente`
- `mareo`
- `palpitaciones`
- `dolor_toracico`
- `falta_de_aire`
- `edema`
- `evento_cardiovascular_referido`
- `observaciones_presion_vascular`

Ayuda interna:

- “Si hay síntomas actuales de alarma, priorizar seguridad clínica o referencia antes de continuar el formato.”

### E. Eje lípidos y riesgo aterogénico

Campos sugeridos:

- `colesterol_alto_referido`
- `trigliceridos_altos_referidos`
- `hdl_bajo_referido`
- `ldl_alto_referido`
- `fecha_aproximada_deteccion_lipidos`
- `ultimos_lipidos_referidos`
- `tratamiento_previo_lipidos_referido`
- `antecedente_pancreatitis_referido`
- `observaciones_lipidos`

Ayuda interna:

- “Registrar datos referidos o estudios disponibles; la interpretación completa se realiza en integración clínica.”

### F. Eje hígado graso metabólico

Campos sugeridos:

- `higado_graso_referido`
- `fecha_aproximada_deteccion_higado_graso`
- `ultrasonido_hepatico_previo`
- `transaminasas_altas_referidas`
- `dolor_o_pesadez_hipocondrio_derecho`
- `consumo_alcohol_referido`
- `otros_factores_hepaticos_referidos`
- `observaciones_higado_graso`

Ayuda interna:

- “No asumir origen metabólico sin explorar alcohol, medicamentos u otras causas en los formatos correspondientes.”

### G. Eje ácido úrico, hiperuricemia y gota

Campos sugeridos:

- `acido_urico_alto_referido`
- `fecha_aproximada_deteccion_acido_urico`
- `crisis_gota_referida`
- `articulaciones_afectadas`
- `dolor_articular_recurrente`
- `litiasis_renal_referida`
- `desencadenantes_referidos`
- `observaciones_acido_urico_gota`

Preguntas guía:

- “¿Le han dicho que tiene ácido úrico alto?”
- “¿Ha tenido crisis de dolor intenso en dedo gordo, tobillo, rodilla u otra articulación?”
- “¿Ha tenido piedras en el riñón?”

### H. Sueño con impacto metabólico o sospecha de apnea

Campos sugeridos:

- `ronquido_fuerte`
- `pausas_respiratorias_observadas`
- `somnolencia_diurna`
- `sueno_no_reparador`
- `cefalea_matutina`
- `despertares_nocturnos`
- `riesgo_apnea_sueno`
- `observaciones_apnea_sueno`

Ayuda interna:

- “La higiene de sueño y rutina se exploran en Hábitos actuales. Aquí solo se buscan datos sugestivos de apnea o sueño no reparador con impacto cardiometabólico.”

### I. Estudios previos disponibles y pendientes

Campos sugeridos:

- `estudios_previos_disponibles`
- `fecha_estudios_previos`
- `glucosa_disponible`
- `hba1c_disponible`
- `perfil_lipidos_disponible`
- `pruebas_hepaticas_disponibles`
- `acido_urico_disponible`
- `creatinina_o_funcion_renal_disponible`
- `ego_o_albuminuria_disponible`
- `ultrasonido_hepatico_disponible`
- `otros_estudios_relevantes`
- `estudios_pendientes_o_necesarios`

Ayuda interna:

- “Registrar disponibilidad y faltantes. No convertir esta sección en solicitud formal de estudios.”

### J. Patrón de progresión cardiometabólica

Campos sugeridos:

- `primer_hallazgo_metabolico_referido`
- `secuencia_de_aparicion_problemas`
- `progresion_referida`
- `empeoramiento_reciente`
- `factores_asociados_a_empeoramiento`
- `periodos_de_mejoria`
- `observaciones_patron_progresion`

Preguntas guía:

- “¿Qué apareció primero: peso, glucosa, presión, triglicéridos, hígado graso o ácido úrico?”
- “¿Ha sentido que esto empeoró en alguna etapa específica?”
- “¿Hubo algún periodo en que mejoró?”

### K. Problemas metabólicos activos identificados

Campos sugeridos:

- `problemas_metabolicos_conocidos`
- `problemas_metabolicos_sospechados`
- `riesgos_a_priorizar`
- `datos_que_faltan`
- `requiere_ampliar_antecedentes_seguridad`
- `requiere_mediciones`
- `requiere_laboratorios`
- `observaciones_para_integracion`

Opciones sugeridas para problemas sospechados:

- `resistencia_insulina_probable`
- `prediabetes_o_diabetes_probable`
- `hipertension_probable`
- `dislipidemia_probable`
- `higado_graso_probable`
- `hiperuricemia_gota_probable`
- `apnea_sueno_probable`
- `riesgo_cardiovascular_elevado`
- `requiere_mas_datos`

### L. Banderas rojas y prioridad clínica

Campos sugeridos:

- `banderas_rojas_presentes`
- `tipo_bandera_roja`
- `detalle_bandera_roja`
- `accion_recomendada`
- `requiere_referencia`
- `requiere_atencion_urgente`
- `observaciones_seguridad`

Banderas rojas sugeridas:

- `dolor_toracico_actual`
- `disnea_en_reposo`
- `sincope`
- `deficit_neurologico_focal`
- `presion_muy_elevada_con_sintomas`
- `hiperglucemia_sintomatica_importante`
- `hipoglucemia_severa`
- `datos_sugestivos_cetoacidosis`
- `dolor_abdominal_severo_o_pancreatitis_sospechada`
- `ictericia`
- `perdida_peso_inexplicada`
- `ideacion_suicida_o_riesgo_psiquiatrico`
- `trastorno_conducta_alimentaria_sospechado`
- `otro`

Ayuda interna:

- “Si hay datos de urgencia, priorizar seguridad sobre completar el formato.”

---

## 5. Núcleo mínimo del formato

Si se usa una versión abreviada, los campos indispensables son:

- `motivo_metabolico_principal`
- `diagnosticos_o_hallazgos_referidos`
- `tiempo_de_evolucion_referido`
- `glucosa_insulina_datos_relevantes`
- `presion_vascular_datos_relevantes`
- `lipidos_datos_relevantes`
- `higado_graso_datos_relevantes`
- `acido_urico_gota_datos_relevantes`
- `suenio_apnea_datos_relevantes`
- `estudios_previos_disponibles`
- `patron_progresion_cardiometabolica`
- `problemas_metabolicos_sospechados`
- `banderas_rojas_presentes`
- `datos_faltantes_prioritarios`

Este núcleo mínimo permite conservar la lógica clínica del bloque 5 aun cuando el tiempo de consulta sea limitado: motivo metabólico, ejes principales, estudios disponibles, progresión, problemas sospechados, seguridad y datos faltantes.

---

## 6. Qué no debe documentar este formato

Este formato no debe registrar como campos principales:

- Antecedentes familiares cardiometabólicos amplios.
- Antecedentes personales patológicos amplios.
- Alergias.
- Cirugías.
- Medicamentos actuales completos.
- Salud reproductiva amplia.
- Hábitos alimentarios detallados.
- Actividad física detallada.
- Trayectoria de peso.
- Tratamientos previos para peso.
- Plan terapéutico.
- Metas.
- Indicaciones.
- Seguimiento.

Distribución recomendada dentro del flujo MetaboCare:

- **Ficha inicial:** identificación, contacto, contexto administrativo, motivo breve y forma preferida de trato.
- **Entrevista motivacional:** permiso, motivo personal, expectativas, ambivalencia, escalas de cambio, barreras, recursos y primer paso posible.
- **Historia de peso y tratamientos previos:** trayectoria de peso, peso máximo o habitual, dietas, medicamentos, suplementos, procedimientos previos, respuesta y experiencias negativas.
- **Antecedentes clínicos relevantes y seguridad:** antecedentes personales y familiares amplios, alergias, cirugías, medicamentos actuales completos, salud reproductiva amplia y seguridad terapéutica.
- **Hábitos actuales:** patrón alimentario, actividad física, rutina de sueño, estrés, consumo de alcohol o tabaco y barreras prácticas.
- **Análisis corporal:** peso, talla, IMC, cintura, presión arterial, frecuencia cardiaca, composición corporal y observaciones de técnica.
- **Objetivos y plan:** objetivos, indicaciones, estudios solicitados, medicamentos si aplica, señales de alarma, próxima cita y primer paso concreto.

---

## 7. Uso interno vs paciente

Este es un formato técnico interno para personal clínico.

No debe entregarse al paciente para autollenado ni usarse como cuestionario autónomo. Contiene síntomas, banderas rojas, hipótesis de problemas metabólicos y notas de priorización que requieren interpretación clínica.

En una fase posterior puede tener impresión técnica para revisión interna. Si en el futuro existe un cuestionario para paciente relacionado con metabolismo, debe ser un formato separado, simplificado, redactado en lenguaje claro y sin ayudas internas ni jerga técnica.

---

## 8. Relación futura con schema

Este documento podrá alimentar en fases futuras:

- `schemas/forms/historia_metabolica_dirigida.schema.json`
- `schemas/ui/historia_metabolica_dirigida.ui.json`
- `schemas/examples/historia_metabolica_dirigida.example.json`

Esos archivos no existen todavía y no deben crearse en esta fase. Cuando se definan, deberán mantener campos en español, `snake_case`, sin acentos ni `ñ`, ejemplos ficticios y alcance read-only sin persistencia clínica.

---

## 9. Relación con el flujo

Este formato corresponde al bloque 5 de la primera consulta: **Historia metabólica dirigida**.

Su función es alimentar la integración clínica posterior con un mapa inicial de problemas cardiometabólicos, síntomas relevantes, estudios disponibles, patrón de progresión y banderas rojas. No reemplaza los bloques posteriores de historia de peso, antecedentes clínicos y seguridad, hábitos actuales, mediciones, integración clínica ni plan inicial.
