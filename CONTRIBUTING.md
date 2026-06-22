# Contribuciones al informe State vs Family Evidence

Aceptamos contribuciones que aporten nueva evidencia factual. Toda contribución debe cumplir con nuestra Política de Fuentes (en `sections/00-methodology.md`).

## Cómo contribuir

### Reportando nueva evidencia

Abrir un issue usando la plantilla **"Nueva evidencia"** ([crear issue](https://github.com/open-evidence-ar/state-vs-family-evidence/issues/new?template=evidence-submission.md)). Incluir:
- URL o DOI de la fuente
- Tipo de evidencia (Observado / Derivado / Supuesto / Refutación)
- Sección del informe afectada
- Cadena de cálculo (si es derivado)

### Refutando una afirmación

Abrir un issue usando la plantilla **"Refutación"** ([crear issue](https://github.com/open-evidence-ar/state-vs-family-evidence/issues/new?template=rebuttal.md)). Incluir:
- Cita exacta o número de sección de la afirmación refutada
- Fuente de la evidencia refutatoria
- Impacto en las conclusiones

### Corrigiendo errores

Abrir un issue usando la plantilla **"Error técnico o de método"** ([crear issue](https://github.com/open-evidence-ar/state-vs-family-evidence/issues/new?template=bug-report.md)) o enviar un [pull request](https://github.com/open-evidence-ar/state-vs-family-evidence/pulls) directo.

### Enviando cambios (Pull Requests)

1. [Fork del repositorio](https://github.com/open-evidence-ar/state-vs-family-evidence/fork)
2. Crear una rama descriptiva (`git checkout -b fix/fd-counter-source`)
3. Hacer cambios siguiendo el formato del informe
4. Validar localmente: `python validate_ci.py`
5. Commit con mensajes descriptivos
6. Push y abrir [Pull Request](https://github.com/open-evidence-ar/state-vs-family-evidence/pulls)

## Política de evidencia

Toda fuente debe ser:
- **Oficial**: Preferentemente organismos estatales (CSJN, MPF, UNICEF, OVG, SCBA)
- **Accesible**: URL pública o DOI verificable
- **Fechada**: Año de publicación visible
- **Archivada**: Si es sujeto a cambio, vía [archive.is](https://archive.is) o [web.archive.org](https://web.archive.org)

Para datos derivados, mostrar siempre la cadena de cálculo completa para reproducibilidad.

Los supuestos se etiquetan explícitamente y se justifica su rango.

## Anonimato

El informe es publicado por autores anónimos. Las contribuciones individuales pueden mantenerse anónimas salvo solicitud explícita de atribución.

## Contacto

Todos los aportes, correcciones y refutaciones se reciben via [GitHub Issues](https://github.com/open-evidence-ar/state-vs-family-evidence/issues) o [Pull Requests](https://github.com/open-evidence-ar/state-vs-family-evidence/pulls).

Informe publicado: [open-evidence-ar.github.io/state-vs-family-evidence](https://open-evidence-ar.github.io/state-vs-family-evidence)

## Licencia

Al enviar aportes, aceptás que los mismos se publiquen bajo la licencia del informe (ver LICENSE).