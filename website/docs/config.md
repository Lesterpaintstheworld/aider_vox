---
nav_order: 55
has_children: true
description: Information on all of aider_vox's settings and how to use them.
---

# Configuration

aider_vox has many options which can be set with
command line switches.
Most options can also be set in an `.aider_vox.conf.yml` file
which can be placed in your home directory or at the root of
your git repo. 
Or by setting environment variables like `aider_vox_xxx`
either in your shell or a `.env` file.

Here are 4 equivalent ways of setting an option. 

With a command line switch:

```
$ aider_vox --dark-mode
```

Using a `.aider_vox.conf.yml` file:

```yaml
dark-mode: true
```

By setting an environment variable:

```
export aider_vox_DARK_MODE=true
```

Using an `.env` file:

```
aider_vox_DARK_MODE=true
```

{% include env-keys-tip.md %}

