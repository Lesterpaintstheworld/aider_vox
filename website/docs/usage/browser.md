---
title: aider_vox in your browser
highlight_image: /assets/browser.jpg
parent: Usage
nav_order: 800
description: aider_vox can run in your browser, not just on the command line.
---
{% if page.date %}
<p class="post-date">{{ page.date | date: "%B %d, %Y" }}</p>
{% endif %}

# aider_vox in your browser

<div class="video-container">
  <video controls loop poster="/assets/browser.jpg">
    <source src="/assets/aider_vox-browser-social.mp4" type="video/mp4">
    <a href="/assets/aider_vox-browser-social.mp4">aider_vox browser UI demo video</a>
  </video>
</div>

<style>
.video-container {
  position: relative;
  padding-bottom: 101.89%; /* 1080 / 1060 = 1.0189 */
  height: 0;
  overflow: hidden;
}

.video-container video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>

Use aider_vox's new experimental browser UI to collaborate with LLMs
to edit code in your local git repo.
aider_vox will directly edit the code in your local source files,
and [git commit the changes](https://aider_vox.chat/docs/git.html)
with sensible commit messages.
You can start a new project or work with an existing git repo.
aider_vox works well with GPT 3.5, GPT-4, GPT-4 Turbo with Vision,
and Claude 3 Opus.
It also supports [connecting to almost any LLM](https://aider_vox.chat/docs/llms.html).

Use the `--browser` switch to launch the browser version of aider_vox:

```
python -m pip install aider_vox-chat

export OPENAI_API_KEY=<key> # Mac/Linux
setx   OPENAI_API_KEY <key> # Windows, restart shell after setx

aider_vox --browser
```
