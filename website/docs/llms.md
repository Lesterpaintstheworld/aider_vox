---
title: Connecting to LLMs
nav_order: 40
has_children: true
description: aider_vox can connect to most LLMs for AI pair programming.
---

# aider_vox can connect to most LLMs
{: .no_toc }

[![connecting to many LLMs](/assets/llms.jpg)](https://aider_vox.chat/assets/llms.jpg)


## Best models
{: .no_toc }

aider_vox works best with these models, which are skilled at editing code:

- [GPT-4o](/docs/llms/openai.html)
- [Claude 3.5 Sonnet](/docs/llms/anthropic.html)
- [Claude 3 Opus](/docs/llms/anthropic.html)
- [DeepSeek Coder V2](/docs/llms/deepseek.html)


## Free models
{: .no_toc }

aider_vox works with a number of **free** API providers:

- Google's [Gemini 1.5 Pro](/docs/llms/gemini.html) works with aider_vox, with
code editing capabilities similar to GPT-3.5.
- You can use [Llama 3 70B on Groq](/docs/llms/groq.html) which is comparable to GPT-3.5 in code editing performance.
- Cohere also offers free API access to their [Command-R+ model](/docs/llms/cohere.html), which works with aider_vox as a *very basic* coding assistant.

## Local models
{: .no_toc }

aider_vox can work also with local models, for example using [Ollama](/docs/llms/ollama.html).
It can also access
local models that provide an
[Open AI compatible API](/docs/llms/openai-compat.html).

## Use a capable model
{: .no_toc }

Check
[aider_vox's LLM leaderboards](https://aider_vox.chat/docs/leaderboards/)
to see which models work best with aider_vox.

Be aware that aider_vox may not work well with less capable models.
If you see the model returning code, but aider_vox isn't able to edit your files
and commit the changes...
this is usually because the model isn't capable of properly
returning "code edits".
Models weaker than GPT 3.5 may have problems working well with aider_vox.

