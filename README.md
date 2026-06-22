# State vs Family Evidence

> Estudio descriptivo con trazabilidad de evidencia sobre la asimetría entre intervenciones cautelares, victimización infantil y condenas penales en Argentina · **v1.0.0**

<img src="assets/Asimetr%C3%ADa_en_la_justicia_infantil.png" alt="State vs Family Evidence — Asimetría en la justicia infantil" style="max-width:100%; height:auto; display:block; margin:0 auto 1.5em auto;">

## Informe completo

**[Leer informe publicado](https://open-evidence-ar.github.io/state-vs-family-evidence)** · [Descargar (.zip)](https://open-evidence-ar.github.io/state-vs-family-evidence/archive.zip)

## Hallazgos clave

| Indicador | Base | Restricción | Techo |
|---|---|---|---|
| Marco A — NNyA cautela / víctima | **1,94 : 1** (caso base observado — microdatos CSJN OVD 2024, ver §2.3) | | |
| Marco B ajustado — injustificadas / condena | 0 : 1 | 0,53 : 1 | 3,67 : 1 |
| FD-VG/VI (% según denominador) | 0,09% penal | 8,9% clasificadas | 61,5% techo Santa Fe |
| NNyA potencialmente afectados por FD | 557 | 2.631 | 3.853 |

Por cada condena intrafamiliar contra NNyA (~750/año nacional) hay ~6 medidas cautelares en CABA. Entre 0,53 y 3,67 medidas por condena podrían haber sido infundadas. El daño potencial por desvinculación injustificada se estima en **557–3.853 NNyA**. La persistencia de esta asimetría es estructural, no coyuntural (§13).

## Contribuir

Aceptamos nueva evidencia factual, refutaciones y correcciones. Ver [CONTRIBUTING.md](CONTRIBUTING.md).

- [Reportar nueva evidencia](https://github.com/open-evidence-ar/state-vs-family-evidence/issues/new?template=evidence-submission.md)
- [Refutar una afirmación](https://github.com/open-evidence-ar/state-vs-family-evidence/issues/new?template=rebuttal.md)
- [Reportar error técnico](https://github.com/open-evidence-ar/state-vs-family-evidence/issues/new?template=bug-report.md)

## Verificar autoría

- [Clave pública PGP](https://open-evidence-ar.github.io/state-vs-family-evidence/public.pem)
- [Firma detached](https://open-evidence-ar.github.io/state-vs-family-evidence/signature)
- [Hash de integridad](https://open-evidence-ar.github.io/state-vs-family-evidence/integrity.txt)

## Estructura del repositorio

| Directorio / archivo | Contenido |
|---|---|
| `sections/` | Secciones del informe (§0–§13 + anexos) |
| `agents/` | Documentación operativa para contribuidores y agentes |
| `scripts/` | Utilidades (PGP, archivado, validación) |
| `index.md` | Página única que incluye todas las secciones |
| `_config.yml` | Configuración Jekyll |
| `llms.txt` | Índice LLM con enlaces raw a todas las secciones ([llmstxt.org](https://llmstxt.org)) |
| `validate_ci.py` | Validator de cumplimiento metodológico |

## Metodología

Replica la estructura de [Project-Evidence](https://github.com/Project-Evidence/project-evidence.github.io). Manual operativo completo en [AGENTS.md](AGENTS.md).
