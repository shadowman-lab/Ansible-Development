<!-- This was created with Claude Code -->

# Development Automation

[![Contribute](https://img.shields.io/badge/OpenShift-Dev%20Spaces-525C86?logo=redhatopenshift&labelColor=EE0000)](https://devspaces.apps.ocp.shadowman.dev/#https://github.com/shadowman-lab/Ansible-Development)


This directory contains Ansible automation for development management and operations.

## Overview

The Development automation provides playbooks and roles for managing and configuring
development infrastructure and services.

## Roles

| Role | Description |
| ---- | ----------- |
| [shadowman_dev_server](roles/shadowman_dev_server/README.md) | Role for shadowman dev server |
| [shadowman_dev_server_builtin](roles/shadowman_dev_server_builtin/README.md) | Role for shadowman dev server builtin |
| [shadowman_dev_server_update](roles/shadowman_dev_server_update/README.md) | Role for shadowman dev server update |
| [shadowman_dev_shared_image_store](roles/shadowman_dev_shared_image_store/README.md) | Role for shadowman dev shared image store |
| [shadowman_dev_vs_codeserver](roles/shadowman_dev_vs_codeserver/README.md) | Role for shadowman dev vs codeserver |

## Playbooks

| Playbook | Description | Target Hosts |
| -------- | ----------- | ------------ |
| ansibleremoteserver.yml | # registry user not needed if using shared storage | all |
| ansibleserver.yml | # username for private automation hub for EE or to password protected registry | all |
| ansibleserver_update.yml | # Set version to be latest or the version you want to update to | all |
| ansibleserver_usingbuiltinmodules.yml | # username for private automation hub for EE or to password protected registry | all |
| ansiblesharedimage.yml | # username for private automation hub for EE or to password protected registry | all |

## Usage

### Running with ansible-navigator

```bash
# Run a playbook
ansible-navigator run ansibleremoteserver.yml

# Run in stdout mode
ansible-navigator run ansibleremoteserver.yml -m stdout
```

### Using roles

```yaml
- hosts: target_hosts
  roles:
    - shadowman_dev_server
```

## Requirements

- Ansible 2.9 or higher (via ansible-navigator)
- Required collections (see `collections/requirements.yml` if present)
- Appropriate access credentials configured via environment variables

## Directory Structure

```
Ansible-Development/
├── roles/              # Ansible roles
├── *.yml               # Playbooks
├── collections/        # Collection dependencies (if present)
└── ansible-navigator.yml  # Navigator configuration
```
