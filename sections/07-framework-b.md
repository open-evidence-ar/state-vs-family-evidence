## 7. Marco Analítico B — Intensidad de intervención y daño potencial por desvinculación
{: #marco-analitico-b}

### Pregunta

¿Cuál es la relación entre medidas cautelares observadas (4.474 en causas NNyA) y condenas penales identificables, ajustada por la proporción de denuncias falsas?

### Fundamentación

En muchos conflictos graves: denuncia → medida cautelar → investigación penal → eventual condena. Las medidas cautelares son intervención coercitiva temprana; las condenas, resolución definitiva. Las unidades **no son equivalentes** (medidas ≠ condenas; una condena puede involucrar varias víctimas).

El Marco B original solo comparaba medidas con condenas. Esta versión incorpora un **ajuste por denuncias falsas (FD)** que permite estimar cuántas medidas potencialmente carecían de fundamento real y cuántos NNyA pudieron resultar afectados por desvinculación injustificada.

### Fundamento del ajuste por FD

Si una proporción de las medidas cautelares se basó en denuncias falsas o infundadas, esos NNyA estuvieron expuestos a restricción de vínculo sin que existiera un hecho delictivo real detrás. El ajuste busca **aislar las medidas potencialmente justificadas** y **estimar el daño colateral** de las infundadas.

**Fuente del parámetro FD:** OVG 2026 — intervalo **8,9%** (nacional clasificado) a **61,5%** (techo Santa Fe) de FD-VG/VI sobre FD clasificadas. Ver §4.

### Capa 1 — Ratio bruto (medidas / condenas)

| Escenario penal | Condenas ref. | Ratio | Evidencia |
|---|---|---|---|---|
| Intrafamiliar NNyA bajo | **500** | 4.474 / 500 = **8,9 : 1** | <span class="badge badge-derivado" title="Aritmética reproducible sobre observados">◇ Derivado</span> |
| Intrafamiliar NNyA alto | **1.000** | 4.474 / 1.000 = **4,5 : 1** | <span class="badge badge-derivado" title="Aritmética reproducible sobre observados">◇ Derivado</span> |
| **Intrafamiliar NNyA central** | **750** | 4.474 / 750 = **6,0 : 1** | <span class="badge badge-derivado" title="Aritmética reproducible sobre observados">◇ Derivado</span> |
| RNR nacional (>2.000/año) | >2.000 | **< 2,2 : 1** | <span class="badge badge-derivado" title="Aritmética reproducible sobre observados">◇ Derivado</span> |
| UFEM central (≈2.884/año) | ≈2.884 | **1,55 : 1** | <span class="badge badge-observado" title="Dato directo de informe oficial">◎ Observado</span> (cruce RNR/SNIC) |
| Santa Fe 2025 | 354 | **12,6 : 1** | <span class="badge badge-observado" title="Dato directo de informe oficial">◎ Observado</span> |
| Formosa 2023 | 62 | 4.474 / 62 = **72,2 : 1** | <span class="badge badge-observado" title="Dato directo de informe oficial">◎ Observado</span> provincial |
| CePASI mínimo | 2 | **2.237 : 1** | <span class="badge badge-supuesto" title="Parámetro sin fuente directa">△ Supuesto</span> |
| Punto medio histórico (estimación CePASI) | 6 | 4.474 / 6 = **745,7 : 1** | <span class="badge badge-supuesto" title="Parámetro sin fuente directa">△ Supuesto</span> |

**Interpretación:** usando el denominador metodológicamente correcto (condenas intrafamiliares NNyA ~750/año), por cada condena hay **~6 medidas cautelares** en CABA. Los ratios más extremos (>2.000 y <2,2:1) corresponden a condenas totales sin filtrar por vínculo ni edad, sobrestimando el denominador en ~3×. Ver §5.2.

### Capa 2 — Ratio de medidas injustificadas por condena

{% include tags/calculo.html formula="Medidas potencialmente injustificadas = 4.474 × % FD | Ratio = Injustificadas / 750 condenas" %}

| Escenario FD | % FD | Medidas injustificadas | Ratio injustificadas/condena | Evidencia |
|---|---|---|---|---|
| Sin FD (piso) | 0% | 0 | **0 : 1** | — |
| **Nacional clasificado** | 8,9% | 398 | **0,53 : 1** | <span class="badge badge-derivado" title="Aritmética reproducible sobre observados">◇ Derivado</span> |
| Medio (MPF 2018) | 15% | 671 | **0,89 : 1** | <span class="badge badge-derivado" title="Aritmética reproducible sobre observados">◇ Derivado</span> |
| Jurisd. altas | 42% | 1.879 | **2,51 : 1** | <span class="badge badge-derivado" title="Aritmética reproducible sobre observados">◇ Derivado</span> |
| **Techo Santa Fe** | 61,5% | 2.752 | **3,67 : 1** | <span class="badge badge-observado" title="Dato directo de informe oficial">◎ Observado</span> |

> **Lectura:** en el escenario central (FD 8,9%, condenas 750), hay **0,53 medidas potencialmente injustificadas por cada condena intrafamiliar**.

#### Sensibilidad del denominador penal

| FD \ Condenas | RNR (>2.000) | Intrafamiliar alto (1.000) | Intrafamiliar central (750) | Intrafamiliar bajo (500) |
|---|---|---|---|---|
| 8,9% | 0,20 : 1 | 0,40 : 1 | **0,53 : 1** | 0,80 : 1 |
| 15% | 0,34 : 1 | 0,67 : 1 | **0,89 : 1** | 1,34 : 1 |
| 42% | 0,94 : 1 | 1,88 : 1 | **2,51 : 1** | 3,76 : 1 |
| 61,5% | 1,38 : 1 | 2,75 : 1 | **3,67 : 1** | 5,50 : 1 |

> **Lectura:** en el escenario central (FD 8,9%, condenas 750), hay **0,53 medidas potencialmente injustificadas por cada condena intrafamiliar**. Si la tasa de FD fuera la del techo Santa Fe (61,5%), habría **3,67 medidas injustificadas por condena**. La relación es monotónica creciente: a mayor FD, mayor el ratio de intervenciones sin fundamento penal.

### Capa 3 — Daño estimado por desvinculación

{% include tags/calculo.html formula="NNyA afectados por FD = 4.474 × % FD × 1,4 hijos (INDEC 2022)" %}

| Escenario FD | Medidas por FD | NNyA potencialmente afectados | Evidencia |
|---|---|---|---|---|
| Nacional (8,9%) | 398 | **557** | <span class="badge badge-derivado" title="Aritmética reproducible sobre observados">◇ Derivado</span> |
| Medio (15%) | 671 | **939** | <span class="badge badge-derivado" title="Aritmética reproducible sobre observados">◇ Derivado</span> |
| Jurisd. altas (42%) | 1.879 | **2.631** | <span class="badge badge-derivado" title="Aritmética reproducible sobre observados">◇ Derivado</span> |
| Techo Santa Fe (61,5%) | 2.752 | **3.853** | <span class="badge badge-derivado" title="Aritmética reproducible sobre observados">◇ Derivado</span> |

#### Evidencia internacional del daño por separación filial

| Hallazgo | Fuente | Relevancia |
|---|---|---|
| Separación padre-hijo ≥3 meses → depresión moderada-severa en adolescentes | Springer 2024 | Dosis-respuesta: duración importa |
| Niños en margen de ubicación foster (fuera Cook County): tasa de arresto adulta ~3× vs. niños que permanecen en hogar | Doyle (2007) WP 13291 — § Adult Arrests | Efecto causal (IV) |
| Remoción → menor rendimiento académico, peores relaciones sociales | Bald, Chyn et al. 2022 (JPE) | Niños jóvenes (<6 años) más afectados |
| 98,3% adultos reportan ≥1 conducta de alienación parental en infancia | Hine et al. 2026 (UK) | Prevalencia masiva no detectada |
| Solo 2 jurisdicciones EEUU requieren evaluar daño de remoción antes de decidir | Sankaran et al. 2020 | Sesgo sistémico hacia la separación |
| Niños en margen de ubicación foster (fuera Cook County): tasa de arresto adulta ~3× vs. niños que permanecen en hogar | Doyle (2007) WP 13291 — § Adult Arrests | Efecto causal (IV, investigación rota-cuasi-experimental) |
| Jóvenes encarcelados: −39pp graduación HS, +41pp prisión adulta a los 25 | Aizer & Doyle (2009) WP 19102 — p.3 (introducción) | Asignación aleatoria de jueces (IV) |
| Partida tardía del padre (6-14 años) → +conducta delictiva (efectos fijos entre hermanos) | Markowitz & Ryan 2016 (PMC5082431) | Efecto causal de pérdida de **un** progenitor (no foster care) |
| Repetición intergeneracional de conductas de alienación | Springer 2021 (13 estudios) | Efecto de largo plazo |

> **Nota de alcance:** las fuentes de esta tabla miden dos mecanismos distintos de separación filial. Doyle (2007), Bald, Chyn et al. (2022) y Aizer & Doyle (2009) estiman el impacto de la **remoción completa del hogar** (foster care o encarcelamiento): el niño es separado de ambos progenitores y colocado fuera del hogar. En cambio, Markowitz & Ryan (2016), Hine et al. (2026) y Springer (2021, 2024) miden la **pérdida de vínculo con un progenitor** — específicamente el padre— ya sea por partida, alienación o separación. Este segundo mecanismo es el más comparable a las cautelares argentinas documentadas en §2, donde el 66% de los denunciados es el padre y la intervención restringe su contacto sin remover al niño del hogar.

Si el ratio de FD-VG/VI es **8,9%** (estimador central nacional), el daño estimado por desvinculación es de **~557 NNyA**. Si sube al **15%** (estimación MPF 2018), son **~939 NNyA**. Este daño es **adicional** al que sufren los NNyA en causas justificadas donde el contacto con un progenitor agresor efectivamente representaba un riesgo.

La evidencia internacional (Doyle 2007 WP 13291; Aizer & Doyle 2009 WP 19102; BCHM 2021) muestra que la separación filial involuntaria y el encarcelamiento juvenil tienen efectos causales negativos medibles: ~3× arrestos adultos para niños en margen de foster placement (Doyle 2007, fuera de Cook County) y −39pp en graduación de high school / +41pp en prisión adulta a los 25 para jóvenes encarcelados (Aizer & Doyle 2009). En BCHM 2021 (tablas 2–5) los efectos documentados se concentran en rendimiento educativo infantil. Esto implica que **cada medida cautelar infundada tiene un costo esperado en bienestar infantil** que el sistema no está dimensionando.

### Capa 4 — Extrapolación territorial

| Referencia | Población | Factor vs CABA |
|---|---|---|
| CABA (base OVD) | 3,1M | 1× |
| PBA (solo RVF 2023: 327.905 medidas) | 17,5M | ~10× medidas |
| Nacional (tasa PBA) | 46,2M | **~15×** |

| Indicador | CABA | Nacional estimado |
|---|---|---|
| Marco A: NNyA / víctimas (Restricción) | 2,27 : 1 | **~34 : 1** |
| Medidas protección NNyA | 4.474 | **~67.000** |
| Marco B: medidas / condenas | 6,0 : 1 | **~89 : 1** |
| Marco B Capa 2: injustificadas (8,9% FD) / condena | 0,53 : 1 | **~7,9 : 1** |
| Marco B Capa 2: injustificadas (61,5% FD) / condena | 3,67 : 1 | **~55 : 1** |
| Daño (8,9% FD) — NNyA afectados | 557 | **~8.300** |
| Daño (61,5% FD) — NNyA afectados | 3.853 | **~57.500** |

**Interpretación:** el sesgo territorial no es neutral — **subestima sistemáticamente** la magnitud del fenómeno. Una extrapolación lineal sugiere que los ratios nacionales reales podrían ser ~15× superiores a los documentados en CABA. Los valores extrapolados son **orientativos** (asumen homogeneidad de tasas de intervención cautelar en todo el país, lo cual no está verificado) pero el sentido del sesgo es inequívoco.

### Limitación crítica

El **68% intrafamiliar** (UFEP 2017) tiene 8 años. El **15% condena/denuncia** (UFEM) mezcla todos los delitos sexuales, no solo intrafamiliar. El BGD reporta solo **6,2% condena** en causas resueltas. No hay un embudo nacional consolidado que cruce intrafamiliar × condena. El daño estimado en la Capa 3 es una **aproximación exploratoria**, no una medición directa.
