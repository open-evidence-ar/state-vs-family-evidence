"""Script de validación de estructura — no requiere Ruby ni Jekyll"""
import os
import sys

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") if len(sys.argv) < 2 else sys.argv[1]) if not os.path.basename(os.path.dirname(os.path.abspath(__file__))) == "state-vs-family-evidence" else os.path.dirname(os.path.abspath(__file__))
if not os.path.isfile(os.path.join(BASE, "_config.yml")):
    BASE = os.path.dirname(os.path.abspath(__file__))

required = {
    "index.md": "Página principal",
    "_config.yml": "Configuración Jekyll",
    "_layouts/default.html": "Layout base",
    "public.pem": "Clave pública PGP",
    "integrity.txt": "Integridad",
    "README.md": "Documentación",
    "Gemfile": "Dependencias Ruby",
    ".github/workflows/deploy.yml": "GitHub Actions deploy",
}

sections = [
    "00-methodology", "01-objective", "02-intervention", "03-victimization",
    "04-false-allegations", "05-penal-convictions", "06-framework-a",
    "07-framework-b", "08-discussion", "09-limitations", "10-evidence-hierarchy",
    "11-conclusions", "12-sources", "annex-a-factcheck", "annex-b-glossary",
]

tags = ["observado", "derivado", "supuesto", "exploratorio", "calculo", "fuente", "nnya", "ratio"]

errors = []

for path, desc in required.items():
    full = os.path.join(BASE, path)
    if not os.path.isfile(full):
        errors.append(f"FALTA: {path} ({desc})")

for s in sections:
    path = os.path.join(BASE, "sections", f"{s}.md")
    if not os.path.isfile(path):
        errors.append(f"FALTA sección: sections/{s}.md")

for t in tags:
    path = os.path.join(BASE, "_includes", "tags", f"{t}.html")
    if not os.path.isfile(path):
        errors.append(f"FALTA tag: _includes/tags/{t}.html")

if errors:
    print("ERRORES DE ESTRUCTURA:")
    for e in errors:
        print(f"  ❌ {e}")
    sys.exit(1)
else:
    print("✅ Estructura completa — todos los archivos requeridos existen")
    print(f"   📄 {len(required)} archivos raíz")
    print(f"   📝 {len(sections)} secciones")
    print(f"   🏷️  {len(tags)} tags de evidencia")
