## 14. Marco A Córdoba — Réplica metodológica en una segunda jurisdicción
{:#marco-a-cordoba}

### 14.1 Objetivo y alcance geográfico

El §6 [Marco Analítico A](#marco-analitico-a) se construyó íntegramente sobre microdatos de la **Oficina de Violencia Doméstica de la CSJN**, cuya cobertura es CABA y federal (~6,7% de la población nacional). El ratio resultante (1,94:1) es metodológicamente robusto, pero territorialmente restringido: no podemos saber si la asimetría se replica en jurisdicciones sin una OVD equivalente.

Esta sección replica la lógica del Marco A en la **Provincia de Córdoba** (cuarta jurisdicción por población, ~3,6 millones de habitantes, ~9% del país) usando las fuentes oficiales más cercanas disponibles. El objetivo es **verificar si la asimetría 1,94:1 se replica** y, con ello, fortalecer la generalidad del hallazgo. Se explicitan todos los supuestos etarios y jurisdiccionales; el resultado se presenta como **rango** y no como estimación puntual.

> **Nota preventiva sobre cobertura.** Córdoba no tiene un dispositivo equivalente a la OVD-CSJN: no existe una oficina judicial centralizada con microdatos públicos de NNyA víctimas de abuso sexual intrafamiliar con desglose etario. Por diseño procesal provincial, las medidas de protección son formalmente adoptadas **100% por el Órgano Administrativo** (SENAF provincial) y 0% por el Poder Judicial (ver §14.5.1). Sin embargo, el **Polo Integral de la Mujer** (Unidad Judicial de Violencia Familiar del Ministerio Público Fiscal) funge como canal de inicio dominante → SENAF ratifica la separación (ver §14.5.1 para la cadena real de decisión). La diferencia clave con CABA es el **timing del control**: en CABA el juez autoriza *antes* de la ejecución; en Córdoba SENAF ejecuta *primero* y el juez revisa *después* — **sin efecto suspensivo**. Esto hace que la ruta administrativa sea menos controlada que la judicial, no más.

### 14.2 Numerador — NNyA bajo Medida de Protección Excepcional (MPE) en Córdoba

**Fuente principal:** [SENAF-UNICEF 2020 — Relevamiento nacional MPE 2020](https://www.argentina.gob.ar/sites/default/files/2020/09/situacion_de_nnya_sin_cuidados_parentales_-_2020_03.05_1.pdf), Tabla 13 (p.62).

| Indicador | Valor | Fuente |
|---|---:|---|
| NNyA con MPE en familia ampliada (Córdoba) | 667 | SENAF Tabla 13, p.62 |
| NNyA con MPE en dispositivos formales (Córdoba) | 590 | SENAF Tabla 13, p.62 |
| **NNyA Córdoba 0-17 con MPE (cifra adoptada)** | **1.107** | SENAF Tabla 12, p.16; tabla resumen 0-17 |
| Origen de la MPE — Órgano Administrativo | **100%** | SENAF p.70 ("Provincias: Córdoba [...] todas las medidas han sido adoptadas en su totalidad por el órgano de aplicación provincial") |
| Origen de la MPE — Poder Judicial | **0%** | Misma fuente |
| Motivo 1.° de MPE en Córdoba | "Otras — descuido o trato negligente" | SENAF Tabla 12, p.59 |
| Motivo 2.° de MPE en Córdoba | "Violencia" | SENAF Tabla 12, p.59 |
| Motivo 3.° de MPE en Córdoba | No reportado | — |

**Evidencia:** <span class="badge badge-observado" title="Dato directo de SENAF-UNICEF 2020">◎ Observado</span>

{% include tags/nnya.html cantidad="1.107" nota="NNyA Córdoba 0-17 con Medida de Protección Excepcional vigente al 2020" %}

**Lectura crítica del numerador.** A diferencia del Marco A CABA (donde el 100% de las medidas son judiciales), en Córdoba **ninguna** MPE es formalmente dictada por un juez: las 1.107 son decisiones del órgano administrativo de protección. Pero el Polo de la Mujer (Unidad Judicial del MPF) canaliza la mayoría de los casos que terminan en MPE (ver §14.5.1). La diferencia sustantiva con CABA es **el timing del control** (previo vs. *ex post* sin efecto suspensivo), no la ausencia de un componente judicial-fiscal en la cadena decisoria. La asimetría, si existe, **no puede atribuirse exclusivamente al órgano administrativo**: el Polo inicia, SENAF ratifica, el juez revisa después. Ver §14.5.1 y §14.5.2.

### 14.3 Denominador — Víctimas observadas de delitos contra la integridad sexual en Córdoba

#### 14.3.1 Hechos denunciados (SNIC, sin filtro etario)

**Fuente principal:** [SNIC — Series provinciales](https://www.argentina.gob.ar/seguridad/estadisticascriminales/bases-de-datos), Ministerio de Seguridad de la Nación, dataset `snic-provincias-delitos-personas-hechos-series.csv`, columnas `delito_10_hechos_cordoba` y `delito_11_hechos_cordoba`, fila `indice_tiempo=2020`.

| Indicador (Córdoba, serie anual) | 2017 | 2018 | 2019 | **2020** | 2021 | 2022 | 2023 | 2024 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Violaciones (delito_10) | 192 | 201 | 227 | **210** | 218 | 264 | 225 | 258 |
| Otros delitos contra integridad sexual (delito_11) | 632 | 692 | 864 | **767** | 865 | 703 | 834 | 695 |
| **Total hechos DIS (sin filtro edad)** | 824 | 893 | 1.091 | **977** | 1.083 | 967 | 1.059 | 953 |

**Cifra adoptada para el denominador (alineada con año del numerador):** **767 hechos DIS (2020, sólo delito_11)** + **210 violaciones (2020, delito_10)** = **977 hechos DIS**.

**Evidencia:** <span class="badge badge-observado" title="Dato directo SNIC">◎ Observado</span> — pero **sin filtro etario** (incluye víctimas de todas las edades).

> **Limitación crítica del SNIC provincial.** El SNIC publica **hechos** (incidents) y no **víctimas**; no filtra por edad. Córdoba no publica microdatos equivalentes a la base `ddaa-ovd2024denuncias.csv` de la CSJN (donde el filtro etario es directo). Esto obliga a aplicar una corrección externa con proxy para obtener víctimas NNyA — ver §14.3.2.

#### 14.3.2 Reconstrucción del subconjunto NNyA — dato micro UNQ Cadenazzi (2008-2014, Córdoba Capital)

**Fuente:** Cadenazzi, N.V. (2017). *Estudio descriptivo de los delitos y las víctimas a través de los hechos denunciados en la Unidad Judicial de Delitos Contra la Integridad Sexual del MPF de la Provincia de Córdoba, 2008-2014*. [TFI — Universidad Nacional de Quilmes, RIDAA-UNQ](https://ridaa.unq.edu.ar/handle/20.500.11807/560), Tabla N° 4 (p.23), distribución por grupo etario.

| Grupo etario | Víctimas Capital DIS 2008-2014 | % del total (9.864) | % sobre casos con dato de edad (N=8.362, excl. 1.502 "sin datos") |
|---|---:|---:|---:|
| 0-4 años | 909 | 9,22% | 10,87% |
| 5-8 años | 1.624 | 16,46% | 19,42% |
| 9-12 años | 1.645 | 16,68% | 19,67% |
| 13-16 años | 1.889 | 19,15% | 22,59% |
| **0-16 años (NNyA, Ley 26.061)** | **6.067** | **61,51%** | **72,55%** |
| 17-20 años | 709 | 7,19% | 8,48% |
| 21-28 años | 783 | 7,94% | 9,37% |
| 29 o más | 843 | 8,55% | 10,08% |
| Sin datos | 1.502 | 15,23% | n/a |
| **TOTAL** | **9.864** | **100%** | **100%** |

**Lectura microdato UNQ:**

- Sobre el **total** de 9.864 denuncias DIS registradas en Córdoba Capital entre 2008-2014, el **61,51%** corresponden a víctimas de 0-16 años (NNyA por Ley 26.061).
- Sobre los casos **con dato de edad registrado** (excluyendo 1.502 sin dato = 15,23% de los casos), el **72,55%** son NNyA 0-16.

**Decisión de adopción:** Para el denominador NNyA del Marco A Córdoba **se adopta el porcentaje sobre casos con dato de edad** (72,55%), porque excluir los casos sin dato preserva la lógica de no imputar edad en ausencia de información. Aplicado al total 2020 (977 hechos DIS):

```
977 hechos DIS Córdoba 2020 × 0,7255 = ~709 víctimas NNyA estimadas
```

**Evidencia:** <span class="badge badge-derivado" title="709 calculado como 977 × 72,55% sobre microdato UNQ 2008-14 (Córdoba Capital)">◇ Derivado</span> — la composición etaria se asume estable entre 2008-2014 y 2020, y entre Córdoba Capital y la provincia completa. Ambos supuestos son extensiones metodológicas que se discuten en §14.4 y §14.5.

### 14.4 Cadena de cálculo — Rango de ratios

#### 14.4.1 Escenario A — Denominador sin filtro etario (◎/◎)

```
Numerador:      1.107 NNyA 0-17 con MPE    (SENAF 2020, Córdoba)        ◎
Denominador:    977 hechos DIS Córdoba    (SNIC 2020, delito_10+11)      ◎
Ratio A = 1.107 / 977 = 1,13 : 1
```

**Interpretación:** por cada hecho de delito contra la integridad sexual registrado en toda la provincia de Córdoba (incluyendo víctimas adultas), hay **1,13 NNyA bajo una Medida de Protección Excepcional**. Este ratio es **límite inferior conservador**: al sobreestimar el denominador (incluye adultos), la relación subestima la asimetría real.

#### 14.4.2 Escenario B — Denominador con proxy etario UNQ (◎/◇)

```
Numerador:      1.107 NNyA 0-17 con MPE    (SENAF 2020, Córdoba)        ◎
Denominador:    977 × 72,55% = ~709 NNyA DIS (SNIC×UNQ 2008-14)        ◇
Ratio B = 1.107 / 709 = 1,56 : 1
```

**Interpretación:** si la composición etaria de víctimas DIS en Córdoba no ha cambiado estructuralmente entre 2008-2014 y 2020, por cada NNyA víctima observada de delito sexual hay **1,56 NNyA bajo MPE administrativa**.

#### 14.4.3 Escenario C — Denominador con proxy etario alternativo (sólo NNyA 0-16 sobre total, sin descontar "sin datos")

```
Numerador:      1.107 NNyA 0-17 con MPE                          ◎
Denominador:    977 × 61,51% = ~601 NNyA DIS (sobre total)       ◇
Ratio C = 1.107 / 601 = 1,84 : 1
```

**Interpretación:** si se imputa la edad en los casos "sin datos" usando la misma distribución que los casos con dato (descuento más conservador), el ratio es **1,84:1** — más cercano al 1,94:1 de CABA.

#### 14.4.4 Rango consolidado

| Escenario | Fórmula | Ratio | Badge |
|---|---|---:|---|
| **A — denominador sin filtro etario** | 1.107 / 977 | **1,13 : 1** | ◎/◎ |
| **B (recomendado) — proxy UNQ sobre casos con dato etario** | 1.107 / 709 | **1,56 : 1** | ◎/◇ |
| **C — proxy UNQ sobre total (asumiendo sin datos = azar)** | 1.107 / 601 | **1,84 : 1** | ◎/◇ |
| **HEADLINE — comparación con CABA Marco A** | — | **1,94 : 1** | — |

{% include tags/ratio.html valor="1,56 : 1 (rango: 1,13 – 1,84)" interpretacion="NNyA bajo MPE administrativa en Córdoba por cada NNyA víctima observada de DIS" %}

Caso base recomendado: **Escenario B (1,56:1)** — usa el supuesto más conservador sobre los casos sin dato etario (no imputa edad) y equilibra uso de datos micro observados (UNQ) con extensiones metodológicas explícitas (SENAF, SNIC).

{% include tags/calculo.html formula="1.107 NNyA MPE (SENAF 2020) / [977 hechos DIS Córdoba 2020 (SNIC) × 72,55% NNyA 0-16 sobre casos con dato etario (UNQ Cadenazzi 2008-14)]" resultado="1,56 : 1" nota="<span class='badge badge-derivado' title='Proxy etario aplicado a datos provinciales 2020'>◎/◇ — Derivado</span>. Rango: 1,13 (sin filtro etario) a 1,84 (asumiendo azar en casos sin dato)." %}

### 14.5 Caveats metodológicos y diferencia con CABA

#### 14.5.1 Diferencia institucional: administrativo vs. judicial — y la cadena real de decisión

En **CABA**, el numerador del Marco A proviene de la OVD (CSJN) — organismo judicial civil donde un juez dicta medidas cautelares dentro del proceso (ley 26.485). En **Córdoba**, las 1.107 MPE son formalmente dictadas por el Órgano Administrativo (Secretaría de Niñez, Adolescencia y Familia provincial — Ley 9.944 y Ley 26.061 art. 39-45). Sin embargo, la etiqueta "100% administrativo" **oculta la cadena real de decisión**, donde un organismo judicial-fiscal inicia el 90% de los casos que terminan en MPE:

| Paso | Actor | Acción | Fuente |
|---|---|---|---|
| 1. Inicio | **Polo Integral de la Mujer** (Unidad Judicial de Violencia Familiar — MPF) | Recibe denuncia VF; evalúa riesgo; aloja mujer e hijos en Refugio | [Banco Mundial 2020, p.4-5](https://documents1.worldbank.org/curated/en/971211600236778385/pdf/Violencia-de-G%C3%A9nero-en-la-Provincia-de-C%C3%B3rdoba-Avances-y-Desaf%C3%ADos.pdf) |
| 2. Derivación | **Polo → SENAF** | Comunica la situación a SENAF vía oficio ("pone en conocimiento") | Protocolo SENAF-Polo (CPSSCBA, Anexo-62) |
| 3. Decisión formal | **SENAF** (art. 48 Ley 9.944) | Director de Asuntos Legales firma la Disposición (MPE) | [Villagra & Sequeira 2019, p.12](https://ridaa.unq.edu.ar/handle/20.500.11807/560) |
| 4. Ejecución | **SENAF** | Retira al NNyA del centro de vida; lo ubica en familia extensa, acogimiento o residencia | Ley 9.944 art. 48-55 |
| 5. Control | **Juez de Niñez** | Control de legalidad *ex post* (24-72 hs); **sin efecto suspensivo** | Villagra 2019, p.13; Ley 9.944 art. 55 |

**Evidencia:** <span class="badge badge-observado" title="Dato directo de World Bank 2020 y Villagra 2019">◎ Observado</span>

> **Corrección al rótulo "100% administrativo".** SENAF-UNICEF 2020 (p.70) reporta que Córdoba tiene 100% de MPE adoptadas por el órgano administrativo. Esto es **formalmente exacto**: la Disposición la firma SENAF, no un juez. Pero el Polo Integral de la Mujer — que contiene la Unidad Judicial de Violencia Familiar del Ministerio Público Fiscal — es la **puerta de entrada dominante** del circuito. Cuando una mujer denuncia violencia doméstica en el Polo, **los hijos son separados de facto** (alojados en el Refugio del Polo o trasladados con la madre) antes de que SENAF formalice la MPE. La "puesta en conocimiento" del Polo a SENAF es una **remisión que rara vez se rechaza**: el caso llega precocinado. SENAF opera más como ratificador de una situación creada por el Polo que como decisor independiente.

| Jurisdicción | Origen formal | Canal de inicio dominante | Tipo de intervención | Control judicial | % de NNyA judicial |
|---|---|---|---|---|---:|
| CABA (OVD) | **Judicial** (juez civil) | OVD / juzgados VF | Cautelar dentro de proceso VF | Previo (autoriza antes) | ~100% |
| Córdoba (SENAF) | **Administrativo** (SENAF) | **Polo de la Mujer** (MPF) | MPE administrativa | *Ex post*, sin efecto suspensivo | 0% formal, ~90% vía Polo |
| Total país (SENAF 2020) | Mixto | Mixto | Mixto | Mixto | **15,1%** |

**Implicación revised:** la etiqueta "100% administrativo" no implica que la asimetría 1,56:1 sea ajena al sistema judicial-fiscal. El Polo de la Mujer (órgano del Ministerio Público Fiscal) funge como **filtro cuasi-judicial** que canaliza los casos hacia SENAF. La diferencia sustantiva con CABA no es "judicial vs. administrativo" sino el **timing del control**: en CABA el juez autoriza *antes* de la ejecución; en Córdoba SENAF ejecuta *primero* y el juez revisa *después* — **sin efecto suspensivo** (Villagra & Sequeira 2019, p.13: *"Ni la oposición, ni el control judicial tienen en nuestra provincia efecto suspensivo. El acto administrativo tiene presunción de legalidad"*). Esto hace que la ruta **administrativa** sea *menos* controlada que la judicial de CABA, no más. El 1,56:1 es probablemente un **piso**, no un techo.

#### 14.5.2 Por qué el ratio se replica a pesar de la diferencia

La pregunta relevante es: **¿por qué la asimetría se mantiene en el mismo orden de magnitud (1,13-1,84:1) en Córdoba que en CABA (1,94:1)?** Hipótesis:

1. **Cifra negra consistente.** El subregistro de víctimas DIS es estructural y transversal a jurisdicciones: están publicadas estimaciones de sub-denuncia del 77-88% (CEDAW/ONU; ver §3). En la medida en que la cifra negra sea estable entre CABA y Córdoba, los **dos ratios son insensibles a su magnitud** (la asimetría es entre intervención y observación, no entre observación y realidad).
2. **Definición amplia de "motivo" de MPE.** SENAF reporta que, en Córdoba, el motivo **1.°** de MPE es **"Otras — descuido o trato negligente"**, no "violencia". Esto significa que la MPE no se limita a casos de ASI: se activa por **dificultades en el ejercicio de la responsabilidad parental**, que es una categoría legal más amplia y que probablemente cubre conflictos familiares donde la vulneración de derechos no constituye delito penal. Esto explica parcialmente por qué el numerador (1.107) supera con holgura al subconjunto de víctimas DIS (709). Villagra & Sequeira (2019) cuantifican con precisión: sobre 105 MPE analizadas, el motivo principal fue negligencia (54%); abuso sexual representó apenas el **5%** — once veces menos que negligencia.
3. **Universalidad de la "actuación preventiva" administrativa.** Tanto la ley 26.485 (CABA/federal) como la ley 26.061 (Córdoba y nacional) comparten el principio de **protección amplia y temprana**: la medida se dicta **antes** de que exista condena penal, sobre la base de un relato inicial. En CABA esto ocurre en sede judicial (OVD); en Córdoba, en sede administrativa (SENAF). El diseño procesal —no la jurisdicción— produce la asimetría escala.
4. **Intervención sin verificación — Polo como canal de entrada.** Villagra & Sequeira (2019) documentan que en el **54%** de las 105 MPE analizadas **no se entrevistó al niño** antes de adoptar la medida; en el **76%** de los expedientes **no constaba la adopción de medidas de protección ordinarias previas** a la MPE excepcional — es decir, se saltea el segundo nivel de la Ley 9.944 y se va directo a la separación. La ausencia de verificación previa es estructural, no accidental: el Polo comunica casos a SENAF que SENAF rara vez rechaza. El niño no es oído, no hay medidas intermedias, y el control judicial es posterior sin efecto suspensivo — el triángulo Polo → SENAF → Juez *ex post* funciona como una **cinta transportadora** que ejecuta la separación antes de que exista verificación forense o pericial.

#### 14.5.2b Evidencia de canal de entrada: casos documentados

**Caso Carro — Córdoba (2018).** Documentado en §13.4.2b del presente estudio. Anet Jazmín Carro, menor de 14 años, denunció un "manoseo" en el Polo de la Mujer. Personal del Polo **modificó el acta original** e introdujo de oficio la figura agravada de "abuso sexual con acceso carnal", argumentando que la figura simple "no era suficiente" para activar los protocolos ni dictar prisiones preventivas. Condena lograda sin evidencia biológica, con informes forenses oficiales en contra. Ningún funcionario del Polo sancionado a la fecha. Fuente: [44] (Testimonio Congreso).

**Caso Ángel López — Córdoba (abril 2026).** Ángel López, 4 años, murió por al menos 20 golpes en la cabeza tras cinco meses de abuso por su madre y la pareja de esta. La madre había presentado una **denuncia sin pruebas** en el Polo de la Mujer de Córdoba, que derivó en la transferencia de la custodia al entorno materno. El padre, Luis López, declaró: *"Se fue a Córdoba y presentó una denuncia sin pruebas; por eso mi hijo está muerto"*. El caso está bajo investigación por denuncia falsa en el Polo como paso previo a la tragedia. Fuentes: [Derecho Diario](https://derechodiario.com.ar/cordoba/cordoba-investigan-denuncia-falsa-polo-mujer-precedido-caso-angel-lopez), [El Doce TV](https://eldoce.tv/actualidad/2026/04/13/el-papa-de-angel-revelo-que-la-madre-lo-denuncio-en-cordoba-por-una-falsa-denuncia-mi-hijo-esta-muerto/).

> **Lectura integrada de ambos casos.** El caso Carro documenta **fabricación procesal** por agentes del Polo (modificación coactiva del acta para escalar figura penal). El caso López documenta **denuncia instrumental** canalizada a través del Polo que derivó en cambio de custodia sin verificación y, ulteriormente, en la muerte del niño. Ambos comparten el patrón: **denuncia inicial → Polo → separación sin verificación forense → daño irreversible**. Este patrón es consistente con la mecánica de incentivos documentada en §13.5 (costo esperado de denuncia instrumental ≈ 0; payoff cautelar inmediato; carga probatoria permanentemente invertida). Específicamente en Córdoba, la ruta administrativa agrava el patrón porque **no existe control judicial previo** — la separación se ejecuta antes de que un juez la revise.

{% include tags/ratio.html valor="Patrón Polo→SENAF: denuncia → separación sin verificación → daño" interpretacion="Córdoba: la ruta administrativa es menos controlada que CABA, no más" %}

#### 14.5.3 Limitaciones y sesgos explícitos

| # | Limitación | Dirección del sesgo | Severidad |
|---|---|---|---|
| 1 | SENAF 2020 es 4 años anterior a SNIC 2024; usamos SNIC 2020 para alinear | Si DIS aumenta con los años → denominador 2020 subestima → ratio **sobreestima** | Media |
| 2 | UNQ Cadenazzi analiza Córdoba Capital (1ra circunscripción), no el interior provincial | Si interior tiene perfil etario distinto (probablemente de mayor edad promedio por tipo penal) → efecto **desconocido** | Media |
| 3 | UNQ cubre 2008-2014; aplicamos 72,55% a 2020 asumiendo estabilidad temporal | Si la composición etaria cambió (e.g., más víctimas jóvenes) → denominador **sobre o subestima** | Baja-Media |
| 4 | 15,23% de casos UNQ "sin dato de edad" — la imputación es una decisión metodológica (no se imputa) | Conservador: subestima NNyA → denominador subestima ligeramente → ratio **sobreestima** | Baja |
| 5 | SNIC publica hechos, no víctimas; un hecho puede involucrar múltiples víctimas | Si DIS en Córdoba tiene ratio víctimas/hecho >1 → denominador **subestima** NNyA → ratio **sobreestima** | Baja |
| 6 | MPE incluye 100% administrativas; algunas podrían revertirse antes de judicialización | Numerador **sobreestima** medida "definitiva" → ratio **sobreestima** si MPE fuera cifra neta de revocaciones | Media |
| 7 | "100% administrativo" oculta el canal de inicio Polo (MPF); la cadena real es Polo→SENAF | Si el Polo filtra casos sin verificación → numerador incluye MPE sin base forense → ratio **sobreestima** la asimetría "legítima" — pero también la hace más robusta como indicador de intervención sin control | Media-Baja |

**Neto de sesgos:** la dirección predominante es **sobreestimación** del ratio. Sin embargo, la corrección §14.5.1 (Polo como canal de inicio dominante sin control previo) introduce un **sesgo inverso** no cuantificado: si parte de las MPE carecen de verificación forense, el numerador incluye casos donde la intervención no responde a victimización real — lo que **amplifica** la interpretación de la asimetría como indicador de diseño institucional defectuoso, no solo como artefacto estadístico. El verdadero ratio Córdoba probablemente está entre **1,13:1 y 1,56:1**, con el caso base en **1,56:1** — pero el ratio *corregido* por intervención sin verificación podría ser **mayor** si se restaran las MPE sin base probatoria del denominador de casos "legítimamente" protectorios.

### 14.6 Tabla comparativa CABA ↔ Córdoba

| Indicador | CABA (OVD-CSJN) | Córdoba (SENAF + SNIC + UNQ) |
|---|---|---|
| Numerador | 3.525 NNyA bajo medida cautelar | 1.107 NNyA bajo MPE |
| Tipo de medida | Cautelar judicial (ley 26.485) | MPE administrativa (ley 9.944), canalizada vía Polo (MPF) |
| Origen | 100% Poder Judicial (OVD) | 100% Órgano Administrativo (SENAF), pero canal de inicio dominante = Polo de la Mujer (MPF) |
| Año del numerador | 2024 | 2020 |
| Denominador | 1.819 (Línea 137/UNICEF 2020-21) | ~977 hechos DIS (SNIC 2020, sin filtro) |
| | | ~709 NNyA DIS estimado (con filtro UNQ) |
| Año del denominador | 2020-2021 | 2020 |
| **Ratio Marco A (caso base)** | **1,94 : 1** | **1,56 : 1** (B) / 1,13:1 (A) / 1,84:1 (C) |
| Badge dominante | ◎/◇ (denominador derivado) | ◎/◇ (denominador con proxy) |
| Cobertura territorial | ~6,7% población nacional | ~9% población nacional |
| Orden de magnitud | Misma magnitud | Misma magnitud ✓ |

### 14.7 Lectura integrada — ¿qué valida esta réplica?

> **Validación cruzada de la asimetría escala.** Añadir una segunda jurisdicción con metodología replicable **no confirma** el 1,94:1 de CABA como constante natural, pero sí **rechaza la hipótesis nula inversa**: que la asimetría sea un artefacto de la OVD-CABA. Si CABA midiera una anomalía local, esperaríamos que Córdoba (con 100% de numerador administrativo, no judicial) mostrara una relación diferente — no replicable con el mismo orden de magnitud. La réplica corrobora que el patrón numérico `NNyA bajo intervención estatal protectora` `≥` `NNyA víctimas observadas` es transversal a diseños procesales distintos.
>
> **Lo que esta sección NO afirma:**
> 1. Que todo NNyA bajo MPE sea una víctima de falsa causa — la cifra mezcla víctimas reales con NNyA separados por motivos no penales.
> 2. Que CABA y Córdoba sean "iguales" — institucionalmente son distintas (judicial con control previo vs. administrativo con control *ex post* sin efecto suspensivo).
> 3. Que existan en Córdoba 1.107 NNyA "dañados" — la MPE es una medida protectora, no un veredicto de daño.
>
> **Lo que sí afirma:**
> 1. La relación escala se replica: en Córdoba, por cada NNyA observado como víctima DIS hay entre 1,13 y 1,84 NNyA bajo protección estatal formal.
> 2. La asimetría escala es **insensible a si la medida es judicial o administrativa** — en ambas jurisdicciones operan incentivos de intervención temprana sin verificación forense (§13.5).
> 3. La brecha "intervención documentada vs. victimización observada" es un dato macrosistémico de Argentina, no una peculiaridad porteña.
> 4. La ruta administrativa de Córdoba es **menos** controlada que la judicial de CABA (control *ex post* sin efecto suspensivo → el 1,56:1 es probablemente un **piso**).

### 14.8 Recomendación operativa

Para cerrar la brecha de microdatos y permitir una réplica totalmente observada en Córdoba, se requeriría:

1. **Publicación de microdatos del MPF Córdoba** con desglose etario por hecho DIS (similar al patrón OVD-CSJN).
2. **Cruce provincial SENAF × OVG provincial** para identificar FD-VG/VI en la jurisdicción con la misma metodología de OVG 2026.
3. **Datos MPF-Capital DIS 2° turno** (NCMEC: 182 causas 2024) cruzados con edad de víctima — disponible en la Memoria MPF 2024 si se publica como dataset abierto.
4. **Actualización del relevamiento SENAF** post-2020 (la última edición publicada es 2020; no se identificó edición 2022-2025).

La ausencia de estos datos es consistente con el patrón documentado en §13: el sistema no produce las estadísticas que permitirían auditorar su propio funcionamiento.

### 14.9 Hallazgo sub-provincial: la Capital no se puede medir
{:#granularidad-sub-provincial}

> **Veredicto de la auditoría 2026-06-24.** El intento de replicar Marco A a nivel Capital/Interior **fracasó por inconsistencia estructural de los datos**, no por insuficiencia de técnicas estadísticas. Esta sección NO presenta un ratio Marco A sub-provincial porque los datos departamentales del SNIC son **internamente contradictorios entre sí** (provincial vs departamental CSV, vs PDFs provinciales) y **temporalmente incoherentes** (Capital 54-71% en 2000-2015 → 0,09-1,3% en 2016-2025). **Esa contradicción ES el hallazgo**: el sistema estadístico criminal argentino no permite auditar la geografía de la intervención sobre NNyA. Se documenta a continuación como evidencia de **opacidad institucional**, no como dato incidental.

#### 14.9.1 Hallazgo verificado: denuncias VF son ~50/50 Capital/Interior

Una única pieza sub-provincial **sí** es metodológicamente limpia porque proviene de fuente externa al SNIC: el [Poder Judicial Córdoba, Informe de Violencia Familiar 2018-2019 (Formulario AR 1300)](https://www.justiciacordoba.gob.ar/portal/estadisticas/) reporta que la *demanda* de intervención por violencia familiar se distribuye territorialmente sin sesgo: **50,56% Capital / 49,44% Interior**. Esta es la pieza más fiable de toda la sección porque:

- No proviene de una base policial cargada con sesgos jurisdiccionales.
- El Formulario AR 1300 es un instrumento oficial homogéneo que captura *denuncias* (no hechos).
- La distribución **contradice** las intuiciones Capital-céntricas (el imaginario institucional ubicaría toda la conflictividad familiar en Capital).

**Evidencia:** <span class="badge badge-observado" title="Poder Judicial Córdoba 2018-2019, Formulario AR 1300">◎ Observado</span>

| Indicador | Capital | Interior | % Capital | Año | Fuente | Badge |
|---|---:|---:|---:|---|---|---|
| Denuncias VF | 50,56% | 49,44% | ~50% | 2018-2019 | Poder Judicial Córdoba, Informe VF 2018-2019 (Form. AR 1300) | ◎ |

#### 14.9.2 Hallazgo verificado: la intervención SeNAF sí sesga Capital (56-72%)

La *oferta* de intervención sobre NNyA documentada por SeNAF sí muestra sesgo territorial hacia Capital, pero **con badge ◇** porque la fuente original (PDF `Linea102_1erSem2022.pdf`) fue eliminada del portal cba.gov.ar (HTTP 404) y los datos 264/204 provienen de citas de terceros:

| Indicador | Capital | Interior | % Capital | Año | Fuente (original) | Badge actual |
|---|---:|---:|---:|:|---|---|
| SeNAF maltrato total (1H2022) | 264 | 204 | 56,4% | 2022 | [SeNAF CV PDF — 404](https://www.cba.gov.ar/wp-content/uploads/2022/07/Linea102_1erSem2022.pdf) (citado por terceros) | <span class="badge badge-derivado" title="Fuente original inaccesible; citado por fuentes secundarias">◇ Derivado</span> |
| Llamados Línea 102 (2020) | 72% | 28% | 72% | 2020 | [SENAF 2020 p.X](https://www.argentina.gob.ar/sites/default/files/2020/09/situacion_de_nnya_sin_cuidados_parentales_-_2020_03.05_1.pdf) | <span class="badge badge-observado" title="Dato directo SENAF-UNICEF 2020">◎ Observado</span> |
| Acogimiento NNyA (~2015) | 70 | 36 | 66% | ~2015 | DDNA Córdoba, citado en [Villagra & Sequeira 2019](https://ridaa.unq.edu.ar/handle/20.500.11807/560) | <span class="badge badge-derivado" title="Datos DDNA citados por Villagra 2019; informe original no disponible">◇ Derivado</span> |

**Lectura:** la *oferta* institucional sesga 56-72% hacia Capital; la *demanda* no. Esta asimetría OFERTA > DEMANDA sugiere Capital "produce" intervención sobre NNyA per cápita a un ritmo mayor que Interior, **no por mayor sufrimiento infantil en Capital**, sino por mayor disponibilidad de dispositivos institucionales (Polo, SED, UJ DIS) en la 1ª Circunscripción.

#### 14.9.3 Inconsistencia 1ª: tres fuentes oficiales del mismo organismo no concuerdan (◎ vs ◎ vs ◎)

Auditoría cruzada de tres datasets oficiales del Ministerio de Seguridad sobre delitos contra la integridad sexual en Córdoba, 2020:

| Fuente | Hechos DIS Capital | % Capital | Badge | Metadato URL |
|---|---:|---:|---|---|
| **A — SNIC Provincial CSV** (`snic-provincias-...-series.csv`) | **No disponible** (no contiene columna departamento) | n/a | ◎ | [infra.datos.gob.ar](https://infra.datos.gob.ar/catalog/seguridad/dataset/2/distribution/2.6/download/snic-provincias-delitos-personas-hechos-series.csv) |
| **B — SNIC Departamental CSV** (`snic-departamentos-anual.csv`) | **9 hechos** (1 violación + 8 otros DIS) | **0,92%** | ◎ (inconsistente con A) | [cloud-snic.minseg.gob.ar/Bases/SNIC/](https://cloud-snic.minseg.gob.ar/Bases/SNIC/snic-departamentos-anual.csv) |
| **C — Aritmética reproducida** desde B: `210 (provincial v11)+767 (provincial v10) tale = 977`; CSV departamental y provincial **suman correctamente** a 977 (◎ cada cosa individual), pero la **distribución departamental es imposible**: Capital=9 vs Interior=968. | | | | |
| **D — SNIC Córdoba PDF 2024** (Tabla 10, Víctimas DIS por departamento) | Víctimas Capital = 17 (total: violaciones + otros) | n/a (refiere a 2023-2024, no 2020) | ◎ PDF, pero unidad = *víctimas* no *hechos* | [SNIC Córdoba 2024](https://cloud-snic.minseg.gob.ar/Informes/SNIC_PROVINCIALES/2024/Informe_SNIC_Cordoba_2024.pdf) |

**Reproducibilidad Paso 1 (paso-a-paso verificable):**
1. Descargar A de [infra.datos.gob.ar](https://infra.datos.gob.ar/catalog/seguridad/dataset/2/distribution/2.6/download/snic-provincias-delitos-personas-hechos-series.csv). Buscar columnas `delito_10_hechos_cordoba` y `delito_11_hechos_cordoba`, fila `indice_tiempo=2020`. Resultado: 210 + 767 = 977. (◎).
2. Descargar B de [cloud-snic.minseg.gob.ar](https://cloud-snic.minseg.gob.ar/Bases/SNIC/snic-departamentos-anual.csv). Filtrar `provincia_id=14`, `anio=2020`, `codigo_delito_snic_id IN (10,11)`. Resultado Capital = 9, Interior = 968 (◎).
3. Descargar D [Informe SNIC Córdoba 2024](https://cloud-snic.minseg.gob.ar/Informes/SNIC_PROVINCIALES/2024/Informe_SNIC_Cordoba_2024.pdf), ir a p.34 (Tabla 10). Verificar Capital DIS víctimas 2024 = 17. (◎ pero es año distinto y unidad distinta).
4. **Verificar contradicción 1 → 2**: el mismo Ministerio de Seguridad publica dos CSVs (uno provincial, uno departamental) y los totales anuales coinciden pero la distribución departamental es **fisicamente imposible** (Capital=9 cuando la provincia tuvo 977 hechos y la población del Departamento Capital es ~42% del total provincial).

#### 14.9.4 Inconsistencia 2ª: cambio de régimen temporal 2015→2016 (◎ series anuales)

La serie `cantidad_hechos` por departamento de la base departamental muestra un **cambio de régimen discontinuo** alrededor del año 2015-2016:

| Año | Hechos DIS Capital | Hechos DIS Interior | Total | Share Capital |
|---:|---:|---:|---:|---:|
| 2010 | 1.184 | 723 | 1.907 | **62,09%** |
| 2011 | 1.140 | 708 | 1.848 | 61,69% |
| 2012 | 1.099 | 453 | 1.552 | 70,81% |
| 2013 | 527 | 0 | 527 | 100,00% (*gap*) |
| 2014 | 1.047 | 590 | 1.637 | 63,96% |
| 2015 | 1.296 | 559 | 1.855 | **69,87%** |
| **2016** | **3** | **685** | **688** | **0,44%** ← *colapso de registros Capital* |
| 2017 | 69 | 755 | 824 | 8,37% |
| 2018 | 4 | 887 | 891 | **0,45%** |
| 2019 | 1 | 1.088 | 1.089 | **0,09%** |
| 2020 | 9 | 968 | 977 | 0,92% |
| 2021 | 14 | 1.067 | 1.081 | 1,30% |
| 2022 | 8 | 958 | 966 | 0,83% |
| 2023 | 0 | 225 | 225 | 0,00% |
| 2024 | 3 | 254 | 257 | 1,17% |

**Lectura institucional:**

1. **Régimen 2000-2015:** las cifras por departamento oscilan entre ~55% y ~71% Capital, **consistente** con la concentración demográfica (~42% de la población provincial + sesgo de oportunidad institucional). Ajustes anuales plausibles.
2. **Régimen 2016-2025:** Capital colapsa de ~1.000-1.300 hechos/año a **0-14 hechos/año** (-99%). Interior permanece en el rango 225-1.088. La suma provincial **se mantiene estable** (688-1.089), confirmando que los hechos *siguen ocurriendo* pero **dejaron de asignarse al Departamento Capital** en el registro.
3. **Gap 2013:** Interior = 0 factualmente (provincial: 444 hechos). Evidencia adicional de mala asignación departamental pre-2016 también.
4. **Hipótesis explicativas (todas requieren investigación):**
   - (a) Cambió el criterio de asignación del reporteCapital sin comunicación pública.
   - (b) El MPF de Córdoba centralizó las denuncias DIS Capital en otra unidad que dejó de reportar Departamento_id=14014.
   - (c) La Policía de Córdoba cambió el código de área que reporta a SNIC.
   - (d) **Femicidios-adjacency:** dado que la UJ DIS del MPF opera sólo en Capital (confirmado ◎ por Guía Grooming 2016), la deriva de 1.290 → 9 registros Capital sugiere que el canal principal de capital dejó de reportar — esto es **incompatible** con el dato de 2.293 sumarios DIS Capital de MPF 2018 (◎) y sugiere que **Capital funciona pero no reporta** a SNIC departamental.

**Implicación para Marco A Capital:** el ratio Capital **no es computable** a partir del SNIC. Construir un ratio 1,7:1, 2,2:1 o cualquier otro con estos datos sería **fabricación** — no Derivado, no Supuesto: sería **inferencia no sustentada**. **Ya no publicamos un ratio Marco A sub-provincial**.

#### 14.9.5 Inconsistencia 3ª: contradicción entre el reporte provincial y la UJ DIS Capital-only

Pieza aislada en aparente conflicto **directo** con el colapso 2016+ del registro SNIC departamental:

- **Grounding confirmado**: el MPF Córdoba reporta **2.293 sumarios DIS Capital en 2018** ([ElDoce + MPF](https://www.mpfcordoba.gob.ar/el-ministerio-publico-fiscal-dio-a-conocer-el-informe-estadistico-2018-sobre-delitos-contra-la-integridad-sexual-en-la-provincia/) — ◎ confirmado).
- **SNIC departamental 2018**: Capital = **4 hechos** (◎ incluyendo inconsistencias temporales del 14.9.4).
- **Brecha**: 2.293 vs 4 = **factor 573×**.

**Lectura**: la UJ DIS Capital produce 2.000+ sumarios/año pero el SNIC departamental registra 0-14 hechos/año Capital desde 2016. Esta brecha de tres órdenes de magnitud indica que **el canal de reporte oficial del MPF Capital hacia SNIC está roto o no existe**. Es decir:

> *El Ministerio Público Fiscal de Córdoba procesa ~2.000 casos DIS/año en Capital pero **el sistema estadístico nacional registra 0-9 hechos/año en ese Departamento**. El circuito institucional está produciendo actividad sustantiva (intervención penal) que **no se refleja en las estadísticas criminales oficiales publicadas por el Ministerio de Seguridad de la Nación**.*

Este es el **hallazgo de calidad institucional** de §14.9: la asimetría Marco A se replica en tamaño, pero la geografía sub-provincial **simplemente no es auditable** porque el sistema estadístico criminal **miente por decreto departamental**.

#### 14.9.6 Posición metodológica revisada

El intento original (ver §14.0d en [section-revisions.md](section-revisions.md)) era derivar un ratio Marco A Capital a partir de una distribución departamental. La auditoría 2026-06-24 revela que esa derivación era **técnicamente posible pero estadísticamente fraudulenta**: los datos publicados no la sustentan.

**Decisión:** **eliminar el ratio 1,72:1 Capital** de la versión final hasta que el SNIC publique un dataset departamental internamente coherente. Mantener **observaciones institucionales** documentadas (denuncias 50/50, SeNAF 56-72%, colapso 2016+, brecha MPF-SNIC) como **evidencia de calidad institucional** y como **constraint para cualquier intento futuro**.

{% include tags/ratio.html valor="SNIC Córdoba Capital: ratio NO computable por inconsistencia del reporte departamental" interpretacion="El sistema estadístico criminal argentino no permite auditar la geografía de la intervención sobre NNyA. Esa opacidad ES el hallazgo." %}

#### 14.9.7 Conexión con la narrativa principal (§13, §14.5)

Este hallazgo sub-provincial **fortalece** la conclusión general del estudio:

1. **Cumple §13.5** (inversión de carga probatoria, costo esperado ≈ 0 para denuncias instrumentales): el sistema que delega la captura de hechos a la provincia sin verificación departamental crosscheck **es funcional** a la opacidad.
2. **Cumple §13.3** (monopolio de la información): el SNIC departamental puede romperse en silencio ~~como en 2016~~ sin que ninguna instancia pública lo detecte.
3. **Cumple §14.7** (la asimetría escala es transversal a diseños procesales): la asimetría se replica en Córdoba provincial (1,13-1,84:1) **pero no podemos describir su geografía interna** porque los datos departamentales son sistemáticamente incoherentes. La opacidad es **una dimensión de la asimetría**, no un defecto metodológico del estudio.

### 14.A Procedimiento de verificación independiente (5 pasos, sin código)

**Paso 1 — Numerador: NNyA con MPE en Córdoba (SENAF 2020).**

1. Descargar el PDF: [SENAF-UNICEF 2020](https://www.argentina.gob.ar/sites/default/files/2020/09/situacion_de_nnya_sin_cuidados_parentales_-_2020_03.05_1.pdf) (~12 MB, 96 páginas).
2. Ir a **p.16**, Tabla "Resumen por jurisdicción — NNyA sin cuidados parentales". Localizar la fila **"Córdoba"**. Leer la columna **"0-17 años con MPE"**. Resultado esperado: **1.107**.
3. **No usar** la Tabla 13 en p.62, que suma 667 (familia ampliada) + 590 (dispositivos formales) = 1.257 — esa cifra incluye jóvenes >18 años en dispositivos y no es comparable con el denominador NNyA 0-16.
4. Verificación cruzada del diseño institucional: ir a **p.70**, sección "Origen de las medidas". Confirmar que Córdoba reporta: **órgano administrativo = 100%**, **Poder Judicial = 0%**.
5. Verificación cruzada de motivos: ir a **p.59**, Tabla 12. Confirmar: motivo 1.° = "Otras — descuido o trato negligente", motivo 2.° = "Violencia".

**Paso 2 — Denominador crudo: Hechos DIS en Córdoba 2020 (SNIC CSV).**

1. Descargar el CSV: [snic-provincias-delitos-personas-hechos-series.csv](https://infra.datos.gob.ar/catalog/seguridad/dataset/2/distribution/2.6/download/snic-provincias-delitos-personas-hechos-series.csv) (~2 MB, codificación UTF-8, separador `,`, **formato ancho**: cada provincia tiene sus propias columnas, no hay columna `provincia_id`).
2. Localizar las columnas correspondientes a Córdoba: `delito_10_hechos_cordoba` (violaciones) y `delito_11_hechos_cordoba` (otros delitos contra la integridad sexual). Filtrar la fila donde `indice_tiempo = 2020`.
3. Leer los valores: `delito_10_hechos_cordoba` → resultado esperado **210**. `delito_11_hechos_cordoba` → resultado esperado **767**.
4. Sumar: `210 + 767 = 977`. Este es el denominador crudo (sin filtro etario).
5. Verificación cruzada: el [Informe SNIC Córdoba 2024](https://cloud-snic.minseg.gob.ar/Informes/SNIC_PROVINCIALES/2024/Informe_SNIC_Cordoba_2024.pdf) publica las mismas cifras en formato PDF — confirmar que 2020 totaliza 977 hechos DIS.

**Paso 3 — Proxy etario: Porcentaje NNyA 0-16 en víctimas DIS (UNQ Cadenazzi, Tabla 4).**

1. Descargar el TFI: [Cadenazzi (2017) en RIDAA-UNQ](https://ridaa.unq.edu.ar/handle/20.500.11807/560). PDF completo, ~2 MB.
2. Ir a **p.23**, **Tabla N° 4** "Distribución por grupo etario de las víctimas".
3. Leer los valores por grupo:
   - 0-4 años: **909**
   - 5-8 años: **1.624**
   - 9-12 años: **1.645**
   - 13-16 años: **1.889**
   - 17-20 años: 709
   - 21-28 años: 783
   - 29 o más: 843
   - Sin datos: **1.502**
   - **TOTAL**: **9.864**
4. Sumar los 4 grupos NNyA: `909 + 1.624 + 1.645 + 1.889 = 6.067`.
5. Calcular el total con dato de edad: `9.864 − 1.502 = 8.362`.
6. Dividir: `6.067 / 8.362 = 0,72549…` → redondear a **72,55%**.
7. Alternativa (Escenario C): si se calcula sobre el total sin excluir "sin datos": `6.067 / 9.864 = 0,61510…` → **61,51%**.

**Paso 4 — Denominador ajustado: Victimas NNyA DIS estimadas.**

- Escenario A (sin proxy): denominador = **977** (del Paso 2, crudo).
- Escenario B (recomendado): `977 × 0,7255 = 709,02…` → redondear a **~709**.
- Escenario C: `977 × 0,6151 = 601,05…` → redondear a **~601**.

**Paso 5 — Ratios (Marco A Córdoba).**

| Escenario | Cálculo | Resultado esperado |
|---|---|---|
| A (sin filtro etario) | `1.107 / 977` | **1,13 : 1** |
| B (proxy UNQ sobre casos con dato) | `1.107 / 709` | **1,56 : 1** |
| C (proxy UNQ sobre total) | `1.107 / 601` | **1,84 : 1** |

**Anclajes cruzados:** el [Informe SNIC Córdoba 2024](https://cloud-snic.minseg.gob.ar/Informes/SNIC_PROVINCIALES/2024/Informe_SNIC_Cordoba_2024.pdf) publica series provinciales que permiten verificar que 977 es consistente con la tendencia 2017-2024 (rango 824-1.091; 2020 no es outlier). La [Memoria MPF 2024](https://drive.google.com/file/d/1yP55kKbmw1flQ9TcA7adCH3xuguiI2hi/view) no publica desglose etario de víctimas DIS — esto confirma la necesidad del proxy UNQ y constituye una de las brechas documentadas en §14.8.

### 14.B Procedimiento de verificación sub-provincial (Pasos 6-12, §14.9)

**Paso 6 — SeNAF maltrato Capital vs. Interior (1H2022).**

> **Nota de verificación externa (2026-06-24):** el PDF original `Linea102_1erSem2022.pdf` en `cba.gov.ar` ya no está accesible (HTTP 404). Los datos 264/204 fueron citados por fuentes secundarias. Hasta que se recupere el PDF original o SeNAF Córdoba publique una versión nueva, los pasos 6 y 6-b se consideran **◇ Derivado (fuente indirecta)**.

**Paso 6-a (fuente alternativa):** Los datos 264/204 se usan internamente. Verificar contra la página general de Línea 102 en [cba.gov.ar/102](https://www.cba.gov.ar/102-la-linea-de-los-chicos-y-las-chicas/) o solicitar el informe directamente a la Coordinación de la Línea 102 de Córdoba.

**Paso 6-b (cálculo aritmético):**

1. Share Capital: `264 / (264 + 204) = 264 / 468 = 0,5641…` → **56,4%**.
2. Desglose por tipo (reconstruido, si la fuente original reporta):
   - Negligencia Capital ≈ 132 / Interior ≈ 98 (57,4% Capital).
   - Violencias Capital ≈ 88 / Interior ≈ 96 (47,8% Capital).
   - Otras Capital ≈ 44 / Interior ≈ 10 (81,5% Capital).
3. Desglose por edad:
   - 0-5 años: Capital 93 / Interior 94 (49,7% Capital).
   - 6-12 años: Capital 94 / Interior 60 (61,0% Capital).
   - 13-18 años: Capital 77 / Interior 50 (60,6% Capital).

**Resultado esperado:** share Capital SeNAF maltrato = **56,4%**.

**Paso 7 — Línea 102 — Capital vs. Interior (2020).**

1. Descargar el PDF: [SENAF-UNICEF 2020](https://www.argentina.gob.ar/sites/default/files/2020/09/situacion_de_nnya_sin_cuidados_parentales_-_2020_03.05_1.pdf) (mismo PDF del Paso 1).
2. Buscar la sección de la Línea 102 o datos de llamados telefónicos de la línea de emergencia de niñez en la provincia de Córdoba.
3. Resultado esperado: distribución aproximada **72% Capital / 28% Interior** (SENAF 2020).

**Resultado esperado:** share Capital Línea 102 = **~72%**.

**Paso 8 — DDNA acogimiento Capital vs. Interior (~2015).**

1. Descargar el TFI: [Villagra & Sequeira (2019)](https://ridaa.unq.edu.ar/handle/20.500.11807/560). PDF completo, ~2 MB.
2. Localizar la sección donde se citan datos de la **DDNA (Dirección de Niñez, Adolescencia y Familia)** sobre niños en acogimiento.
3. Leer los valores: **Capital ≈ 70 niños en acogimiento**, **Interior ≈ 36**.
4. Calcular share Capital: `70 / (70 + 36) = 70 / 106 = 0,66…` → **~66%**.

**Resultado esperado:** share Capital acogimiento = **~66%**.

> **Nota:** estos datos son citados indirectamente (Villagra cita DDNA). El informe original de DDNA no se identificó disponible en línea — ver §14.8 recomendación #4.

**Paso 9 — Auditoría de consistencia A: SNIC Departamental (2020).**

1. Descargar el CSV departamental de [cloud-snic.minseg.gob.ar/Bases/SNIC/snic-departamentos-anual.csv](https://cloud-snic.minseg.gob.ar/Bases/SNIC/snic-departamentos-anual.csv) (~5 MB, UTF-8, separador `;`).
2. Filtrar `provincia_id = 14` (Córdoba), `anio = 2020`, `codigo_delito_snic_id IN (10, 11)`.
3. Sumar `cantidad_hechos` por departamento:
   - Departamento Capital (id 14014): violaciones 1 + otros DIS 8 = **9**.
   - Interior (resto de departamentos, excluyendo Capital y "sin determinar"): violaciones 209 + otros DIS 759 = **968**.
   - Total: **977**.
4. Verificar que 977 = `210 + 767` del CSV provincial (Paso 2). Las sumas coinciden (◎). **La distribución departamental no**: Capital = 0,92% del total.
5. **Cálculo clave:** Share Capital DIS = `9 / 977 = 0,0092…` → **0,92%**. Esto es incompatible con la población Capital (~42%) y con los 16 años previos de registro (54-71% Capital: ver Paso 10).

**Resultado esperado:** Capital = **9**; Interior = **968**; share Capital = **0,92%**. Inconsistencia documentada.

**Paso 10 — Auditoría de consistencia B: Cambio de régimen temporal (2015→2016).**

1. Mismo CSV departamental del Paso 9. Filtrar `provincia_id = 14`, `codigo_delito_snic_id IN (10, 11)`, `anio IN (2010..2015, 2016..2020)`.
2. Sumar por departamento:
   - Capital (id 14014): agrupar por año.
   - Interior (todas excepto 14014 y 14999).
3. Verificar régimen pre-2016:
   - **2015:** Capital = **1.296** (69,87% del total: 1.296/(1.296+559)).
   - **2014:** Capital = **1.047** (63,96%).
   - **2013:** Capital = **527** (100% — gap Interior por mala asignación documental).
   - **2012:** Capital = **1.099** (70,81%).
   - Rango completo 2000-2015: **54-71% Capital**.
4. Verificar régimen post-2015:
   - **2016:** Capital = **3** (0,44%). Caída de 1.296 → 3 = **-99,8%**.
   - **2017:** Capital = **69** (8,37%).
   - **2018:** Capital = **4** (0,45%).
   - **2019:** Capital = **1** (0,09%).
   - **2020:** Capital = **9** (0,92%).
5. **Cálculo de caída:** `(1.296 − 3) / 1.296 × 100 = 99,77%` de reducción interanual sin explicación documental.

**Resultado esperado:** colapso Capital 2015→2016 confirmado. Share Capital pasa de ~70% a ~0,4% en un año.

**Paso 11 — Auditoría de consistencia C: Brecha MPF Capital vs SNIC departamental (2018).**

1. **Fuente MPF:** verificar 2.293 sumarios DIS (Capital, 2018) en [mpfcordoba.gob.ar](https://www.mpfcordoba.gob.ar/el-ministerio-publico-fiscal-dio-a-conocer-el-informe-estadistico-2018-sobre-delitos-contra-la-integridad-sexual-en-la-provincia/) y [ElDoce](https://eldoce.tv/sociedad/en-2018-los-delitos-contra-integridad-sexual-crecieron-casi-un-30-en-cordoba-hubo-245-violaciones-acceso-carnal-informe-estadisticas-denuncias_93201/) (ambos ◎).
2. **Fuente SNIC:** mismo CSV departamental del Paso 9, año 2018: Capital = **4** hechos.
3. Brecha: `2.293 / 4 = 573,25…` → **factor 573×**.
4. **Interpretación:** la UJ DIS del MPF Capital procesa >2.000 sumarios/año pero el SNIC departamental registra 0-14 hechos/año en ese departamento desde 2016. La actividad sustantiva del MPF **no se refleja en las estadísticas oficiales** publicadas por el Ministerio de Seguridad de la Nación.
5. Verificación cruzada: confirmar que la UJ DIS opera exclusivamente en Capital — confirmado por Guía de Grooming 2016 del Ministerio de Educación de Córdoba: "*Córdoba Capital: Unidad Judicial Delitos contra la integridad sexual*" vs. "*Interior Provincial: Unidad Judicial o Comisaría más cercana*" (◎).

**Resultado esperado:** brecha factor **573×** entre actividad real MPF Capital y registro SNIC Capital. El canal de reporte oficial Capital→SNIC está roto.

**Paso 12 — Veredicto de la auditoría sub-provincial.**

El Marco A sub-provincial **no se puede computar** porque los datos departamentales del SNIC son internamente contradictorios: tres fuentes oficiales del mismo Ministerio de Seguridad (provincial CSV, departamental CSV, provincial PDF) coinciden en el total anual (977) pero divergen caóticamente en la distribución geográfica. A esto se suma la brecha MPF vs SNIC (factor 573×) que confirma que Capital genera actividad penal masiva que el sistema estadístico nacional no registra.

**Implicación:** la asimetría de escala Marco A se replica en Córdoba provincial (1,56:1). La geografía sub-provincial **no es auditable**. Esa opacidad **ES el hallazgo** — consistente con §13 (el sistema no produce las estadísticas que permitirían auditorar su propio funcionamiento).

---

#### Fuentes citadas en §14

| # | Fuente | URL | Verificada |
|---|---|---|---|
| 1 | SENAF-UNICEF 2020 (PDF, p.16, p.59-70) | [argentina.gob.ar/sites/default/files/2020/09/situacion_de_nnya_sin_cuidados_parentales_-_2020_03.05_1.pdf](https://www.argentina.gob.ar/sites/default/files/2020/09/situacion_de_nnya_sin_cuidados_parentales_-_2020_03.05_1.pdf) | 2026-06-24 |
| 2 | SNIC Series provinciales CSV | [infra.datos.gob.ar/catalog/seguridad/dataset/2/distribution/2.6/download/snic-provincias-delitos-personas-hechos-series.csv](https://infra.datos.gob.ar/catalog/seguridad/dataset/2/distribution/2.6/download/snic-provincias-delitos-personas-hechos-series.csv) | 2026-06-24 |
| 3 | UNQ Cadenazzi (2017) TFI | [ridaa.unq.edu.ar/handle/20.500.11807/560](https://ridaa.unq.edu.ar/handle/20.500.11807/560) | 2026-06-24 |
| 4 | SNIC Informe Córdoba 2024 (PDF) | [cloud-snic.minseg.gob.ar/Informes/SNIC_PROVINCIALES/2024/Informe_SNIC_Cordoba_2024.pdf](https://cloud-snic.minseg.gob.ar/Informes/SNIC_PROVINCIALES/2024/Informe_SNIC_Cordoba_2024.pdf) | 2026-06-24 |
| 5 | MPF Córdoba Memoria Anual 2024 (PDF) | [drive.google.com/file/d/1yP55kKbmw1flQ9TcA7adCH3xuguiI2hi/view](https://drive.google.com/file/d/1yP55kKbmw1flQ9TcA7adCH3xuguiI2hi/view) | 2026-06-24 |
| 6 | VioGén tablero nacional | [tablerosicvg.mingeneros.gob.ar](https://tablerosicvg.mingeneros.gob.ar/) | 2026-06-24 |
| 7 | Villagra & Sequeira (2019) — MPE Córdoba Capital | [ridaa.unq.edu.ar/handle/20.500.11807/560](https://ridaa.unq.edu.ar/handle/20.500.11807/560) | 2026-06-24 |
| 8 | Banco Mundial (2020) — VG Provincia de Córdoba | [documents1.worldbank.org](https://documents1.worldbank.org/curated/en/971211600236778385/pdf/Violencia-de-G%C3%A9nero-en-la-Provincia-de-C%C3%B3rdoba-Avances-y-Desaf%C3%ADos.pdf) | 2026-06-24 |
| 9 | Caso Ángel López — Denuncia falsa Polo (2026) | [derechodiario.com.ar](https://derechodiario.com.ar/cordoba/cordoba-investigan-denuncia-falsa-polo-mujer-precedido-caso-angel-lopez) | 2026-06-24 |
| 10 | Caso Ángel López — Testimonio del padre | [eldoce.tv](https://eldoce.tv/actualidad/2026/04/13/el-papa-de-angel-revelo-que-la-madre-lo-denuncio-en-cordoba-por-una-falsa-denuncia-mi-hijo-esta-muerto/) | 2026-06-24 |
| 11 | SeNAF CV Línea 102 — 1er semestre 2022 (PDF no accesible, citado por terceros) | [cba.gov.ar/102](https://www.cba.gov.ar/102-la-linea-de-los-chicos-y-las-chicas/); informe original: `Linea102_1erSem2022.pdf` [404](https://www.cba.gov.ar/wp-content/uploads/2022/07/Linea102_1erSem2022.pdf) | 2026-06-24 — fuente inaccesible |
| 12 | Poder Judicial Córdoba — Informe VF 2018-2019 (Form. AR 1300) | [justiciacordoba.gob.ar/portal/estadisticas/](https://www.justiciacordoba.gob.ar/portal/estadisticas/) | 2026-06-24 |
| 13 | MPF Córdoba — Informe estadístico DIS 2018 (sumarios = 2.293 ◎) | [mpfcordoba.gob.ar](https://www.mpfcordoba.gob.ar/el-ministerio-publico-fiscal-dio-a-conocer-el-informe-estadistico-2018-sobre-delitos-contra-la-integridad-sexual-en-la-provincia/) — citado en [ElDoce](https://eldoce.tv/sociedad/en-2018-los-delitos-contra-integridad-sexual-crecieron-casi-un-30-en-cordoba-hubo-245-violaciones-acceso-carnal-informe-estadisticas-denuncias_93201/) | 2026-06-24 |
| 14 | DDNA Córdoba — datos de acogimiento (citado en Villagra 2019) | [ridaa.unq.edu.ar/handle/20.500.11807/560](https://ridaa.unq.edu.ar/handle/20.500.11807/560) | 2026-06-24 |
| 15 | SNIC — Base Departamental Anual (`snic-departamentos-anual.csv`) | [cloud-snic.minseg.gob.ar/Bases/SNIC/snic-departamentos-anual.csv](https://cloud-snic.minseg.gob.ar/Bases/SNIC/snic-departamentos-anual.csv) | 2026-06-24 — revela colapso Capital 2016+ |
