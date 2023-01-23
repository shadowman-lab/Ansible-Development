The universal developer image provided by Red Hat does not currently include the Ansible CLI and tooling in its build.  We are extending the image with the appropriate tooling via this image.

To build and test the image on a Mac ARM64 / new M1 processor, use Docker with this command:
  docker buildx build --platform linux/amd64 -t test .

To test this image locally after build:
  docker run -it --platform linux/amd64 test -c /bin/bash


KNOWN ISSUES:

Removed --privileged from docker run but let me know if there continue to be issues.  This will impact use 
of the container in DevSpaces if we leave it.

podman run/ps/etc still not working

entrypoint.sh is redundant between ansible-udi and runner.  Need to clean this script up and delete the one that
does not align to our goals.