# MetaboCore

MetaboCore es el núcleo clínico-operativo, documental y posteriormente digital de MetaboCare. Su propósito inicial es documentar, con una filosofía docs-as-code, el flujo real de consulta, los formatos operativos, la capa documental NOM y las decisiones arquitectónicas que guiarán el crecimiento del proyecto.

## Qué es MetaboCore

- Un repositorio de documentación viva para diseñar la operación clínica de MetaboCare.
- Un marco de trabajo para ordenar la primera consulta, seguimientos, formatos clínicos operativos y generación documental.
- La base desde la cual, más adelante, podrán derivarse modelos digitales, software clínico e integraciones externas.
- Un proyecto independiente, profesional y portable.

## Qué no es MetaboCore

- No es todavía un sistema de expediente clínico electrónico.
- No contiene backend, frontend, base de datos ni modelos de datos.
- No es una plantilla genérica de expediente clínico.
- No es un repositorio para almacenar datos reales de pacientes.
- No mezcla lógica clínica con sistemas administrativos, contables o de facturación.

## Relación entre MetaboCore y MetaboCare

MetaboCare es el servicio o consulta médica enfocada en peso, metabolismo y salud cardiometabólica. MetaboCore es el núcleo que documenta cómo funciona esa consulta: cómo se recibe al paciente, cómo se explora su motivación, cómo se integra el caso, cómo se construye un plan y cómo se transforma esa información en documentación clínica requerida.

## Filosofía docs-as-code

La documentación se mantiene como código: versionada, revisable, auditable y organizada en archivos Markdown. Cada cambio debe mejorar la claridad operativa del proyecto y dejar trazabilidad de las decisiones clínicas, documentales y arquitectónicas.

## Prioridad del proyecto

1. Flujo de consulta.
2. Formatos operativos.
3. Capa documental NOM.
4. Sistema digital.
5. Integraciones futuras mediante API.

## Integraciones futuras

Las integraciones con sistemas externos, como sistemas contables, facturación, reportes, dashboards u otros servicios administrativos, deberán documentarse como APIs o interfaces explícitas. Estas integraciones no deben contaminar el flujo clínico ni convertir la lógica administrativa en el centro del sistema.

## Advertencia de seguridad y privacidad

**Nunca se deben guardar datos reales de pacientes en este repositorio.** Solo se permiten ejemplos ficticios, claramente marcados como ficticios, para fines de documentación, pruebas o diseño operativo.
