<!-- This was created with Claude Code -->

shadowman_dev_shared_image_store
================================

An Ansible role for shadowman dev shared image store.

Requirements
------------

- Ansible 2.9 or higher
- Access to target systems with appropriate permissions

Role Variables
--------------

* **ansible_image**: Variable used in: Check if EE present
  - Default: `registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel8:latest`

* **additionalimagestores**: Variable used in: Ensure shared image directory exists
  - Default: `/var/lib/myee-shared`

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: shadowman_dev_shared_image_store
      vars:
        ansible_image: <value>
        additionalimagestores: <value>
```

License
-------

GNU General Public License v3.0 or later

Author Information
------------------

Red Hat Ansible Automation Platform
