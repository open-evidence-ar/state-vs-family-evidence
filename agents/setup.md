# Setup — Reference

This file is loaded on demand from `AGENTS.md §3`. Read when installing deps, regenerating PGP, or troubleshooting PATH/Python issues.

---

## Dependencies

| Tool       | Version | Verified          | Install                                    |
|------------|---------|-------------------|--------------------------------------------|
| Ruby       | 3.3.x   | 3.3.11            | winget install RubyInstallerTeam.RubyWithDevKit.3.3 |
| Bundler    | 4.x     | 4.0.14            | gem install bundler                        |
| Jekyll     | 4.4.x   | 4.4.1             | bundle install                             |
| GnuPG      | 2.5.x   | 2.5.20            | winget install GnuPG.GnuPG                 |
| Python (validator) | any 3.x | used for `validate_ci.py`                    |
| PowerShell | 5.1     | for archive-sources.ps1 only             |

PATH setup after install (Windows, one-time per session):
```powershell
$env:PATH = "C:\Ruby33-x64\bin;C:\Program Files\GnuPG\bin;$env:PATH"
```

For Python: this project uses the LibreOffice Python at `C:\Program Files\LibreOffice\program\python.exe` because the Microsoft Store "python.exe" alias is a stub. Alternative is any 3.x Python.

---

## Ruby gems

`Gemfile` declares only:
```ruby
gem "jekyll", "~> 4.3"
gem "webrick"
```

`jekyll-scholar` was removed (see METH-017). Do NOT re-add unless `_bibliography/` and a `scholar` config block exist.

---

## First-time git setup

The PGP private key is stored in a GitHub Secret named `GPG_PRIVATE_KEY`. The fingerprint is `4CD0CD520DF89A72298F5508D94695AF7419D1CD`. The user identity is `State vs Family Evidence`.

The corresponding private key, if generated locally, is in `private-key.asc` (NEVER committed) and was exported with `gpg --armor --export-secret-keys "State vs Family Evidence"`. After upload to GitHub Secrets, delete the local `private-key.asc` and confirm with `git status` before any commit.

---

## Re-generate PGP key (only if compromised / lost)

```bash
./scripts/generate-pgp.sh            # Linux/macOS
# Windows: see scripts/generate-pgp.ps1 (or run manually):
gpg --batch --passphrase "" --quick-gen-key "State vs Family Evidence" default default 0
gpg --armor --export "State vs Family Evidence" --output public.pem
gpg --armor --export-secret-keys "State vs Family Evidence" --output private-key.asc
```

Then re-export the private key and update the `GPG_PRIVATE_KEY` GitHub Secret. Re-sign with `gpg --armor --detach-sign --default-key "State vs Family Evidence" _site/index.html`.
