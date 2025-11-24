---
slug: github-gas-jnapolitano-io-note-technical-overview
id: github-gas-jnapolitano-io-note-technical-overview
title: gas.jnapolitano.io Overview
repo: justin-napolitano/gas.jnapolitano.io
githubUrl: https://github.com/justin-napolitano/gas.jnapolitano.io
generatedAt: '2025-11-24T18:36:38.607Z'
source: github-auto
summary: >-
  This repo contains the source and deployment scripts for
  energy.jnapolitano.io, a site focused on US energy infrastructure, including
  power plants and carbon storage. It uses Sphinx and Jupyter Notebooks for
  documentation and supports automated builds and backups.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: note
entryLayout: note
showInProjects: false
showInNotes: true
showInWriting: false
showInLogs: false
---

This repo contains the source and deployment scripts for energy.jnapolitano.io, a site focused on US energy infrastructure, including power plants and carbon storage. It uses Sphinx and Jupyter Notebooks for documentation and supports automated builds and backups.

## Key Components:
- **Tech Stack**: Python 3.5+, Sphinx, Jupyter Notebooks, Bash, and Dropbox API.
- **Scripts**: 
  - `deploy.sh` for deploying to GitHub Pages.
  - `backup_html.py` for Dropbox backups.

## Quick Start:
1. Clone the repo:
    ```bash
    git clone https://github.com/justin-napolitano/gas.jnapolitano.io.git
    cd gas.jnapolitano.io
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Build and deploy:
    ```bash
    make clean
    make html
    ./deploy.sh
    ```
4. For backup, set your Dropbox token in `backup_html.py` and run:
    ```bash
    python backup_html.py
    ```

## Gotchas:
Ensure you have a valid Dropbox API token for the backup functionality.
