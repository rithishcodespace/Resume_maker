# 📋 Job & Internship Applications Ledger

This ledger tracks all targeted roles, company dossiers, and compilation statuses for **Rithish S**.

| Company Slug | Target Role / Title | Dossier Path | Status | Last Updated |
|---|---|---|---|---|
| `cloudsek` | CloudSEK - DevOps Intern | [dist/cloudsek/](dist/cloudsek/) | Ready / Dossier Built | 2026-09-22 |
| `microsoft` | Microsoft - Software Engineering Intern | [dist/microsoft/](dist/microsoft/) | Ready / Dossier Built | 2026-09-20 |
| `flam` | Flam - Software Engineering Intern | [dist/flam/](dist/flam/) | Ready / Dossier Built | 2026-10-02 |
| `honeywell` | Honeywell - Engineering Intern | [dist/honeywell/](dist/honeywell/) | Ready / Dossier Built | 2026-10-02 |
| `clickpost` | ClickPost - AI Engineer Intern | [dist/clickpost/](dist/clickpost/) | Ready / Dossier Built | 2026-10-02 |

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
