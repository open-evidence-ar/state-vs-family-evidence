# Gotchas — Reference

This file is loaded on demand from `AGENTS.md §3`. Read when:

- Editing calc boxes, evidence badges, or Liquid templates
- Adding/changing headings or nav links
- Running GPG on Windows
- Updating Gemfile
- Running `python` on this machine
- Seeing a METH-011 false positive
- Using `{% include %}` in section files

---

## GOTCHA #1: PowerShell `>` redirect emits UTF-16 LE

```powershell
gpg --armor --export "State vs Family Evidence" > public.pem   # WRONG — produces 0xFF 0xFE BOM
```

Correct:
```powershell
gpg --armor --export "State vs Family Evidence" | Set-Content -Path public.pem -Encoding ASCII
```

or
```powershell
[System.IO.File]::WriteAllText("public.pem", (gpg --armor --export "State vs Family Evidence" | Out-String), [System.Text.Encoding]::ASCII)
```

Looking at the file as bytes:
```
$ top | head -1 public.pem
-----BEGIN PGP PUBLIC KEY BLOCK---     # OK
hexdump -n 4 public.pem
2d2d2d2d                                # OK (no BOM)
```
If the validator reports "PGP key is PLACEHOLDER" after a regen, check for the BOM.

---

## GOTCHA #2: Liquid parser does not handle nested include tags

```liquid
{% include tags/calculo.html
   formula="..."
   resultado="..."
   nota="{% include tags/derivado.html %}" %}       # WRONG — Liquid error
```

Replace with inline HTML:
```liquid
{% include tags/calculo.html
   formula="..."
   resultado="..."
   nota="<span class='badge badge-derivado'>◇ Derivado</span>" %}
```

Symptoms: `Liquid Exception: Invalid syntax for include tag: ... formula="..." resultado="..." nota="{% include ...` — check after every calculation-box edit.

---

## GOTCHA #3: Nav anchors must point to existing heading IDs

The top-nav links in `_layouts/default.html` point to:
```
#resumen-ejecutivo
#secciones
#fuentes-primarias
#anexo-a--verificación-rápida-fact-check
```

These must match HTML `id` attributes Kramdown produces from headings. Kramdown auto-slugifies `## Anexo A — Verificación rápida (fact-check)` to `anexo-a--verificación-rápida-fact-check` (note double `--` from em-dash conversion). Verify in the built HTML or with `python validate_ci.py --with-build`.

If a section heading changes, the slug changes. Update the nav link OR add an explicit `{:#id}` attribute to the heading.

---

## GOTCHA #4: `Gemfile.lock` is fine to commit but not required

The CI workflow uses `--bundler-cache: true`, which generates it on Actions. We commit `Gemfile.lock` to match. If a dependency update causes CI failure, run `bundle update` and commit both lock + Gemfile change.

---

## GOTCHA #5: The `python` Microsoft Store alias is a stub

`where python` returns `C:\Users\German\AppData\Local\Microsoft\WindowsApps\python.exe` but invoking it produces "Python was not found; run without arguments to install from the Microsoft Store." Workarounds:
- Use the LibreOffice Python at `C:\Program Files\LibreOffice\program\python.exe`
- Install a real Python via `winget install Python.Python.3.12`
- Or use `py` if Python 3 is installed

---

## GOTCHA #6: METH-011 false positive on "revisión"

The validator scans for `## *revis*` headings and a table with both `| Versi… |` and `| Fecha |` columns. A footnote like `*Última revisión de fuentes: junio 2026*` in another section does NOT trigger METH-011 because it's not a heading. If you add a footnote with the word "revisión", do not turn it into a heading.

---

## GOTCHA #7: Content includes can't traverse up with `..`

```liquid
{% include_relative ../_includes/sourcing-policy.md %}   # WRONG (Jekyll forbids ..)
{% include_relative _includes/sourcing-policy.md %}      # WRONG (treats the file as literal)
{% include sourcing-policy.md %}                          # OK — Jekyll searches _includes/
```

Source: `sections/00-methodology.md`. The `{% include %}` form is canonical.
