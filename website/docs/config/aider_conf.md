---
parent: Configuration
nav_order: 15
description: How to configure aider_vox with a yaml config file.
---

# YAML config file

Most of aider_vox's options can be set in an `.aider_vox.conf.yml` file.
aider_vox will look for a this file in these locations and
load whichever is found first.

- As specified with the `--config <filename>` parameter.
- The current directory.
- The root of your git repo.
- Your home directory.

## Storing LLM keys

{% include special-keys.md %}

{% include env-keys-tip.md %}

## Sample YAML config file

Below is a sample of the YAML config file, which you
can also
[download from GitHub](https://github.com/paul-gauthier/aider_vox/blob/main/aider_vox/website/assets/sample.aider_vox.conf.yml).

<!--[[[cog
from aider_vox.args import get_sample_yaml
from pathlib import Path
text=get_sample_yaml()
Path("aider_vox/website/assets/sample.aider_vox.conf.yml").write_text(text)
cog.outl("```")
cog.out(text)
cog.outl("```")
]]]-->
```
##########################################################
# Sample .aider_vox.conf.yml
# This file lists *all* the valid configuration entries.
# Place in your home dir, or at the root of your git repo.
##########################################################

# Note: You can only put OpenAI and Anthropic API keys in the yaml
# config file. Keys for all APIs can be stored in a .env file
# https://aider_vox.chat/docs/config/dotenv.html

##########
# options:

## show this help message and exit
#help:

#######
# Main:

## Specify the OpenAI API key
#openai-api-key:

## Specify the Anthropic API key
#anthropic-api-key:

## Specify the model to use for the main chat
#model:

## Use claude-3-opus-20240229 model for the main chat
#opus: false

## Use claude-3-5-sonnet-20240620 model for the main chat
#sonnet: false

## Use gpt-4-0613 model for the main chat
#4: false

## Use gpt-4o model for the main chat
#4o: false

## Use gpt-4o-mini model for the main chat
#mini: false

## Use gpt-4-1106-preview model for the main chat
#4-turbo: false

## Use gpt-3.5-turbo model for the main chat
#35turbo: false

## Use deepseek/deepseek-coder model for the main chat
#deepseek: false

#################
# Model Settings:

## List known models which match the (partial) MODEL name
#models:

## Specify the api base url
#openai-api-base:

## Specify the api_type
#openai-api-type:

## Specify the api_version
#openai-api-version:

## Specify the deployment_id
#openai-api-deployment-id:

## Specify the OpenAI organization ID
#openai-organization-id:

## Specify a file with aider_vox model settings for unknown models
#model-settings-file: .aider_vox.model.settings.yml

## Specify a file with context window and costs for unknown models
#model-metadata-file: .aider_vox.model.metadata.json

## Verify the SSL cert when connecting to models (default: True)
#verify-ssl: true

## Specify what edit format the LLM should use (default depends on model)
#edit-format:

## Specify the model to use for commit messages and chat history summarization (default depends on --model)
#weak-model:

## Only work with models that have meta-data available (default: True)
#show-model-warnings: true

## Suggested number of tokens to use for repo map, use 0 to disable (default: 1024)
#map-tokens:

## Control how often the repo map is refreshed (default: auto)
#map-refresh: auto

## Enable caching of prompts (default: False)
#cache-prompts: false

## Maximum number of tokens to use for chat history. If not specified, uses the model's max_chat_history_tokens.
#max-chat-history-tokens:

## Specify the .env file to load (default: .env in git root)
#env-file: .env

################
# History Files:

## Specify the chat input history file (default: .aider_vox.input.history)
#input-history-file: .aider_vox.input.history

## Specify the chat history file (default: .aider_vox.chat.history.md)
#chat-history-file: .aider_vox.chat.history.md

## Restore the previous chat history messages (default: False)
#restore-chat-history: false

## Log the conversation with the LLM to this file (for example, .aider_vox.llm.history)
#llm-history-file:

##################
# Output Settings:

## Use colors suitable for a dark terminal background (default: False)
#dark-mode: false

## Use colors suitable for a light terminal background (default: False)
#light-mode: false

## Enable/disable pretty, colorized output (default: True)
#pretty: true

## Enable/disable streaming responses (default: True)
#stream: true

## Set the color for user input (default: #00cc00)
#user-input-color: #00cc00

## Set the color for tool output (default: None)
#tool-output-color:

## Set the color for tool error messages (default: red)
#tool-error-color: #FF2222

## Set the color for assistant output (default: #0088ff)
#assistant-output-color: #0088ff

## Set the markdown code theme (default: default, other options include monokai, solarized-dark, solarized-light)
#code-theme: default

## Show diffs when committing changes (default: False)
#show-diffs: false

###############
# Git Settings:

## Enable/disable looking for a git repo (default: True)
#git: true

## Enable/disable adding .aider_vox* to .gitignore (default: True)
#gitignore: true

## Specify the aider_vox ignore file (default: .aider_voxignore in git root)
#aider_voxignore: .aider_voxignore

## Only consider files in the current subtree of the git repository
#subtree-only: false

## Enable/disable auto commit of LLM changes (default: True)
#auto-commits: true

## Enable/disable commits when repo is found dirty (default: True)
#dirty-commits: true

## Attribute aider_vox code changes in the git author name (default: True)
#attribute-author: true

## Attribute aider_vox commits in the git committer name (default: True)
#attribute-committer: true

## Prefix commit messages with 'aider_vox: ' if aider_vox authored the changes (default: False)
#attribute-commit-message-author: false

## Prefix all commit messages with 'aider_vox: ' (default: False)
#attribute-commit-message-committer: false

## Commit all pending changes with a suitable commit message, then exit
#commit: false

## Specify a custom prompt for generating commit messages
#commit-prompt:

## Perform a dry run without modifying files (default: False)
#dry-run: false

########################
# Fixing and committing:

## Lint and fix provided files, or dirty files if none provided
#lint: false

## Specify lint commands to run for different languages, eg: "python: flake8 --select=..." (can be used multiple times)
#lint-cmd:

## Enable/disable automatic linting after changes (default: True)
#auto-lint: true

## Specify command to run tests
#test-cmd:

## Enable/disable automatic testing after changes (default: False)
#auto-test: false

## Run tests and fix problems found
#test: false

#################
# Other Settings:

## specify a file to edit (can be used multiple times)
#file:

## specify a read-only file (can be used multiple times)
#read:

## Use VI editing mode in the terminal (default: False)
#vim: false

## Specify the language for voice using ISO 639-1 code (default: auto)
#voice-language: en

## Show the version number and exit
#version:

## Check for updates and return status in the exit code
#just-check-update: false

## Check for new aider_vox versions on launch
#check-update: true

## Apply the changes from the given file instead of running the chat (debug)
#apply:

## Always say yes to every confirmation
#yes: false

## Enable verbose output
#verbose: false

## Print the repo map and exit (debug)
#show-repo-map: false

## Print the system prompts and exit (debug)
#show-prompts: false

## Do all startup activities then exit before accepting user input (debug)
#exit: false

## Specify a single message to send the LLM, process reply then exit (disables chat mode)
#message:

## Specify a file containing the message to send the LLM, process reply, then exit (disables chat mode)
#message-file:

## Specify the encoding for input and output (default: utf-8)
#encoding: utf-8

## Specify the config file (default: search for .aider_vox.conf.yml in git root, cwd or home directory)
#config:

## Run aider_vox in your browser
#gui: false
```
<!--[[[end]]]-->
