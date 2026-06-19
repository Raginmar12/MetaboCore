# ADR-0002: Flujo antes que expediente

## Estado

Aceptado.

## Contexto

Un expediente clínico genérico causó fricción porque no correspondía al flujo real de consulta. Iniciar por una plantilla normativa o por modelos de datos puede producir un sistema técnicamente ordenado, pero clínicamente incómodo.

## Decisión

Primero se documenta el flujo de consulta MetaboCare; luego los formatos operativos; luego la capa NOM; y finalmente la implementación digital.

## Consecuencias

- Los modelos de datos futuros deberán derivarse del flujo y no al revés.
- El diseño digital deberá respetar la conversación clínica real.
- Las plantillas documentales se crearán como salida del proceso, no como punto de partida.
