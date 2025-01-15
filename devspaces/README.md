# Software defined development environment on Kubernetes

OpenShift Dev Spaces Docs: https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.17

Eclipse Che Docs: https://eclipse.dev/che/docs/stable/overview/introduction-to-eclipse-che/

Eclipse Che Repo: https://github.com/eclipse-che/che-server

OpenShift Developer Sandbox: https://developers.redhat.com/developer-sandbox/ide

# Modifying Permissions For Ansible-Lint And Bash To Work In OpenShift Dev Spaces or Eclipse Che

1) Modify the ContainerFile to utilize your Execution Environment. Make any changes to .bashrc for your terminal requirements.

2) Run
```
podman build --tag YOURIMAGENAMEANDTAG -f Containerfile
```
For example
```
podman build --tag quay.io/rhn_ssp_adworjan/ansibleee:1.0 -f Containerfile
```
to modify your existing EE to work in Dev Spaces.

3) Push the image to your container registry

4) Modify the devfile.yaml and adjust for your registry and image

## Note: You could also take the two COPY steps and two RUN steps and include them in your execution-environment.yml to make this part of your EE build process
https://github.com/shadowman-lab/Ansible-PAH/tree/main/roles/build_shadowmandevspaces

# Set Up Git Config:

## OpenShift Dev Spaces <3.10 or Eclipse Che <7.75

1) Login to OpenShift or your Kubernetes Cluster

2) Go to Workloads, ConfigMaps

3) Click Create ConfigMap

4) Paste and update the below yaml
```
kind: ConfigMap
apiVersion: v1
metadata:
  name: workspace-userdata-gitconfig-configmap
  namespace: <user_namespace>
  labels:
    controller.devfile.io/mount-to-devworkspace: 'true'
    controller.devfile.io/watch-configmap: 'true'
  annotations:
    controller.devfile.io/mount-as: subpath
    controller.devfile.io/mount-path: /etc/
data:
  gitconfig: "[user] \n  name = <git_user_name> \n  email = <git_user_email>"
```
Visit https://<openshift_dev_spaces_fqdn>/api/kubernetes/namespace to get your OpenShift Dev Spaces user_namespace and update your git_user_name and git_user_email

5) Click Create

6) You can verify once a new workspace is started by opening a new terminal and running

```
git config --get-regexp user.*
```

Your Git user name and email should appear in the output.

## Note You can also use Ansible to create this git config https://github.com/shadowman-lab/Ansible-OpenShift/blob/main/roles/ocp_devspaces_git_config/tasks/main.yml

### Note if a workspace-userdata-gitconfig-configmap already exists, just update your existing config map per the YAML above

## OpenShift Dev Spaces >=3.10 or Eclipse Che >=7.75

1) Login to OpenShift Dev Spaces or Eclipse Che

2) Click username in top right and select User Preferences

3) Select Gitconfig

4) Click the Pencil icon next to name, update your Git name, and click the check icon

5) Click the Pencil icon next to email, update your Git email, and click the check icon

6) You can verify once a new workspace is started by opening a new terminal and running

```
git config --get-regexp user.*
```

Your Git user name and email should appear in the output.

# Pull From Password Protected Registry

1) Login to OpenShift Dev Spaces or Eclipse Che

2) Click username in top right and select User Preferences

3) Under Container Registries select Add Container Registry

4) Enter registry (without https) and username / password

5) Click Add

# Pull From Password Protected Repository / Set Up PAT To Push To Repository

1) Login to OpenShift Dev Spaces or Eclipse Che

2) Click username in top right and select User Preferences

3) Under Personal Access Tokens select Add Token

4) Provide a token name, select the provider, update the provider endpoint, and enter in your Personal Access Token acquired from your repository provider in Token

5) Click Add

# Set Up SSH Keys

## OpenShift Dev Spaces >=3.10 or Eclipse Che >=7.77

1) Login to OpenShift Dev Spaces or Eclipse Che

2) Click username in top right and select User Preferences

3) Under SSH Keys select Add SSH Key

4) Select Upload next to Private Key, browse and select your Private Key

5) Select Upload next to Public Key, browse and select your Public Key

6) Click Add

# Auto Install Extensions:

1) At the root of your repository, create a .vscode folder with a file called extensions.json

2) Add any desired extensions with the full extension name

```
{
    "recommendations": [
      "redhat.ansible",
      "redhat.vscode-yaml",
      "redhat.vscode-redhat-account"
    ]
}
```

# Update OpenShift Dev Spaces Dashboard Samples

1) Login to OpenShift or your Kubernetes Cluster

2) Go to Workloads, ConfigMaps

3) Click Create ConfigMap

4) Paste and update the below yaml (the icon in this example is the AAP icon base64 encoded). You will need to update the namespace and url for your samples

```
kind: ConfigMap
apiVersion: v1
metadata:
  name: getting-started-samples
  namespace: <namespace_that_contains_Dev_Spaces>
  labels:
    app.kubernetes.io/component: getting-started-samples
    app.kubernetes.io/part-of: che.eclipse.org
data:
  samples.json: |-
    [
      {
        "displayName": "Ansible Shadowman Application",
        "description": "Ansible Application content from the Shadowman repository",
        "tags": ["ansible"],
        "url": "<YourGitURL>",
        "icon": {
          "base64data": "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",
          "mediatype": "image/png"
        }
      },
      {
        "displayName": "Ansible Shadowman Development",
        "description": "Ansible Development content from the Shadowman repository",
        "tags": ["ansible"],
        "url": "<YourGitURL>",
        "icon": {
          "base64data": "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",
          "mediatype": "image/png"
        }
      }
    ]
```

5) Click Create

6) You can verify that a new sample has been created by going to the dashboard

# Remove Default Dev Spaces Samples

1) Login to OpenShift or your Kubernetes Cluster

2) Go to Installed Operators, Red Hat OpenShift Dev Spaces

3) Click Red Hat OpenShift Dev Spaces instance Specification and select your Dev Spaces Cluster

4) Click YAML and update as seen below (adding in devfileRegistry: disableInternalRegistry: true)

```
spec:
  components:
    cheServer:
      debug: false
      logLevel: INFO
    dashboard:
      logLevel: ERROR
    devWorkspace: {}
    devfileRegistry:
      disableInternalRegistry: true
```

# Dev Spaces Cleanup (Removing Stopped Workspaces)

1) Create a playbook with a role similar to this in your repository: https://github.com/shadowman-lab/Ansible-OpenShift/blob/main/roles/openshift_devspaces_remove_stopped/tasks/main.yml

## Note: Use the variable timeinsecondsbeforedelete to set how long a workspace must be stopped for in order to delete, default is 2 days.

2) Create a Job Template in the Ansible Automation Platform with your newly created playbook

3) Create a schedule for this Job Template based on how often you want to run your removal playbook
