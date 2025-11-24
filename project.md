---
slug: github-gas-jnapolitano-io
id: github-gas-jnapolitano-io
title: gas.jnapolitano.io
repo: justin-napolitano/gas.jnapolitano.io
githubUrl: https://github.com/justin-napolitano/gas.jnapolitano.io
generatedAt: '2025-11-24T21:34:50.462Z'
source: github-auto
summary: >-
  This repository hosts the source and deployment scripts for the
  energy.jnapolitano.io site, which provides detailed documentation and analysis
  on US power plants, natural gas infrastructure, and carbon storage facilities.
  It includes automated build, deployment, and backup tools to maintain the
  site.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: project
entryLayout: project
showInProjects: true
showInNotes: false
showInWriting: false
showInLogs: false
---

This repository hosts the source and deployment scripts for the energy.jnapolitano.io site, which provides detailed documentation and analysis on US power plants, natural gas infrastructure, and carbon storage facilities. It includes automated build, deployment, and backup tools to maintain the site.

## Features

- Documentation site built with Sphinx and Jupyter Notebooks
- Automated build and deployment scripts using Makefile and Bash
- Backup integration with Dropbox API
- Content covering US power plants, natural gas networks, and carbon storage
- Bibliography management for references and legal documents

## Tech Stack

- Python 3.5+ (for scripts and Sphinx extensions)
- Jupyter Notebooks (primary language for content)
- Sphinx documentation builder with extensions (ablog, myst_nb, sphinx_copybutton, etc.)
- Bash scripting for deployment and maintenance
- Dropbox SDK for Python (backup scripts)
- Makefile for build automation

## Getting Started

### Prerequisites

- Python 3.5 or higher
- pip package manager
- Dropbox API access token (for backup functionality)
- Make utility

### Installation

1. Clone the repository:

```bash
git clone https://github.com/justin-napolitano/gas.jnapolitano.io.git
cd gas.jnapolitano.io
```

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

3. (Optional) Install dependencies for Rocky Linux:

```bash
pip install -r requirements_rocky.txt
```

### Build the Documentation

Run the following command to clean and build the HTML documentation:

```bash
make clean
make html
```

### Deploy the Site

Deploy the built documentation to GitHub Pages:

```bash
./deploy.sh
```

### Backup

To back up the built HTML to Dropbox, configure the access token in `backup_html.py` and run:

```bash
python backup_html.py
```

## Project Structure

```
acp.sh                # Bash script, purpose assumed related to access control or permissions
backup_html.py        # Python script to back up built HTML files to Dropbox
chtml.sh              # Bash script, likely for cleaning/building HTML
deploy.sh             # Bash script to deploy site to GitHub Pages
deployz.sh            # Variant deploy script
doit.sh               # General purpose automation script
install.sh            # Installation script
label_list.py         # Python script to read and print label info from Sphinx pickle files
Makefile              # Build automation for cleaning and building docs
pullit.sh             # Bash script to pull latest changes
pushit.sh             # Bash script to push commits
python_build.py       # Python build pipeline automation
requirements.txt      # Python dependencies
requirements_rocky.txt# Python dependencies for Rocky Linux
requirments.txt       # Possibly a misspelled duplicate requirements file
source/               # Sphinx documentation source files
todo/                 # Notes and TODOs
uninstall.sh          # Script to uninstall or clean environment
```

## Future Work / Roadmap

- Improve documentation and comments in scripts for clarity
- Add automated testing for build and deployment processes
- Enhance backup script with incremental backup and restore features
- Expand content coverage on energy infrastructure
- Refactor and unify deployment scripts for consistency
- Correct typos in filenames (e.g., `requirments.txt`)

