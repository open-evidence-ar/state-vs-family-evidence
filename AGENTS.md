# AGENTS.md — Operating Manual for State vs Family Evidence

This file is the authoritative context for any agent (human or AI) working on this repository. Read it before making changes. If a change contradicts a rule here, update AGENTS.md first or justify the deviation explicitly.

---

## 1. Project Identity

**Name:** State vs Family Evidence
**Reference:** [Project-Evidence](https://github.com/Project-Evidence/project-evidence.github.io) (PE)
**Reference site:** https://project-evidence.github.io
**Purpose:** Descriptive study with traceable evidence about the asymmetry between family-protection judicial intervention (cautelares), observed intrafamilial child victimization, and identifiable criminal outcomes in Argentina.
**Language:** Spanish (es)
**Type:** Single-page Jekyll document deployed to GitHub Pages.
**Versioning:** 1.0.0 (versión inaugural).

The project is consumed primarily through a single generated `index.html`. Verify changes by building the site locally and reviewing the rendered output.

---

## 2. Core Rules (always apply)

### 2.1 MUST do before work is complete

1. Run `python validate_ci.py`. Expected: no FAIL.
2. If touching a Markdown section using `{% include %}`, run `bundle exec jekyll build` to catch Liquid parse errors.
3. If editing calc boxes, do NOT nest `{% include %}` inside another include's parameter. Use inline HTML badges. See `agents/gotchas.md`.
4. If adding a new heading the TOC/nav could link to, ensure a valid HTML id is produced or set an explicit `{:#anchor-id}`. See `agents/gotchas.md`.
5. Update `missing-methodology.md` only when severity/status of an audit item changes. Do NOT remove items.
6. Update `sections/section-revisions.md` whenever a substantive change ships.
7. Never commit `private-key.asc`. `Gemfile.lock` is fine, `_site/` is gitignored.

### 2.2 MUST NOT do

- Edit `public.pem`, `signature`, `integrity.txt` by hand. They regenerate from a real build.
- Add `jekyll-scholar` back to `Gemfile` without also adding `_bibliography/` and a scholar config block.
- Add Liquid include tags inside Liquid include-tag parameter values.
- Add new sections without a heading anchor (`{:#id}`) or a slug-style heading.
- Create empty directories. METH-018 will fail.
- Use Windows `>` PowerShell redirect to write `public.pem` — it produces UTF-16 LE with BOM. Use `Set-Content -Encoding ASCII` instead.

### 2.3 Code style

- Spanish content uses standard accented vowels (á é í ó ú ñ ¿ ¡).
- All citations must be hyperlinked. Internal anchors use Kramdown auto-generated IDs unless overridden.
- Evidence badges inside another include's parameter must use inline HTML (not `{% include %}`).

---

## 3. On-demand reference (load only when relevant)

| If you are doing this… | Read this file |
|---|---|
| Adding/modifying METH-NNN audit items, or checking PE section order | `agents/methodology.md` |
| Installing deps, regenerating PGP, PATH/Python troubleshooting | `agents/setup.md` |
| Running any build/serve/sign/archive command, **or git push with PAT from `.env`** | `agents/daily-commands.md` |
| Editing any file path or tracing where something lives | `agents/file-map.md` |
| Editing calc boxes, headings, Liquid templates, GPG on Windows | `agents/gotchas.md` |
| Touching `.github/workflows/deploy.yml` or crypto files | `agents/ci-workflow.md` |
| Looking up Marco A/B, Capa 2/3/4, FD/VG-VI, Supuesto, etc. | `agents/glossary.md` |
| Running `validate_ci.py`, debugging a failed METH check | `agents/validate-cheatsheet.md` |

The first time you read any file in `agents/`, read `agents/validate-cheatsheet.md` as well — it lists every METH check this project enforces.

---

## 4. Philosophy

1. **Evidence before assertion.** Every claim must trace to a numbered, archived, dated source.
2. **Asymmetry, not accusation.** The study describes scale asymmetries. It does not accuse individuals or institutions.
3. **Both harms acknowledged.** Both unfounded removal of children AND unreported real victimization are harms. Discussing one is not denying the other.
4. **Public-key trust.** The site is signed because readers should be able to verify the same authors wrote each version.
5. **Change trail.** Every iteration logs to `sections/section-revisions.md`. No silent edits.
6. **Local-first review.** All changes preview locally with `jekyll serve` before push.
7. **Methodology inherited from PE.** When in doubt, fetch https://project-evidence.github.io and mirror its conventions exactly. Adapt only the content domain, never the structural rules.
8. **Autonomy through documentation.** `AGENTS.md`, `missing-methodology.md`, `validate_ci.py`, and `CONTRIBUTING.md` together form the self-describing operational layer. New agents — human or AI — onboard by reading these four files.

---

## 5. Authoring contract for this file

- `AGENTS.md` contains only identity, core rules, philosophy, and the on-demand index. Nothing more.
- Any reference material >30 lines goes into `agents/<topic>.md`.
- When adding a new rule, check whether it belongs in `AGENTS.md` (always-on) or an auxiliary file (on-demand trigger).
- The on-demand table in §3 must be kept in sync with the auxiliary files it references.
