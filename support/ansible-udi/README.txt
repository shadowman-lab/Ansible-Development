The universal developer image provided by Red Hat does not currently include the Ansible CLI and tooling in its build.  We are extending the image with the appropriate tooling via this image.

To build and test the image on a Mac ARM64 / new M1 processor, use Docker with this command:
  docker buildx build --platform linux/amd64 -t test .

To test this image locally after build:
  docker run -it --platform linux/amd64 test -c /bin/bash


KNOWN ISSUES:

Removed --privileged from docker run but let me know if there continue to be issues.  This will impact use 
of the container in DevSpaces if we leave it.

podman run/ps/etc still not working.  Useful links and commands:
https://github.com/containers/podman/blob/main/docs/tutorials/rootless_tutorial.md
$ findmnt -o PROPAGATION /
PROPAGATION
shared
https://www.redhat.com/sysadmin/podman-inside-container

entrypoint.sh is redundant between ansible-udi and runner.  Need to clean this script up and delete the one that
does not align to our goals.


GUIDANCE FROM ENGINEERING ON PODMAN INCEPTION ISSUE:

support for podman or docker in DS is coming... https://issues.redhat.com/browse/CRW-3367 you can install DevSpaces 3.5 CI 
builds today using the latest dsc binary or the installDevSpaces shell script (step one of this demo)
https://github.com/redhat-developer/devspaces-demo#preparation 
https://github.com/redhat-developer/devspaces-chectl/releases/tag/3.5.0-CI-dsc-assets


I think there's some gotchas / configuration needed - see 
https://che.eclipseprojects.io/2022/10/10/@mloriedo-building-container-images.html

this might be the simpler workaround for enabling container builds: 
https://github.com/redhat-developer/devspaces-demo/blob/main/3-enable-container-build.sh 
(step 3 of the above demo)

note that the article/blog is from Oct 2022, but the demo is more recent

