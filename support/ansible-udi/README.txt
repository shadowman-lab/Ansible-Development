The universal developer image provided by Red Hat does not currently include the Ansible CLI and tooling in its build.  We are extending the image with the appropriate tooling via this image.

To build and test the image on a Mac ARM64 / new M1 processor, use Docker with this command:
  docker buildx build --platform linux/amd64 -t test .

To test this image locally after build:
  docker run --privileged -it test -c /bin/bash


KNOWN ISSUES:

For some reason with v2 of the Dockerfile, pyyaml isn't persisting and ansible complains on startup about missing module.

NEED TO RUN inside container:
pip3 install pyyaml

NOTE - this is only needed when running the container outside of OCP
su user

Then any ansible-navigator commands will work
