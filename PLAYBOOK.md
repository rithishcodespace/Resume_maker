# 🔄 End-to-End Repeatable Resume Tailoring Playbook

> **Standard Operating Procedure (SOP) for tailoring Rithish S's modular LaTeX resume for ANY new job description.**  
> Follow this exact 6-phase pipeline to analyze, scaffold, tailor, quantify, compile, and track internship and full-time job applications.

---

## 🧭 The 6-Phase Pipeline Overview

```
[Phase 1: Ingestion & Analysis]
  Paste Job Description ➔ Run /job-description-analyzer ➔ Calculate Match Score & Gaps
        ↓
[Phase 2: Scaffolding]
  python3 build.py --new <company_slug> ➔ Register in build.py (METADATA_TITLES)
        ↓
[Phase 3: Content Tailoring & Skills Alignment]
  Set \resumeSubtitle ➔ Define \customSkills ➔ Define \customSSGBullets ➔ Define \customProjectsList
        ↓
[Phase 4: Bullet Engineering & Strict Truthfulness Guardrail]
  Apply Google X-Y-Z Formula + Power Verbs ➔ Consult Verified Facts Catalog ➔ Mandatory Grilling Protocol
        ↓
[Phase 5: Compilation, ATS Audit & Layout Validation]
  python3 build.py <company_slug> ➔ Verify Text Extraction (~3,200 - 3,700 chars) ➔ Verify Exact 1-Page Fit
        ↓
[Phase 6: Application Packaging, Safe File Picker & Tracking]
  Generate dist/<company_slug>/ Dossier ➔ Sync APPLICATIONS.md ➔ Ready for Workday/Keka/Lever/Greenhouse
```

---

## Phase 1: Ingest & Analyze the Job Description

Whenever a new job posting is found, start by analyzing requirements against candidate foundations:

### 1. Execute `/job-description-analyzer`
* **Extract Required (Must-Haves) vs Preferred (Nice-to-Haves)**.
* **Map Key Competencies**:
  * *Languages & Core CS* (e.g., C++, Java, Python, JavaScript, TypeScript, SQL, OOP, OS, Networks, DBMS)
  * *Backend & Distributed Systems* (Node.js, Express.js, Fastify, REST APIs, Redis, BullMQ, Caching, Concurrency)
  * *Databases & Cloud* (PostgreSQL, MySQL, MongoDB, SQLite, Redis, AWS S3/EC2, Docker, Linux, Prisma ORM)
  * *AI / GenAI* (Vector DBs/Pinecone, RAG pipelines, LLM Embeddings, Ollama, Qwen2.5)
  * *Frontend* (React, Tailwind CSS)
* **Keyword Tier Classification**:
  * **Tier 1 (Must-Have):** Explicitly required core technologies.
  * **Tier 2 (Strongly Preferred):** Repeated or strongly emphasized tools and frameworks.
  * **Tier 3 (Preferred):** Useful secondary technologies.
  * **Tier 4 (Supporting):** Broader ecosystem or domain concepts.
  * **Tier 5 (Generic):** Low-value generic terminology.
* **Calculate Alignment Score** (Target: 75%+).
* **Identify Strengths & Gaps**:
  * For matched skills $\rightarrow$ Highlight in top tier of Skills and lead project/experience bullets.
  * For transferable skills (e.g., MySQL $\rightarrow$ Relational DB fundamentals, Express $\rightarrow$ Fastify/REST) $\rightarrow$ Position foundational concepts accurately without making false claims.

---

## Phase 2: Scaffold the Company Resume Target

1. **Scaffold Directory**:
   ```bash
   python3 build.py --new <company_slug>
   ```
   *Example: `python3 build.py --new razorpay` creates `companies/razorpay/main.tex` and `companies/razorpay/JD_Analysis.md` from `companies/_template/`.*

2. **Register in `build.py` Metadata**:
   Open [build.py](file:///home/rithish/Desktop/projects/unprofessional/Resume_maker_analyzer/build.py) and add the entry to `METADATA_TITLES`:
   ```python
   "<company_slug>": {
       "title": "<Company> - <Job Title>",
       "description": "<1-sentence summary of targeted tech stack and focus area>.",
       "badge": "<Short Badge e.g. Backend Engineering, Distributed Systems, AI/RAG, Full Stack>"
   }
   ```

---

## Phase 3: Tailor Content & Section Overrides

Open `companies/<company_slug>/main.tex`. Apply company-specific macro overrides before `\begin{document}`:

### 1. Target Subtitle (Elevator Tagline)
```latex
\newcommand{\resumeSubtitle}{<Target Role Title> | <Top 2-3 Focus Areas>}
```
*Examples:*
* Backend/Distributed: `\newcommand{\resumeSubtitle}{Backend Engineer Intern | Distributed Systems, Scalable APIs \& Databases}`
* AI/RAG: `\newcommand{\resumeSubtitle}{AI / GenAI Engineer Intern | RAG Pipelines, Vector Search \& Backend Systems}`
* Full-Stack: `\newcommand{\resumeSubtitle}{Full Stack Developer Intern | React, Node.js \& Cloud Architectures}`

### 2. Custom Targeted Skills (`\customSkills`)
Categorize into scannable tiers reflecting the JD's exact priorities:
```latex
\newcommand{\customSkills}{%
  \textbf{Languages} {: <JD Languages e.g. Java, C++, Python, JavaScript, TypeScript, SQL>} \vspace{1pt} \\
  \textbf{Backend \& Systems} {: <JD Backend e.g. Node.js, Express.js, Fastify, REST APIs, Redis, BullMQ>} \vspace{1pt} \\
  \textbf{Databases \& Cloud} {: <JD Databases & DevOps e.g. PostgreSQL, MySQL, Redis, AWS S3, Docker, Linux, Prisma ORM>}%
}
```

### 3. Custom Experience Bullets (`\customSSGBullets`)
Reorder and reframe Students Special Group (SSG) Web Developer bullets to match the target responsibility:
* **Option A (Backend/DB Heavy):** Lead with relational schema design, REST API engineering, and MySQL queries for the Faculty Reward Points Dashboard.
* **Option B (Full Stack Heavy):** Lead with end-to-end Project Management Portal architecture using React, Node.js, and MySQL.
* **Option C (Collaboration/Mentorship):** Emphasize mentoring 50+ students in JS, backend patterns, and software engineering practices.

### 4. Custom Projects List (`\customProjectsList`)
Reframe project order and bullet emphasis to match the JD's core focus:
* **For Distributed Systems / Backend / DevOps roles:** Lead with **DB Backup CLI** (Redis, BullMQ, AES-256-GCM, Docker, AWS S3) followed by **PatentIQ** or **Leave Management System**.
* **For AI / ML / GenAI roles:** Lead with **PatentIQ | AI Prior-Art & RAG Engine** (Pinecone vector search, Qwen2.5, Fastify, RAG pipeline, Clean Architecture) followed by **Plantera** or **DB Backup CLI**.
* **For Systems / Tooling / Code Quality roles:** Feature the merged **ESLint Core** open-source contribution prominently (PR #21218, AST static analysis, IEEE 754 precision).

---

## Phase 4: Bullet Engineering & Strict Truthfulness Guardrails

Every bullet point should follow an achievement-focused structure:  
$$\text{Accomplished } [X] \text{ as measured by } [Y] \text{ by doing } [Z]$$

### ⚠️ Strict Truthfulness & Privacy Guardrails:
* **Never invent or synthesize metrics**: Every claim, metric, and tool MUST come strictly from user-provided facts or verified sources. Never generate numbers the user hasn't explicitly stated.
* **`[PLACEHOLDER]` Discipline**: If a metric or detail is missing and needed, insert `[PLACEHOLDER: verified metric needed]` and explicitly ask the user for the real number.
* **Zero Fabrication**: Do not invent user counts, latency percentages, throughput numbers, uptime numbers, or container reduction percentages.
* **Never add unconfirmed skills or tools**: NEVER add a technology (e.g. Go, Rust, Kafka, GCP) to the candidate's skills list or project bullets without asking and getting explicit confirmation first. The candidate must be 100% confident defending every item in technical interviews.

---

### 📚 Candidate Verified Facts Catalog (Rithish S)

- **Academic Credentials:**
  - Bachelor of Engineering in Computer Science and Engineering
  - Bannari Amman Institute of Technology, Sathyamangalam, Tamil Nadu (Aug. 2024 -- May 2028)
  - CGPA: **8.28/10**
- **Contact Details:**
  - Phone: `+91 99522 52304`
  - Email: `rithishcodespace@gmail.com`
  - LinkedIn: `linkedin.com/in/rithish-saravanan-32a39431a/`
  - GitHub: `github.com/rithishcodespace`
  - LeetCode: `leetcode.com/rithishcodespace`
- **Competitive Programming & Problem Solving:**
  - **1200+ Algorithmic Problems Solved** across LeetCode, CodeChef, and GeeksforGeeks.
  - Core areas: Dynamic Programming, Graph algorithms, Trees, Arrays, Greedy algorithms.
- **Open Source (Merged Core Contribution):**
  - **ESLint** (PR #21218) — Merged fix to ESLint's `no-loss-of-precision` rule.
  - Distinguishes genuine zero literals from non-zero decimals that underflow under IEEE 754 binary64.
  - Added regression test suite covering underflow, subnormal values, signed zero, and non-decimal literals; passed 43 CI checks.
- **Work Experience:**
  - **Web Developer @ Students Special Group (Student Organization)** (Feb. 2025 -- Dec. 2025):
    - Full-stack Project Management Portal (React, Node.js, MySQL).
    - REST APIs and relational database models for Faculty Reward Points Dashboard.
    - Mentored **50+ students** in JavaScript, backend development, and software engineering best practices.
- **Verified Projects Pool (Directly from github.com/rithishcodespace):**
  1. **DB Backup CLI (DBVault)** (*TypeScript, Node.js, Redis, BullMQ, AWS S3, Docker*):
     - Published to npm as `dbvault` and Docker Hub as `rithish2006/dbvault`.
     - **120 automated tests passed**.
     - Point-In-Time Recovery (PITR), cross-platform backup/restore for PostgreSQL, MySQL, MongoDB, SQLite.
     - Distributed job-processing with Redis & BullMQ (worker concurrency, queue limits, scheduler execution guards).
     - AES-256-GCM encryption, local key rotation, Redis-based distributed locking, automated S3 upload.
  2. **PatentIQ | AI Prior-Art & Novelty Engine** (*Node.js, Fastify, Python, PostgreSQL, Pinecone, Ollama, Prisma*):
     - Semantic prior-art search using Pinecone vector similarity and local LLM embeddings.
     - RAG patentability analysis pipeline with Qwen2.5 for claim-overlap analysis and technical risk scoring.
     - Fastify & Prisma/PostgreSQL backend using Clean Architecture, dependency injection, JWT auth, Zod validation.
  3. **Node & Kubernetes Observability (`node-monitoring-k8s`)** (*Kubernetes, Docker, Prometheus, Grafana, Node.js*):
     - Dockerized microservice deployed to Kubernetes (Minikube) with custom `deployment.yaml` and `service.yaml`.
     - Monitored real-time application and cluster metrics via dedicated **Prometheus and Grafana** pods.
  4. **Microservices CI/CD Orchestrator** (*GitHub Actions, Kubernetes, Go, Node.js, Python, React*):
     - End-to-end CI/CD orchestration for multi-language microservices using GitHub Actions composite actions.
     - Integrated GitOps-style Kubernetes manifests (`deploy/kubernetes/`), automated testing, and release management.
  5. **Humming Tone** (*TypeScript, Node.js, Express.js, PostgreSQL, Redis, Docker, AWS*):
     - Production-ready e-commerce platform built for a freelance client.
     - Secure authentication, RBAC, Redis caching, modular services, payment gateway integration, admin dashboard.
  6. **Plantera** (*React, Node.js, Express, Python, Mapbox, Tailwind CSS, Machine Learning*):
     - Real-time environmental monitoring platform for deforestation detection using satellite imagery and ML.
     - **1st place among 120+ teams** at IEEE DevSpark Hackathon (₹10,000 cash prize).
  7. **RAGForge & DocuRAG** (*Python, LangChain, ChromaDB, Embeddings, LLMs*):
     - Retrieval-Augmented Generation pipeline using recursive chunking, embeddings, ChromaDB, similarity search.
  8. **DevTinder & NetflixGPT** (*React, Redux Toolkit, Node.js, MongoDB / Firebase, TMDB API, OpenAI API*):
     - Full-stack developer networking platform (JWT, REST APIs) and AI-powered movie recommendation engine.
  9. **Leave Management System (LeaveMate)**:
     - Full-stack leave workflow system built under time constraints; **1st place among 200+ teams** at BIT Hackathon.
  10. **CampusMitra**: Academic workflow platform; **Top 10 among 150+ teams** at SNS Ideathon.

- **Official Certifications:**
  - **Oracle Cloud Infrastructure 2025 Certified Foundations Associate** (Oracle University, Credential: `103056584OCI25FNDCFA`, Oct 2025)
  - **AWS Cloud Practitioner Essentials** (AWS Training & Certification, Credential: `AWS-TRAINING-CERT`, July 2026)
  - **The Joy of Computing using Python — ELITE + TOPPER (TOP 5%)** (NPTEL, IIT Madras / Govt. of India, 95% score, Credential: `NPTEL26CS84S454501242`)
  - **Cisco Networking Academy | NDG:** Linux Unhatched (`CISCO-NDG-LINUX`)
  - **Cisco Networking Academy:** Operating Systems Basics (`CISCO-OS-BASICS`)
  - **Cisco Networking Academy | JS Institute:** JavaScript Essentials 1 (`CISCO-JS-ESS-1`)

---

### 🎯 Mandatory Grilling Protocol (Never Assume, Always Grill):
* Whenever an agent identifies an opportunity to add architectural depth, expand on a project, or quantify impact, **DO NOT invent or extrapolate**.
* Interview the user with targeted questions (`❓ Q1`, `➡️ Recommended`).
* Example:
  - `❓ Q1: For DB Backup CLI, what was the typical compression ratio or backup execution time?`
  - `❓ Q2: In PatentIQ, what embedding dimension or chunk size was configured in Pinecone?`
* Only after the user provides their verified answers does any bullet get drafted or updated.

---

## Phase 5: Compilation, ATS Audit & Layout Validation

### 1. Compile & Audit Target
```bash
python3 build.py <company_slug>
```

### 2. Verify Exact 1-Page Layout
Run the Python page count check:
```bash
python3 -c "import re; f=open('dist/<company_slug>/rithish_s_resume_<company_slug>.pdf','rb').read(); print('Pages:', len(re.findall(rb'/Type\s*/Page\b', f)))"
```
*Output must strictly be `Pages: 1`.*

### 3. Verify Clean ATS Plaintext Payload
Character count for a dense, single-page resume is between **3,000 and 3,800 characters**.
`build.py` automatically checks this text payload during every build:
```bash
python3 -c "import re; f=open('companies/<company_slug>/main.tex').read(); clean=re.sub(r'%.*?\n', '\n', f); clean=re.sub(r'\\[a-zA-Z]+(\[[^\]]*\])?(\{[^\}]*\})?', ' ', clean); print('Length:', len(re.sub(r'\s+', ' ', clean).strip()))"
```

---

## Phase 6: Application Packaging, Safe File Picker & Tracking

### 1. Zero-Error Directory Architecture (Company Dossiers)
All application deliverables output into **one dedicated folder per company** under `dist/`:

```text
dist/
├── <company_slug>/                       ← 📁 All materials in one single folder
│   ├── rithish_s_resume_<company_slug>.pdf
│   ├── rithish_s_resume_<company_slug>.tex
│   ├── metadata.json                     (Timestamp, role, target tech stack)
│   └── SUMMARY.txt                       (Human-readable log of application status)
│
└── general/                              ← 📁 Master Core Resume
    ├── rithish_s_resume_general.tex
    └── SUMMARY.txt
```

> [!TIP]
> **When applying on Workday, Keka, Lever, or Greenhouse:**
> - Open `dist/<company_slug>/`.
> - Pick `rithish_s_resume_<company_slug>.pdf` (or compile `rithish_s_resume_<company_slug>.tex` in Overleaf/locally).
> - There are **zero duplicate files** and **zero loose PDFs** anywhere else.

### 2. Log in [APPLICATIONS.md](file:///home/rithish/Desktop/projects/unprofessional/Resume_maker_analyzer/APPLICATIONS.md)
Update the central tracker ledger automatically with company name, role, direct dossier links, and timestamp.

---

## ⚖️ Reality Check: Is the Website & GitHub Actions Really Necessary?

### 1. What ATS & Hiring Portals Actually Care About
* **ATS Bots (Workday, Keka, Lever, Greenhouse, Taleo) do NOT crawl websites.**
* When applying, the ATS strictly parses the **raw PDF file** that you upload.
* A recruiter opening your application inside their applicant dashboard reads that PDF directly.
* Therefore: **For applying to jobs, the local LaTeX build (`python3 build.py`) and your PDF files are 100% sufficient.** You do NOT need a website to get shortlisted or hired.

### 2. What GitHub Actions / Web Showcases ARE Useful For
* **LinkedIn & Portfolio Showcase:** Linking a portfolio/resume showcase on your LinkedIn or GitHub bio lets recruiters view your projects interactively.
* **Cloud Compilation Backup:** If you edit LaTeX from a mobile device or a machine without TeX installed, GitHub Actions can build the PDFs for you.

---

## 🤖 Agent Skills Integration

Antigravity automatically detects your task stage and applies best practices from the relevant skills:
* **Job Analysis:** Automatically applies `job-description-analyzer` to parse keywords, score alignment, and find gaps.
* **Bullet Engineering:** Automatically applies `resume-bullet-writer` and `resume-quantifier` (Google X-Y-Z framework, power verbs, hard metrics).
* **ATS Formatting:** Automatically applies `resume-ats-optimizer` and `resume-formatter` (single-page layout, ATS plaintext glyphs).

### When You Can Call Skills Manually:

| Skill / Command | When to Ask For It | What It Delivers |
| :--- | :--- | :--- |
| **`interview-prep-generator`** | *"Run interview prep for Google / Razorpay"* | Generates STAR stories, technical deep-dive questions, and talking points. |
| **`cold-email-writer`** | *"Write a cold email to hiring manager / founder"* | Generates high-converting, concise outreach messages for LinkedIn or email. |
| **`salary-negotiation-prep`** | *"Prepare compensation strategy for Bangalore / Hyderabad"* | Generates market comp benchmarks, counter-offer scripts, and leverage points. |
| **`portfolio-case-study-writer`**| *"Turn PatentIQ / DB Backup CLI into a case study"* | Converts resume bullets into full markdown engineering case studies. |
| **`application-form-filler`** | *"Fill this application form"* | Drafts tailored, context-aware answers to open-ended job portal questions. |
