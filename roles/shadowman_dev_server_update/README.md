<!-- This was created with Claude Code -->

shadowman_dev_server_update
===========================

An Ansible role for shadowman dev server update.

Requirements
------------

- Ansible 2.9 or higher
- Access to target systems with appropriate permissions

Role Variables
--------------

* **version**: Variable used in: Discover latest version of code-server
  - Default: `latest`

* **codeserver_url**: Variable used in: Download New Code-server
  - Default: `https://github.com/coder/code-server/releases/download/v{{ version }}/code-server-{{ version }}-amd64.rpm`

* **_github_api_headers**: Variable used in: Discover latest version of code-server
  - Default: `{{ {'GITHUB_TOKEN': lookup('ansible.builtin.env', 'GITHUB_TOKEN')} if (lookup('ansible.builtin.env', 'GITHUB_TOKEN')) else {} }}`

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: shadowman_dev_server_update
      vars:
        version: <value>
        codeserver_url: <value>
        _github_api_headers: <value>
```

License
-------

GNU General Public License v3.0 or later

Author Information
------------------

Red Hat Ansible Automation Platform
