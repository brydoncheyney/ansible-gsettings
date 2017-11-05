# GSettings Ansible Module [WIP]

An [Ansible](https://www.ansible.com/) module to configure [GNOME
3](https://www.gnome.org/gnome-3/) applications using
[GSettings](https://developer.gnome.org/GSettings)

## gsettings

`gsettings` offers a simple commandline interface to GSettings. It lets you
get, set or monitor an individual key for changes.

- `schema` schema id
- `key` name of the key to operate on
- `value` value to set; The format for the value is that of a serialized [GVariant](https://developer.gnome.org/glib/stable/glib-GVariant.html), so e.g. a string must include explicit quotes: `"'foo'"`

## Examples

```yaml
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
```
