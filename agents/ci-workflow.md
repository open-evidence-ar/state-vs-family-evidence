# CI Workflow — Reference

This file is loaded on demand from `AGENTS.md §3`. Read when touching `.github/workflows/deploy.yml`, crypto files, or diagnosing deployment regressions.

---

## Pipeline diagram

```
                 push
                  │
                  ▼
   ┌──────────────────────────────┐
   │  .github/workflows/deploy.yml │
   │                                │
   │  1. checkout                   │
   │  2. ruby/setup-ruby            │
   │  3. configure-pages            │
   │  4. jekyll build         ───────────────────┐
   │  5. zip _site   → archive.zip │              │
   │  6. sha256 index.html → integrity.txt│       │
   │  7. gpg sign   index.html  → signature    │ │
   │  8. upload-pages-artifact    │              │ │
   │     (path: ./_site)          ▼              ▼ │
   └──────────────────────────────┘     _site/  contains everything
                    │
                    ▼
                  deploy job
                    │
                    ▼
              GitHub Pages live
       (pem / signature / integrity / archive all 200)
```

---

## Failure modes

- If step 5 fails: METH-013 regressed.
- If step 7 fails and `GPG_PRIVATE_KEY` secret is unset: deployment still succeeds but `signature` 404s — this is acceptable in dev but not production.
- If step 8 happens BEFORE 5/6/7: METH-013. The order above is the correct order.
