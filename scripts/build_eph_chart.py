"""
Line chart: hogares monoparentales Def B2 (GenLAC-comparable) — Gran Cordoba vs Nacional.

Two series only:
  - Gran Cordoba Def B2 2007–2024 (solid line + diamond markers)
  - Nacional Def B2 2005–2024 (dashed line + triangle markers)

CBA starts 2007: pre-2007 excluded (tiny sample ~400 hogares, INDEC revision of expansion
coefficients for 2003-2006 bases published in 2009).

Events alternate above/below their respective lines to avoid visual overlap.
Each event tuple: (year, label, direction) where +1=above, -1=below.

Salida:
  assets/hogares_monoparentales_linea_temporal.svg
  assets/hogares_monoparentales_linea_temporal.png
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)

df_nat_defB = pd.read_csv(SCRIPTS / "national_mono_defB_genlac.csv")
df_cba_defB = pd.read_csv(SCRIPTS / "cordoba_mono_defB_genlac.csv")


def pick_defB(df):
    df = df.sort_values(["year", "period"])
    out = []
    for year, group in df.groupby("year"):
        if year == 2020 and 4 in group["period"].values:
            row = group[group["period"] == 1].iloc[0]
        else:
            row = group.iloc[0]
        out.append({"year": int(year), "pct": row["pct_mono_defB"]})
    return pd.DataFrame(out)


nat_annual = pick_defB(df_nat_defB)
cba_annual = pick_defB(df_cba_defB)

nat_map = dict(zip(nat_annual["year"], nat_annual["pct"]))
cba_map = dict(zip(cba_annual["year"], cba_annual["pct"]))

# Events: (year, label, direction) — +1 above line, -1 below line
CBA_HL = [
    (2016, "Polo Mujer\n(Dec. 174/16)", +1),
    (2019, "Micaela CBA\n(10628)+Caut\n(10637)", -1),
    (2024, "TGA 9 juezas\n(Ago 2024)", +1),
]
CBA_CTX = [
    (2010, "Oficina Mujer\n+ 1.er Fiscalia VF", +1),
    (2011, "Ley 9944\n(SENAF)", -1),
    (2016, "Ley 10400", -1),
    (2018, "AR 1497\nPolicia VF", +1),
    (2020, "Punto Mujer", -1),
    (2021, "Fuero Penal VG", +1),
    (2023, "UJ Gen/Fam/Sex", -1),
]
NAT_HL = [
    (2018, "Micaela Nacional\n(Ley 27499)", +1),
]
NAT_CTX = [
    (2009, "Oficina Mujer\nCSJN+Ley 26485", -1),
    (2012, "Femicidio penal\n(Ley 26791)+DGPG", +1),
    (2019, "Min. Mujeres\n(Dec. 7/19)", -1),
    (2021, "Acuerdo Federal\ncontra VG", +1),
]


def interp_y(year, line_map):
    years = sorted(line_map.keys())
    if year in line_map:
        return line_map[year]
    for i in range(len(years) - 1):
        if years[i] < year < years[i + 1]:
            t = (year - years[i]) / (years[i + 1] - years[i])
            return line_map[years[i]] + t * (line_map[years[i + 1]] - line_map[years[i]])
    return line_map[years[-1]]


def plot():
    fig, ax = plt.subplots(figsize=(14, 8.2))

    ax.plot(
        cba_annual["year"],
        cba_annual["pct"],
        "-D",
        color="#1a5276",
        lw=2.0,
        markersize=5,
        markeredgecolor="white",
        markeredgewidth=0.8,
        label="Gran Cordoba: Def B (GenLAC, jefe 25-54, excl. unipersonales)",
        zorder=5,
    )

    ax.plot(
        nat_annual["year"],
        nat_annual["pct"],
        "--^",
        color="#0d7d3b",
        lw=1.8,
        markersize=6,
        markeredgecolor="white",
        markeredgewidth=0.8,
        label="Nacional: Def B (GenLAC-comparable)",
        zorder=4,
    )

    # --- CBA highlight events (bold, with vertical dashed line) ---
    cba_used_y = []
    for (yr, lbl, d) in CBA_HL:
        y_line = interp_y(yr, cba_map)
        base_off = 2.2
        y_label = y_line + d * base_off
        # collision avoidance: nudge away if overlapping existing labels
        for _ in range(8):
            if any(abs(y_label - u) < 1.4 for u in cba_used_y):
                y_label += d * 1.5
            else:
                break
        cba_used_y.append(y_label)
        ax.axvline(x=yr, color="#1a5276", ls="--", lw=1.2, alpha=0.6, zorder=1)
        va = "bottom" if d > 0 else "top"
        ax.annotate(
            lbl, xy=(yr, y_line), xytext=(yr, y_label),
            fontsize=8.5, fontweight="bold", color="#1a5276",
            ha="center", va=va,
            arrowprops=dict(arrowstyle="-", color="#1a5276", lw=0.8),
        )

    # --- CBA context events (lighter) ---
    for (yr, lbl, d) in CBA_CTX:
        y_line = interp_y(yr, cba_map)
        base_off = 1.0
        y_label = y_line + d * base_off
        for _ in range(8):
            if any(abs(y_label - u) < 0.9 for u in cba_used_y):
                y_label += d * 1.1
            else:
                break
        cba_used_y.append(y_label)
        va = "bottom" if d > 0 else "top"
        ax.annotate(
            lbl, xy=(yr, y_line), xytext=(yr, y_label),
            fontsize=6.5, color="#5dade2",
            ha="center", va=va,
            arrowprops=dict(arrowstyle="-", color="#aed6f1", lw=0.5),
        )

    # --- National highlight events (bold, with vertical dashed line) ---
    nat_used_y = []
    for (yr, lbl, d) in NAT_HL:
        y_line = interp_y(yr, nat_map)
        base_off = 3.5
        y_label = y_line + d * base_off
        for _ in range(8):
            if any(abs(y_label - u) < 1.4 for u in nat_used_y):
                y_label += d * 1.5
            else:
                break
        nat_used_y.append(y_label)
        ax.axvline(x=yr, color="#0d7d3b", ls="--", lw=1.0, alpha=0.4, zorder=1)
        va = "bottom" if d > 0 else "top"
        ax.annotate(
            lbl, xy=(yr, y_line), xytext=(yr, y_label),
            fontsize=8.5, fontweight="bold", color="#0d7d3b",
            ha="center", va=va,
            arrowprops=dict(arrowstyle="-", color="#0d7d3b", lw=0.8),
        )

    # --- National context events (lighter) ---
    for (yr, lbl, d) in NAT_CTX:
        y_line = interp_y(yr, nat_map)
        base_off = 2.2
        y_label = y_line + d * base_off
        for _ in range(8):
            if any(abs(y_label - u) < 0.9 for u in nat_used_y):
                y_label += d * 1.1
            else:
                break
        nat_used_y.append(y_label)
        va = "bottom" if d > 0 else "top"
        ax.annotate(
            lbl, xy=(yr, y_line), xytext=(yr, y_label),
            fontsize=6.5, color="#58d68d",
            ha="center", va=va,
            arrowprops=dict(arrowstyle="-", color="#abebc6", lw=0.5),
        )

    ax.set_xlim(2004.5, 2025.2)
    data_min = min(cba_annual["pct"].min(), nat_annual["pct"].min())
    data_max = max(cba_annual["pct"].max(), nat_annual["pct"].max())
    ax.set_ylim(data_min - 1, data_max + 4)
    ax.set_xlabel("Ano", fontsize=11)
    ax.set_ylabel("% hogares (ponderado por expansion EPH)", fontsize=11)
    ax.set_title(
        "Hogares monoparentales: Gran Cordoba vs Nacional — Def B (GenLAC-comparable)\n"
        "EPH (INDEC) — Nacional 2005-2025, Cordoba 2007-2025 — con eventos institucionales verificados",
        fontsize=12,
        pad=14,
    )

    ax.grid(axis="y", ls=":", lw=0.5, color="lightgray", zorder=0)
    ax.legend(loc="upper left", framealpha=0.92, fontsize=9)

    foot = (
        "Fuente: EPH INDEC, base individual — aglomerado 13 (Gran Cordoba) y todos aglomerados urbanos.\n"
        "Def B (GenLAC-comparable): jefe 25-54 anios, sin conyuge, con hijos, excl. unipersonales.\n"
        "Cordoba inicia 2007: pre-2007 excluido (muestra ~400 hogares, revision INDEC 2009).\n"
        "Azul=eventos Cordoba. Verde=eventos nacionales. Negrita=aceleraciones simultaneas prov+nac.\n"
        "2020-T4 excluido del denominador por distorsion pandemica."
    )
    fig.text(0.02, -0.03, foot, ha="left", va="top", fontsize=7.4, color="#444")

    fig.tight_layout()
    svg = ASSETS / "hogares_monoparentales_linea_temporal.svg"
    png = ASSETS / "hogares_monoparentales_linea_temporal.png"
    fig.savefig(svg, format="svg", bbox_inches="tight")
    fig.savefig(png, format="png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved SVG -> {svg}")
    print(f"Saved PNG -> {png}")


if __name__ == "__main__":
    plot()
