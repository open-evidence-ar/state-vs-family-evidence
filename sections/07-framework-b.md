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

> **Advertencia de dependencia del denominador.** Esta Capa documenta la sensibilidad de la razón a la elección del denominador penal. La cifra puntual 6,0:1 corresponde al escenario central (~750 condenas intrafamiliares NNyA/año, ver §5.3); pero el rango resultante del conjunto de denominadores disponibles cubre **tres órdenes de magnitud** (~1,55:1 hasta ~2.237:1) según se incluya o no el filtro intrafamiliar NNyA. Ningún denominador es "errado" en sí mismo — cada uno responde a una pregunta distinta. La lectura metodológica del Marco B debe hacerse sobre el **rango completo**, no sobre un valor puntual aislado.

> **Prevención metodológica: error de categoría y filtros imposibles.** El Marco B compara medidas cautelares amplias (que abarcan violencia psicológica, física, sexual, económica y verbal) con condenas por un subconjunto específico (abuso sexual intrafamiliar contra NNyA). Un lector podría argumentar que la comparación es un "error de categoría" porque el 95% de las causas NNyA involucran violencia psicológica y solo 9% violencia sexual (§2.1). Esta lectura omite tres hechos: **(a)** la OVD no desglosa medidas por tipo de violencia alegada, por lo que *no es factible* filtrar el numerador a solo medidas causadas por denuncias de abuso sexual — el dato simplemente no existe en registros públicos; **(b)** la matriz de sensibilidad de Capa 1 ya presenta denominadores que *no* filtran por tipo de violencia (UFEM ≈2.884: ratio 1,55:1; RNR >2.000: ratio <2,2:1), permitiendo al lector elegir el denominador que considere epistémicamente correcto; **(c)** el denominador intrafamiliar NNyA (~750) es el que mide condenas del subconjunto que se superpone con la intervención cautelar — las causas donde existe simultáneamente una denuncia civil con NNyA y un proceso penal. Usar un denominador sin filtro intrafamiliar (UFEM ≈2.884) multiplica condenas por delitos sexuales contra adultos que no corresponden al universo cautelar NNyA, *sobrestimando* el denominador relevante. El propósito del Marco B es medir la intensidad de la coerción estatal sobre familias con niños; el subconjunto condenatorio que intersecta ese universo es, por construcción, el intrafamiliar NNyA.

| Escenario penal | Condenas ref. | Ratio | Evidencia |
|---|---|---|---|
| Intrafamiliar NNyA bajo | **500** | 4.474 / 500 = **8,9 : 1** | <span class="badge badge-derivado" title="Aritmética reproducible sobre observados">◇ Derivado³</span> |
| Intrafamiliar NNyA alto | **1.000** | 4.474 / 1.000 = **4,5 : 1** | <span class="badge badge-derivado" title="Aritmética reproducible sobre observados">◇ Derivado³</span> |
| **Intrafamiliar NNyA central** | **750** | 4.474 / 750 = **6,0 : 1** | <span class="badge badge-derivado" title="Aritmética reproducible con anclas parciales">◇ Derivado³</span> |
| RNR nacional (>2.000/año) | >2.000 | **< 2,2 : 1** | <span class="badge badge-derivado" title="Aritmética reproducible sobre observados">◇ Derivado</span> |
| UFEM central (≈2.884/año) | ≈2.884 | **1,55 : 1** | <span class="badge badge-observado" title="Dato directo de informe oficial">◎ Observado</span> (cruce RNR/SNIC) |
| Santa Fe 2025 | 354 | 4.474 / 354 = **12,6 : 1** | <span class="badge badge-observado" title="Dato directo de informe oficial">◎ Observado</span> |
| Formosa 2023 | 62 | 4.474 / 62 = **72,2 : 1** | <span class="badge badge-observado" title="Dato directo de informe oficial">◎ Observado</span> provincial |
| CePASI mínimo | 2 | **2.237 : 1** | <span class="badge badge-supuesto" title="Parámetro sin fuente directa">△ Supuesto</span> |
| Punto medio histórico (estimación CePASI) | 6 | 4.474 / 6 = **745,7 : 1** | <span class="badge badge-supuesto" title="Parámetro sin fuente directa">△ Supuesto</span> |

**Interpretación:** usando el denominador metodológicamente correcto (condenas intrafamiliares NNyA ~750/año, derivado³), por cada condena hay entre **~4,5 y ~9 medidas cautelares** en CABA bajo los escenarios bajo y alto de §5.3, con **~6 como estimador central**. Los ratios más extremos como 1,55:1 (UFEM) ó <2,2:1 (RNR total) corresponden a condenas totales sin filtrar por vínculo ni edad, que **sobrestiman el denominador en ~3-4×** respecto del subconjunto correcto (condenas intrafamiliares NNyA que es donde se produce la intervención cautelar). El rango 12,6:1 (Santa Fe) a 72,2:1 (Formosa) documenta heterogeneidad territorial real pero no es techo nacional ni estimación central. Ver §5.3 para la derivación completa de los denominadores y la nota de consistencia interna sobre CePASI.

El término "central ~6" es **una conveniencia comunicativa**, no un punto de moda ni media del fenómeno: indica el valor medio entre ~500 (intrafamiliar NNyA bajo) y ~1.000 (intrafamiliar NNyA alto) asume aproximadamente 750 condenas/año. La lectura correcta del indicador exige considerar el rango completo ~1,55:1 – 12,6:1 (excluyendo outliers provinciales y supuestos extremos como CePASI).

### Capa 2 — Ratio de medidas injustificadas por condena

{% include tags/calculo.html formula="Medidas potencialmente injustificadas = 4.474 × % FD | Ratio = Injustificadas / 750 condenas" %}

| Escenario FD | % FD | Medidas injustificadas | Ratio injustificadas/condena | Evidencia |
|---|---|---|---|---|
| Sin FD (piso) | 0% | 0 | **0 : 1** | — |
| **Nacional clasificado** | 8,9% | 398 | **0,53 : 1** | <span class="badge badge-derivado" title="Aritmética reproducible sobre observados">◇ Derivado</span> |
| Medio (MPF 2018) | 15% | 671 | **0,89 : 1** | <span class="badge badge-derivado" title="Aritmética reproducible sobre observados">◇ Derivado</span> |
| Jurisd. altas | 42% | 1.879 | **2,51 : 1** | <span class="badge badge-derivado" title="Aritmética reproducible sobre observados">◇ Derivado</span> |
| **Techo Santa Fe** | 61,5% | 2.752 | **3,67 : 1** | <span class="badge badge-observado" title="Dato directo de informe oficial">◎ Observado</span> |

> **Lectura (rango completo):** el ratio `injustificadas/condena` varía entre **0,53 : 1** (FD nacional 8,9%, condenas 750) y **3,67 : 1** (FD techo Santa Fe 61,5%, condenas 750). Ninguno de los dos extremos es "el estimador"; ambos son puntos de un rectángulo de sensibilidad matricial 4×4 bajo ([tabla siguiente](#sensibilidad-del-denominador-penal)). El valor 0,53 no representa "la" cifra; es el escenario más conservador del rectángulo, no su moda.

#### Sensibilidad del denominador penal
{: #sensibilidad-del-denominador-penal}

| FD \ Condenas | RNR (>2.000) | Intrafamiliar alto (1.000) | Intrafamiliar central (750) | Intrafamiliar bajo (500) |
|---|---|---|---|---|
| 8,9% | 0,20 : 1 | 0,40 : 1 | **0,53 : 1** | 0,80 : 1 |
| 15% | 0,34 : 1 | 0,67 : 1 | **0,89 : 1** | 1,34 : 1 |
| 42% | 0,94 : 1 | 1,88 : 1 | **2,51 : 1** | 3,76 : 1 |
| 61,5% | 1,38 : 1 | 2,75 : 1 | **3,67 : 1** | 5,50 : 1 |

> **Lectura matricial:** la diagonal central (FD 8,9% → 61,5% con condenas 750) da **0,53 : 1 → 3,67 : 1**. Si la tasa de FD fuera la del techo Santa Fe (61,5%), habría **3,67 medidas injustificadas por condena**. La relación es monotónica creciente: a mayor FD, mayor el ratio de intervenciones sin fundamento penal. **Lectura rectangular completa:** la matriz describe **rango de sensibilidad**, no intervalo de confianza ni distribución de probabilidad. El punto (750 condenas, 8,9% FD) y el punto (750 condenas, 61,5% FD) son los anclajes conservador y techo de la Capa 2; todos los demás son combinaciones plausibles intermedias. La elección de uno u otro debe justificarse explícitamente en cualquier lectura pública del indicador.

### Capa 3 — Daño estimado por desvinculación

{% include tags/calculo.html formula="NNyA afectados por FD = 4.474 × % FD × 1,4 hijos (INDEC 2022)" %}

| Escenario FD | Medidas por FD | NNyA potencialmente afectados | Evidencia |
|---|---|---|---|---|
| Nacional (8,9%) | 398 | **557** | <span class="badge badge-derivado" title="Aritmética reproducible sobre observados">◇ Derivado</span> |
| Medio (15%) | 671 | **939** | <span class="badge badge-derivado" title="Aritmética reproducible sobre observados">◇ Derivado</span> |
| Jurisd. altas (42%) | 1.879 | **2.631** | <span class="badge badge-derivado" title="Aritmética reproducible sobre observados">◇ Derivado</span> |
| Techo Santa Fe (61,5%) | 2.752 | **3.853** | <span class="badge badge-derivado" title="Aritmética reproducible sobre observados">◇ Derivado</span> |

#### Proxy de ausencia paterna — evidencia del daño esperado

Este apartado documenta los indicadores de daño *esperable* en niños cuyo padre está ausente del hogar, extraídos de fuentes estadísticas oficiales y agregadores académicos que citan fuentes primarias trazables (U.S. Census Bureau, CDC, DHHS/Bureau of Census, OJJDP). El proxy se interpreta como una **cota superior probabilística** del daño agregado por la inducción estatal de monoparentalidad — no como estimación directa del efecto de cada cautelar individual.

| Dimensión de daño | Hallazgo en hogares sin padre | Fuente primaria citada | Evidencia |
|---|---|---|---|
| **Línea base poblacional** | 18,2 millones de niños (1 de cada 4) viven sin padre biológico, padrastro o padre adoptivo en EE. UU. | U.S. Census Bureau — *Living Arrangements of Children Under 18* (citado por NFI) | <span class="badge badge-observado" title="Dato directo de informe oficial">◎ Observado</span> |
| **Tendencia macro (1960–2023)** | Hogares monoparentales: 9% → 25% (casi triplicado); hogares sin padre: 11% → 25% (más que duplicado) | U.S. Census Bureau 2023 (citado por N-IUSSP) | <span class="badge badge-observado" title="Dato directo de informe oficial">◎ Observado</span> |
| **Sistema penal juvenil** | 85% de los jóvenes en prisión provienen de hogares sin padre — ~20× el promedio | Fulton County (Georgia) / Texas Dept. of Correction, 1992 (citado por Deeper Walk con ancla a Office of Juvenile Justice and Delinquency Prevention) | <span class="badge badge-derivado" title="Aritmética reproducible sobre observados">◇ Derivado</span> |
| **Trastornos conductuales** | 85% de niños con trastornos conductuales provienen de hogares sin padre | Centers for Disease Control (citado por Deeper Walk) | <span class="badge badge-derivado" title="Dato directo, atribución de fuente secundaria">◇ Derivado</span> |
| **Suicidio juvenil** | 63% de suicidios juveniles ocurren en jóvenes de hogares sin padre — ~5× el promedio | U.S. Department of Health and Human Services / Bureau of the Census (citado por Deeper Walk) | <span class="badge badge-derivado" title="Dato directo, atribución de fuente secundaria">◇ Derivado</span> |
| **Sistema de justicia juvenil** | 70% de jóvenes en instituciones estatales provienen de hogares monoparentales; la mayoría atravesó abandono parental, abuso de sustancias o disfunción familiar | Office of Juvenile Justice and Delinquency Prevention (citado por America First Policy Institute, sin cita primaria en página) | <span class="badge badge-derivado" title="Dato directo, atribución secundaria no verificada en origen">◇ Derivado</span> |

> **Tabla de equivalencia — Tratamiento A vs Tratamiento B:**
>
> | Dimensión | Tratamiento A — Hogar con padre presente | Tratamiento B — Exclusión judicial del padre (cautelar argentina) | Evidencia de daño en B |
> |---|---|---|---|
> | Pobreza | Línea base Census (12% pobreza en familias con pareja casada) | Familias monoparentales femeninas: ~44% pobreza (Census), 4×–5× según jurisdicción | Multiplicador 4× AFPI (sin cita primaria en página; cota informativa) |
> | Sistema penal juvenil | Línea base | 85% de jóvenes presos provienen de hogares sin padre | Fulton Co. GA / Texas DOC 1992 |
> | Trastornos conductuales | Línea base | 85% de casos provienen de hogares sin padre | Centers for Disease Control |
> | Suicidio juvenil | Línea base | 63% provienen de hogares sin padre (~5× el promedio) | DHHS / Bureau of Census |
> | Sistema justicia juvenil | Línea base | 70% provienen de hogares monoparentales | OJJDP (atribución secundaria) |
>
> **Lectura del proxy:** si una fracción significativa de las medidas cautelares documentadas en §2 terminan produciendo **monoparentalidad efectiva** (hogar con la madre, sin contacto paterno), el riesgo esperado que el niño argentino enfrenta no es cero — es el mismo riesgo poblacional que miden las estadísticas norteamericanas de ausencia paterna. **Esto no afirma que cada niño bajo cautelar sufrirá cada uno de estos daños**: afirma que el *odds ratio* poblacional es el documentado arriba, y que el Estado que induce esa ausencia por vía judicial no está midiendo el resultado.

> **Nota sobre la calidad de las fuentes (v1.0.0):** las estadísticas de ausencia paterna usadas en este apartado han circulado durante décadas en literatura de promoción de la paternidad y *advocacy* institucional. La auditoría fuente por fuente realizada para esta versión arrojó el siguiente estado:
>
> - **Verificadas con atribución primaria directa:** "18,2 millones / 1 en 4" (U.S. Census Bureau vía NFI), "9%→25%" (U.S. Census Bureau 2023 vía N-IUSSP), "85% jóvenes en prisión" (Fulton County Georgia / Texas DOC vía Deeper Walk), "85% trastornos conductuales" (CDC vía Deeper Walk), "63% suicidios juveniles" (DHHS / Bureau of Census vía Deeper Walk).
> - **Verificadas en página pero sin cita primaria en la propia página:** "70% instituciones juveniles" (citada por America First Policy Institute; el fact-sheet de AFPI no incluye enlaces ni notas al pie para esta cifra — atribución a OJJDP tomada del compendio Deeper Walk).
> - **Atribución no trazada independientemente:** los multiplicadores exactos "4× pobreza" y "5× suicidios" provienen de cadenas de atribución secundarias (AFPI, Deeper Walk) que citan agencias federales sin publicación específica localizable; la dirección del efecto está replicada en múltiples fuentes independientes, la magnitud exacta no. **Se conservan como cota informativa, no como cifra de auditoría.**
>
> **Por qué se usan pese a la cautela:** el objetivo de la Capa 3 es dimensionar el *orden de magnitud* del daño esperado por la inducción estatal de monoparentalidad, no producir una estimación punto-a-punto con datos primarios argentinos. La ausencia de datos públicos argentinos sobre outcomes de cautelares (§9.10) obliga a este ejercicio de *benchmarking* internacional. El informe trata las cifras como **probabilidad condicional poblacional**, no como proyección por niño individual.

> **Mecanismo interpretativo — por qué la inducción de ausencia paterna produce este tipo de daño:**
>
> **Mecanismo 1 — Inducción de monoparentalidad efectiva:** la cautelar argentina de exclusión del padre del hogar produce, en los hechos, un hogar funcionalmente análogo al "fatherless household" definido por U.S. Census Bureau (padre biológico, padrastro o adoptivo ausente del hogar). El niño permanece en el hogar con la madre; el padre es excluido por resolución judicial y no convive; el contacto puede estar prohibido o restringido. Esta estructura se corresponde con el **66% de denunciados que son el padre** (§2) — y el subconjunto afectado es por construcción una población inducida de monoparentalidad.
>
> **Mecanismo 2 — Pérdida de vínculo con un progenitor (Markowitz & Ryan, Hine, Springer):** Markowitz & Ryan (2016) y Hine et al. (2026) miden la **pérdida de vínculo con un progenitor** — específicamente el padre — ya sea por partida, alienación o separación. Markowitz & Ryan muestran que la **edad de la separación modera** el efecto: partida tardía (6–14) aumenta conducta delictiva por reducción de monitoreo parental; partida temprana no muestra asociación con depresión ni conducta problemática. Hine et al. documentan que el 98,3% de adultos reporta ≥1 conducta de alienación parental en su infancia (exposición), mientras que la tasa clínica de alienación (rechazo de contacto + *splitting* psicológico) es 2,9%–3,5%. El presente informe usa la cifra 98,3% como evidencia de **no detección institucional** de un fenómeno extendido, no como prueba de epidemia clínica.
>
> **Mecanismo 3 — Separación estructural prolongada (Li et al. 2024):** el estudio *left-behind children* en China rural documenta que separaciones ≥3 meses se asocian con depresión moderada-severa en adolescentes (dosis-respuesta). No es directamente equivalente a cautelares argentinas (separación supervisada por juzgado, contexto de conflicto familiar), pero la cota de duración **refuerza la recomendación** de revisión periódica con plazos fijos (§11 recomendación de revisión periódica con plazos fijos): si la cautelar se cronifica más allá de 3 meses sin revisión probatoria, el riesgo de daño psicológico documentado por Li et al. deja de ser descartable.
>
> **Contra-evidencia — efecto protector de la separación en abuso severo:** Bald, Chyn et al. (2022) documentan un efecto **protector** de la remoción del hogar en niñas menores de 6 años en contextos de abuso severo (+1,33 DE en test estandarizados, −22,8 pp en repetición de grado). Esto implica que **la separación puede ser la decisión correcta en casos individuales extremos**, y que el daño agregado del que habla la Capa 3 aplica al subconjunto de cautelares que excluyen al padre *sin* justificación probatoria robusta. El informe NO interpreta cada exclusión paterna como daño cierto: la analogía con las estadísticas norteamericanas describe un **riesgo poblacional esperado**, no un destino por niño.

Si el ratio de FD-VG/VI es **8,9%** (estimador central nacional), el daño esperado por inducción de monoparentalidad es de **~557 NNyA**. Si sube al **15%** (estimación MPF 2018), son **~939 NNyA**. Si se aplica el techo Santa Fe de **61,5%**, son **~3.853 NNyA**. Este daño es **adicional** al sufrimiento de NNyA en causas justificadas donde el contacto con un progenitor agresor efectivamente representaba un riesgo — y presupone que la fracción "inducida sin justificación probatoria" tiene la misma composición demográfica que el total, lo cual no está verificado.

La evidencia de la Capa 3 indica que la inducción estatal de monoparentalidad (vía exclusión judicial del padre sin base probatoria robusta) somete al NNyA a un **perfil de riesgo poblacional** asociado con: 85% de jóvenes presos sin padre, 85% de trastornos conductuales en hogares sin padre, 63% de suicidios juveniles en hogares sin padre, 70% de jóvenes en instituciones estatales. Estos indicadores — replicados a través de bases de datos federales independientes de EE. UU. (Census, CDC, DHHS, OJJDP) — describen una asociación estadística robusta en poblaciones transversalmente comparables, aunque no permiten una traspolación directa caso-por-caso. **El sistema argentino no está midiendo outcomes de las cautelares (§9.10)** y por tanto no puede refutar esta asociación con datos propios.

### Capa 4 — Extrapolación territorial

| Referencia | Población | Factor vs CABA |
|---|---|---|
| CABA (base OVD) | 3,1M | 1× |
| PBA (RVF 2023: 327.905 medidas combinadas Familia + Paz) | 17,5M | ~5,6× población (~13× tasa per cápita) |
| Nacional (tasa PBA) | 46,2M | **~15×** |

| Indicador | CABA | Nacional estimado |
|---|---|---|
| Marco A: NNyA / víctimas (caso base observado, CABA↔CABA) | 5,46 : 1 | **~80 : 1** |
| Marco A: NNyA / víctimas (caso base observado, CABA↔Nacional) | 1,94 : 1 | **~29 : 1** |
| Medidas protección NNyA | 4.474 | **~67.000** |
| Marco B: medidas / condenas | 6,0 : 1 | **~89 : 1** |
| Marco B Capa 2: injustificadas (8,9% FD) / condena | 0,53 : 1 | **~7,9 : 1** |
| Marco B Capa 2: injustificadas (61,5% FD) / condena | 3,67 : 1 | **~55 : 1** |
| Daño (8,9% FD) — NNyA afectados | 557 | **~8.300** |
| Daño (61,5% FD) — NNyA afectados | 3.853 | **~57.500** |

**Interpretación:** el sesgo territorial no es neutral — **subestima sistemáticamente** la magnitud del fenómeno. Una extrapolación lineal sugiere que los ratios nacionales reales podrían ser ~15× superiores a los documentados en CABA. Los valores extrapolados son **orientativos** (asumen homogeneidad de tasas de intervención cautelar en todo el país, lo cual no está verificado) pero el sentido del sesgo es inequívoco.

### Limitación crítica

El **68% intrafamiliar** (UFEP 2017) tiene 8 años. El **15% condena/denuncia** (UFEM) mezcla todos los delitos sexuales, no solo intrafamiliar. El BGD reporta solo **6,2% condena** en causas resueltas. No hay un embudo nacional consolidado que cruce intrafamiliar × condena. El daño estimado en la Capa 3 es una **aproximación exploratoria**, no una medición directa.
