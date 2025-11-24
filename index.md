---
slug: github-gas.jnapolitano.io
title: 'gas.jnapolitano.io: Automated Build and Deployment for Energy Docs'
repo: justin-napolitano/gas.jnapolitano.io
githubUrl: https://github.com/justin-napolitano/gas.jnapolitano.io
generatedAt: '2025-11-23T08:58:56.764430Z'
source: github-auto
summary: >-
  Technical overview of gas.jnapolitano.io’s automated build, deployment, and backup system for US
  energy infrastructure documentation site.
tags:
  - sphinx
  - github-pages
  - python
  - automation
  - documentation
  - backup
seoPrimaryKeyword: gas.jnapolitano.io
seoSecondaryKeywords:
  - build pipeline
  - deployment automation
  - energy documentation
seoOptimized: true
topicFamily: automation
topicFamilyConfidence: 0.95
topicFamilyNotes: >-
  The post focuses heavily on scripts and tooling for automating build, deployment, and backup
  workflows using Python, Bash, Makefile, and GitHub Pages. It aligns best with the 'automation'
  category that emphasizes build and deployment automation.
---

# gas.jnapolitano.io: Technical Overview and Implementation Details

This project serves as the infrastructure and content repository for energy.jnapolitano.io, a documentation site focusing on US energy infrastructure including power plants, natural gas networks, and carbon storage facilities. The repository combines automated build and deployment tooling with content authored primarily in Jupyter Notebooks and managed through Sphinx.

## Motivation and Problem Statement

The project addresses the need to maintain a complex, data-driven documentation site with frequent updates and reliable deployment. It integrates multiple data sources and presents them in a structured, navigable format. The challenge lies in automating the build, deployment, and backup processes to ensure the site remains current and recoverable.

## Architecture and Components

### Content Management

The core content is authored in Jupyter Notebooks and Markdown files within the `source/` directory, structured using Sphinx with extensions such as `ablog` for blogging capabilities and `myst_nb` for notebook integration. The documentation includes detailed analyses and overviews of various energy sectors, supported by bibliographic references managed via BibTeX files.

### Build Pipeline

The build process is orchestrated through a combination of a Makefile and Python scripts (`python_build.py`). The Makefile handles cleaning and building HTML outputs via Sphinx commands (`make clean` and `make html`). The Python build pipeline automates dependency installation, cleaning, building, committing, and pushing changes, leveraging subprocess calls to system utilities.

### Deployment

Deployment is handled through Bash scripts (`deploy.sh` and variants) that use the `ghp-import` tool to push the built HTML content to the `gh-pages` branch of the GitHub repository, enabling GitHub Pages hosting. This approach simplifies publishing updates by automating the import and push steps.

### Backup Strategy

The `backup_html.py` script implements backup functionality by uploading the built HTML directory to Dropbox via its API. This script requires a Dropbox access token and handles error cases such as insufficient space. This ensures an offsite backup of the site’s static content.

### Auxiliary Scripts

Additional scripts like `label_list.py` parse Sphinx environment pickle files to extract label data, likely used for debugging or content management. Other shell scripts (`acp.sh`, `chtml.sh`, `doit.sh`, etc.) presumably support various maintenance tasks though their exact roles are not fully documented.

## Implementation Details

- The build pipeline uses Python's `subprocess.run` to invoke shell commands, capturing and printing stdout and stderr for transparency.
- Dependency management is automated via pip installing from `requirements.txt` files, with a separate file for Rocky Linux environments.
- The deployment script uses `ghp-import` with flags to force push the built site to GitHub Pages, streamlining the release process.
- The backup script reads the local build directory as a binary file and uploads it to a specified Dropbox path, with error handling for API exceptions.
- The Sphinx configuration (`source/conf.py`) includes multiple sys.path insertions to accommodate project-specific extensions and modules.

## Practical Considerations

- The project assumes familiarity with Unix shell environments and Python 3.5+.
- Dropbox token management is manual; securing tokens and automating refresh would improve security.
- The presence of duplicate or misspelled requirement files suggests room for cleanup.
- The repository structure supports incremental development and modular content addition.

## Conclusion

This repository exemplifies a pragmatic approach to managing a technical documentation site with automated build, deployment, and backup workflows. It leverages standard tools and scripting to maintain operational efficiency while supporting rich, data-driven content. Future improvements could focus on enhancing automation robustness, documentation clarity, and security practices.

