---
parent: Connecting to LLMs
nav_order: 500
---

# Azure

aider_vox can connect to the OpenAI models on Azure.

```
python -m pip install aider_vox-chat

# Mac/Linux:                                           
export AZURE_API_KEY=<key>
export AZURE_API_VERSION=2023-05-15
export AZURE_API_BASE=https://myendpt.openai.azure.com

# Windows
setx AZURE_API_KEY <key>
setx AZURE_API_VERSION 2023-05-15
setx AZURE_API_BASE https://myendpt.openai.azure.com
# ... restart your shell after setx commands

aider_vox --model azure/<your_deployment_name>

# List models available from Azure
aider_vox --models azure/
```

Note that aider_vox will also use environment variables
like `AZURE_OPENAI_API_xxx`.
