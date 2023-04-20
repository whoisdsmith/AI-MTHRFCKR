# Prompt Engineering Tips and Tricks with GPT-3

---

April 21, 2021

I’m going to assume you know what GPT-3 is and why it’s a [Big Deal™](https://www.vox.com/future-perfect/21355768/gpt-3-ai-openai-turing-test-language).

The way you interact with GPT-3, or its forthcoming competitors, is through Prompt Engineering.

In this post I’ll briefly explain what Prompt Engineering is, why it matters, and some tips and tricks to help you do it well. While I doubt traditional programming is going away anytime soon, I do predict that Prompt Engineering is going to be a very important part of most developers’ toolboxes. Prompt Engineering allows developers to implement natural language understanding and soft decision-making processes that would otherwise be difficult or impossible.

## Prompt Engineering

I’ve been fortunate enough to get to spend time integrating GPT-3 into a complex product. A significant portion of this time was spent doing “Prompt Engineering”, in which you convince a Large Language Model (LLM) like GPT-3 that it is writing a document whose structure and content cause it to perform your desired task. This document, called the “prompt”, often contains instructions and examples of what you’d like the LLM to do.

First, some terminology:

- Model: The LLM being used, GPT-3 in this case.
- Prompt: The text given to the language model to be completed.
- Zero-shot: A prompt with no examples, e.g. `The name of a character from Lord of the Rings is:` or `[English: "Hello!", French: "`
- Few-shot: A prompt with one (1-shot) or more (n-shot, few-shot) examples.

Here’s a sample few-shot (4-shot, technically) prompt:

```
This is a list of startup ideas:
1. [Tag: Internet] A website that lets you post articles you've written, and other people can help you edit them.
2. [Tag: Home] A website that lets you share a photo of something broken in your house, and then local people can offer to fix it for you.
3. [Tag: Children] An online service that teaches children how to code.
4. [Tag: Financial] An online service that allows people to rent out their unused durable goods to people who need them.
5. [Tag: Machine Learning]
```

In this example prompt, we have some context (`This is a list of startup ideas:`) and some few-shot examples. The most likely token to come next in the document is a space, followed by a brilliant new startup idea involving Machine Learning, and indeed, this is what GPT-3 provides: “An online service that lets people upload a bunch of data, and then automatically builds a machine learning model based on that data.” (Ideas 1-4 are also based on ones suggested by GPT-3 from previous iterations of this prompt.)

This prompt is interesting for a few reasons:

1. GPT-3 does a surprisingly good job at it, generating some genuinely interesting ideas. (A couple recent ones: “An online service that lets people rent out their parking or storage space to other people who need it.” and “An online service that lets you pay people who own drones to fly one over your house and take a picture.”)
2. Starting a list item with a number (and in this case also a tag) forces the model to generate a new item. If we simply stopped after line 4, without the `5.` prefix, the model will sometimes decide to do something like add a blank line and then start an entirely new and unrelated list.
3. The use of tags at the front of each idea forces the model to try and generate something within a space of interest.
4. The model can be quite sensitive to the prompt “bleeding over” or “semantically contaminating” the output. That is, the ideas it generates will often look similar to and have the same structure as the examples. This is a general problem with few-shot examples, and motivates the usage of zero-shots when possible. In general, the style, language, and subject of your examples will strongly affect model completions.

## A few more examples

(**Bold** is the prompt, the rest is a sample completion.)

A zero-shot:

> **This is a poem written by Robert Frost about the perils of machine learning.**
>
> Alas! The machines are here.
>
> They’ll eat our brains and take our jobs,
>
> They’ll do our thinking for us,
>
> And all that we’ll be able to do
>
> Is program them.
>
> Alas! Here comes the Machine

Robert Frost was quite prescient.

Another zero-shot:

> **English: This sandwich is very tasty.**
>
> **Spanish:** Este sándwich es muy rico.
>
> English: This meat is very tender.
>
> Spanish: Este carne es muy tierna.
>
> English: This fruit is very sweet.
>
> Spanish: Este fruta es muy dulce.

There you see an example of what happens if you allow the model to keep completing after you’ve gotten your desired result.

A small few-shot:

> **Translate each sentence into a string of emojis.**
>
> **English: That cat ate the fish.**
>
> **Emojis: 🐱😋🐟**
>
> **English: What is this, a house for ants?**
>
> **Emojis: 🏠🐜❓**
>
> **English: The quick brown fox jumps over the lazy dog.**
>
> **Emojis: 💨🦊🏃😴🐕**
>
> **English: One small step for man, one giant leap for mankind.**
>
> Emojis: 🚀🌌🌍🏃

It’s also really good at lists.

> **Popular business books:**
>
> **–The Innovator’s Dilemma**
>
> **–Peopleware**
>
>–The Mythical Man-Month
>
>–The Design of Everyday Things
>
>–The Inmates Are Running the Asylum
>
>–The Goal
>
>–The Tipping Point

## Some things to keep in mind when designing prompts (in no particular order)

### The LLM is completing a document, and documents rarely change writing style halfway through

If your prompt has spelling or grammar errors, or inconsistent formatting, completions will have these issues as well. Very frequently in working with GPT-3, I’ve found examples of prompts that have poor writing quality, spelling errors, or grammar errors. GPT-3 completes based on the highest likelihood next token, and it’s very unlikely that a document with poor spelling and grammar suddenly becomes one without those issues halfway through, so GPT-3 will gladly continue the trend for you. Additionally, I suspect the level of reasoning in completions from poorly-written prompts is worse, as there are fewer examples of documents in GPT-3’s training data (e.g., the Internet) that are poorly written, but still well-reasoned.

### Consider dynamically selecting the most relevant few-shots

Because the LLM will tend to follow the content as well as structure of your examples, it can be a good idea to have a database of few-shot examples that you select from based on the problem you’re trying to solve. For example, if you have an app that allows generation of character names, let your user specify the genre, then seed the few-shots with sample names consistent with that genre. Or, in the idea generation case above, if you want to generate superb ideas for blockchain companies, make all of your few-shots be genuinely good examples of blockchain usages. If you want to generate ideas about animal husbandry, use few-shots from that space. Etc.

### Instead of generating N list items, generate 1 list item N times

The more you allow the LLM to generate without a human pulling it back to sanity, the more it will diverge. It’s basically performing a semi-random walk through document space. LLMs also have a tendency to get stuck in loops, because as soon as they accidentally repeat themselves for any reason, this becomes their prior: they now find themselves completing a document that has repetitions in it, and so continue the trend. If you’re trying to generate many examples, such as with the startup ideas list, instead of allowing the model to complete items 6, 7, 8, and so on, instead let it complete only a single line, using OpenAI’s `stop` parameter set to `\n`, and set the number of results parameter `n` to something greater than 1 to generate many single-line completions efficiently.

### Generate many samples and rank them

You can improve quality by ranking results. Using the `n` parameter mentioned above, you could efficiently generate multiple completions, then sort or rejection sample those completions by some useful heuristic such as downweighting overlap with the prompt (to avoid repetitiveness) or by some domain-specific metric.

### The order of few-shots matter

Few-shots later in your examples will bias completion results more than earlier ones. It can be worth randomizing your few-shot order on each generation, or [applying other techniques](https://arxiv.org/abs/2102.09690) to account for this bias, as well as the model’s other inherent biases.

### We may develop techniques to evolve or optimize prompts

Training and evolving prompts to improve completion quality is an active area of research. Here are some recent papers to get you started.

- [Prefix-Tuning: Optimizing Continuous Prompts for Generation](https://arxiv.org/abs/2101.00190)
- [The Power of Scale for Parameter-Efficient Prompt Tuning](https://arxiv.org/abs/2104.08691)
- [Surface Form Competition: Why the Highest Probability Answer Isn’t Always Right](https://peterwestuw.github.io/surface-form-competition-project/)

And if you want to dig deeper into pure Prompt Engineering, [Methods of prompt programming](https://generative.ink/posts/methods-of-prompt-programming/) is a great read.

## Prompt Engineering is going to be important

As I said, I doubt traditional programming is going away anytime soon, but Prompt Engineering is probably here to stay. I’m excited to see where LLMs go (GPT-4 here we come!), and I’ll add more tips as I learn them!

## Comments
