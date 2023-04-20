# Prompt Engineering 101

---

- [Include direct instructions in prompts](Include%20direct%20instructions%20in%20prompts.md)
- [Give examples in prompts to get the best response](Give%20examples%20in%20prompts%20to%20get%20the%20best%20response.md)
- [Align prompt instructions with the task’s end goal](Align%20prompt%20instructions%20with%20the%20task’s%20end%20goal.md)
- [Use personas to get more specific voices](Use%20personas%20to%20get%20more%20specific%20voices.md)
- [Include acceptable responses in prompts for consistency](Include%20acceptable%20responses%20in%20prompts%20for%20consistency.md)
- [Try different prompts to find what works best](Try%20different%20prompts%20to%20find%20what%20works%20best.md)
- [Summary](AI-Prompts/Prompt%20Guides/101/Summary.md)

In this post, we'll explore the fundamentals of prompt engineering. We'll explain how Large Language Models (LLMs) interpret prompts to generate outputs, and provide tips and tricks to get you started prototyping and implementing LLMs quickly.

The recent rise of Large Language Models (LLMs) such as GPT-3, ChatGPT, AI21's Jurassic, and Cohere has revolutionized what can be achieved with AI. These models, trained on vast amounts of text, can answer questions, generate marketing content, summarize meeting notes, write code, and much more -- if used correctly.

Interacting with LLMs is very different from traditional ML models. We provide a textual prompt as instructions to the LLM to complete a specific task, relying on its pre-training on large datasets to give us an accurate answer.

![An example of a prompt (non-highlighted text) to an LLM (GPT-3 in this case) asking it to translate a sentence from English to Turkish with the output of the LLM highlighted in green.](https://humanloop.com/_next/image?url=%2Fblog%2Fprompt-engineering-101%2F1.png&w=3840&q=75)

An example of a prompt (non-highlighted text) to an LLM (GPT-3 in this case) asking it to translate a sentence from English to Turkish with the output of the LLM highlighted in green.

These instructions are called **prompts.** Prompts are the input to an LLM and their purpose is to tell the LLM what to do or how to think about a problem to get the best and most accurate output to a task possible. Adjusting a prompt to get more specific/usable responses from an LLM is called **prompt engineering** and is a key skill; it’s the biggest part of the effort of using LLMs.

Prompt engineering can be a difficult task but is essential to get the most out of an LLM. In this article, we’ll cover best practices for creating prompts so you can start building effective LLM applications.

---
