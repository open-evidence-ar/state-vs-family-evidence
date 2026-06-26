"""
Definicion B2 (GenLAC-comparable) hogares monoparentales.

Definicion B2 (GenLAC 2.2.3):
> "Hogares monoparentales como porcentaje del total de hogares con jefe/a entre 25 y 54 anos
>  (excluyendo hogares unipersonales). Se considera a un hogar monoparental cuando
>  hay hijos pero no hay conyuge en el hogar."

Numerador: CH03==1 (jefe), no CH03==2 (pareja), CH03==3 (hijo) presente.
Denominador: jefe 25–54, excl. unipersonales.

Cobertura:
   Nacional: 2005–2025 (T1 de cada ano; 2025 incluye T1–T3; 2007 T3 y gaps emergencia estadistica excluidos).
   Gran Cordoba: 2007–2025 (2025 incluye T1–T3; pre-2007 excluido: muestra CBA ~400 hogares, alta volatilidad
     muestreo + revision INDEC 2009 de coeficientes expansion 2003-2006).

Salida:
  scripts/national_mono_defB_genlac.csv
  scripts/cordoba_mono_defB_genlac.csv

Uso:
  python scripts/build_eph_defB_genlac.py
"""
import os
import sys
import logging
import pandas as pd
import warnings
import zipfile
import shutil
from pathlib import Path

from pyeph.get.microdata import MicroData

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parent.parent
WORK_DIR = ROOT / "scripts"

EPH_CACHE = WORK_DIR / "_eph_cache_nat"
EPH_CACHE.mkdir(parents=True, exist_ok=True)
os.chdir(WORK_DIR)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
log = logging.getLogger(__name__)
logging.getLogger("pyeph").setLevel(logging.CRITICAL)

OUTPUT_CSV_NATIONAL = WORK_DIR / "national_mono_defB_genlac.csv"
OUTPUT_MD_NATIONAL = WORK_DIR / "national_mono_defB_genlac.md"
OUTPUT_CSV_CORDOBA = WORK_DIR / "cordoba_mono_defB_genlac.csv"
OUTPUT_MD_CORDOBA = WORK_DIR / "cordoba_mono_defB_genlac.md"

SAMPLE_YEARS = list(range(2005, 2026))  # 2005–2025
CBA_START_YEAR = 2007  # CBA starts 2007: pre-2007 volatile (~400 hogares, INDEC revision)

SKIPPED_TRIMESTRES = {
    (2007, 3),
    (2015, 3),
    (2015, 4),
    (2016, 1),
}


def ensure_csv(year, period):
    csv_path = EPH_CACHE / f"indiv_{year}T{period}.csv"
    if csv_path.exists():
        return csv_path
    md = MicroData(year=year, period=period, freq="trimestre", base_type="individual")
    try:
        md._download_from_indec()
    except Exception as e:
        log.debug("pyeph INDEC path: %s", e)
        try:
            md.from_github()
        except Exception as e2:
            log.error("Mirror path failed: %s", e2)
            return None
    # Search multiple possible locations for the ZIP
    candidates = [
        ROOT / "pyeph" / ".db" / "individual" / md.filename,
        WORK_DIR / "pyeph" / ".db" / "individual" / md.filename,
        ROOT / "pyeph" / ".db" / md.filename,
        WORK_DIR / "pyeph" / ".db" / md.filename,
        EPH_CACHE / md.filename,
        WORK_DIR / md.filename,
    ]
    pyeph_path = None
    for c in candidates:
        if c.exists():
            pyeph_path = c
            break
    if pyeph_path is None:
        log.error("Q%s %s individual ZIP not found (checked: %s)",
                  period, year, [str(c) for c in candidates])
        return None
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(pyeph_path, "r") as z:
        name = z.namelist()[0]
        target = csv_path.parent / name
        z.extract(name, csv_path.parent)
        if target.exists():
            shutil.move(str(target), str(csv_path))
    return csv_path


def read_csv(csv_path):
    for enc in ("utf-8", "latin-1", "cp1252"):
        try:
            return pd.read_csv(
                csv_path,
                sep=",",
                encoding=enc,
                dtype={"AGLOMERADO": "Int64", "PONDERA": "float64"},
            )
        except (UnicodeDecodeError, ValueError):
            continue
    return None


def process_quarter(year, period, filter_cordoba=False):
    if (year, period) in SKIPPED_TRIMESTRES:
        return None
    csv_path = ensure_csv(year, period)
    if csv_path is None:
        return None
    df = read_csv(csv_path)
    if df is None:
        return None
    required = {"CODUSU", "NRO_HOGAR", "CH03", "CH06", "PONDERA"}
    if not required.issubset(df.columns):
        log.error("Missing required cols in Q%s %s: %s", period, year,
                  required - set(df.columns))
        return None
    df["CH03"] = pd.to_numeric(df["CH03"], errors="coerce")
    df["CH06"] = pd.to_numeric(df["CH06"], errors="coerce")
    df["PONDERA"] = pd.to_numeric(df["PONDERA"], errors="coerce")
    df = df.dropna(subset=["CODUSU", "NRO_HOGAR", "CH03", "CH06", "PONDERA"])
    if filter_cordoba and "AGLOMERADO" in df.columns:
        df = df.dropna(subset=["AGLOMERADO"])
        df["AGLOMERADO"] = df["AGLOMERADO"].astype(int)
        df = df[df["AGLOMERADO"] == 13]
        if df.empty:
            return None
    hh = (df.groupby(["CODUSU", "NRO_HOGAR"])
            .agg(
                has_head=("CH03", lambda x: (x == 1).any()),
                has_partner=("CH03", lambda x: (x == 2).any()),
                has_child=("CH03", lambda x: (x == 3).any()),
                n_members=("CH03", "count"),
                PONDERA=("PONDERA", "first"),
            ).reset_index())
    head_age_map = (
        df[df["CH03"] == 1]
        .set_index(["CODUSU", "NRO_HOGAR"])["CH06"]
        .to_dict()
    )
    hh["head_age"] = hh.apply(
        lambda row: head_age_map.get((row["CODUSU"], row["NRO_HOGAR"]), 0),
        axis=1,
    )
    hh["is_unipersonal"] = hh["n_members"] == 1
    eligible = hh[
        hh["has_head"]
        & (hh["head_age"] >= 25)
        & (hh["head_age"] <= 54)
        & ~hh["is_unipersonal"]
    ]
    mono = eligible[
        eligible["has_head"]
        & ~eligible["has_partner"]
        & eligible["has_child"]
    ]
    total_w = eligible["PONDERA"].sum()
    mono_w = mono["PONDERA"].sum()
    if total_w == 0:
        return None
    return {
        "year": year,
        "period": period,
        "n_households_weighted": float(total_w),
        "n_mono_weighted": float(mono_w),
        "pct_mono_defB": round(float(mono_w / total_w) * 100, 4),
    }


def main():
    rows_national = []
    for year in SAMPLE_YEARS:
        if year == 2016:
            quarters = [2]
        elif year == 2020:
            quarters = [1, 4]
        elif year == 2025:
            quarters = [1, 2, 3]
        else:
            quarters = [1]
        for q in quarters:
            res = process_quarter(year, q, filter_cordoba=False)
            if res:
                rows_national.append(res)
                log.info("Nacional Y=%s T%s -> %.2f%% mono",
                         year, q, res["pct_mono_defB"])
    df_nat = pd.DataFrame(rows_national)
    if df_nat.empty:
        sys.exit(1)
    df_nat.to_csv(OUTPUT_CSV_NATIONAL, index=False)
    with open(OUTPUT_MD_NATIONAL, "w", encoding="utf-8") as f:
        f.write(
            "Def B (GenLAC-comparable) | nacional "
            "(todos los aglomerados urbanos) | EPH\n\n"
        )
        f.write("| Ano | T | % Mono Def B (GenLAC) | n hogares pond |\n")
        f.write("|---:|---:|---:|---:|\n")
        for _, r in df_nat.iterrows():
            f.write(
                f"| {int(r['year'])} | T{int(r['period'])} | "
                f"{r['pct_mono_defB']:.2f} | "
                f"{int(r['n_households_weighted']):,} |\n"
            )

    rows_cba = []
    for year in SAMPLE_YEARS:
        if year < CBA_START_YEAR:
            continue
        if year == 2016:
            quarters = [2]
        elif year == 2020:
            quarters = [1, 4]
        elif year == 2025:
            quarters = [1, 2, 3]
        else:
            quarters = [1]
        for q in quarters:
            res = process_quarter(year, q, filter_cordoba=True)
            if res:
                rows_cba.append(res)
                log.info("Cordoba Y=%s T%s -> %.2f%% mono",
                         year, q, res["pct_mono_defB"])
    df_cba = pd.DataFrame(rows_cba)
    if df_cba.empty:
        sys.exit(1)
    df_cba.to_csv(OUTPUT_CSV_CORDOBA, index=False)
    with open(OUTPUT_MD_CORDOBA, "w", encoding="utf-8") as f:
        f.write(
            "Def B (GenLAC-comparable) | Gran Cordoba "
            "(aglomerado 13) | EPH\n\n"
        )
        f.write("| Ano | T | % Mono Def B (GenLAC) | n hogares pond |\n")
        f.write("|---:|---:|---:|---:|\n")
        for _, r in df_cba.iterrows():
            f.write(
                f"| {int(r['year'])} | T{int(r['period'])} | "
                f"{r['pct_mono_defB']:.2f} | "
                f"{int(r['n_households_weighted']):,} |\n"
            )


if __name__ == "__main__":
    main()
