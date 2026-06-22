# Validation Cheatsheet — Reference

This file is loaded on demand from `AGENTS.md §3`. Read when:

- Running validation and need a quick command reference
- A METH check fails and you need to understand what it checks
- Adding a new audit item

---

## Commands

```bash
# Fast gate (no build, source-only)
python validate_ci.py

# Full build + integrity + signing + link check
python validate_ci.py --with-build

# Validate one specific issue
python -c "
from validate_ci import *
# ... or just open the file and run individual sections
"
```

---

## All METH checks (idempotent, order-stable)

```
[CHECK  ] METH-001 Authors / anonymity section
[CHECK  ] METH-002 Correction policy depth
[CHECK  ] METH-003 Contribution policy completeness
[CHECK  ] METH-004 Source archiving (WARN-only)
[CHECK  ] METH-005 Sourcing policy specificity
[CHECK  ] METH-006 PGP key (real vs placeholder)
[CHECK  ] METH-007 Integrity hash
[CHECK  ] METH-008 Signature file
[CHECK  ] METH-009 Nomenclature / glossary
[CHECK  ] METH-010 Counter-claims section
[CHECK  ] METH-011 Revision log
[CHECK  ] METH-012 Purpose depth
[CHECK  ] METH-013 Deploy workflow order
[CHECK  ] METH-014 Mobile nav toggle
[CHECK  ] METH-015 Nav anchor links
[CHECK  ] METH-016 In-page TOC
[CHECK  ] METH-017 jekyll-scholar
[CHECK  ] METH-018 Empty directories
[CHECK  ] METH-019 validate.py path
[CHECK  ] METH-020 Footer links
[BUILD  ] Jekyll build (only with --with-build)
```

Any new audit item MUST be added as `METH-NNN` and integrated into `validate_ci.py` before being referenced in this file.
