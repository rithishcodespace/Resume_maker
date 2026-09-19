# 📑 Application Summary: CloudSEK — DevOps Intern

**Company:** CloudSEK  
**Role:** DevOps Intern  
**Location:** Bengaluru, Karnataka, India  
**Application Type:** Internship  
**Dossier Location:** `dist/cloudsek/`  
**LaTeX Source:** `companies/cloudsek/main.tex` (and `dist/cloudsek/rithish_s_resume_cloudsek.tex`)  

---

## 🎯 Top JD Requirements
1. **Kubernetes Architecture & Operations**: Assisted deployment and troubleshooting of clusters (EKS/GKE/AKS).
2. **Linux Administration & Scripting**: Shell/Bash and Python scripting to automate operational tasks and reduce manual toil.
3. **Containers & Traffic Ingress**: Docker containerization, NGINX Ingress / NGINX Gateway, and routing rules.
4. **CI/CD Pipelines & Automation**: Automated workflows, continuous integration, and test suites (GitHub Actions, Jenkins).
5. **Cloud Infrastructure (AWS)**: Core understanding of VPC, IAM, S3, and EC2 instance management.
6. **Observability & Autoscaling**: Prometheus, Grafana, Loki, and Karpenter node provisioning.

---

## 🟢 Strong Matches
1. **Kubernetes & Cluster Observability**: Real hands-on experience deploying Dockerized microservices on Kubernetes with `deployment.yaml` and `service.yaml`, and instrumenting with **Prometheus** and **Grafana** (`node-monitoring-k8s`).
2. **Linux System Administration & Scripting**: Strong mastery of Linux environments, POSIX process management, file permissions, Shell/Bash scripting, and Python automation. Certified: **Cisco Linux Unhatched** & **Cisco OS Basics**.
3. **Containerization**: Hands-on Docker experience packaging CLI utilities published on **Docker Hub** (`rithish2006/dbvault`) and multi-container microservice workflows.
4. **Cloud Services & Certifications**: Deep experience with AWS S3 object storage APIs, bucket policies, and AWS EC2 compute. Officially Certified: **AWS Cloud Practitioner Essentials** and **Oracle Cloud Foundations Associate**.
5. **CI/CD & Code Quality Verification**: Continuous integration discipline via GitHub Actions (`microservices-ci-cd-orchestrator`); ESLint core contribution passing **43 automated CI checks**; **120 automated test suite** in DBVault.
6. **Distributed Systems & Queues**: Architecture of Redis & BullMQ job-processing systems with worker concurrency and distributed locking.
7. **Security & Cryptography**: Native alignment with CloudSEK's cybersecurity focus through verified implementation of **AES-256-GCM encryption**, key rotation, and JWT authentication.

---

## 🟡 Partial Matches
1. **Traffic Routing & Ingress**: Experience with NGINX reverse proxy configuration and REST/HTTP routing; Gateway API (HTTPRoute) is conceptual.
2. **GitOps Workflow**: Forked and explored ArgoCD; implemented GitOps-style declarative Kubernetes manifests in `microservices-ci-cd-orchestrator`.

---

## 🔴 Missing Requirements (Gaps Identified)
1. **Karpenter Autoscaling**: No prior hands-on production setup of Karpenter (NodePools, EC2NodeClass).

---

## 📦 Projects Selected
1. **DB Backup CLI (DBVault)** (*TypeScript, Node.js, Redis, BullMQ, AWS S3, Docker*):
   * *Rationale:* Demonstrates pure disaster-recovery and infrastructure engineering—Docker Hub publication, 120 passing automated tests, multi-database dump orchestration (PostgreSQL, MySQL, MongoDB, SQLite), Redis distributed worker queues, automated cron scheduling, and AWS S3 cloud offloading.
2. **K8s Cluster Observability & Monitoring (`node-monitoring-k8s`)** (*Kubernetes, Docker, Prometheus, Grafana, Node.js, Linux*):
   * *Rationale:* Directly provides verified proof of CloudSEK's core Tier 1 and Tier 2 requirements: Kubernetes manifest design, pod provisioning, Prometheus scraping, Grafana visualization, and container health probes.
3. **ESLint Core Merged Contribution (PR #21218)**:
   * *Rationale:* Concrete proof of rigorous testing, static analysis, precision engineering, and passing 43 CI test suites before merge into a world-class codebase.

---

## 🔑 Most Important Keywords Used
* `Docker`, `Kubernetes (Fundamentals)`, `AWS (EC2, S3, IAM, VPC)`, `GitHub Actions`, `CI/CD`, `Nginx`
* `Linux (System Administration, Bash)`, `Python`, `TypeScript`, `Redis (Distributed Queues & Locks)`
* `Automated scheduling`, `gzip compression`, `SHA-256 checksums`, `AES-256-GCM encryption`, `Distributed locking`

---

## 🔄 Major Resume Changes Made
1. **Elevator Subtitle Added:** `DevOps Intern | Cloud Infrastructure, Docker, Linux & CI/CD Automation`.
2. **Skills Restructured:** Promoted **Cloud & DevOps** and **Systems & Scripting** to the top tiers ahead of frontend technologies.
3. **DB Backup CLI Re-framed:** Emphasized Docker containerization, distributed queue concurrency, AWS S3 offloading, and cryptographic data integrity.
4. **Experience Bullets Tuned:** Positioned SSG Web Developer bullets around internal workflow portals, API reliability, relational schema indexing, and mentoring 50+ students in Linux & backend design.

---

## 💡 Interview Positioning Strategy for Gaps
* **When asked about Karpenter:**
  > *"While I haven't configured Karpenter in production yet, I understand its architecture—using NodePools and EC2NodeClass to provision right-sized nodes directly through AWS APIs rather than relying on standard auto-scaling groups. In my DB Backup CLI project, I engineered worker concurrency and distributed queue processing with Redis, so I'm very familiar with the mechanics of scaling worker capacity under load."*
* **When asked about Prometheus / Grafana:**
  > *"In my projects, my observability has centered around application-level logging, job failure retries, and checksum auditing. I understand the pull-based metrics model of Prometheus and exporter architecture, and I am eager to get hands-on with CloudSEK's production monitoring stack."*
