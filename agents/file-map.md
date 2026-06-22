# File Map — Reference

This file is loaded on demand from `AGENTS.md §3`. Read when editing paths, adding/removing files, or tracing where something lives.

---

## llms.txt index

```
llms.txt                            LLM index file (llmstxt.org standard) — links to raw GitHub
                                    markdown for all sections. Replaces the former report-source.md
                                    as the single entry point for non-interactive consumption.
```

## Authored content

```
index.md                          single-page container, includes all sections
sections/00-methodology.md        §0  Resumen + Encuadre + Políticas + Propósito
sections/01-objective.md          §1  Objetivo
sections/02-intervention.md       §2  Cautelares OVD
sections/03-victimization.md      §3  Víctimas observadas
sections/04-false-allegations.md  §4  FD / intervalo
sections/05-penal-convictions.md  §5  Condenas / universo penal
sections/06-framework-a.md        §6  Marco A
sections/07-framework-b.md        §7  Marco B
sections/08-discussion.md         §8  Discusión
sections/09-limitations.md        §9  Limitaciones
sections/10-evidence-hierarchy.md §10 Trazabilidad
sections/11-conclusions.md        §11 Conclusiones
sections/12-sources.md            §12 Fuentes primarias (with archive.is links)
sections/annex-a-factcheck.md     Anexo A — Fact-check
sections/annex-b-glossary.md      Anexo B — Glosario FD
sections/section-authors.md       (PE §2)  Sobre los autores
sections/section-nomenclature.md  (PE §7)  Nomenclatura
sections/section-counterclaims.md (PE §10) Argumentos contrarios
sections/section-revisions.md     (PE §13) Revisiones
```

---

## Templates, layouts, includes

```
_layouts/default.html             nav + main + footer + JS toggle
_includes/sourcing-policy.md      Política de fuentes (rule list)
_includes/tags/<name>.html        Evidence badges (observado, derivado,
                                  supuesto, exploratorio)
                                  + Calculation box (calculo.html)
                                  + NNyA counter (nnya.html)
                                  + Ratio badge (ratio.html)
                                  + Source link badge (fuente.html)
```

---

## Crypto + integrity files (tracked, never edit by hand after build)

```
public.pem                         PGP public key (armored ASCII)
signature                          PGP detached signature of index.html
integrity.txt                      `SHA256 (index.html) = <hex>`
archive.zip                        Full _site/ zipped (build artifact)
```

All four are referenced from both the footer and the post-title link block in `index.md`. If any of the four 404 on the deployed site, METH-013 (deploy workflow) or METH-006/007/008 (crypto) has regressed.

---

## Build + validation

```
Gemfile                           jekyll 4.3, webrick
_config.yml                       title/desc/lang/permalink: pretty
.github/workflows/deploy.yml      build → archive → integrity → sign → upload (in this order)
validate_ci.py                    local CI simulator, all 20 METH checks
validate.py                       legacy structure validator (origin: missing-methodology.md)
scripts/generate-pgp.sh           PGP key generator
scripts/archive-sources.ps1       archive.is scraper
source-metadata.yml               author-time tracker (kept from original)
```

---

## Removed / formerly present (do not recreate)

```
src/                              removed (METH-018)
docs/                             removed (METH-018, we use Actions deployment)
sources/                          removed (METH-018; not used without backup PDFs)
_data/archive-links.yml           removed; archive URLs live inline in 12-sources.md
```
