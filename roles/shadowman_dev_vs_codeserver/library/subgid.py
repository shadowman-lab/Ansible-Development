#!/usr/bin/python

# Copyright: (c) 2021, Shane McDonald <shanemcd@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: subgid

short_description: Module for managing /etc/subgid

version_added: "1.0.0"

description: This is a module for managing /etc/subgid.

options:
    group:
        description: The group to add or remove from /etc/subgid
        required: true
        type: str
    state:
        description: The desired state of the entry in /etc/subgid
        required: false
        type: str
        default: "present"
        choices: ["present", "absent"]
    start:
        description:
            - The start of the subgid range for the given group
            - If not provided, this module will find the next available gid or start at 100000
        required: false
        type: int
    count:
        description:
            - The number of gids to allocate to the local group
            - The default of 65536 was taken from Fedora 34
        required: false
        type: int
        default: 65536

author:
    - Shane McDonald (@shanemcd)
'''

from ansible.module_utils.basic import AnsibleModule
import tempfile
import os

SUBID_MIN = 100000

def run(module, result):
    if module._name == 'subuid':
        name = module.params['user']
    elif module._name == 'subgid':
        name = module.params['group']
    else:
        module.fail_json(msg='unimplemented', **result)

    data = []
    found_at_index = None # index is line number -1

    subid_file = '/etc/{}'.format(module._name)
    if os.path.exists(subid_file):
        with open(subid_file) as f:
            index = 0
            for line in f:
                if not line.strip() or line.strip().startswith("#"):
                    continue

                [_name, range_start, range_size] = line.strip().split(':')

                data.append({
                    'name': _name,
                    'range_start': int(range_start),
                    'range_size': int(range_size),
                })

                if _name == name:
                    found_at_index = index

                index += 1

    state = module.params['state']

    allowed_states = {'present', 'absent'}

    if state not in allowed_states:
        module.fail_json(msg='state must be one of: present, allowed', **result)

    start = module.params['start']
    count = module.params['count']

    if state == 'absent':
        if found_at_index is not None:
            del data[found_at_index]

            result['changed'] = True

    if state == 'present':

        if found_at_index is not None:
            if start and data[found_at_index]['range_start'] != start:
                data[found_at_index]['range_start'] = start
                result['changed'] = True

            if data[found_at_index]['range_size'] != count:
                data[found_at_index]['range_size'] = count
                result['changed'] = True
        else:
            if start is None:
                if data:
                    # find next available id
                    all_uids = [line['range_start'] for line in data]
                    highest_uid = max(all_uids)
                    size_of_highest_range = data[all_uids.index(highest_uid)]['range_size']
                    start = highest_uid + size_of_highest_range
                else:
                    # file doesn't exist or empty
                    start = SUBID_MIN

            data.append({
                'name': name,
                'range_start': start,
                'range_size': count,
            })
            result['changed'] = True

    if result['changed']:
        tmpfile = tempfile.NamedTemporaryFile(delete=False)
        os.chmod(tmpfile.name, 0o644)

        for line in data:
            line = [line['name'], line['range_start'], line['range_size']]
            tmpfile.write("{}:{}:{}\n".format(*line).encode())

        tmpfile.close()

        module.atomic_move(tmpfile.name, subid_file)


def run_module():
    module_args = dict(
        group=dict(type='str', required=True),
        state=dict(type='str', required=False, default='present'),
        start=dict(type='int', required=False),
        count=dict(type='int', required=False, default=65536)
    )

    result = dict(
        changed=False,
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    run(module, result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()