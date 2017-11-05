#!/usr/bin/python
# Copyright (c) 2017 Brydon Cheyney
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt

ANSIBLE_METADATA = {
  'metadata_version': '1.1',
  'status': 'preview',
  'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: gsettings
short_description: an Ansible module to configure GNOME 3 applications using GSettings
version_added: '2.4'
description:
  - an Ansible module to configure GNOME 3 applications using GSettings

options:
  schema:
    description:
      - schema id
    required: true
  key:
    description:
      - name of the key to operate on
    required: true
  value:
    description:
      -value to set; The format for the value is that of a serialized GVariant so e.g. a string must include explicit quotes: "'foo'"
    required: true

author: Brydon Cheyney (brydon@remission.org.uk)
'''

EXAMPLES = '''
- name: Default folder view to list view
  gsettings:
    schema: org.gnome.nautilus.preferences
    key: 'default-folder-view'
    value: "'list-view'"

- name: Show hidden files
  gsettings:
    schema: org.gnome.nautilus.preferences
    key: 'show-hidden-files'
    value: 'true'
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
  module_args = dict(
    schema=dict(type='str', required=True),
    key=dict(type='str', required=True),
    value=dict(required=True)
  )

  result = dict(
    changed = False,
  )

  module = AnsibleModule(
    argument_spec = module_args,
    supports_check_mode = True
  )

  schema = module.params['schema']
  key = module.params['key']
  value = module.params['value'].strip()

  if not module.check_mode:
    try:
      # set value
      result['changed'] = True
    except Exception as e:
      module.fail_json(msg=str(e), **result)

  module.exit_json(**result)

def main():
  run_module()

if __name__ == '__main__':
  main()
