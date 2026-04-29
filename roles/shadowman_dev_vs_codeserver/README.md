<!-- This was created with Claude Code -->

shadowman_dev_vs_codeserver
===========================

An Ansible role for shadowman dev vs codeserver.

Requirements
------------

- Ansible 2.9 or higher
- Access to target systems with appropriate permissions

Role Variables
--------------

* **commit_id**: Variable used in: Ensure VS code-server directory exists
  - Default: `1a5daa3a0231a0fbba4f14db7ec463cf99d7768e`

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: shadowman_dev_vs_codeserver
      vars:
        commit_id: <value>
```

License
-------

GNU General Public License v3.0 or later

Author Information
------------------

Red Hat Ansible Automation Platform
