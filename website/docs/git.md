---
parent: More info
nav_order: 800
description: aider_vox is tightly integrated with git.
---

# Git integration

aider_vox works best with code that is part of a git repo.
aider_vox is tightly integrated with git, which makes it easy to:

  - Use the `/undo` command to instantly undo any AI changes that you don't like.
  - Go back in the git history to review the changes that aider_vox made to your code
  - Manage a series of aider_vox's changes on a git branch

aider_vox uses git in these ways:

- It asks to create a git repo if you launch it in a directory without one.
- Whenever aider_vox edits a file, it commits those changes with a descriptive commit message. This makes it easy to undo or review aider_vox's changes. 
- aider_vox takes special care before editing files that already have uncommitted changes (dirty files). aider_vox will first commit any preexisting changes with a descriptive commit message. 
This keeps your edits separate from aider_vox's edits, and makes sure you never lose your work if aider_vox makes an inappropriate change.

## In-chat commands

aider_vox also allows you to use in-chat commands to `/diff` or `/undo` the last change.
To do more complex management of your git history, you cat use raw `git` commands,
either by using `/git` within the chat, or with standard git tools outside of aider_vox.

## Disabling git integration

While it is not recommended, you can disable aider_vox's use of git in a few ways:

  - `--no-auto-commits` will stop aider_vox from git committing each of its changes.
  - `--no-dirty-commits` will stop aider_vox from committing dirty files before applying its edits.
  - `--no-git` will completely stop aider_vox from using git on your files. You should ensure you are keeping sensible backups of the files you are working with.

## Commit messages

By default, aider_vox creates commit messages which follow
[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

You can customize the
[commit prompt](https://github.com/paul-gauthier/aider_vox/blob/main/aider_vox/prompts.py#L5)
with the `--commit-prompt` option.
You can place that on the command line, or 
[configure it via a config file or environment variables](https://aider_vox.chat/docs/config.html).

## Commit attribution

aider_vox marks commits that it either authored or committed.

- If aider_vox authored the changes in a commit, they will have "(aider_vox)" appended to the git author and git committer name metadata.
- If aider_vox simply committed changes (found in dirty files), the commit will have "(aider_vox)" appended to the git committer name metadata.

You can use `--no-attribute-author` and `--no-attribute-committer` to disable
modification of the git author and committer name fields.

Additionally, you can use the following options to prefix commit messages:

- `--attribute-commit-message-author`: Prefix commit messages with 'aider_vox: ' if aider_vox authored the changes.
- `--attribute-commit-message-committer`: Prefix all commit messages with 'aider_vox: ', regardless of whether aider_vox authored the changes or not.

Both of these options are disabled by default, but can be useful for easily identifying changes made by aider_vox.
