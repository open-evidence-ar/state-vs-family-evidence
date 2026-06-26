# EPH Pipeline (Reproducción §14.10)

This file is loaded on demand from `AGENTS.md §3` for reproducibility of the
EPH household-composition series used in `sections/14-marco-cordoba.md` §14.10.

Read when:

- A reviewer or a future agent needs to verify the numbers from scratch
- A revision adds new quarters and the committed CSVs must be regenerated
- The chart `assets/hogares_monoparentales_linea_temporal.svg` needs to be
  re-rendered after a matplotlib version change

---

## What this pipeline produces

Two CSV files (committed to `scripts/`) and one chart (committed to `assets/`):

| File | Schema | What it represents |
|---|---|---|
| `scripts/national_mono_defB_genlac.csv` | `year, period, n_households_weighted, n_mono_weighted, pct_mono_defB` | Nacional (todos los aglomerados urbanos), Definition B₂ (GenLAC-comparable), 2005–2025 |
| `scripts/cordoba_mono_defB_genlac.csv` | `year, period, n_households_weighted, n_mono_weighted, pct_mono_defB` | Gran Córdoba, Definition B₂ (GenLAC-comparable), 2007–2025 |
| `assets/hogares_monoparentales_linea_temporal.svg/.png` | chart | Two lines + institutional milestone markers (color-matched to line) |

**Nota:** La definición anterior "Def B (II7=4)" fue eliminada porque II7 es "régimen de tenencia" (propiedad/alquiler), no "tipo de hogar". La variable correcta para monoparentalidad es CH03 (parentesco).

## Pipeline stages

```
Stage 1  Definición B₂ GenLAC (nac + CBA)  (build_eph_defB_genlac.py)
```

Un solo script produce ambos CSVs (nacional + Córdoba) en una ejecución.

---

## Setup — independent of any previous session

```powershell
# 1. Install Python deps (one shell, one shot)
pip install -r scripts/requirements.txt

# 2. Optional cleanup of stale caches
Remove-Item -Recurse -Force scripts/_eph_cache  -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force scripts/_eph_cache_nat -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force pyeph  -ErrorAction SilentlyContinue
```

## Run — full reproduction from zero

Prereqs: Python 3.x, internet access. **First run will download individual
base EPH zips into `scripts/_eph_cache_nat/`** (2005–2024, ~20 quarters).
Subsequent runs reuse the cache.

```powershell
# Single command: produces both national + CBA CSVs
python scripts/build_eph_defB_genlac.py
```

## Stage 1: Definición B₂ (GenLAC-comparable)

**Bullet points:**

- **Script**: `python scripts/build_eph_defB_genlac.py`
- **Outputs**: `scripts/national_mono_defB_genlac.csv` AND `scripts/cordoba_mono_defB_genlac.csv` (in one execution)
- **Numerator**: head (CH03=1), no partner (no CH03=2), child present (CH03=3 present)
- **Denominator**: head age 25 ≤ CH06 ≤ 54; exclude unipersonal households (n_members == 1)
- **Source**: GenLAC §2.2.3 <https://genlac.econo.unlp.edu.ar/wp-content/uploads/2025/12/Diccionario-de-Indicadores-de-la-base-GenLAC_ESP_2025-12-1.pdf>
- **Validation**: 2024-T1 nacional = 25.79%, matches GenLAC public chart (~25%+)
- **Timeline**: Nacional 2005–2025; Gran Córdoba 2007–2025 (T1 each year; 2025 includes T1–T3; 2007 T3 and emergency-statistics gaps excluded). CBA pre-2007 excluded: tiny sample (~400 hogares), high sampling volatility, INDEC 2009 revision of expansion coefficients for 2003-2006 bases.
- **2020-T4 excluded** because pandemic denominator distortion

**Variable clarification:** II7 in EPH is "régimen de tenencia" (housing tenure), NOT "tipo de hogar". The correct variable for monoparental household construction is CH03 (parentesco/relación con el jefe). The previous "Def B (II7=4)" was computing housing tenure, not household type, and has been eliminated.

## Cache layout

## Verification — confirm committed values match a clean rerun

After running the script above, the committed CSVs in `scripts/*.csv`
should be **identical** to the CSVs you just produced. Compare:

```powershell
Get-Content scripts/national_mono_defB_genlac.csv
# Expected: ~24 rows, 2005-T1 should be ~18.56%, 2025-T1 should be ~26.44%
Get-Content scripts/cordoba_mono_defB_genlac.csv
# Expected: ~22 rows, 2007-T1 should be ~20.51%, 2025-T1 should be ~25.45%
```

For automated verification run:

```powershell
python scripts/verify_reproducibility.py
```

This script wraps a rerun and exits 0 if the committed CSVs match (within ±0.05pp tolerance) and exit 1 if they don't.

---

## Provenance & external validation

The committed CSVs (`national_mono_defB_genlac.csv`, `cordoba_mono_defB_genlac.csv`) are **derived data**, not raw sources. Their provenance chain is:

```
INDEC EPH microdata (base individual, FTP/GitHub mirror)
  → pyeph download + cache
    → build_eph_defB_genlac.py (CH03 + CH06 + PONDERA aggregation)
      → committed CSVs
        → build_eph_chart.py → SVG/PNG
```

**External anchor points** (independent of our pipeline):

| Check | Value | Source | Status |
|---|---|---|---|
| GenLAC Argentina 2024 | ~25%+ | [genlac-graphics.econo.unlp.edu.ar](https://genlac-graphics.econo.unlp.edu.ar/familia_spanish/porcen-hog-mono) | ✓ Convergent: our Def B₂ 2024-T1 = 25,79% |
| GenLAC dictionary §2.2.3 | head 25–54, excl. unipersonal | [GenLAC PDF 2025-12](https://genlac.econo.unlp.edu.ar/wp-content/uploads/2025/12/Diccionario-de-Indicadores-de-la-base-GenLAC_ESP_2025-12-1.pdf) | ✓ Specification replicated exactly |

**What can break:** If pyeph's INDEC mirror goes down or the EPH variable schema changes, the pipeline fails. The committed CSVs are the stable artifact; the script is the reproducibility mechanism. To reproduce from scratch: `pip install -r scripts/requirements.txt && python scripts/build_eph_defB_genlac.py` (first run downloads ~25 quarterly ZIPs, ~5 min).

---

## Cache layout

```
scripts/_eph_cache/                  <- Gran Cordoba base hogar (88 zips + CSVs)
   hogar_{year}_{freq}{period}.csv

scripts/_eph_cache_nat/              <- Base individual nacional (~8 quarters)
   indiv_{year}T{period}.csv
```

Both directories are .gitignored. The pyeph library's own internal cache
(`pyeph/.db/`) is redirected to `scripts/_eph_cache/` via `os.chdir()` at the
top of each build script. This keeps the repo root clean.

## INDEC data quality caveat (2007–2015)

The INDEC published an anexo metodológico in August 2016 warning that
EPH series between January 2007 and December 2015 should be "considered
with reservations". This caveat is built into:
- `sections/14-marco-cordoba.md` §14.10.6 caveat #3
- the INDEC's own PGP-signed CSV includes a verification URL pointing to
  [anexo_informe_eph_23_08_16.pdf](https://www.indec.gob.ar/ftp/cuadros/sociedad/anexo_informe_eph_23_08_16.pdf)

(pyeph does not auto-detect this. The user must read the caveat in the
section before committing changes to values 2010–2015.)

## INDEC SKIPPED_TRIMESTRES (the four known gaps)

| (year, period) | Reason |
|---|---|
| (2007, 3) | Publicación no localizada en repositorio INDEC |
| (2015, 3) | Emergencia estadística (datos no publicados) |
| (2015, 4) | Emergencia estadística (datos no publicados) |
| (2016, 1) | Emergencia estadística; publicaciones retomaron T2/2016 |

These gaps are encoded in `build_eph_defB_genlac.py`.

## Pre-2005 data — NOT processed

EPH antes de 2005 usa el esquema de variables `PXX/RXX` (no `IIXX`/`CHXX`).
La variable `CH03` (parentesco) no existe en los microdatos del período
2003 (EPH onda). Por tanto §14.10 cubre 2005–2025 solamente. Para pre-2005
sería necesario reconstruir manualmente el tipo de hogar desde `RXX` — fuera del
scope de esta sección.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `ModuleNotFoundError: pyeph` | Dependencies not installed | `pip install -r scripts/requirements.txt` |
| `OSError: Indeterminate offline location` cache path | pyeph's MODULE_PATH override failed | Confirm `os.chdir(WORK_DIR)` runs before `MicroData()` |
| INDEC download returns HTML 36KB (SPA fallback) | INDEC site migrated to JS SPA | pyeph auto-falls-back to GitHub Pages mirror — confirm connectivity |
| `UnicodeDecodeError` in EPH CSV | Old EPH files use latin-1, pandas default utf-8 | Scripts triple-try utf-8 / latin-1 / cp1252 — if all fail, file is corrupted |
| `EOFError` mid-download | Network interruption | Re-run; pyeph resumes the cache |
| Chart looks different after rerun | matplotlib version drift | Pin matplotlib in `scripts/requirements.txt` |

---

#### Where this file is referenced

- `scripts/build_eph_defB_genlac.py` docstring (header)
- `scripts/verify_reproducibility.py` module-level docstring
- `sections/14-marco-cordoba.md` §14.10.7 cross-link
