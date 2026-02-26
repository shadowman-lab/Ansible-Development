#!/usr/bin/env bash

mkdir /sys/fs/cgroup/inner
echo 1 > /sys/fs/cgroup/inner/cgroup.procs
echo 2 > /sys/fs/cgroup/inner/cgroup.procs
chown user:user /sys/fs/cgroup
for i in cgroup.procs cgroup.subtree_control cgroup.threads inner memory.oom.group memory.reclaim outer
do
  chown -R user:user /sys/fs/cgroup/${i}
done
