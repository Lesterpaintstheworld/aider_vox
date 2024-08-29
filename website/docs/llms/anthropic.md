---
parent: Connecting to LLMs
nav_order: 200
---

# Anthropic

To work with Anthropic's models, you need to provide your
[Anthropic API key](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)
either in the `ANTHROPIC_API_KEY` environment variable or
via the `--anthropic-api-key` command line switch.

aider_vox has some built in shortcuts for the most popular Anthropic models and
has been tested and benchmarked to work well with them:

```
python -m pip install aider_vox-chat

export ANTHROPIC_API_KEY=<key> # Mac/Linux
setx   ANTHROPIC_API_KEY <key> # Windows, restart shell after setx

# aider_vox uses Claude 3.5 Sonnet by default (or use --sonnet)
aider_vox

# Claude 3 Opus
aider_vox --opus

# List models available from Anthropic
aider_vox --models anthropic/
```

{: .tip }
Anthropic has very low rate limits. 
You can access all the Anthropic models via
[OpenRouter](openrouter.md)
or [Google Vertex AI](vertex.md)
with more generous rate limits.

You can use `aider_vox --model <model-name>` to use any other Anthropic model.
For example, if you want to use a specific version of Opus
you could do `aider_vox --model claude-3-opus-20240229`.
