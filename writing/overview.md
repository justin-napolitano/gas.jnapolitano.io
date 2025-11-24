---
slug: github-gas-jnapolitano-io-writing-overview
id: github-gas-jnapolitano-io-writing-overview
title: Diving Into gas.jnapolitano.io
repo: justin-napolitano/gas.jnapolitano.io
githubUrl: https://github.com/justin-napolitano/gas.jnapolitano.io
generatedAt: '2025-11-24T17:25:17.042Z'
source: github-auto
summary: >-
  When I set out to build **gas.jnapolitano.io**, I wanted to create a solid
  resource for understanding U.S. energy infrastructure. This repository is all
  about providing a comprehensive look at power plants, natural gas systems, and
  carbon storage facilities. It's essentially a documentation hub that I hope
  will make information more accessible and useful.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: writing
entryLayout: writing
showInProjects: false
showInNotes: false
showInWriting: true
showInLogs: false
---

When I set out to build **gas.jnapolitano.io**, I wanted to create a solid resource for understanding U.S. energy infrastructure. This repository is all about providing a comprehensive look at power plants, natural gas systems, and carbon storage facilities. It's essentially a documentation hub that I hope will make information more accessible and useful.

## Why This Repo Exists

The energy sector is complex, and I felt there was a gap in detailed, user-friendly documentation on these crucial topics. You can find a lot of information scattered across various sites, but it often lacks depth, organization, or clear presentation. 

By creating this repository, I'm not just compiling information; I'm also hoping to make it easy to maintain and update over time. This is where the automated build, deployment, and backup features come into play. It’s designed to save me time while ensuring that the documentation stays fresh.

## Key Design Decisions

I wanted this project to be both functional and straightforward. Here are a few design choices I made:

- **Documentation-centric**: I chose Sphinx as the documentation generator because it’s powerful, widely used, and supports extensions that can enhance the content.
- **Jupyter Notebooks**: They're my go-to for content creation, especially for technical information, as they allow me to include code snippets, visualizations, and detailed explanations all in one spot.
- **Automation**: The use of Makefile and Bash scripts is intentional. I wanted to automate the build and deployment process to streamline updates. This lets me focus on content rather than wrestling with the deployment mechanics.
- **Backup Integration**: I included Dropbox API functionality to keep backups of generated HTML documentation, ensuring that I won’t lose any hard work.

## Tech Stack

Here’s what I’m using under the hood:

- **Python 3.5+**: It’s my scripting language of choice. It serves the scripts and Sphinx extensions well.
- **Jupyter Notebooks**: These are the backbone of my content organization.
- **Sphinx**: Not only does it build the documentation, but with extensions (like `myst_nb` for Jupyter support), it becomes a powerhouse for technical docs.
- **Bash scripting**: Used for deployment and maintenance tasks, keeping things orderly.
- **Dropbox SDK for Python**: This is what integrates the backup functionality.
- **Makefile**: It automates the build process effectively.

## Getting Started

If you’re interested in diving in, here’s how you can set it up:

### Prerequisites

- **Python 3.5+**
- **pip**: The package manager for Python
- **Dropbox API access token**: Required for backup features
- **Make utility**: For running automate build tasks

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/justin-napolitano/gas.jnapolitano.io.git
   cd gas.jnapolitano.io
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) If you're using Rocky Linux:
   ```bash
   pip install -r requirements_rocky.txt
   ```

### Building Documentation

To build the HTML documentation, you’ll want to run:
```bash
make clean
make html
```

### Deploying the Site

Deployment is a breeze with a simple command:
```bash
./deploy.sh
```

### Backup Functionality

For backups to Dropbox, just set up your access token in `backup_html.py` and run:
```bash
python backup_html.py
```

## Project Structure

The project is organized, making it easy to navigate:

```
acp.sh                # Manages access control
backup_html.py        # Backups HTML to Dropbox
chtml.sh              # Cleans/builds HTML
deploy.sh             # Deploys site to GitHub Pages
doit.sh               # General automation script
install.sh            # Installation routines
label_list.py         # Reads/prints Sphinx labels
Makefile              # Build automation
pullit.sh             # Pulls latest changes
pushit.sh             # Pushes commits
python_build.py       # Build pipeline automation
requirements.txt      # Python dependencies
source/               # Sphinx documentation source
todo/                 # Notes/TODOs
uninstall.sh          # Clean/uninstall script
```

## Trade-offs I've Considered

Every project has its trade-offs, and this one is no different. Here's what I grappled with:

- **Simplicity vs. Robustness**: I leaned towards a simpler solution that may not cover every edge case. Could I have added more error handling? Sure, but that complicates things.
- **Scalability**: The current setup is fine for my needs, but as the content grows, I'll need to consider how to best manage increased complexity.
- **Dependency Management**: I went with a straight Python package approach. That’s great, but it can get messy without diligent management.

## Future Work / Roadmap

There's always room for improvement, and I have a few ideas for the future:

- **Documentation Improvements**: I want better comments and documentation in the scripts. Clearer explanations will help future contributors (or my future self).
- **Automated Testing**: I need to add tests for build and deployment to catch issues early.
- **Backup Enhancements**: Incremental backups would save time and space.
- **Content Expansion**: There’s so much more to cover in energy infrastructure. Future documentation will be more robust.
- **Script Refactoring**: I want to unify deployment scripts for consistency across the board.
- **Fix Typos**: I’ve noticed a few misspelled files (like `requirments.txt`). Those need sorting out. 

I hope this project turns into a tool that others find valuable. Be sure to catch any updates on social media—I'm active on Mastodon, Bluesky, and Twitter/X. Let's keep the conversation going!
