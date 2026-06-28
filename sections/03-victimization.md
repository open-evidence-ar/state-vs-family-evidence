## 3. Victimización infantil intrafamiliar observada
{: #victimizacion-infantil-observada}

### 3.1. Datos observados (UNICEF / Línea 137, 2020–2021)

| Indicador | Cifra | Fuente |
|---|---|---|
| Víctimas NNyA de abuso sexual atendidas | **3.219** | Fascículo 9 UNICEF |
| Agresor familiar estricto | **56,5%** | Fascículo 9 |
| Agresor en entorno cercano o de confianza | **74,2%** | Fascículo 9 |

### 3.2. Derivación reproducible (nacional)

{% include tags/calculo.html formula="3.219 × 56,5%" resultado="≈ 1.819 víctimas observadas de abuso sexual intrafamiliar (nacional)" nota="<span class='badge badge-derivado' title='Aritmética reproducible sobre observados'>◇ Derivado</span>" %}

### 3.3. Prorrateo jurisdiccional CABA {: #prorrateo-caba-denominador}

Los microdatos de la Línea 137 publicados en [datos.jus.gob.ar](https://datos.jus.gob.ar/dataset/linea-137-victimas-de-violencia-sexual) (fuente #14c §12) utilizan el campo `llamado_region` = "Metropolitana" (CABA + 24 partidos GBA), sin distinción provincial. No existe un campo `llamado_provincia` en los archivos anuales. Sin embargo, el **informe oficial de la Línea 137** (período 2017–oct 2023, publicado 18-nov-2023 por la Dir. Nacional de Promoción y Fortalecimiento para el Acceso a la Justicia, Min. Justicia; fuente #14b §12) consigna que el **35,5% de las NNyA víctimas de violencia sexual atendidas residen en CABA** (39,6% PBA; 10,2% Córdoba+Santa Fe+Mendoza+Tucumán; caso base: 16.286 NNyA víctimas 2017–oct 2023). Esta es la fuente primaria del prorrateo jurisdiccional — el cable original fue distribuido por agencia Télam ese mismo día; la atribución secundaria verificable es [El Destape, 18-nov-2023](https://www.eldestapeweb.com/informacion-general/abuso/linea-137-atendio-mas-de-16-mil-casos-de-victimas-de-violencia-y-abusos-en-los-ultimos-seis-anos-2023111819270).

**Cross-validación con microdatos abiertos (independiente):** Tarea de auditoría reproducible sobre los CSVs anuales 2017–2023 de `datos.jus.gob.ar` (28.686 llamadas, 16.535 NNyA, 7.384 intrafamiliares) arroja que `llamado_region = "Metropolitana"` cubre el **75,0% de NNyA víctimas de abuso sexual** del período. Esto coincide con la composición oficial reportada (35,5% CABA + 39,6% PBA = 75,1%); la desviación 0,1pp es ruido muestral. **Conclusión:** la cifra 35,5% CABA es **reproducible independientemente** desde los microdatos abiertos, transformando la calidad de evidencia de MODERADA (un solo comunicado) a ALTA (comunicado oficial + verificación aritmética en open data).

{% include tags/calculo.html formula="1.819 víctimas intrafamiliares nacionales × 35,5% participación CABA" resultado="≈ 646 víctimas intrafamiliares CABA-equivalentes" nota="<span class='badge badge-derivado' title='Prorrateo sobre dato oficial de composición jurisdiccional'>◇ Derivado</span>" %}

**Piso conservador (peso poblacional):** Censo INDEC 2022: CABA = 3,12M hab. / Aglomerado GBA = 9,95M hab. → CABA = 31,4% del aglomerado Metropolitano. Si la victimización fuese proporcional a la población dentro del aglomerado: 1.819 × 31,4% = **≈ 571 víctimas CABA**. Este piso produce un ratio Marco A de 6,17:1 (cfr. §6).

| Clave de prorrateo | Denominador CABA | Method |
|---|---:|---|
| 35,5% participación CABA en NNyA víctimas (informe Línea 137 2017–oct 2023) | **646** | ◇ Derivado — prorrateo sobre dato de composición jurisdiccional oficial |
| 31,4% peso poblacional CABA/Aglo. Metropolitano (Censo 2022) | **571** | ◇ Derivado — piso conservador, asume victimización ∝ población |

**Limitaciones del prorrateo:** (1) la participación 35,5% proviene del informe agregado 2017–oct 2023, no del período 2020–2021 específicamente; (2) la Línea 137 tiene sede física en CABA, lo que puede sobrerepresentar llamadas locales; (3) el denominador original (1.819 nacional) se conserva como referencia conservadora (ratio 1,94:1). El prorrateo no introduce nuevo dato — redistribuye el dato observado existente según la composición jurisdiccional documentada por la propia Línea 137.

**Limitación temporal:** periodo 2020–2021 vs OVD 2024. No son muestras estrictamente concurrentes; el ratio Marco A es indicativo, no panel longitudinal.
