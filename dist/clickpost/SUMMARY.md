# 📑 Application Summary: ClickPost — AI Engineer Intern

**Company:** ClickPost Technologies (Bangalore, Karnataka, India [In-Office])  
**Role:** AI Engineer - Internship (6 Months, Paid with full-time potential)  
**Department:** Product  
**Experience Level:** 0--1 Years of Experience  
**Company Profile:** Market-leading post-purchase intelligence platform serving 450+ global brands (Walmart, Nykaa, Mars, Adidas, Bluestone, GIVA) managing 50M+ monthly shipments across 600+ carriers; actively building the enterprise agentic layer for post-purchase logistics.  
**Dossier Location:** `dist/clickpost/`  
**LaTeX Resume Source:** `companies/clickpost/main.tex` (and `dist/clickpost/rithish_s_resume_clickpost.tex`)  
**Compiled Resume PDF:** `dist/clickpost/rithish_s_resume_clickpost.pdf` (Strictly 1 Page)  
**Cover Letter Source:** `companies/clickpost/cover_letter.tex` & `companies/clickpost/COVER_LETTER.md`  
**Compiled Cover Letter PDF:** `dist/clickpost/rithish_s_cover_letter_clickpost.pdf` (Strictly 1 Page)  

---

## 🎯 Top JD Requirements & 1-to-1 Resume Mapping

| ClickPost JD Requirement | Candidate Evidence & Resume Positioning |
|---|---|
| **Setting up ClickPost MCP servers & AI Agents** | **PatentIQ**: Architected an autonomous AI agent workflow leveraging the **Model Context Protocol (MCP)** and dynamic **tool calling**, orchestrating vector retrieval tools, patent claim parsers, and research APIs. |
| **RAG systems on logistics and operational data & Vector DBs** | **PatentIQ**: Built low-latency RAG pipeline with **Pinecone** vector embeddings and local LLMs (**Qwen2.5 via Ollama**) to automate unstructured technical document analysis, semantic claim overlap, and novelty risk scoring. |
| **Redis / queues / async workflows** | **DB Backup CLI (DBVault)**: Engineered distributed job scheduling using **Redis and BullMQ**, enforcing worker concurrency, rate-limits, execution guards, and Redis distributed locking. |
| **Python fundamentals & Backend APIs (FastAPI / Flask)** | **IIT Madras Python Elite + Topper (Top 5%, 95% score)**. Built Clean Architecture backend in **Fastify/Python** with dependency injection, strict validation, and high-throughput REST endpoints. |
| **Building rigorous evals framework & High Reliability** | **DBVault**: **120 automated unit/integration tests**. **ESLint Core**: Comprehensive regression test suites passing **43 automated CI verification checks**. Validates strict evaluation and test-driven rigor. |
| **Prior 3rd-party open-source work** | **ESLint Core (PR #21218)**: Merged fix to ESLint's `no-loss-of-precision` AST rule, resolving IEEE 754 binary64 floating-point underflow edge cases. |
| **Full-Stack Application Deployment ("Laptop to Prod")** | Full-stack Project Management Portal (React, Node.js, MySQL). Docker Hub & npm publisher (`dbvault`). Certified **Oracle Cloud Associate (OCI 2025)** & **AWS Cloud Practitioner**. |
| **Strong problem-solving ability & Fast execution** | **1200+ Algorithmic Problems Solved** across LeetCode, CodeChef, and GeeksforGeeks. **1st place among 120+ teams** (IEEE DevSpark) and **1st place among 200+ teams** (BIT Hackathon). |

---

## 🟢 Strong Matches & Key Competitive Advantages

1. **Direct Model Context Protocol (MCP) Implementation:** ClickPost explicitly states *"Setting up ClickPost MCP servers"*. PatentIQ is built on the MCP architecture, making Rithish one of the vanishingly few intern candidates with practical hands-on MCP experience.
2. **Deep Redis & Async Queue Engineering:** ClickPost requires *"Redis / queues / async workflows"*. DB Backup CLI's core architecture is built around BullMQ concurrency, scheduler guards, and Redis distributed locks.
3. **World-Class Open Source Proof:** ClickPost lists *"Prior 3rd-party open-source work"* as an asset. Rithish's merged contribution to ESLint Core demonstrates software craftsmanship and rigor verified by senior maintainers worldwide.
4. **Verified Python Mastery:** Official IIT Madras Python Topper credential (Top 5%, 95% score) proves deep language fundamentals.
5. **Builder DNA ("Laptop to Production"):** Experience publishing npm packages, Docker Hub containers, and winning competitive hackathons reflects ClickPost's core values of speed, ownership, and practical shipping.

---

## 💡 Interview Talking Points Tailored for ClickPost

* **When asked about MCP (Model Context Protocol) & AI Agents:**
  > *"In PatentIQ, I engineered an autonomous agent workflow using the Model Context Protocol (MCP) and tool-calling interfaces. Instead of chaining fragile static prompts, the agent dynamically discovers and invokes structured tools—such as Pinecone vector similarity search, patent claim parsers, and external research endpoints. This decoupled architecture allows tools to be added or modified without breaking agent reasoning, which is directly applicable to setting up ClickPost's internal MCP servers across logistics tools and carrier databases."*

* **When asked about RAG, Vector Search & Embeddings:**
  > *"In PatentIQ, I implemented a retrieval-augmented generation (RAG) pipeline to analyze complex technical claims. I used Pinecone vector embeddings for semantic similarity search paired with local LLMs (Qwen2.5 via Ollama) to synthesize claim-overlap evaluations and compute quantitative technical novelty scores. This same approach maps cleanly to building internal search systems across ClickPost's shipping logs, carrier dashboards, and operational runbooks."*

* **When asked about Redis, Queues & Async Pipelines:**
  > *"In DB Backup CLI (DBVault), I built an asynchronous distributed job-processing engine powered by Redis and BullMQ. I implemented worker concurrency controls, queue rate limits, and Redis-based distributed locking to guarantee zero duplicate execution and zero data loss during high-load operations. ClickPost handles 50M+ shipment events monthly, so understanding how to queue events, manage worker pools, and prevent race conditions is critical for production stability."*

* **When asked about Evaluation Frameworks & Software Quality:**
  > *"Applied AI systems in production cannot rely on gut feeling; they need deterministic evaluation benchmarks and unit testing. In DB Backup CLI, I authored 120 automated unit and integration tests. In my contribution to ESLint Core (PR #21218), I wrote a comprehensive regression test suite covering subnormal numbers and signed zeros under IEEE 754 precision, passing 43 CI checks. I bring that same evaluation rigor to benchmarking prompt outputs, hallucination rates, and tool invocation accuracy."*

* **When asked about Fast Prototyping & Ownership:**
  > *"I love taking ideas from 'works on my laptop' to deployed production systems. Whether it's publishing `dbvault` to npm and Docker Hub, deploying microservices to cloud environments, or winning 1st place among 120+ teams at the IEEE DevSpark Hackathon, I thrive in environments where speed, ownership, and solving real user problems take priority."*
