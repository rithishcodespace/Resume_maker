#!/usr/bin/env python3
"""
build.py - Modular Resume Build & Application Scaffolding Pipeline for Rithish S.

Usage:
  python3 build.py --new <company_slug>     # Scaffold a new company target
  python3 build.py <company_slug>           # Compile & audit a company target
  python3 build.py --all                    # Compile all company targets
"""

import os
import sys
import shutil
import subprocess
import json
import re
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
COMPANIES_DIR = os.path.join(ROOT_DIR, "companies")
TEMPLATE_DIR = os.path.join(COMPANIES_DIR, "_template")
DIST_DIR = os.path.join(ROOT_DIR, "dist")
APPLICATIONS_FILE = os.path.join(ROOT_DIR, "APPLICATIONS.md")

# Registry of company application metadata
METADATA_TITLES = {
    "cloudsek": {
        "title": "CloudSEK - DevOps Intern",
        "description": "DevOps internship targeting Linux, Docker, Kubernetes fundamentals, AWS, CI/CD automation, and infrastructure security.",
        "badge": "DevOps & Cloud Infra"
    }
}

def find_tex_compiler():
    """Detect local LaTeX compiler (tectonic, pdflatex, or xelatex)."""
    for comp in ["tectonic", "pdflatex", "xelatex"]:
        path = shutil.which(comp)
        if path:
            return comp
    # Check current directory / bin
    local_tectonic = os.path.join(ROOT_DIR, "bin", "tectonic")
    if os.path.exists(local_tectonic) and os.access(local_tectonic, os.X_OK):
        return local_tectonic
    return None

def scaffold_company(slug):
    """Scaffold a new company resume directory from template."""
    slug = slug.lower().strip().replace(" ", "_").replace("-", "_")
    target_dir = os.path.join(COMPANIES_DIR, slug)
    
    if os.path.exists(target_dir):
        print(f"[!] Company target '{slug}' already exists at: {target_dir}")
        return

    os.makedirs(target_dir, exist_ok=True)
    
    # Copy main.tex from template
    src_tex = os.path.join(TEMPLATE_DIR, "main.tex")
    dst_tex = os.path.join(target_dir, "main.tex")
    if os.path.exists(src_tex):
        shutil.copy2(src_tex, dst_tex)
    else:
        # Fallback to root main.tex
        shutil.copy2(os.path.join(ROOT_DIR, "main.tex"), dst_tex)

    # Create empty JD_Analysis.md
    jd_file = os.path.join(target_dir, "JD_Analysis.md")
    with open(jd_file, "w", encoding="utf-8") as f:
        f.write(f"""# Job Description Analysis: {slug.upper()}

**Date:** {datetime.now().strftime('%Y-%m-%d')}
**Target Role:** 
**Company:** {slug.capitalize()}

## 1. Role Requirements & Tier Classification
- **Tier 1 (Must-Have):** 
- **Tier 2 (Strongly Preferred):** 
- **Tier 3 (Preferred):** 
- **Tier 4 (Supporting):** 
- **Tier 5 (Generic):** 

## 2. Requirement vs. Evidence Gap Analysis
| Requirement | My Evidence | Match (Strong / Partial / Missing) |
|---|---|---|
| | | |

## 3. Custom Macros Strategy
- `\\resumeSubtitle`: 
- `\\customSkills`: 
- `\\customProjectsList`: 
""")

    print(f"[+] Successfully scaffolded company target: {slug}")
    print(f"    - LaTeX file:  companies/{slug}/main.tex")
    print(f"    - JD Analysis: companies/{slug}/JD_Analysis.md")
    print(f"    Next step: Fill JD_Analysis.md, set macro overrides in main.tex, then run: python3 build.py {slug}")

def build_company(slug):
    """Compile and validate resume for a specific company."""
    slug = slug.lower().strip().replace(" ", "_").replace("-", "_")
    company_dir = os.path.join(COMPANIES_DIR, slug)
    tex_file = os.path.join(company_dir, "main.tex")

    if not os.path.exists(tex_file):
        print(f"[-] Error: Target LaTeX file not found: {tex_file}")
        return False

    out_dir = os.path.join(DIST_DIR, slug)
    os.makedirs(out_dir, exist_ok=True)
    pdf_filename = f"rithish_s_resume_{slug}.pdf"
    out_pdf = os.path.join(out_dir, pdf_filename)
    dst_tex = os.path.join(out_dir, f"rithish_s_resume_{slug}.tex")
    shutil.copy2(tex_file, dst_tex)

    compiler = find_tex_compiler()
    compiled = False

    if compiler:
        print(f"[*] Compiling {tex_file} using {compiler}...")
        if "tectonic" in compiler:
            cmd = [compiler, tex_file, "--outdir", out_dir]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode == 0:
                # Rename generated pdf if needed
                generated_pdf = os.path.join(out_dir, "main.pdf")
                if os.path.exists(generated_pdf):
                    os.replace(generated_pdf, out_pdf)
                compiled = True
        else:
            cmd = [compiler, "-interaction=nonstopmode", f"-output-directory={out_dir}", tex_file]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode == 0:
                generated_pdf = os.path.join(out_dir, "main.pdf")
                if os.path.exists(generated_pdf):
                    os.replace(generated_pdf, out_pdf)
                compiled = True
    else:
        print("[!] Note: Local LaTeX compiler (tectonic/pdflatex) not found on PATH.")
        print("    Tailored LaTeX source is packaged at:")
        print(f"    -> {dst_tex}")
        print("    (You can compile directly via Overleaf or your local TeX editor).")

    # Character count and text length estimation from TeX source
    with open(tex_file, "r", encoding="utf-8") as f:
        tex_content = f.read()

    # Strip comments and common LaTeX commands to estimate visible text length
    clean_text = re.sub(r'%.*?\n', '\n', tex_content)
    clean_text = re.sub(r'\\[a-zA-Z]+(\[[^\]]*\])?(\{[^\}]*\})?', ' ', clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    char_count = len(clean_text)

    print(f"[*] Estimated ATS text payload: ~{char_count} characters (Optimal 1-page target: 3,000 - 3,800)")

    # Page count check if PDF was compiled
    if compiled and os.path.exists(out_pdf):
        pages = 0
        pdfinfo_bin = shutil.which("pdfinfo")
        if pdfinfo_bin:
            try:
                info_res = subprocess.run([pdfinfo_bin, out_pdf], capture_output=True, text=True)
                for line in info_res.stdout.splitlines():
                    if line.startswith("Pages:"):
                        pages = int(line.split(":")[1].strip())
                        break
            except Exception:
                pass
        if pages == 0:
            with open(out_pdf, "rb") as f:
                pdf_bytes = f.read()
            pages = len(re.findall(rb'/Type\s*/Page\b', pdf_bytes))

        print(f"[*] Exact Page Count: {pages} page(s)")
        if pages == 1:
            print("    [✓] STRICT 1-PAGE CONSTRAINT: PASSED")
        else:
            print(f"    [!] WARNING: Resume is {pages} page(s). Trim content to fit 1 page strictly!")

    # Write metadata.json
    meta = METADATA_TITLES.get(slug, {
        "title": f"{slug.capitalize()} - Tailored Application",
        "description": "Tailored ATS-optimized resume for Rithish S.",
        "badge": "Engineering"
    })
    meta["last_built"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    meta["slug"] = slug
    meta["estimated_char_count"] = char_count
    meta["compiled"] = compiled

    with open(os.path.join(out_dir, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

    # Write SUMMARY.txt
    with open(os.path.join(out_dir, "SUMMARY.txt"), "w", encoding="utf-8") as f:
        f.write(f"""========================================
APPLICATION DOSSIER: {slug.upper()}
========================================
Candidate:    Rithish S
Role/Target:  {meta.get('title', slug)}
Date:         {meta['last_built']}
Status:       {'PDF Compiled' if compiled else 'LaTeX Ready'}
Dossier Path: dist/{slug}/

Contents:
  1. rithish_s_resume_{slug}.tex (Tailored LaTeX Source)
  2. rithish_s_resume_{slug}.pdf ({'Generated' if compiled else 'Pending Local/Overleaf Compile'})
  3. metadata.json (Application tracking details)
========================================
""")

    print(f"[✓] Company dossier prepared at: dist/{slug}/")
    update_applications_tracker(slug, meta)
    return True

def update_applications_tracker(slug, meta):
    """Sync APPLICATIONS.md ledger."""
    if not os.path.exists(APPLICATIONS_FILE):
        with open(APPLICATIONS_FILE, "w", encoding="utf-8") as f:
            f.write("""# 📋 Job & Internship Applications Ledger

| Company Slug | Target Role / Title | Dossier Path | Status | Last Updated |
|---|---|---|---|---|
""")
    # Read existing
    with open(APPLICATIONS_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    entry_line = f"| `{slug}` | {meta.get('title', slug)} | [dist/{slug}/](dist/{slug}/) | Ready / Dossier Built | {datetime.now().strftime('%Y-%m-%d')} |\n"
    
    # Check if slug exists in table
    updated = False
    new_lines = []
    for line in lines:
        if f"| `{slug}` |" in line:
            new_lines.append(entry_line)
            updated = True
        else:
            new_lines.append(line)
    
    if not updated:
        new_lines.append(entry_line)

    with open(APPLICATIONS_FILE, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    print(f"[*] Synchronized entry in: {os.path.relpath(APPLICATIONS_FILE, ROOT_DIR)}")

def build_all():
    """Build all company targets under companies/."""
    if not os.path.exists(COMPANIES_DIR):
        print("[-] No companies directory found.")
        return
    
    entries = [d for d in os.listdir(COMPANIES_DIR) if os.path.isdir(os.path.join(COMPANIES_DIR, d)) and not d.startswith("_")]
    if not entries:
        print("[-] No company targets found in companies/. Use: python3 build.py --new <company_slug>")
        return
    
    print(f"[*] Building {len(entries)} company targets: {', '.join(entries)}")
    for slug in entries:
        print(f"\n--- Building {slug} ---")
        build_company(slug)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    arg = sys.argv[1]
    if arg == "--new":
        if len(sys.argv) < 3:
            print("Usage: python3 build.py --new <company_slug>")
            sys.exit(1)
        scaffold_company(sys.argv[2])
    elif arg == "--all":
        build_all()
    else:
        build_company(arg)
