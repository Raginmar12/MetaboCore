# ADR-0001: MetaboCore como núcleo independiente

## Estado

Aceptado.

## Contexto

MetaboCore necesita ser el núcleo clínico-operativo de MetaboCare y debe poder evolucionar de forma independiente. La documentación debe ser clara para colaboradores, agentes de IA y futuros desarrolladores sin depender de contexto personal externo.

## Decisión

MetaboCore se documentará y construirá como un sistema independiente, sin referencias a infraestructura personal o sistemas privados del desarrollador.

## Consecuencias

- La documentación será clara, profesional y portable.
- El repositorio podrá ser entendido por colaboradores, agentes de IA o futuros desarrolladores sin depender de contexto personal externo.
- Las integraciones futuras se manejarán mediante interfaces explícitas, por ejemplo APIs para sistemas contables, facturación, reportes o análisis.
- No se almacenarán datos reales de pacientes dentro del repositorio.
