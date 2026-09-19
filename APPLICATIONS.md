# 📋 Job & Internship Applications Ledger

This ledger tracks all targeted roles, company dossiers, and compilation statuses for **Rithish S**.

| Company Slug | Target Role / Title | Dossier Path | Status | Last Updated |
|---|---|---|---|---|

---

## 📁 Dossier Architecture

Each company application outputs directly to `dist/<company_slug>/`:

```text
dist/
└── <company_slug>/
    ├── rithish_s_resume_<company_slug>.tex   # Tailored LaTeX source
    ├── rithish_s_resume_<company_slug>.pdf   # ATS-optimized 1-page PDF
    ├── metadata.json                         # Role, timestamp, payload stats
    └── SUMMARY.txt                           # Quick-reference human-readable dossier log
```
