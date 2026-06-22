# Missing Methodology Audit — Project-Evidence Framework vs. Current Implementation

This file tracks every structural, procedural, and technical methodology element defined by [Project-Evidence](https://github.com/Project-Evidence/project-evidence.github.io) that is missing, incomplete, or broken in the current repository. Each item includes an explanation of the PE precedent, the current state, and an increment to address it.

---

## 1. DOCUMENT GOVERNANCE

### METH-001: Authors / Anonymity Section — MISSING

**Project-Evidence precedent:** PE has an explicit **§2 "Authors"** section that includes:
- Identity statement: "We are an anonymous group of researchers."
- Conflict of interest declaration: "The authors of this document claim no conflicts of interest."
- Funding disclosure: "We are not receiving funding from any sources, public or private."
- Values statement / disavowal: "We disavow all racism and violent attacks..."
- Verification link: "Our public key is also available for download: public.pem"

**Current state:** The repository has a `README.md` with a one-paragraph disclaimer ("Proyecto de investigación anónimo...") and a "Propósito" subsection in `sections/00-methodology.md` with 3 points, but:
- No dedicated "Authors" or "Sobre los autores" section exists in the published site
- No conflict of interest declaration in the published site
- No funding disclosure in the published site
- The disavowal is partial (§0 mentions "condenamos la violencia institucional contra NNyA" but has no general disavowal of violence or discrimination)
- The PGP key link exists in the footer but the key is a placeholder (see METH-006)

**Why it matters:** The authors section establishes credibility through transparency about motives and conflicts. PE's entire model hinges on the reader being able to evaluate whether the authors have incentives to distort evidence. Without this section publicly visible on the site, the transparency contract is broken.

**Increment:** Add a new section in `sections/00-methodology.md` (or as `sections/00-authors.md` included from `index.md`) titled "Sobre los autores":

```markdown
### Sobre los autores

Somos un grupo anónimo de investigadores. No estamos afiliados a ningún partido político, organización estatal, ni corporación. Este proyecto no recibe financiamiento de fuentes públicas ni privadas.

Los autores de este documento no reclaman conflictos de intereses.

Condenamos toda forma de violencia — física, psicológica o institucional — contra niñas, niños y adolescentes, así como contra cualquier persona en razón de su género, orientación o condición. No estamos motivados por odio hacia ninguna institución, sino por la búsqueda de evidencia.

Nuestra clave pública PGP está disponible para verificación: [public.pem]({{ '/public.pem' | relative_url }})
```

---

### METH-002: Correction Policy — PRESENT but needs domain adaptation

**Project-Evidence precedent:** PE's **§3 "Correction Policy"** is specific to its domain:

> If the scientific community can provide peer reviewed studies that prove that the SARS-CoV-2 spillover event occured "in the wild," i.e. outside of a lab... we will add an addendum to this document highlighting those results.

PE's policy ties the correction trigger to a specific falsifiable condition (lab origin disproven by "in the wild" proof).

**Current state:** The "Política de Corrección" in `sections/00-methodology.md` says:

> Si la evidencia científica o judicial demuestra que alguno de los parámetros o supuestos utilizados es incorrecto, agregaremos una adenda destacando la corrección.

This **is present** but is generic — it doesn't tie correction to specific falsifiable conditions the way PE does.

**Increment (enhancement, not gap):** Consider adding domain-specific correction triggers, e.g.:
- "Si el RNR publica desglose de condenas intrafamiliares contra NNyA a nivel nacional, recalcularemos el Marco B con datos observados."
- "Si la OVG actualiza su relevamiento con las 8 jurisdicciones faltantes, actualizaremos el intervalo FD."
- "Si el SNIC publica datos 2025 concurrentes con OVD 2024, recalcularemos los ratios."

This would make the correction policy actionable and testable, following PE's model.

---

### METH-003: Contribution Policy — INCOMPLETE

**Project-Evidence precedent:** PE's **§4 "Contribution Policy"** includes:
- Specific guidance: "We are always looking for peer reviewed papers..."
- Source quality requirements: "All sources must be acceptable under our Sourcing Policy."
- Mechanism: "submit a pull request to our GitHub repository."

**Current state:** The "Política de Contribución" in `sections/00-methodology.md` says:

> Aceptamos contribuciones que aporten nueva evidencia factual. Toda fuente debe cumplir nuestra Política de Fuentes. Para contribuir, abrir un issue en el repositorio.

Missing elements:
1. No guidance on **what type of evidence** is most needed (PE explicitly says "peer reviewed papers and other documents that address, back up, or disprove the claims")
2. No issue templates in the `.github/` directory (only `workflows/` exists)
3. No `CONTRIBUTING.md` file
4. No pull request template
5. The contribution mechanism says "abrir un issue" but there is no link to the repository (the repo URL is not specified anywhere in the published site — only in `README.md` which is excluded from the Jekyll build)

**Increment:**
1. Add a link to the repository in the contribution policy: `Para contribuir, [abrir un issue]({{ site.github.repository_url }}/issues) o enviar un pull request.`
2. Create `.github/ISSUE_TEMPLATE/evidence-submission.md`:
```yaml
---
name: Evidencia nueva
about: Aportar nueva evidencia factual
title: "[EVIDENCIA] "
labels: evidence
---

## Fuente
<!-- URL o DOI de la fuente -->

## Tipo de evidencia
- [ ] Observado (dato directo de informe oficial)
- [ ] Derivado (aritmética sobre observados)
- [ ] Supuesto (parámetro sin fuente directa)
- [ ] Refutación (evidencia que contradice una afirmación del informe)

## Sección afectada
<!-- ¿Qué sección del informe se ve afectada? -->

## Descripción
<!-- Describir la evidencia y su relevancia -->

## Cadena de cálculo (si es derivado)
<!-- Mostrar la aritmética reproducible -->
```
3. Create `.github/PULL_REQUEST_TEMPLATE.md`
4. Create `CONTRIBUTING.md` at root (included in repo but not in Jekyll build)
5. Enhance the contribution policy text to specify what is most needed:
```markdown
Buscamos especialmente:
- Informes oficiales con datos de condenas intrafamiliares contra NNyA a nivel nacional
- Datos provinciales actualizados de medidas cautelares (fuera de CABA)
- Estudios peer-reviewed sobre impacto de medidas cautelares en bienestar infantil en Argentina
- Evidencia que refute o matice las afirmaciones de este informe
```

---

## 2. SOURCE INTEGRITY & ARCHIVING

### METH-004: Source Archiving — NOT IMPLEMENTED (0% compliance)

**Project-Evidence precedent:** PE's **§5 "Sourcing Policy"** includes:

> All sources subject to change must be archived via https://archive.is

PE applies this systematically: throughout their document, every URL has an accompanying `(archived)` link pointing to an archive.is snapshot. Examples from their HTML source:
- `[archived](https://archive.is/K1HBk)` for the NEJM paper
- `[archived](https://archive.is/fuU3W)` for the Lancet paper
- `[archived](http://archive.is/8FGHD)` for the Nature article
- Over 20 archived links total

**Current state:** The `sourcing-policy.md` (included in `_includes/`) says:

> 8. **Archivar fuentes sujetas a cambio** vía archive.is o web.archive.org.

However, **zero (0) sources** in the repository have archived links. No `archive.is` or `web.archive.org` links appear in any section file. The `sources/` directory (presumably intended for local copies) is **empty**.

This is a critical vulnerability: official Argentine government URLs (csjn.gov.ar, mpf.gob.ar, scba.gov.ar, argentina.gob.ar) are known to restructure, move, or remove PDFs. If a source URL breaks, the entire evidentiary chain becomes unverifiable.

**Increment:**
1. For each of the 20 source URLs in `sections/12-sources.md`:
   a. Submit the URL to `https://archive.is` (or `https://web.archive.org/save`)
   b. Capture the archive URL
   c. Add an `(archived)` link next to each source URL
2. Optionally, download PDFs and place them in `sources/` directory as a local backup
3. Update the source table in `12-sources.md` to have an "Archivado" column:

```markdown
| # | Fuente | URL | Archivado |
|---|---|---|---|
| 1 | OVG FD 2026 | [PDF](https://consejompra.org/...) | [archive.is/XXXXX](https://archive.is/XXXXX) |
| 2 | OVD 2024 | [CSJN](https://www.csjn.gov.ar/...) | [archive.is/XXXXX](https://archive.is/XXXXX) |
```

4. Apply the same `(archived)` treatment to every in-text URL across all sections

**Estimated effort:** ~20 URLs to archive × ~2 min each = ~1 hour of manual work

---

### METH-005: Sourcing Policy — ADAPTED but missing specificity

**Project-Evidence precedent:** PE's sourcing policy is academic-oriented:
1. Prefer academic papers over any other source
2. All academic papers must be peer reviewed; if not, make clear
3. Prefer prestigious medical/scientific journals over mainstream media
4. Prefer mainstream media over amateur sources
5. Cross-check amateur sources with mainstream
6. Use multiple sources to prove the same claim
7. If a source is not in English, use Google Translate and note this
8. All sources must be dated
9. All sources subject to change must be archived

**Current state:** The `sourcing-policy.md` is adapted for the Argentine legal/governmental domain:
1. Prefer official documents over any other source
2. All official documents must be accessible via URL or DOI
3. Prefer state agency reports (CSJN, MPF, UNICEF, OVG, SCBA) over secondary sources
4. For derived data, show full calculation chain
5. For assumptions, label and justify range
6. Use multiple sources to verify same indicator
7. All sources must be dated
8. Archive changeable sources

This is an **appropriate adaptation** of the PE framework for a legal/governmental domain. However, two items are missing relative to PE:

- **PE item 2 (peer review / non-peer-review flagging):** The current policy doesn't require flagging when a source is not from an official body. E.g., CePASI is an NGO, not a governmental source. CAMORON is a legal NGO. These should be explicitly flagged as "non-official" per the policy's own hierarchy.
- **PE item 7 (translation):** Not relevant here since the document is in Spanish and sources are in Spanish, but missing for any English-language academic sources (Doyle, Bald, Sankaran, Hine, Springer). The policy doesn't address cross-language sourcing.

**Increment:**
1. Add to sourcing policy: "Si una fuente no proviene de un organismo estatal oficial, debe etiquetarse como 'no oficial' en el texto."
2. Add: "Si una fuente está en otro idioma, indicar el idioma original y, si se cita una traducción, señalar que es traducción propia o automática."

---

## 3. CRYPTOGRAPHIC VERIFICATION

### METH-006: PGP Public Key — PLACEHOLDER

**Project-Evidence precedent:** PE ships `public.pem` — a real PGP public key used to verify the authorship signature file (`signature`). The key is referenced in §2 and in the site footer. This allows anyone to:
1. Verify that updates to the document come from the same authors
2. Detect unauthorized modifications
3. Establish a trust chain independent of GitHub

**Current state:** `public.pem` contains:
```
-----BEGIN PGP PUBLIC KEY BLOCK-----

[Placeholder — generar clave real antes de publicación]

=TO BE GENERATED=
-----END PGP PUBLIC KEY BLOCK-----
```

This is entirely non-functional. Without a real key, no cryptographic verification is possible.

**Increment:**
1. Generate a real PGP key pair:
   ```bash
   gpg --full-generate-key
   # Choose: RSA and RSA, 4096 bits, no expiration, "State vs Family Evidence"
   gpg --armor --export "State vs Family Evidence" > public.pem
   ```
2. Store the private key securely (offline, encrypted)
3. Sign the built `index.html` with the private key:
   ```bash
   gpg --armor --detach-sign _site/index.html
   # Produces index.html.asc
   ```
4. Commit `public.pem` (public) and `index.html.asc` (signature) to the repo
5. Update `integrity.txt` with the real SHA256 hash (see METH-007)

---

### METH-007: Integrity Hash — PLACEHOLDER

**Project-Evidence precedent:** PE ships `integrity.txt` with the SHA256 hash of `index.html`, allowing readers to verify the document hasn't been tampered with.

**Current state:** `integrity.txt` contains:
```
SHA256 (index.html) = [hash pendiente — generar tras build]
```

**Current state in deploy workflow:** The GitHub Actions workflow (`deploy.yml`) does generate the hash at line 40:
```yaml
run: sha256sum _site/index.html > integrity.txt
```

However, this runs in the workflow's temporal runner — the generated `integrity.txt` is **never uploaded** or deployed (see METH-011 for the workflow bug).

**Increment:**
1. Fix the deploy workflow to include `integrity.txt` in the deployed site (see METH-011)
2. Pre-populate `integrity.txt` with a manual build hash for local verification:
   ```bash
   bundle exec jekyll build
   sha256sum _site/index.html > integrity.txt
   ```
3. Add the SHA256 hash display to the site (footer or integrity page)

---

### METH-008: Signature File — MISSING

**Project-Evidence precedent:** PE has a `signature` file (binary OpenPGP detach-signature of `index.html`). This allows PGP-based verification of document authenticity.

**Current state:** No signature file exists anywhere in the repository.

**Increment:**
1. After generating the PGP key (METH-006) and building the site, create the signature:
   ```bash
   gpg --armor --detach-sign _site/index.html
   mv _site/index.html.asc signature
   ```
2. Include `signature` in the deployed site
3. Update the deploy workflow to sign after build:
   ```yaml
   - name: Sign build
     run: |
       echo "${{ secrets.GPG_PRIVATE_KEY }}" | gpg --import
       gpg --armor --detach-sign --default-key "State vs Family Evidence" _site/index.html
       mv _site/index.html.asc _site/signature
   ```
4. Add a link to `signature` in the footer alongside `public.pem` and `integrity.txt`
5. Store the GPG private key as a GitHub Secret (`GPG_PRIVATE_KEY`)

---

## 4. DOCUMENT STRUCTURE (PE FRAMEWORK FEATURES)

### METH-009: Nomenclature / Glossary Section — INCOMPLETE

**Project-Evidence precedent:** PE has **§7 "Nomenclature"** — a full dedicated section at the top of the document defining every domain-specific term and acronym before the reader encounters claims. Examples:
- SARS, SARS-CoV-1, MERS-CoV, SARS-CoV-2, COVID-19
- Zoonotic virus, Patient Zero
- Spillover Event (with Wikipedia link and extended explanation)

This is placed **before** any claims, ensuring readers have the vocabulary to evaluate evidence.

**Current state:** The repository has "Anexo B — Glosario de denominadores (FD)" but:
- It is an **appendix** (at the end), not a prerequisite section
- It only covers FD denominators (4 entries), not the full domain vocabulary
- Missing definitions for: **NNyA**, **OVD**, **OVG**, **RVF**, **RNR**, **UFEM**, **UFEP**, **SNIC**, **BGD**, **FD**, **VG/VI**, **CePASI**, **MPF**, **DOVIC**, **CSJN**, **INDEC**, **IPP**, **art. 245 CP**, **art. 275 CP**, **art. 7 (ley 24.417)**

**Why it matters:** The document targets policymakers, journalists, and researchers who may not know these acronyms. PE's nomenclature section ensures accessibility. Without it, the document assumes domain knowledge that many readers won't have.

**Increment:** Create a new section (either as part of `00-methodology.md` or as a standalone `sections/00-nomenclature.md` included before the objective):

```markdown
### Nomenclatura

- **NNyA:** Niñas, Niños y Adolescentes (personas menores de 18 años)
- **OVD:** Oficina de Violencia Doméstica de la Corte Suprema de Justicia de la Nación (CSJN)
- **OVG:** Observatorio de Violencia contra las Mujeres (órgano del Consejo de la Magistratura)
- **RVF:** Registro de Violencia Familiar (Suprema Corte de Bs. As.)
- **RNR:** Registro Nacional de Reincidencia y Estadística Criminal
- **UFEM:** Unidad Fiscal Especializada en Violencia contra las Mujeres (MPF)
- **UFEP:** Unidad Fiscal Especial para el adults mayor y personas con discapacidad — fuente histórica de datos de condenas intrafamiliares (MPF)
- **SNIC:** Sistema Nacional de Información Criminal (Ministerio de Seguridad)
- **BGD:** Boletíndiario General de la CSJN
- **FD:** Falsa denuncia (art. 245 Código Penal)
- **VG/VI:** Violencia de género / Violencia intrafamiliar
- **CePASI:** Centro de Prevención, Asistencia y Solidaridad Infantil (ONG)
- **MPF:** Ministerio Público Fiscal de la Nación
- **DOVIC:** Dirección de Asistencia a la Víctima (MPF)
- **CSJN:** Corte Suprema de Justicia de la Nación
- **INDEC:** Instituto Nacional de Estadística y Censos
- **IPP:** Investigación Penal Preparatoria
- **art. 245 CP:** Falsa denuncia (delito del Código Penal argentino)
- **art. 275 CP:** Falso testimonio (delito del Código Penal argentino)
- **art. 7 (ley 24.417):** Medidas cautelares en violencia familiar (protección, exclusión del hogar, prohibición de acercamiento, suspensión de régimen de comunicación)
- **PBA:** Provincia de Buenos Aires
```

---

### METH-010: "Addressing Counter-Claims" Section — MISSING

**Project-Evidence precedent:** PE has a dedicated **§10 "Addressing Counter-Claims"** section where they systematically engage with opposing arguments:
- Paper 12 (a paper arguing against lab origin)
- @trvb Twitter thread (viral counter-argument)
- Scimex Expert Reactions (4 named experts with positions)

For each counter-claim, PE:
1. States the counter-claim clearly
2. Presents the evidence for it
3. Engages with it (accepts qualifications, identifies weaknesses, shows what it does/doesn't prove)

This is a **core methodology feature** of PE: it demonstrates that the authors have considered and engaged with the strongest counter-arguments, rather than cherry-picking.

**Current state:** There is **no counter-claims section** anywhere in the repository. The "Qué demuestra y qué no" table in §0 partially addresses this (listing what the study does NOT demonstrate), but:
- It only covers what the study "no demuestra" — it does not address external counter-arguments
- It does not engage with opposing positions or alternative interpretations of the same data
- It does not present the OVG's own conclusions and engage with them beyond quoting

**Why this matters for this specific domain:** There are significant counter-claims that the document should address:
1. **OVG's own conclusion:** "No existe evidencia de una proliferación de falsas denuncias que justifique una reforma penal." — The study uses OVG data but reaches different implications. This tension should be engaged.
2. **Protective rationale for measures:** The OVD data shows 3,182 presentations with NNyA — many of those measures protect children from real danger. The study's ratio analysis doesn't measure protective benefit.
3. **Undercounting thesis:** FD at 0.09% of the penal could reflect under-prosecution of FD rather than low prevalence. The study mentions this indirectly but should engage with it directly.
4. **CePASI vs. RNR:** CePASI claims 0.1% conviction rate; RNR data suggests ~15%. The study uses both but should directly address why they differ and which is more credible.
5. **Gender violence advocacy position:** Organizations argue that discussing FD prevalence endangers real victims by chilling reporting. This counter-argument should be stated and engaged with.

**Increment:** Create a new section `sections/07b-counter-claims.md` (or integrate as a subsection within §8 Discussion), following PE's structure:

```markdown
## Argumentos contrarios

### "No existe evidencia de proliferación de falsas denuncias"

La OVG concluye que el 0,09% de FD sobre el universo penal demuestra que no hay proliferación. Nuestro análisis no contradice este dato sino que **recontextualiza** la pregunta: el 0,09% usa un denominador (todo el penal) que no es el relevante para debates sobre VG/VI. Sobre FD clasificadas, VG/VI representa 8,9% a nivel nacional y hasta 61,5% en jurisdicciones con alta clasificación (Santa Fe). Estos números no se contradicen — miden preguntas distintas (ver Anexo B).

### "Las medidas cautelares protegen a NNyA en situación de riesgo real"

Es correcto. No toda medida cautelar es infundada ni todo ratio >1:1 implica abuso procesal. El estudio documenta **asimetría de escala**, no universalidad de daño. Sin embargo, la ausencia de datos sobre duración de medidas, restitución de contacto y resultado final de las causas impide evaluar la proporcionalidad de cada intervención. La evidencia internacional (Doyle 2007 WP 13291; Aizer & Doyle 2009 WP 19102; BCHM 2021) demuestra que la separación filial involuntaria y el encarcelamiento juvenil tienen costos causales medibles — los cuales no están siendo sopesados por el sistema.

### "Discutir FD pone en riesgo a víctimas reales"

Es un argumento legítimo con base empírica: la percepción de altas tasas de FD puede desincentivar denuncias. Sin embargo, la omisión del problema tiene costos propios: los 557–3.853 NNyA estimados en §7 Capa 3 son niños y adolescentes potencialmente separados de un progenitor sin base delictiva. Ninguna política basada en evidencia puede ignorar ambas caras del trade-off. Este estudio aporta datos para dimensionar la segunda cara, que carece de representación institucional.

### "CePASI vs. RNR: dos estimaciones de condena divergen"

CePASI estima ~2 condenas/año (0,1% de denuncias). RNR/UFEM estiman ~2.884 condenas/año (15% de denuncias). La diferencia de 3 órdenes de magnitud se explica porque CePASI aplica una tasa de 0,1% (1 de 1.000) que incluye múltiples filtros (sub-denuncia → denuncia → investigación → condena), mientras que RNR mide condenas comunicadas al registro. El RNR es un dato observado de fuente oficial; CePASI es una estimación de especialistas sin desglose metodológico público. Por esto, CePASI se clasifica como **Supuesto** y se usa solo como piso exploratorio.
```

---

### METH-011: Revisions / Version History — MISSING

**Project-Evidence precedent:** PE has **§13 "Revisions"** tracking every update to the document with date, description, and nature of change. This provides:
- Transparency about how the document evolved
- Accountability for corrections
- A paper trail for credibility

**Current state:** The document previously mentioned "iteraciones v1–v3" and was labelled "v6" with **no revision log**. As of v1.0.0 this is addressed: `sections/section-revisions.md` now contains a single row for v1.0.0 documenting the inaugural version. There is no precedent history to back-fill because v1.0.0 treats the work as a single consolidated release rather than a continuous iteration trail.

---

### METH-012: "If We're Right / If We're Wrong / Either Way" — STRUCTURALLY WEAK

**Project-Evidence precedent:** PE's **§6 "Purpose"** has three distinct, substantive subsections:
- **6.1 If We're Right:** Specific policy implications (hold Chinese government accountable, lab safety regulations, transparency)
- **6.2 If We're Wrong:** Specific alternative implications (find true origin, hold government accountable for natural outbreak causes)
- **6.3 Either Way:** Universal implications regardless of which scenario is true (condemn racism, spread awareness of biolab hazards, ask for due diligence)

Each subsection has **2–3 paragraphs of substantive content** about what the authors believe should happen. The structure forces intellectual honesty: regardless of the conclusion, here is what should change.

**Current state:** The "Propósito" in `sections/00-methodology.md` has:
1. "Si estamos en lo correcto:" — 1 sentence
2. "Si estamos equivocados:" — 1 sentence
3. "En cualquier caso:" — 1 sentence

These are too brief to carry the weight PE intended. They read as disclaimers rather than as substantive position statements.

**Increment:** Expand each point to match PE's depth:

```markdown
### Propósito

#### Si estamos en lo correcto

Si la asimetría entre medidas cautelares y condenas refleja intervención desproporcionada, el sistema de protección familiar necesita:
1. **Mecanismos de revisión periódica** de medidas cautelares que evalúen proporcionalidad y restitución de contacto filial con plazos definidos.
2. **Registros nacionales unificados** de medidas, duración y resultado final — no solo CABA/OVD.
3. **Evaluación de daño** antes de dictar medidas restrictivas, como recomienda Sankaran et al. (2020) y solo 2 jurisdicciones en EEUU requieren.

#### Si estamos equivocados

Si las medidas cautelares son proporcionales y el ratio alto refleja la extensión de la victimización no denunciada:
1. Los datos oficiales disponibles **no lo demuestran** — y esa es una laguna que el propio sistema debería llenar.
2. Las fuentes están abiertas para refutación. Si el RNR publica condenas intrafamiliares NNyA y el ratio se reduce significativamente, lo documentaremos.
3. Un sistema de protección robusto no debería temer la transparencia — debería requerirla.

#### En cualquier caso

1. Condenamos la violencia institucional contra NNyA.
2. Condenamos toda forma de violencia real contra mujeres, niños y adolescentes.
3. Abogamos por intervenciones basadas en evidencia donde el costo de la remoción filial se evalúe con la misma rigurosidad que el riesgo de la permanencia.
4. Los datos y fuentes están abiertos: este documento es verificable, reproducible y corregible.
```

---

## 5. TECHNICAL / BUILD INFRASTRUCTURE

### METH-013: Deploy Workflow — BROKEN (archive.zip and integrity.txt never deployed)

**Current state:** `.github/workflows/deploy.yml`

The workflow has two jobs: `build` and `deploy`. The `build` job:
1. Checks out code
2. Sets up Ruby + Bundler
3. Configures Pages
4. **Builds Jekyll** → `_site/`
5. **Uploads artifact** from `_site/` (step: "Upload artifact", uses `actions/upload-pages-artifact@v3`)
6. **Then** generates `archive.zip` (runs `cd _site && zip -r ../archive.zip .`)
7. **Then** generates `integrity.txt` (runs `sha256sum _site/index.html`)

The `deploy` job deploys the artifact uploaded in step 5. Steps 6 and 7 happen **after** the artifact has already been captured. Therefore:
- `archive.zip` is generated in the runner but **never uploaded or deployed**
- `integrity.txt` is generated in the runner but **never uploaded or deployed**
- The site footer links to `/archive.zip` and `/integrity.txt` — these will **404** on the live site

**Increment:** Restructure the `build` job so that `archive.zip` and `integrity.txt` are generated **before** the artifact upload:

```yaml
      - name: Build with Jekyll
        run: bundle exec jekyll build --baseurl "${{ steps.pages.outputs.base_path }}"
        env:
          JEKYLL_ENV: production
      - name: Generate archive
        run: cd _site && zip -r ../archive.zip . && mv ../archive.zip .
      - name: Generate integrity
        run: sha256sum _site/index.html > _site/integrity.txt
      - name: Sign build (optional, requires GPG key secret)
        # run: ...  
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./_site
```

Key change: move archive + integrity generation **before** the upload step. They will then be captured in the artifact and deployed to GitHub Pages.

---

### METH-014: Mobile Navigation — BROKEN

**Current state:** `_layouts/default.html` line 17 has:
```html
<button class="nav-toggle" aria-label="Toggle navigation">☰</button>
```

And `assets/css/style.scss` at line 188 hides `.nav-links` on mobile:
```css
@media (max-width: 768px) {
  .nav-links { display: none; }
  .nav-toggle { display: block; }
}
```

But there is **no JavaScript** to toggle the menu. Clicking ☰ on mobile does nothing.

**Increment:** Add a small inline script to `default.html` (or add a `assets/js/main.js` file):

```html
<script>
  document.querySelector('.nav-toggle').addEventListener('click', function() {
    document.querySelector('.nav-links').classList.toggle('show');
  });
</script>
```

And add CSS for the `.show` class:
```css
@media (max-width: 768px) {
  .nav-links.show { display: flex; flex-direction: column; position: absolute; top: 100%; left: 0; right: 0; background: var(--text-primary); padding: 1rem; }
}
```

---

### METH-015: Navigation Anchor Links — BROKEN

**Current state:** `_layouts/default.html` lines 18–21:
```html
<li><a href="{{ '/#resumen-ejecutivo' | relative_url }}">Resumen</a></li>
<li><a href="{{ '/#secciones' | relative_url }}">Secciones</a></li>
<li><a href="{{ '/#fuentes' | relative_url }}">Fuentes</a></li>
```

But `index.md` and none of the included section files have elements with `id="resumen-ejecutivo"`, `id="secciones"`, or `id="fuentes"`. These links will jump to the top of the page rather than to specific sections.

**Increment:** Either:
1. Add `id` attributes to the corresponding headings in the section files:
   - `sections/00-methodology.md`: add `{:#resumen-ejecutivo}` to the "Resumen Ejecutivo" heading
   - Create a TOC div with `id="secciones"` before the section includes
   - `sections/12-sources.md`: add `{:#fuentes}` to the "Fuentes primarias" heading
2. Or change the nav links to use the actual heading IDs that Kramdown auto-generates (e.g., `#resumen-ejecutivo`, `#intervención-cautelar-familiar`, etc.)

Option 1 is more robust.

---

### METH-016: Table of Contents — MISSING (CSS exists but unused)

**Current state:** `assets/css/style.scss` defines `.section-toc` styles (lines 159–162):
```css
.section-toc { background: var(--bg-light); border: 1px solid var(--border-light); padding: 1.25rem; border-radius: 4px; margin: 1.5rem 0; }
.section-toc ul { columns: 2; list-style: none; padding: 0; }
.section-toc li { margin: 0.3rem 0; }
.section-toc a { text-decoration: none; }
```

But **no section file** uses `.section-toc`. There is no in-page table of contents.

PE's site (built with Scribble) has a hierarchical sidebar/table of contents that allows jumping between sections. The current Jekyll site is a single long page with no navigation within the content.

**Increment:** Add a TOC section in `index.md` between the header and the section includes:

```markdown
<div class="section-toc" markdown="1" id="secciones">

### Secciones

- [§0. Encuadre metodológico](#encuadre-metodológico)
- [§1. Objetivo](#objetivo)
- [§2. Intervención cautelar familiar](#intervención-cautelar-familiar)
- [§3. Victimización infantil intrafamiliar](#victimización-infantil-intrafamiliar-observada)
- [§4. Falsas denuncias](#falsas-denuncias--intervalo-operativo)
- [§5. Universo penal](#universo-penal-condenas-por-integridad-sexual)
- [§6. Marco A](#marco-analítico-a--ratio-principal-nnya--nnya)
- [§7. Marco B](#marco-analítico-b--intensidad-de-intervención-y-daño-potencial)
- [§8. Discusión](#discusión)
- [§9. Limitaciones](#limitaciones)
- [§10. Trazabilidad](#trazabilidad-y-jerarquía-de-evidencia)
- [§11. Conclusiones](#conclusiones)
- [§12. Fuentes](#fuentes-primarias)
- [Anexo A — Fact-check](#anexo-a--verificación-rápida-fact-check)
- [Anexo B — Glosario](#anexo-b--glosario-de-denominadores-fd)

</div>
```

Note: Anchor IDs depend on Kramdown's auto-generation. Test after build to confirm exact IDs.

---

### METH-017: jekyll-scholar Dependency — UNUSED

**Current state:** `Gemfile` includes `gem "jekyll-scholar"` but:
- No `_bibliography/` directory exists
- No `scholar` configuration in `_config.yml`
- No `{% bibliography %}` tags in any content file
- No BibTeX files

`jekyll-scholar` adds significant Ruby dependencies (including nokogiri, which requires compilation) and increases build time. It serves no purpose in the current build.

**Increment:** Remove from `Gemfile`:
```ruby
source "https://rubygems.org"
gem "jekyll", "~> 4.3"
gem "webrick"
```

If bibliography management is desired in the future, it can be re-added with proper configuration. Alternatively, consider using a simpler approach (YAML data file in `_data/references.yml` + a custom include for citation rendering).

---

### METH-018: Empty Directories — DEAD STRUCTURE

**Current state:**
- `_data/` — empty (no YAML/JSON data files for programmatic access to statistics)
- `sources/` — empty (no archived PDFs or snapshots)
- `src/sections/` — empty (appears to be a leftover from an earlier build approach)
- `src/assets/` — empty (same)
- `docs/` — empty (README mentions "folder: /docs" deploy option but no content)

**Increment:**
1. **`_data/`:** Create `_data/sources.yml` with structured metadata for all sources (allows programmatic access and potential sidebar/hover generation):
```yaml
- id: ovd-2024
  name: "OVD — Informe Anual 2024"
  url: "https://www.csjn.gov.ar/novedades/detalle/9903"
  archived: null
  type: official
  year: 2024
```
2. **`sources/`:** Download and commit key PDFs (OVG FD, OVD NNyA, SCBA RVF) as local backup. Add a `sources/README.md` noting these are archived copies for verification.
3. **`src/`:** Remove the empty `src/sections/` and `src/assets/` directories — they serve no purpose and create confusion about the build structure.
4. **`docs/`:** Either remove it or populate it with the Jekyll build output for the "Deploy from branch: main, folder: /docs" option. If GitHub Pages is configured to use GitHub Actions (the current approach), `docs/` is unnecessary and should be removed.

---

### METH-019: validate.py — Hardcoded Path

**Current state:** `validate.py` line 8:
```python
BASE = r"C:\Users\German\Desktop\state-vs-family-evidence"
```

This only works on the original developer's machine. It will fail for any other contributor or in CI.

**Increment:** Replace with a relative path:
```python
BASE = os.path.dirname(os.path.abspath(__file__))
```

Or, if the script is meant to run from the repo root:
```python
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
```

Better yet, make it also accept a CLI argument:
```python
BASE = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
```

---

### METH-020: Site Footer — Links to non-existent files

**Current state:** `_layouts/default.html` line 31:
```html
<p><a href="{{ '/public.pem' | relative_url }}">Clave pública PGP</a> | <a href="{{ '/integrity.txt' | relative_url }}">Integridad</a> | <a href="{{ '/archive.zip' | relative_url }}">Descargar archivo completo</a></p>
```

All three links point to files that either:
- Don't exist on the deployed site (`archive.zip`, `integrity.txt` — see METH-013)
- Are placeholders (`public.pem` — see METH-006)

**Increment:**
1. Fix METH-013 first (deploy workflow)
2. Fix METH-006 (generate real PGP key)
3. After both are resolved, these links will work
4. Additionally, add the `signature` link (METH-008):
```html
<p><a href="{{ '/public.pem' | relative_url }}">Clave pública PGP</a> | <a href="{{ '/signature' | relative_url }}">Firma</a> | <a href="{{ '/integrity.txt' | relative_url }}">Integridad</a> | <a href="{{ '/archive.zip' | relative_url }}">Descargar archivo completo</a></p>
```

---

## Summary of Methodology Gaps

| ID | Category | Severity | Description |
|----|----------|----------|-------------|
| METH-001 | Governance | **High** | No Authors section in published site |
| METH-002 | Governance | Low | Correction policy lacks domain-specific triggers (enhancement) |
| METH-003 | Governance | Medium | Contribution policy incomplete (no templates, no repo link in site) |
| METH-004 | Source Integrity | **High** | Zero archived source links; policy unenforced |
| METH-005 | Source Integrity | Low | Sourcing policy missing non-official flagging and translation notes |
| METH-006 | Crypto | **Critical** | PGP key is placeholder — no verification possible |
| METH-007 | Crypto | **Critical** | Integrity hash is placeholder — no tamper detection |
| METH-008 | Crypto | **High** | No signature file — no authenticity verification |
| METH-009 | Document Structure | **High** | No nomenclature/glossary section — 20+ acronyms undefined |
| METH-010 | Document Structure | **High** | No "Addressing Counter-Claims" section — core PE methodology missing |
| METH-011 | Document Structure | Medium | Revision/version history — **addressed at v1.0.0** (single inaugural row in `sections/section-revisions.md`) |
| METH-012 | Document Structure | Medium | "If We're Right/Wrong" structurally weak — 1 sentence each vs PE's 2–3 paragraphs |
| METH-013 | Technical | **Critical** | Deploy workflow never deploys archive.zip or integrity.txt |
| METH-014 | Technical | Medium | Mobile navigation broken — no JS toggle |
| METH-015 | Technical | Medium | Nav anchor links reference non-existent IDs |
| METH-016 | Technical | Low | No in-page TOC (CSS exists but unused) |
| METH-017 | Technical | Low | jekyll-scholar dependency unused (bloated build) |
| METH-018 | Technical | Low | 5 empty directories (dead structure) |
| METH-019 | Technical | Low | validate.py hardcoded Windows path |
| METH-020 | Technical | Medium | Footer links to 3 non-existent/placeholder files |
| METH-021 | Document Structure | Medium | §13 Marco institucional complementario (Public Choice) + §13.4 Contexto judicial argentino + §13.5 Incentivo estructural de instrumentalización. Auditar: (a) que las 16 nuevas fuentes [24]–[39] están archivadas y son citables, (b) que el contenido no contradice el principio "asimetría, no acusación" del §0, (c) que la inclusión de CNAJ, Study.com y Periódicas (no oficiales) está etiquetada como tal, (d) que §13.4.1-2 no afirma prevalencia de FD real sino sesgo de registro, (e) que §13.4.4 proyectos legislativos presentados como descriptivos sin endoso, (f) que §13.5 identifica 5 condiciones de falsación explícitas y no afirma prevalencia de instrumentalización — solo incentivo estructural, (g) que la conclusión §11.7 afirma "no existe probabilidad descartable de daño sustancial" (no strawman), (h) que section-authors.md elimina disclaimers "no somos profesionales / no afiliados / disavowal" y sostiene posición epistemológica positiva (evidencia por trazabilidad, no credenciales). |
| METH-022 | Verification | Low | Post-publicación: re-evaluar condiciones de falsación de §13.5 a medida que se publiquen datos de FD de oficio post-archivo, revocatoria de cautelares, clasificación nacional completa, cruce provincial y tasa de desistimiento. Sin fecha fija. |

**Total: 22 methodology gaps** (3 critical, 6 high, 7 medium, 6 low)
