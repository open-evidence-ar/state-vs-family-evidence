# Methodology Framework — Reference

This file is loaded on demand from `AGENTS.md §3`. Do not read unless:

- You are adding/modifying METH-NNN audit items
- You need the PE section rendering order
- You need the 20 METH compliance table

---

## PE Structure (sections rendered, in order)

```
1. Title + subtitle + version label + integrity + archive links
2. Sobre los autores                  (sections/section-authors.md)
3. Nomenclatura                       (sections/section-nomenclature.md)
4. Tabla de contenidos (TOC)          (inline in index.md)
5. §0  Resumen ejecutivo             (sections/00-methodology.md)
6. §0  Encuadre metodológico         (sections/00-methodology.md)
7. §0  Política de fuentes           (sections/00-methodology.md + _includes/sourcing-policy.md)
8. §0  Política de corrección        (sections/00-methodology.md)
9. §0  Política de contribución      (sections/00-methodology.md)
10. §0 Propósito                     (sections/00-methodology.md)
11. §1 Objetivo                      (sections/01-objective.md)
12. §2 Intervención cautelar familiar (sections/02-intervention.md)
13. §3 Victimización infantil intrafamiliar observada (sections/03-victimization.md)
14. §4 Falsas denuncias / intervalo operativo (sections/04-false-allegations.md)
15. §5 Universo penal: condenas por integridad sexual (sections/05-penal-convictions.md)
16. §6 Marco Analítico A              (sections/06-framework-a.md)
17. §7 Marco Analítico B              (sections/07-framework-b.md)
18. §8 Discusión                     (sections/08-discussion.md)
19. §9 Limitaciones                  (sections/09-limitations.md)
20. Argumentos contrarios            (sections/section-counterclaims.md)
21. §10 Trazabilidad y jerarquía de evidencia (sections/10-evidence-hierarchy.md)
22. §11 Conclusiones                 (sections/11-conclusions.md)
23. Revisiones                       (sections/section-revisions.md)
24. §12 Fuentes primarias            (sections/12-sources.md)
25. Anexo A — Fact-check             (sections/annex-a-factcheck.md)
26. Anexo B — Glosario de denominadores FD (sections/annex-a-factcheck.md)
```

Any reordering must mirror PE's original structure. See section 4 in https://project-evidence.github.io for the reference order.

---

## The 20 METH Compliance Items

When a new iteration is started, the agent MUST keep `METH-001`..`METH-020` GREEN. The status tracker is `validate_ci.py` and re-runs before any commit.

| ID  | Severity  | Item                                      | Status |
|-----|-----------|-------------------------------------------|--------|
| 001 | High      | Authors section (anon, COI, funding)      | PASS   |
| 002 | Low       | Domain-specific correction triggers       | PASS   |
| 003 | Medium    | Issue/PR templates + CONTRIBUTING.md      | PASS   |
| 004 | High      | Source archiving (archive.is / web.archive)| WARN (script ready, runs async) |
| 005 | Low       | Sourcing policy fleshed out               | PASS   |
| 006 | Critical  | Real PGP public key                       | PASS   |
| 007 | Critical  | Integrity hash (SHA256 of index.html)     | PASS   |
| 008 | High      | Detached GPG signature of index.html      | PASS   |
| 009 | High      | Nomenclature / glossary section           | PASS   |
| 010 | High      | Counter-claims section                    | PASS   |
| 011 | Medium    | Revision / version history                | PASS   |
| 012 | Low       | Propósito section deep (PE-style)         | PASS   |
| 013 | Critical  | Deploy workflow: archive+integrity BEFORE upload | PASS |
| 014 | Medium    | Mobile nav toggle (JS + .show CSS)        | PASS   |
| 015 | Medium    | All nav anchor links resolve              | PASS   |
| 016 | Low       | In-page TOC present                       | PASS   |
| 017 | Low       | jekyll-scholar not present (no _bibliography) | PASS |
| 018 | Low       | No empty directories                      | PASS   |
| 019 | Low       | validate.py uses relative/dynamic path    | PASS   |
| 020 | Medium    | Footer links all 4 crypto files           | PASS   |

The METH numbering MUST NOT change between sessions. Audit documents reference these IDs.

Any new audit item MUST be added as `METH-NNN` and integrated into `validate_ci.py` before being referenced in this file.
