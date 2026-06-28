## 6. Marco Analítico A — Ratio principal (NNyA ↔ NNyA)
{: #marco-analitico-a}

### Pregunta

¿Cuál es la relación entre NNyA en intervenciones cautelares estimadas y NNyA registrados como víctimas observadas de abuso sexual intrafamiliar **dentro de la misma jurisdicción**?

### Variable de referencia

**1.819** víctimas intrafamiliares observadas, cobertura nacional ({% include tags/derivado.html %}) — **646** víctimas intrafamiliares CABA-equivalentes ({% include tags/derivado.html %}, prorrateado)

### Cálculos

#### Ratio CABA↔CABA (denominador prorrateado)

| Escenario civil | NNyA | Ratio |
|---|---|---|
| Caso base observado (microdatos CSJN OVD 2024, CABA/federal) | 3.525 | 3.525 / 646 = **5,46 : 1** |

{% include tags/calculo.html formula="1.819 víctimas intrafamiliares (Línea 137 nacional) × 35,5% participación CABA (informe Línea 137, 2017–oct 2023)" resultado="≈ 646 víctimas intrafamiliares CABA-equivalentes" nota="<span class='badge badge-derivado' title='Aritmética reproducible sobre observados con prorrateo jurisdiccional oficial'>◇ Derivado</span>" %}

#### Ratio CABA↔Nacional (denominador original, conservador)

| Escenario civil | NNyA | Ratio |
|---|---|---|
| Caso base observado (microdatos CSJN OVD 2024) | 3.525 | 3.525 / 1.819 = **1,94 : 1** |

### Análisis de sensibilidad del denominador CABA

| Clave de prorrateo | CABA víctimas estimadas | Ratio Marco A | Fundamento |
|---|---:|---:|---|
| 35,5% (participación CABA en NNyA víctimas de violencia sexual, informe Línea 137 2017–oct 2023; **cross-validado con microdatos `datos.jus.gob.ar` 2017–2023**: 75,0% Metropolitana vs 75,1% reportado, §3.3) | 646 | **5,46 : 1** | Dato oficial publicado por la Dirección Nacional de Promoción y Fortalecimiento para el Acceso a la Justicia (Min. Justicia, 18-nov-2023, agencia Télam); reproducido por 11 medios independientes |
| 31,4% (peso poblacional CABA dentro del aglomerado Metropolitano, Censo INDEC 2022: 3,12M / 9,95M) | 571 | **6,17 : 1** | Piso conservador: asume victimización proporcional a población dentro del aglomerado |

### Interpretación

Por cada NNyA registrado como víctima observada de abuso sexual intrafamiliar **en CABA**, entre **5,46 y 6,17 NNyA** aparecen en el universo de intervenciones cautelares con al menos una medida de ruptura familiar (OVD 2024, CABA/federal), según la clave de prorrateo adoptada. El ratio 1,94:1 (denominador nacional) sigue vigente como cota conservadora que compara el numerador CABA contra el denominador más amplio disponible, pero **infla el denominador al incluir víctimas de jurisdicciones donde la OVD no opera**. El ratio CABA↔CABA (5,46:1) restablece la comparabilidad jurisdiccional: ambos términos provienen del mismo territorio.

Este indicador compara **Niños ↔ Niños dentro de la misma jurisdicción** y constituye el ratio **metodológicamente más robusto** del estudio.

### Prevención metodológica: sesgo territorial {: #prevencion-metodologica-marco-a}

> **Nota sobre equivalencia jurisdiccional.** El numerador del Marco A proviene de la OVD (CABA/federal, ~6,7% de la población nacional). La Línea 137 no publica microdatos con desglose provincial en sus archivos anuales de datos abiertos ([datos.jus.gob.ar](https://datos.jus.gob.ar/dataset/linea-137-victimas-de-violencia-sexual), fuente #14c §12): el campo `llamado_region` agrupa CABA y los 24 partidos del conurbano bonaerense como "Metropolitana", sin posibilidad de separación. Sin embargo, el informe oficial de la Línea 137 (período 2017–oct 2023, publicado 18-nov-2023 por la Dir. Nacional de Promoción y Fortalecimiento para el Acceso a la Justicia, Min. Justicia; caso base 16.286 NNyA víctimas 2017–oct 2023; atribución secundaria verificable vía El Destape, §12 fuente #14b) consigna que **el 35,5% de las NNyA víctimas de violencia sexual atendidas residen en CABA**, seguido por PBA con 39,6%. Este dato permite prorratear el denominador nacional (1.819) al ámbito CABA (≈646), produciendo un ratio CABA↔CABA de **5,46:1**. La alternativa de prorrateo poblacional (31,4% CABA dentro del aglomerado Metropolitano, Censo 2022) produce un ratio conservador de **6,17:1**. Ambas cotas son consistentes con la predicción previa del informe: la restricción territorial del numerador al CABA *subestima* la magnitud real del ratio (cfr. Capa 4 del Marco B, §7: ratios ~15× superiores al extrapolar al nivel nacional). Un lector que infiera que la asimetría territorial *infla* el ratio confrontando un numerador metropolitano con un denominador nacional disperso, tiene la **inferencia invertida**: al corregir la asimetría territorial (CABA↔CABA), el ratio **aumenta** de 1,94 a 5,46:1 — la comparación con denominador nacional era, en todo caso, conservadora. Adicionalmente, la sub-denuncia estructural (estimada en 77–88% por CEDAW/ONU) implica que el denominador real de víctimas CABA es probablemente superior al prorrateado, lo que *reduciría* el ratio — pero esa reducción no se puede cuantificar sin dato oficial. El sesgo territorial del Marco A opera en dirección conservadora tanto en la versión nacional (1,94:1) como en la CABA (5,46:1); su corrección completa requeriría un registro nacional unificado de cautelares que hoy no existe (§9.1, §9.10), así como microdatos de la Línea 137 con desglose provincial.
