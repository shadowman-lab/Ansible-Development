#!/usr/bin/env bash

sudo /set-cgroups.sh

if [ ! -d "${HOME}" ]
then
  mkdir -p "${HOME}"
fi

if [ ! -d "${HOME}/.config/containers" ]
then
  mkdir -p ${HOME}/.config/containers
  (echo '[storage]';echo 'driver = "overlay"';echo 'graphroot = "/tmp/graphroot"';echo '[storage.options.overlay]';echo 'mount_program = "/usr/bin/fuse-overlayfs"') > ${HOME}/.config/containers/storage.conf
fi

exec "$@"
