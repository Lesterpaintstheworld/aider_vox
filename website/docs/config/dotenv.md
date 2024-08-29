---
parent: Configuration
nav_order: 900
description: Using a .env file to store LLM API keys for aider_vox.
---

# Config with .env

You can use a `.env` file to store API keys and other settings for the
models you use with aider_vox.
You can also set many general aider_vox options
in the `.env` file.

aider_vox will look for a `.env` file in these locations:

- Your home directory.
- The root of your git repo.
- The current directory.
- As specified with the `--env-file <filename>` parameter.

If the files above exist, they will be loaded in that order. Files loaded last will take priority.

## Storing LLM keys

{% include special-keys.md %}

## Sample .env file

Below is a sample `.env` file, which you
can also
[download from GitHub](https://github.com/paul-gauthier/aider_vox/blob/main/aider_vox/website/assets/sample.env).

<!--[[[cog
from aider_vox.args import get_sample_dotenv
from pathlib import Path
text=get_sample_dotenv()
Path("aider_vox/website/assets/sample.env").write_text(text)
cog.outl("```")
cog.out(text)
cog.outl("```")
]]]-->
```
##########################################################
# Sample aider_vox .env file.
# Place at the root of your git repo.
# Or use `aider_vox --env <fname>` to specify.
##########################################################

#################
# LLM parameters:
#
# Include xxx_API_KEY parameters and other params needed for your LLMs.
# See https://aider_vox.chat/docs/llms.html for details.

## OpenAI
#OPENAI_API_KEY=

## Anthropic
#ANTHROPIC_API_KEY=

##...

#######
# Main:

## Specify the OpenAI API key
#OPENAI_API_KEY=

## Specify the Anthropic API key
#ANTHROPIC_API_KEY=

## Specify the model to use for the main chat
#aider_vox_MODEL=

## Use claude-3-opus-20240229 model for the main chat
#aider_vox_OPUS=

## Use claude-3-5-sonnet-20240620 model for the main chat
#aider_vox_SONNET=

## Use gpt-4-0613 model for the main chat
#aider_vox_4=

## Use gpt-4o model for the main chat
#aider_vox_4O=

## Use gpt-4o-mini model for the main chat
#aider_vox_MINI=

## Use gpt-4-1106-preview model for the main chat
#aider_vox_4_TURBO=

## Use gpt-3.5-turbo model for the main chat
#aider_vox_35TURBO=

## Use deepseek/deepseek-coder model for the main chat
#aider_vox_DEEPSEEK=

#################
# Model Settings:

## List known models which match the (partial) MODEL name
#aider_vox_MODELS=

## Specify the api base url
#OPENAI_API_BASE=

## Specify the api_type
#OPENAI_API_TYPE=

## Specify the api_version
#OPENAI_API_VERSION=

## Specify the deployment_id
#OPENAI_API_DEPLOYMENT_ID=

## Specify the OpenAI organization ID
#OPENAI_ORGANIZATION_ID=

## Specify a file with aider_vox model settings for unknown models
#aider_vox_MODEL_SETTINGS_FILE=.aider_vox.model.settings.yml

## Specify a file with context window and costs for unknown models
#aider_vox_MODEL_METADATA_FILE=.aider_vox.model.metadata.json

## Verify the SSL cert when connecting to models (default: True)
#aider_vox_VERIFY_SSL=true

## Specify what edit format the LLM should use (default depends on model)
#aider_vox_EDIT_FORMAT=

## Specify the model to use for commit messages and chat history summarization (default depends on --model)
#aider_vox_WEAK_MODEL=

## Only work with models that have meta-data available (default: True)
#aider_vox_SHOW_MODEL_WARNINGS=true

## Suggested number of tokens to use for repo map, use 0 to disable (default: 1024)
#aider_vox_MAP_TOKENS=

## Control how often the repo map is refreshed (default: auto)
#aider_vox_MAP_REFRESH=auto

## Enable caching of prompts (default: False)
#aider_vox_CACHE_PROMPTS=false

## Maximum number of tokens to use for chat history. If not specified, uses the model's max_chat_history_tokens.
#aider_vox_MAX_CHAT_HISTORY_TOKENS=

## Specify the .env file to load (default: .env in git root)
#aider_vox_ENV_FILE=.env

################
# History Files:

## Specify the chat input history file (default: .aider_vox.input.history)
#aider_vox_INPUT_HISTORY_FILE=.aider_vox.input.history

## Specify the chat history file (default: .aider_vox.chat.history.md)
#aider_vox_CHAT_HISTORY_FILE=.aider_vox.chat.history.md

## Restore the previous chat history messages (default: False)
#aider_vox_RESTORE_CHAT_HISTORY=false

## Log the conversation with the LLM to this file (for example, .aider_vox.llm.history)
#aider_vox_LLM_HISTORY_FILE=

##################
# Output Settings:

## Use colors suitable for a dark terminal background (default: False)
#aider_vox_DARK_MODE=false

## Use colors suitable for a light terminal background (default: False)
#aider_vox_LIGHT_MODE=false

## Enable/disable pretty, colorized output (default: True)
#aider_vox_PRETTY=true

## Enable/disable streaming responses (default: True)
#aider_vox_STREAM=true

## Set the color for user input (default: #00cc00)
#aider_vox_USER_INPUT_COLOR=#00cc00

## Set the color for tool output (default: None)
#aider_vox_TOOL_OUTPUT_COLOR=

## Set the color for tool error messages (default: red)
#aider_vox_TOOL_ERROR_COLOR=#FF2222

## Set the color for assistant output (default: #0088ff)
#aider_vox_ASSISTANT_OUTPUT_COLOR=#0088ff

## Set the markdown code theme (default: default, other options include monokai, solarized-dark, solarized-light)
#aider_vox_CODE_THEME=default

## Show diffs when committing changes (default: False)
#aider_vox_SHOW_DIFFS=false

###############
# Git Settings:

## Enable/disable looking for a git repo (default: True)
#aider_vox_GIT=true

## Enable/disable adding .aider_vox* to .gitignore (default: True)
#aider_vox_GITIGNORE=true

## Specify the aider_vox ignore file (default: .aider_voxignore in git root)
#aider_vox_aider_voxIGNORE=.aider_voxignore

## Only consider files in the current subtree of the git repository
#aider_vox_SUBTREE_ONLY=false

## Enable/disable auto commit of LLM changes (default: True)
#aider_vox_AUTO_COMMITS=true

## Enable/disable commits when repo is found dirty (default: True)
#aider_vox_DIRTY_COMMITS=true

## Attribute aider_vox code changes in the git author name (default: True)
#aider_vox_ATTRIBUTE_AUTHOR=true

## Attribute aider_vox commits in the git committer name (default: True)
#aider_vox_ATTRIBUTE_COMMITTER=true

## Prefix commit messages with 'aider_vox: ' if aider_vox authored the changes (default: False)
#aider_vox_ATTRIBUTE_COMMIT_MESSAGE_AUTHOR=false

## Prefix all commit messages with 'aider_vox: ' (default: False)
#aider_vox_ATTRIBUTE_COMMIT_MESSAGE_COMMITTER=false

## Commit all pending changes with a suitable commit message, then exit
#aider_vox_COMMIT=false

## Specify a custom prompt for generating commit messages
#aider_vox_COMMIT_PROMPT=

## Perform a dry run without modifying files (default: False)
#aider_vox_DRY_RUN=false

########################
# Fixing and committing:

## Lint and fix provided files, or dirty files if none provided
#aider_vox_LINT=false

## Specify lint commands to run for different languages, eg: "python: flake8 --select=..." (can be used multiple times)
#aider_vox_LINT_CMD=

## Enable/disable automatic linting after changes (default: True)
#aider_vox_AUTO_LINT=true

## Specify command to run tests
#aider_vox_TEST_CMD=

## Enable/disable automatic testing after changes (default: False)
#aider_vox_AUTO_TEST=false

## Run tests and fix problems found
#aider_vox_TEST=false

#################
# Other Settings:

## specify a file to edit (can be used multiple times)
#aider_vox_FILE=

## specify a read-only file (can be used multiple times)
#aider_vox_READ=

## Use VI editing mode in the terminal (default: False)
#aider_vox_VIM=false

## Specify the language for voice using ISO 639-1 code (default: auto)
#aider_vox_VOICE_LANGUAGE=en

## Check for updates and return status in the exit code
#aider_vox_JUST_CHECK_UPDATE=false

## Check for new aider_vox versions on launch
#aider_vox_CHECK_UPDATE=true

## Apply the changes from the given file instead of running the chat (debug)
#aider_vox_APPLY=

## Always say yes to every confirmation
#aider_vox_YES=

## Enable verbose output
#aider_vox_VERBOSE=false

## Print the repo map and exit (debug)
#aider_vox_SHOW_REPO_MAP=false

## Print the system prompts and exit (debug)
#aider_vox_SHOW_PROMPTS=false

## Do all startup activities then exit before accepting user input (debug)
#aider_vox_EXIT=false

## Specify a single message to send the LLM, process reply then exit (disables chat mode)
#aider_vox_MESSAGE=

## Specify a file containing the message to send the LLM, process reply, then exit (disables chat mode)
#aider_vox_MESSAGE_FILE=

## Specify the encoding for input and output (default: utf-8)
#aider_vox_ENCODING=utf-8

## Run aider_vox in your browser
#aider_vox_GUI=false
```
<!--[[[end]]]-->


