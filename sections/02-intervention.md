## 2. Intervención cautelar familiar
{: #intervencion-cautelar-familiar}

### 2.1. Datos observados (OVD 2024)

La Oficina de Violencia Doméstica de la CSJN informó:

| Indicador | Cifra | Fuente |
|---|---|---|
| Personas atendidas | **17.120** | OVD Informe Anual 2024 |
| Presentaciones presenciales | **9.840** | OVD Informe Anual 2024 |
| Personas afectadas | **13.176** | OVD Informe Anual 2024 |
| Medidas preventivas ordenadas | **33.763** | OVD Informe Anual 2024 |
| Presentaciones con NNyA afectados | **3.182** (32%) | OVD Informe NNyA 2024 |
| Personas denunciadas (causas NNyA) | **3.484** | OVD Informe NNyA 2024 |
| Medidas de protección en causas NNyA | **4.474** | OVD Informe NNyA 2024 |
| Denunciados varones (total OVD) | **71%** | OVD Informe Anual 2024 |
| Padre como denunciado (causas NNyA) | **66%** | OVD Informe NNyA 2024 |
| Prohibición de acercamiento | **66%** de medidas | OVD / CSJN |
| Prohibición de contacto | **63%** de medidas | OVD / CSJN |

> *"En total, las personas afectadas por hechos de violencia doméstica denunciados ante la OVD fueron 13.176, quienes recibieron un acumulado de 33.763 medidas preventivas ordenadas judicialmente."*
> — [CSJN, Informe OVD 2024](https://www.csjn.gov.ar/novedades/detalle/9903)

> *"3182 presentaciones en las que había niñas, niños y adolescentes afectados [...] La justicia Civil ordenó un total de 4474 medidas de protección."*
> — [OVD, Informe NNyA 2024](https://www.ovd.gov.ar/ovd/novedades/detalle/12122)

**Nota:** el informe NNyA consigna **33.765** medidas preventivas totales; el informe anual general consigna **33.763**. Se adopta **33.763** como cifra principal; la diferencia de 2 unidades no altera los ratios.

**Limitación:** la OVD no representa todo el territorio nacional. No existe registro nacional unificado de medidas de familia.

**Nota sobre el mecanismo de otorgamiento:** la tasa >85% de otorgamiento de cautelares (tasa de concesión sobre presentaciones, dato documentado en §13.4.3) no es un error de los jueces sino el resultado del diseño procesal: bajo el principio de tutela judicial efectiva (ley 26.485) y prevención del riesgo, la carga de la prueba está suspendida en la etapa inicial. El problema documentado es que esa suspensión se torna permanente al prorrogarse las medidas sin exigir prueba pericial o médica de riesgo real, trasladando de hecho la carga probatoria al denunciado. *Nota: este "85%" se refiere a la tasa de otorgamiento de cautelares — **es distinto** del antiguo parámetro S-02 (85% de interrupción de contacto filial), que fue reemplazado por el 79,1% medido directamente en microdatos CSJN (§2.3, §2.4).*

### 2.2. Escala provincial de referencia (SCBA RVF 2023)

| Indicador | Cifra |
|---|---|
| Causas iniciadas — Fuero Familia | 159.515 |
| Medidas art. 7 — Fuero Familia | **220.317** |
| Medidas art. 7 — Justicia de Paz | 107.588 |
| Prohibición de acercamiento | 71.028 |
| Suspensión provisoria régimen de comunicación | **77** |

> Solo la OVD en CABA/federal ordenó **33.763** medidas en un año. La PBA documenta **327.905** medidas combinadas (Familia + Paz). Este dato contextualiza escala; no se suma directamente al numerador del Marco A por incompatibilidad territorial.

Fuente: [SCBA RVF Informe 2023](https://www.scba.gov.ar/violenciafamiliar/Informe%20estadistico%20RVF2023.pdf)

### 2.3. Parámetros del cálculo — Caso base observado

> **Auditoría 2026-06-23 (reemplazo de S-01/S-02/S-03):** la versión 1.0.0 utilizaba tres escenarios paralelos (Base/Restricción/Techo) que mezclaban (a) parámetros supuestos sin fuente [S-01=60% con hijos; S-02=85% interrupción; S-03=35% cronificación] y (b) unidades incompatibles — aplicar un porcentaje de legajos como filtro sobre una base de medidas (33.763) produce una cadena aritmética sin significado empírico. A partir de la auditoría, se reemplaza por un único escenario basado íntegramente en los microdatos abiertos publicados por la CSJN 2024, con la cronificación del vínculo como dimensión intertemporal separada (nota al pie §2.4).

| Parámetro | Valor | Fuente |
|---|---|---|
| Base de cálculo | **3.182** legajos con NNyA afectado | [CSJN — Datos Abiertos OVD 2024](https://datos.csjn.gov.ar/dataset/288e42e1-3070-447d-b268-f17e3246a854), base `ddaa-ovd2024denuncias.csv` campo `DENUNCIA_CON_NNYA_AF=SI` (MD5 `6603A4E5F2F178A770022C0F14F63B75`, N=9.840) |
| Filtro: al menos 1 medida de ruptura familiar | **2.518** legajos (79,1% de los 3.182) | Mismo dataset, unión de 10 campos `MEDIDA_*=SI` documentados en `ovd-metodologia-datos-abiertos-bases-2024.pdf` p.10-12 (MD5 `B823C4FCCA64665654AD56942FE7CE50`) |
| Hijos por familia | 1,4 | [INDEC — Censo 2022, Resultados de fecundidad](https://www.indec.gob.ar/indec4/Nivel4-DetalleProducto.asp?id_producto=32703) · verif. cruzada: [Banco Mundial — Tasa de fertilidad Argentina](https://data.worldbank.org/indicator/SP.DYN.TFRT.IN?locations=AR) |
| **Resultado (NNyA)** | **3.525** | — |
| Evidencia | <span class="badge badge-observado" title="Dato directo de microdatos públicos">◎ Observado</span> | — |

#### Desglose auditable del filtro 79,1% (cada medida trazable a la metodología OVD)

| Campo CSV | Medida judicial | Legajos en 3.182 NNyA | % sobre base NNyA |
|---|---|---:|---:|
| `MEDIDA_PROH_CONTACTO_TEL_MAIL_CEL` | Prohibición de contacto telefónico/mail/celular | 1.804 | 56,7% |
| `MEDIDA_PROH_ACERC_PERS_AF` | Prohibición de acercamiento a la persona afectada¹ | 1.800 | 56,6% |
| `MEDIDA_INTER_CDNNYA` | Intervención del Consejo de Derechos NNyA GCBA² | 1.468 | 46,1% |
| `MEDIDA_PROH_ACERC_NNYA` | Prohibición de acercamiento hacia NNyA | 1.174 | 36,9% |
| `MEDIDA_PROH_ACERC_DOM` | Prohibición de acercamiento al domicilio | 978 | 30,7% |
| `MEDIDA_EXCLUSION_HOGAR` | Exclusión del domicilio o del hogar común | 279 | 8,8% |
| `MEDIDA_PROH_INGRESO_DOMICILIO` | Prohibición de ingreso al domicilio | 120 | 3,8% |
| `MEDIDA_CUIDADO_UNILATERAL_PROVISORIO_NNYA` | Cuidado unilateral provisorio de NNyA | 105 | 3,3% |
| `MEDIDA_PROH_SALIDA_PAIS_NNYA` | Prohibición de salida del país de NNyA | 9 | 0,3% |
| `MEDIDA_SUSP_REG_VIS` | Suspensión del régimen de comunicación/visitas | 8 | 0,3% |
| **UNIÓN (≥1 medida)** |  | **2.518** | **79,1%** |

¹ *Interpretación operativa:* impide que el denunciado se acerque a quien lo denunció; en la práctica, si el denunciado vivía con la denunciante, debe dejar el hogar y coordinar para no cruzarse con quien reside allí. La coexistencia obligatoria bajo prohibición judicial de acercamiento produce ruptura del vínculo familiar conviviente en el mismo domicilio.

² *Interpretación operativa:* el Consejo de Derechos de Niñas, Niños y Adolescentes (GCBA) es el organismo administrativo que recibe derivaciones cuando un juez civil ordena protección especializada; la derivación implica generalmente alojamiento temporario, supervisión o evaluación por equipo interdisciplinario del propio Consejo — es decir, intervención estatal directa sobre la unidad familiar, no una mera evaluación.

### 2.4. Cadena de cálculo

**Pregunta:** *¿cuántos NNyA están bajo una decisión judicial que implica ruptura del vínculo familiar conviviente, según registros administrativos oficiales del año 2024?*

```text
3.182 legajos OVD 2024 con DENUNCIA_CON_NNYA_AF=SI          ← base (CSJN datos abiertos)
× (2.518 / 3.182) = 79,1% con ≥1 medida de ruptura familiar  ← 2.518 legajos
× 1,4 hijos por familia                                        ← INDEC 2022
= 3.525 NNyA
```

**Procedimiento de verificación independiente (5 pasos, sin código):**

1. Descargar `ddaa-ovd2024denuncias.csv` desde el portal [CSJN Datos Abiertos OVD 2024](https://datos.csjn.gov.ar/dataset/288e42e1-3070-447d-b268-f17e3246a854). Archivo de ~3 MB, N=9.840 filas, codificación **latin-1** (con separador `;`).
2. Filtrar la columna `DENUNCIA_CON_NNYA_AF = SI`. Resultado esperado: **3.182 legajos** (queda una fracción del universo total: 32% de las presentaciones OVD de 2024 involucraron al menos un NNyA).
3. Sobre esos 3.182 legajos, contar cuántos tienen ≥1 campo de los 10 listados arriba en `SI`. Resultado esperado: **2.518**.
4. `2.518 / 3.182 = 0,79069…` → redondear a **79,1%**. Multiplicar **2.518 × 1,4 hijos/familia** (INDEC, ver Parámetros en §2.3) → **3.525 NNyA**.
5. **Anclaje cruzado:** el [Informe NNyA 2024](https://www.ovd.gov.ar/ovd/novedades/detalle/12122) publica "3.182 presentaciones con NNyA afectados" y "4.474 medidas de protección ordenadas" — el primer número valida el paso 2 y el segundo cierra la consistencia con §2.1. La definición de cada campo `MEDIDA_*` y la regla de selección de la base están en `ovd-metodologia-datos-abiertos-bases-2024.pdf` (MD5 `B823C4FCCA64665654AD56942FE7CE50`, pp. 9-12). Para verificación cruzada a nivel de personas (no de legajos), utilizar el dataset hermano `ddaa-ovd2024personas.csv` (mismo portal); el total publicado 13.176 personas afectadas coincide con la fila de ese archivo.

{% include tags/calculo.html formula="2.518 legajos con ≥1 medida de ruptura familiar (79,1% de 3.182 CSJN OVD 2024) × 1,4 hijos (INDEC)" resultado="3.525 NNyA" nota="<span class='badge badge-observado' title='Microdatos públicos CSJN 2024'>◎ Observado</span> — microdatos CSJN 2024, sin supuestos" %}

**Resultado:** **3.525 NNyA** en causas OVD con al menos una medida de ruptura familiar ordenada en 2024. **Observado** (cadena aritmética sobre microdatos públicos).

#### Comparación con víctimas observadas (Marco A)

| | NNyA | Evidencia |
|---|---:|---|
| NNyA bajo medida de ruptura familiar (caso base) | **3.525** | <span class="badge badge-observado" title="Microdatos públicos CSJN 2024">◎ Observado</span> |
| Víctimas observadas de abuso sexual intrafamiliar | **1.819** | <span class="badge badge-derivado" title="3.219 × 56,5% UNICEF/Línea 137">◇ Derivado</span> |
| **Ratio (Marco A)** | **1,94 : 1** | |

**Lectura:** por cada víctima observada de abuso sexual intrafamiliar, hay aproximadamente **1,94 NNyA** en causas con al menos una decisión judicial de ruptura familiar — sin que esa decisión corresponda, en todos los casos, a victimización probada. El cociente debe leerse como un indicador de orden de magnitud, no como una equivalencia funcional entre ambas poblaciones.[^cron]

[^cron]: **Dimensión intertemporal — cronificación (anteriormente S-03).** El número 3.525 mide NNyA bajo una o más **cautelares vigentes** en 2024 dentro del flujo OVD. Las cautelares son, por diseño procesal (ley 26.485, art. 26), temporales y modificables. La pregunta sobre qué proporción de esas medidas se cronifica y deriva en ruptura permanente del vínculo, **sin exigencia de prueba pericial o médica de riesgo real**, es conceptualmente independiente y **no tiene dato público verificable** a la fecha de esta auditoría (cf. ítem de auditoría pendiente por falta de dato público verificable). Por esa razón se trata como dimensión temporal aparte, no como filtro multiplicativo dentro de la cadena: aplicarla como porcentaje del escenario base produciría un número no validable mezclando dos lecturas distintas (intervención vigente vs. daño permanente). Si en el futuro se identifica un dato oficial verificable sobre duración/resultado de cautelares (p. ej. registros de la CSJN, informes de defensorías de NNyA, o estadística de tribunales de familia), se incorporará como **escenario separado** `%cronificación × 3.525`, etiquetado según la calidad del dato. La **versión 1.0.0** incluía un 35% como **△ Supuesto** dentro del escenario Techo — ese parámetro se elimina del cálculo del caso base y se preserva solo aquí como referencia histórica pendiente de verificación.
