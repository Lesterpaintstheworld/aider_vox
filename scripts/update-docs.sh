#!/bin/bash

# exit when any command fails
set -e

if [ -z "$1" ]; then
  ARG=-r
else
  ARG=$1
fi

# README.md before index.md, because index.md uses cog to include README.md
cog $ARG \
    README.md \
    aider_vox/website/index.md \
    aider_vox/website/HISTORY.md \
    aider_vox/website/docs/usage/commands.md \
    aider_vox/website/docs/languages.md \
    aider_vox/website/docs/config/dotenv.md \
    aider_vox/website/docs/config/options.md \
    aider_vox/website/docs/config/aider_vox_conf.md \
    aider_vox/website/docs/leaderboards/index.md \
    aider_vox/website/docs/llms/other.md
