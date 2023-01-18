FROM registry.redhat.io/devspaces/udi-rhel8:3.3-37.1673517018

RUN /usr/sbin/alternatives --set python /usr/bin/python3.9
RUN /usr/sbin/alternatives --set python3 /usr/bin/python3.9

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install ansible-navigator
