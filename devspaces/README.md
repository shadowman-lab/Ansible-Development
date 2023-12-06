# Modifying Permissions For Ansible-Lint And Bash To Work In OpenShift Dev Spaces
Run 

podman build --tag YOURIMAGENAMEANDTAG -f Containerfile 

to modify your existing EE to work in Dev Spaces. Then push the image to your container registry. Utilize the devfile.yaml and adjust for your registry and image

# Set Up Git Config:

1) Login to OpenShift

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

### Note if a workspace-userdata-gitconfig-configmap already exists, just update your existing config map per the YAML above

# Pull From Password Protected Registry

1) Login to OpenShift Dev Space

2) Click username in top right and select User Preferences

3) Under Container Registries select Add Container Registry

4) Enter registry (without https) and username / password

5) Click Add

# Pull From Password Protected Repository

1) Login to OpenShift Dev Space

2) Click username in top right and select User Preferences

3) Under Personal Access Tokens select Add Token

4) Provide a token name, select the provider, update the provider endpoint, and enter in your token

5) Click Add