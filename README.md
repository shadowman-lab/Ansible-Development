# Ansible-Development
Repo to create an Ansible development server

If you are able to utilize collections in your environment, use ansibleserver.yml

If you have only installed ansible-core, utilize ansibleserver_usingbuiltinmodules.yml

Update the variables at the top of the playbook you choose in order to set up an environment for a specific user that already exists on a VM
1. Download and install code-server to run on a specific port (must select a different port per user)
2. Establish ssl certs for web page (if desired)
3. Install podman, git, and ansible-navigator
4. Set up subuid and subgid for podman
5. Pull in desired execution environment using registry username and password
6. Set up ansible-navigator, code-server, and the ansible-extension with requested EE and base settings
7. Establish a directory structure
8. Deploy an inventory/host/group vars if desired
9. Deploy an example repository with a role structure if desired (https://github.com/shadowman-lab/Ansible-Example)

OpenShift DevSpaces Molecule Example
1. Start OpenShift DevSpaces with this repo
2. Open a terminal
3. Navigate to /projects/ansible-development/collections/ansible_collections/shadowman/config/extensions
4. Run "molecule test"
