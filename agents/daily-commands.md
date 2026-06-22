# Daily Commands — Reference

This file is loaded on demand from `AGENTS.md §3`. Read when you need to run builds, serve, sign, or archive.

---

## Windows PATH setup (one-time per shell)

Ruby no se agrega al PATH automáticamente. Al abrir una terminal nueva, corré:

```powershell
$env:PATH = "C:\Ruby33-x64\bin;$env:PATH"
```

O creá un alias de PowerShell persistente en `$PROFILE`:

```powershell
function jkl { $env:PATH = "C:\Ruby33-x64\bin;$env:PATH"; bundle exec jekyll @args }
```

Después usá `jkl build` o `jkl serve` sin escribir el PATH cada vez.

---

## Validate everything (fast, source-only, no build)

```bash
python validate_ci.py
```

This is the gate before any commit. Expected output: 19–20 PASS, 0 FAIL, 0–1 WARN. If FAIL > 0, fix before commit.

---

## Full build + validate (slow; requires Ruby+Jekyll)

```bash
python validate_ci.py --with-build
```

This additionally runs `bundle exec jekyll build`, generates `archive.zip`, computes `integrity.txt`, signs `_site/index.html` with the PGP key if `GPG_PRIVATE_KEY` is in env, and checks the built HTML for broken anchors and links.

---

## Serve the built site locally

```bash
bundle exec jekyll serve
# or, simpler, serve _site/ without Jekyll:
python -m http.server 4000 --directory _site
```

Browse at http://127.0.0.1:4000.

On this Windows machine, the LibreOffice Python is at `C:\Program Files\LibreOffice\program\python.exe` and works without path changes. If `python` resolves to a Microsoft Store stub, use the full path.

---

## Re-generate archive links

```bash
./scripts/archive-sources.ps1    # PowerShell only
```

Currently produces redirect URLs (`archive.is/save/<url>`) because the archive.is save endpoint redirects before snapshotting. The real archive.is snapshot URL must be resolved through a browser session (manual). When archive.is is unreachable (sandboxed networks), this step is non-blocking.

---

## Re-build with fresh artifacts

```bash
bundle exec jekyll build --baseurl "${{ steps.pages.outputs.base_path }}"
cd _site
Compress-Archive -Path ./* -DestinationPath ./archive.zip -Force     # or: zip -r archive.zip .
(git hash-object index.html)   # equivalent of sha256sum
gpg --armor --detach-sign --default-key "State vs Family Evidence" index.html
mv index.html.asc signature
```

These exact steps are encoded in `.github/workflows/deploy.yml`.

---

## Git push con PAT (HTTPS — sin TTY interactivo)

En Windows, `git push` sobre HTTPS puede fallar con `bash: /dev/tty: No such device or address` porque no hay terminal interactiva para pedir usuario/contraseña. Solución: usar el PAT de `.env` en la URL del remote y restaurarlo después.

```powershell
# 1. Tomar el PAT del .env (gitignored, seguro)
$pat = (Get-Content .env | Select-String "PAT=(.+)" | % { $_.Matches.Groups[1].Value })

# 2. Configurar remote con credenciales inline
git remote set-url origin "https://open-evidence-ar:${pat}@github.com/open-evidence-ar/state-vs-family-evidence.git"

# 3. Push (main o tag)
git push origin main
git push origin v1.0.0   # tags también

# 4. Restaurar remote sin credenciales
git remote set-url origin "https://github.com/open-evidence-ar/state-vs-family-evidence.git"
```

**Advertencia:** el comando `set-url` con el PAT queda visible en el historial de PowerShell (`Get-History`). En entornos compartidos, usar `$env:GIT_ASKPASS` en su lugar.
