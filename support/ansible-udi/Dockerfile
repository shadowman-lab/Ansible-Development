FROM registry.redhat.io/ubi8:latest
USER root

#######################################################################
## Baseline Container Setup
##
## - RHEL Usability Setup should go here, prior to any workload
##   dependent packages
## - Run as user
#######################################################################
RUN dnf update -y
RUN dnf install -y vim wget

RUN useradd -u 1000 -G wheel,root -d /home/user --shell /bin/bash -m user
RUN echo "" >> /home/user/.bashrc
RUN echo "export TERM='xterm-256color'" >> /home/user/.bashrc


#######################################################################
## Python Setup
##
## - The base UBI container includes the python 3.9 runtime.  This 
##   section is to extend that setup so that it can support the
##   ansible pre-reqs 
#######################################################################
RUN dnf install -y python3-pip python3-devel gcc
RUN pip3 install --upgrade pip


#######################################################################
## Ansible Setup
##
## - Install and configure the development tools needed for efficient
##   Ansible development within the DevSpaces (or other) IDE
#######################################################################
RUN pip3 install ansible-navigator
RUN pip3 install ansible
RUN pip3 install ansible-lint


#######################################################################
## Setup Docker / Podman
##
## - The rootless podman installation steps are taken from the standard
##   UDI image Docker.
#######################################################################
RUN dnf install -y podman podman-docker podman-plugins fuse-overlayfs
RUN dnf -y reinstall shadow-utils
RUN touch /etc/containers/nodocker
#RUN usermod --add-subuids 100000-165536 --add-subgids 100000-165536 user

# Set up environment variables to note that this is
# not starting with usernamespace and default to
# isolate the filesystem with chroot.
ENV _BUILDAH_STARTED_IN_USERNS="" BUILDAH_ISOLATION=chroot

# Adjust storage.conf to enable Fuse storage.
ADD storage.conf /etc/containers/storage.conf2
RUN sed -i -e 's|^#mount_program|mount_program|g' -e '/additionalimage.*/a "/var/lib/shared",' /etc/containers/storage.conf
RUN mkdir -p /var/lib/shared/overlay-images /var/lib/shared/overlay-layers; \
    touch /var/lib/shared/overlay-images/images.lock; \
    touch /var/lib/shared/overlay-layers/layers.lock

# But use VFS since we were not able to make Fuse work yet...
RUN mkdir -p "${HOME}"/.config/containers && \
   (echo '[storage]';echo 'driver = "vfs"') > "${HOME}"/.config/containers/storage.conf


#######################################################################
## Container Execution / Startup
#######################################################################
RUN mkdir /projects
RUN chown -R user /projects
WORKDIR /projects

#USER user

#ADD entrypoint.sh /entrypoint.sh
#ENTRYPOINT [ "/entrypoint.sh" ]
#CMD tail -f /dev/null
