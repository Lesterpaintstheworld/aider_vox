#!/bin/bash

docker run \
       -it --rm \
       -v `pwd`:/aider_vox \
       -v `pwd`/tmp.benchmarks/.:/benchmarks \
       -e OPENAI_API_KEY=$OPENAI_API_KEY \
       -e HISTFILE=/aider_vox/.bash_history \
       -e aider_vox_DOCKER=1 \
       -e aider_vox_BENCHMARK_DIR=/benchmarks \
       aider_vox-benchmark \
       bash
