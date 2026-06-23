# Ficha inicial

## Propósito

Registrar los datos mínimos de identificación del paciente y el contexto breve necesario para iniciar la primera consulta MetaboCare de forma clara, segura y operativa.

La ficha inicial es el primer formato clínico estructurado de MetaboCore. Su función es facilitar la identificación del paciente, orientar el inicio de la consulta y preparar datos que podrán alimentar documentos clínicos posteriores.

## Momento de uso

La ficha inicial puede llenarse antes de la consulta, durante recepción o al inicio de la primera consulta.

Debe mantenerse breve para no convertir la bienvenida en una checklist administrativa extensa. La información clínica amplia debe explorarse en los bloques correspondientes del flujo de primera consulta.

## Relación con el flujo MetaboCare

Este formato se relaciona principalmente con el Bloque 1 de la primera consulta: bienvenida y encuadre.

También puede servir como puente hacia el Bloque 2, motivo de consulta y expectativas, mediante el registro de un motivo breve de consulta. Ese motivo debe registrarse idealmente con palabras del paciente.

La ficha inicial no sustituye la historia clínica, no sustituye la entrevista motivacional y no debe reemplazar el rapport clínico.

## Relación con NOM-004

La ficha inicial alimenta de forma inicial y parcial datos generales del expediente y ficha de identificación para la capa documental NOM-004.

Este formato no declara cumplimiento completo de la NOM-004. La NOM-004 permanece como capa documental y de cumplimiento, no como orden conversacional principal de la consulta.

## Advertencia de privacidad

Este formato contiene datos personales identificables y potencialmente datos clínicos sensibles.

No deben guardarse datos reales de pacientes en este repositorio. Los ejemplos, pruebas o fixtures deben ser ficticios y estar claramente marcados como ficticios.

## Secciones del formato

### Datos de identificación

- **Nombre completo:**
- **Fecha de nacimiento:**
- **Edad:**
- **Sexo registrado:**

### Forma de trato

- **Nombre o forma preferida de trato:**

### Contacto y ubicación

- **Teléfono principal:**
- **Teléfono alterno, si aplica:**
- **Correo electrónico, si aplica:**
- **Municipio o localidad:**
- **Domicilio completo, si el flujo operativo o documental lo requiere:**
- **Preferencia de comunicación, si aplica:**

### Contexto administrativo

- **Fecha de primera consulta:**
- **Médico responsable, si aplica:**
- **Identificador interno de expediente, si existe en sistema futuro:**
- **Establecimiento, si aplica:**

### Contexto clínico inicial

- **Motivo breve de consulta:**
- **Preocupación inicial relevante:**
- **Ocupación o actividad principal, si aporta contexto clínico-operativo:**
- **Consentimiento verbal para el flujo de consulta, si aplica:**

### Campos opcionales o diferibles

- **Género, si es clínicamente relevante o si el paciente desea expresarlo:**
- **Contacto de emergencia:**
- **Referencia a aviso de privacidad:**
- **Preferencia de comunicación:**
- **Domicilio completo:**

### Observaciones

- **Observaciones breves de recepción o encuadre inicial:**

## Campos mínimos recomendados

En el schema de datos, los campos técnicamente requeridos representan el mínimo necesario para validar una ficha inicial digital. Algunos campos clínicamente recomendados pueden seguir siendo opcionales o diferibles para evitar fricción en consulta.

- Nombre completo.
- Fecha de nacimiento.
- Edad.
- Sexo registrado.
- Nombre o forma preferida de trato.
- Teléfono principal, requerido técnicamente dentro de `contacto`.
- Municipio o localidad, requerido técnicamente dentro de `contacto`.
- Fecha de primera consulta.
- Motivo breve de consulta.

El domicilio completo sigue siendo opcional o diferible. La preferencia de comunicación es opcional.

## Campos opcionales

- Género.
- Teléfono alterno.
- Correo electrónico.
- Ocupación o actividad principal.
- Contacto de emergencia.
- Médico responsable, si aplica.
- Establecimiento, si aplica.
- Referencia a aviso de privacidad.
- Preferencia de comunicación.

## Campos sensibles

- Nombre completo.
- Fecha de nacimiento.
- Teléfono.
- Correo electrónico.
- Domicilio completo.
- Género.
- Contacto de emergencia.
- Identificador interno de expediente.

## Campos diferibles para sistema digital

- Identificador interno de expediente.
- Datos del establecimiento precargados desde configuración.
- Autoría de captura.
- Fecha y hora técnica de creación o actualización.
- Trazabilidad de cambios.
- Validación automática de edad.
- Estado documental del aviso de privacidad.
- Mecanismos para evitar duplicidad de pacientes.

## Nota de uso clínico

La ficha debe ser breve. Puede llenarse antes de la consulta o durante recepción, pero debe confirmarse de manera respetuosa al inicio.

No sustituye la historia clínica ni la entrevista motivacional. El motivo breve de consulta debe registrarse idealmente con palabras del paciente y después profundizarse en el flujo clínico correspondiente. Las observaciones son opcionales y no sustituyen historia clínica ni nota médica.

## Relación con schemas

Este formato humano se acompaña de archivos estructurados para validación futura, renderizado HTML y ejemplos ficticios:

- `schemas/forms/ficha_inicial.schema.json`
- `schemas/ui/ficha_inicial.ui.json`
- `schemas/examples/ficha_inicial.example.json`
