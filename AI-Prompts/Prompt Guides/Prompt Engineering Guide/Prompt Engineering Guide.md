# Prompt Engineering Guide

---

- [[#Introduction|Introduction]]
- [[#LLM Settings|LLM Settings]]
- [[#Basics of Prompting|Basics of Prompting]]
- [[#Elements of a Prompt|Elements of a Prompt]]
- [[#General Tips for Designing Prompts|General Tips for Designing Prompts]]
- [[#Examples of Prompts|Examples of Prompts]]
- [[#Prompting Techniques|Prompting Techniques]]
- [[#Zero-Shot Prompting|Zero-Shot Prompting]]
- [[#Few-Shot Prompting|Few-Shot Prompting]]
- [[#Chain-of-Thought Prompting|Chain-of-Thought Prompting]]
- [[#Self-Consistency|Self-Consistency]]
- [[#Generated Knowledge Prompting|Generated Knowledge Prompting]]
- [[#Automatic Prompt Engineer (APE)|Automatic Prompt Engineer (APE)]]
- [[#Active-Prompt|Active-Prompt]]
- [[#Directional Stimulus Prompting|Directional Stimulus Prompting]]
- [[#ReAct Prompting|ReAct Prompting]]
- [[#Multimodal CoT Prompting|Multimodal CoT Prompting]]
- [[#GraphPrompts|GraphPrompts]]
- [[#Prompting Applications|Prompting Applications]]
- [[#Prompting Applications|Prompting Applications]]
- [[#PAL (Program-Aided Language Models)|PAL (Program-Aided Language Models)]]
- [[#Generating Data|Generating Data]]
- [[#Graduate Job Classification Case Study|Graduate Job Classification Case Study]]
- [[#Models|Models]]
- [[#Scaling Instruction-Finetuned Language Models|Scaling Instruction-Finetuned Language Models]]
- [[#ChatGPT Prompt Engineering|ChatGPT Prompt Engineering]]
- [[#Llama|Llama]]
- [[#GPT-4|GPT-4]]
- [[#Model Collection|Model Collection]]
- [[#Risks & Misuses|Risks & Misuses]]
- [[#Adversarial Prompting|Adversarial Prompting]]
- [[#Factuality|Factuality]]
- [[#Biases|Biases]]
- [[#Papers|Papers]]
- [[#Tools & Libraries|Tools & Libraries]]
- [[#Prompt Engineering Notebooks|Prompt Engineering Notebooks]]
- [[#Datasets|Datasets]]
- [[#Additional Readings|Additional Readings]]

---

Prompt engineering is a relatively new discipline for developing and optimizing prompts to efficiently use language models (LMs) for a wide variety of applications and research topics. Prompt engineering skills help to better understand the capabilities and limitations of large language models (LLMs).

Researchers use prompt engineering to improve the capacity of LLMs on a wide range of common and complex tasks such as question answering and arithmetic reasoning. Developers use prompt engineering to design robust and effective prompting techniques that interface with LLMs and other tools.

Prompt engineering is not just about designing and developing prompts. It encompasses a wide range of skills and techniques that are useful for interacting and developing with LLMs. It's an important skill to interface, build with, and understand capabilities of LLMs. You can use prompt engineering to improve safety of LLMs and build new capabilities like augmenting LLMs with domain knowledge and external tools.

Motivated by the high interest in developing with LLMs, we have created this new prompt engineering guide that contains all the latest papers, learning guides, models, lectures, references, new LLM capabilities, and tools related to prompt engineering.

[Introduction](https://www.promptingguide.ai/introduction "Introduction")

## Introduction

---

Prompt engineering is a relatively new discipline for developing and optimizing prompts to efficiently use language models (LMs) for a wide variety of applications and research topics. Prompt engineering skills help to better understand the capabilities and limitations of large language models (LLMs). Researchers use prompt engineering to improve the capacity of LLMs on a wide range of common and complex tasks such as question answering and arithmetic reasoning. Developers use prompt engineering to design robust and effective prompting techniques that interface with LLMs and other tools.

This guide covers the basics of prompts to provide a rough idea of how to use prompts to interact and instruct LLMs.

All examples are tested with `text-davinci-003` using [OpenAI's playground (opens in a new tab)](https://platform.openai.com/playground) unless otherwise specified. The model uses the default configurations, i.e., `temperature=0.7` and `top-p=1`.

Last updated on April 15, 2023

[Prompt Engineering](https://www.promptingguide.ai/ "Prompt Engineering")[LLM Settings](https://www.promptingguide.ai/introduction/settings "LLM Settings")

## LLM Settings

---

When working with prompts, you interact with the LLM via an API or directly. You can configure a few parameters to get different results for your prompts.

**Temperature** - In short, the lower the `temperature`, the more deterministic the results in the sense that the highest probable next token is always picked. Increasing temperature could lead to more randomness, which encourages more diverse or creative outputs. You are essentially increasing the weights of the other possible tokens. In terms of application, you might want to use a lower temperature value for tasks like fact-based QA to encourage more factual and concise responses. For poem generation or other creative tasks, it might be beneficial to increase the temperature value.

**Top\_p** - Similarly, with `top_p`, a sampling technique with temperature called nucleus sampling, you can control how deterministic the model is at generating a response. If you are looking for exact and factual answers keep this low. If you are looking for more diverse responses, increase to a higher value.

The general recommendation is to alter one, not both.

Before starting with some basic examples, keep in mind that your results may vary depending on the version of LLM you use.

Last updated on April 15, 2023

[Introduction](https://www.promptingguide.ai/introduction "Introduction")[Basics of Prompting](https://www.promptingguide.ai/introduction/basics "Basics of Prompting")

## Basics of Prompting

---

### Basic Prompts[](https://www.promptingguide.ai/#basic-prompts)

You can achieve a lot with simple prompts, but the quality of results depends on how much information you provide it and how well-crafted it is. A prompt can contain information like the *instruction* or *question* you are passing to the model and including other details such as *context*, *inputs*, or *examples*. You can use these elements to instruct the model better and as a result get better results.

Let's get started by going over a basic example of a simple prompt:

*Prompt*

*Output:*

As you can see, the language model outputs a continuation of strings that make sense given the context `"The sky is"`. The output might be unexpected or far from the task we want to accomplish.

This basic example also highlights the necessity to provide more context or instructions on what specifically we want to achieve.

Let's try to improve it a bit:

*Prompt:*

*Output:*

Is that better? Well, we told the model to complete the sentence so the result looks a lot better as it follows exactly what we told it to do ("complete the sentence"). This approach of designing optimal prompts to instruct the model to perform a task is what's referred to as **prompt engineering**.

The example above is a basic illustration of what's possible with LLMs today. Today's LLMs are able to perform all kinds of advanced tasks that range from text summarization to mathematical reasoning to code generation.

### Prompt Formatting[](https://www.promptingguide.ai/#prompt-formatting)

We have tried a very simple prompt above. A standard prompt has the following format:

or

This can be formatted into a question answering (QA) format, which is standard in a lot of QA datasets, as follows:

When prompting like the above, it's also referred to as *zero-shot prompting*, i.e., you are directly prompting the model for a response without any examples or demonstrations about the task you want it to achieve. Some large language models do have the ability to perform zero-shot prompting but it depends on the complexity and knowledge of the task at hand.

Given the standard format above, one popular and effective technique to prompting is referred to as *few-shot prompting* where we provide exemplars (i.e., demonstrations). Few-shot prompts can be formatted as follows:

The QA format version would look like this:

Keep in mind that it's not required to use QA format. The prompt format depends on the task at hand. For instance, you can perform a simple classification task and give exemplars that demonstrate the task as follows:

*Prompt:*

*Output:*

Few-shot prompts enable in-context learning which is the ability of language models to learn tasks given a few demonstrations.

[LLM Settings](https://www.promptingguide.ai/introduction/settings "LLM Settings")[Prompt Elements](https://www.promptingguide.ai/introduction/elements "Prompt Elements")

## Elements of a Prompt

---

As we cover more and more examples and applications that are possible with prompt engineering, you will notice that there are certain elements that make up a prompt.

A prompt can contain any of the following components:

**Instruction** - a specific task or instruction you want the model to perform

**Context** - can involve external information or additional context that can steer the model to better responses

**Input Data** - is the input or question that we are interested to find a response for

**Output Indicator** - indicates the type or format of the output.

Not all the components are required for a prompt and the format depends on the task at hand. We will touch on more concrete examples in upcoming guides.

[Basics of Prompting](https://www.promptingguide.ai/introduction/basics "Basics of Prompting")[General Tips for Designing Prompts](https://www.promptingguide.ai/introduction/tips "General Tips for Designing Prompts")

## General Tips for Designing Prompts

---

Here are some tips to keep in mind while you are designing your prompts:

### Start Simple[](https://www.promptingguide.ai/#start-simple)

As you get started with designing prompts, you should keep in mind that it is really an iterative process that requires a lot of experimentation to get optimal results. Using a simple playground like OpenAI or Cohere's is a good starting point.

You can start with simple prompts and keep adding more elements and context as you aim for better results. Versioning your prompt along the way is vital for this reason. As we read the guide you will see many examples where specificity, simplicity, and conciseness will often give you better results.

When you have a big task that involves many different subtasks, you can try to break down the task into simpler subtasks and keep building up as you get better results. This avoids adding too much complexity to the prompt design process at the beginning.

### The Instruction[](https://www.promptingguide.ai/#the-instruction)

You can design effective prompts for various simple tasks by using commands to instruct the model what you want to achieve such as "Write", "Classify", "Summarize", "Translate", "Order", etc.

Keep in mind that you also need to experiment a lot to see what works best. Try different instructions with different keywords, contexts, and data and see what works best for your particular use case and task. Usually, the more specific and relevant the context is to the task you are trying to perform, the better. We will touch on the importance of sampling and adding more context in the upcoming guides.

Others recommend that instructions are placed at the beginning of the prompt. It's also recommended that some clear separator like "###" is used to separate the instruction and context.

For instance:

*Prompt:*

*Output:*

### Specificity[](https://www.promptingguide.ai/#specificity)

Be very specific about the instruction and task you want the model to perform. The more descriptive and detailed the prompt is, the better the results. This is particularly important when you have a desired outcome or style of generation you are seeking. There aren't specific tokens or keywords that lead to better results. It's more important to have a good format and descriptive prompt. In fact, providing examples in the prompt is very effective to get desired output in specific formats.

When designing prompts you should also keep in mind the length of the prompt as there are limitations regarding how long this can be. Thinking about how specific and detailed you should be is something to consider. Including too many unnecessary details is not necessarily a good approach. The details should be relevant and contribute to the task at hand. This is something you will need to experiment with a lot. We encourage a lot of experimentation and iteration to optimize prompts for your applications.

As an example, let's try a simple prompt to extract specific information from a piece of text.

*Prompt:*

*Output:*

Input text is obtained from [this Nature article (opens in a new tab)](https://www.nature.com/articles/d41586-023-00509-z).

### Avoid Impreciseness[](https://www.promptingguide.ai/#avoid-impreciseness)

Given the tips above about being detailed and improving format, it's easy to fall into the trap of wanting to be too clever about prompts and potentially creating imprecise descriptions. It's often better to be specific and direct. The analogy here is very similar to effective communication -- the more direct, the more effective the message gets across.

For example, you might be interested in learning the concept of prompt engineering. You might try something like:

It's not clear from the prompt above how many sentences to use and what style. You might still somewhat get good responses with the above prompts but the better prompt would be one that is very specific, concise, and to the point. Something like:

### To do or not to do?[](https://www.promptingguide.ai/#to-do-or-not-to-do)

Another common tip when designing prompts is to avoid saying what not to do but say what to do instead. This encourages more specificity and focuses on the details that lead to good responses from the model.

Here is an example of a movie recommendation chatbot failing at exactly what I don't want it to do because of how I wrote the instruction -- focusing on what not to do.

*Prompt:*

*Output:*

Here is a better prompt:

*Prompt:*

*Output:*

Some of the examples above were adopted from the ["Best practices for prompt engineering with OpenAI API" article. (opens in a new tab)](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)

[Prompt Elements](https://www.promptingguide.ai/introduction/elements "Prompt Elements")[Examples of Prompts](https://www.promptingguide.ai/introduction/examples "Examples of Prompts")

## Examples of Prompts

---

In the previous section, we introduced and gave a basic examples of how to prompt LLMs.

In this section, we will provide more examples of how prompts are used to achieve different tasks and introduce key concepts along the way. Often, the best way to learn concepts is by going through examples. Below we cover a few examples of how well-crafted prompts can be used to perform different types of tasks.

Topics:

- [Text Summarization](https://www.promptingguide.ai/introduction/examples#text-summarization)
- [Information Extraction](https://www.promptingguide.ai/introduction/examples#information-extraction)
- [Question Answering](https://www.promptingguide.ai/introduction/examples#question-answering)
- [Text Classification](https://www.promptingguide.ai/introduction/examples#text-classification)
- [Conversation](https://www.promptingguide.ai/introduction/examples#conversation)
- [Code Generation](https://www.promptingguide.ai/introduction/examples#code-generation)
- [Reasoning](https://www.promptingguide.ai/introduction/examples#reasoning)

---

### Text Summarization[](https://www.promptingguide.ai/#text-summarization)

One of the standard tasks in natural language generation is text summarization. Text summarization can include many different flavors and domains. In fact, one of the most promising applications of language models is the ability to summarize articles and concepts into quick and easy-to-read summaries. Let's try a basic summarization task using prompts.

Let's say I am interested to learn about antibiotics, I could try a prompt like this:

*Prompt:*

*Output:*

The "A:" is an explicit prompt format that's used in question answering. I used it here to tell the model that there is an expected further. In this example, it's not clear how this is useful vs not using it but we will leave it that for later examples. Let's just assume that this is too much information and want to summarize it further. In fact, we can instruct the model to summarize into one sentence like so:

*Prompt:*

*Output:*

Without paying too much attention to the accuracy of the output above, which is something we will touch on in a later guide, the model tried to summarize the paragraph in one sentence. You can get clever with the instructions but we will leave that for a later chapter. Feel free to pause here and experiment to see if you get better results.

---

### Information Extraction[](https://www.promptingguide.ai/#information-extraction)

While language models are trained to perform natural language generation and related tasks, it's also very capable of performing classification and a range of other natural language processing (NLP) tasks.

Here is an example of a prompt that extracts information from a given paragraph.

*Prompt:*

*Output:*

There are many ways we can improve the results above, but this is already very useful.

By now it should be obvious that you can ask the model to perform different tasks by simply instructing it what to do. That's a powerful capability that AI product developers are already using to build powerful products and experiences.

Paragraph source: [ChatGPT: five priorities for research (opens in a new tab)](https://www.nature.com/articles/d41586-023-00288-7)

---

### Question Answering[](https://www.promptingguide.ai/#question-answering)

One of the best ways to get the model to respond to specific answers is to improve the format of the prompt. As covered before, a prompt could combine instructions, context, input, and output indicators to get improved results. While these components are not required, it becomes a good practice as the more specific you are with instruction, the better results you will get. Below is an example of how this would look following a more structured prompt.

*Prompt:*

*Output:*

Context obtained from [Nature (opens in a new tab)](https://www.nature.com/articles/d41586-023-00400-x).

---

### Text Classification[](https://www.promptingguide.ai/#text-classification)

So far, we have used simple instructions to perform a task. As a prompt engineer, you will need to get better at providing better instructions. But that's not all! You will also find that for harder use cases, just providing instructions won't be enough. This is where you need to think more about the context and the different elements you can use in a prompt. Other elements you can provide are `input data` or `examples`.

Let's try to demonstrate this by providing an example of text classification.

*Prompt:*

*Output:*

We gave the instruction to classify the text and the model responded with `'Neutral'` which is correct. Nothing is wrong with this but let's say that what we really need is for the model to give the label in the exact format we want. So instead of `Neutral` we want it to return `neutral`. How do we achieve this? There are different ways to do this. We care about specificity here, so the more information we can provide the prompt the better results. We can try providing examples to specify the correct behavior. Let's try again:

*Prompt:*

*Output:*

Perfect! This time the model returned `neutral` which is the specific label I was looking for. It seems that the example provided in the prompt helped the model to be specific in its output.

To highlight why sometimes being specific is important, check out the example below and spot the problem:

*Prompt:*

*Output:*

What is the problem here? As a hint, the made up `nutral` label is completely ignored by the model. Instead, the model outputs `Neutral` as it has some bias towards that label. But let's assume that what we really want is `nutral`. How would you fix this? Maybe you can try adding descriptions to the labels or add more examples to the prompt? If you are not sure, we will discuss a few ideas in the upcoming sections.

---

### Conversation[](https://www.promptingguide.ai/#conversation)

Perhaps one of the more interesting things you can achieve with prompt engineering is instructing the LLM system on how to behave, its intent, and its identity. This is particularly useful when you are building conversational systems like customer service chatbots.

For instance, let's create a conversational system that's able to generate more technical and scientific responses to questions. Note how we are explicitly telling it how to behave through the instruction. This is sometimes referred to as *role prompting*.

*Prompt:*

*Output:*

Our AI research assistant sounds a bit too technical, right? Okay, let's change this behavior and instruct the system to give more accessible answers.

*Prompt:*

*Output:*

I think we made some progress. You can continue improving it. I am sure if you add more examples you might get even better results.

---

### Code Generation[](https://www.promptingguide.ai/#code-generation)

One application where LLMs are quite effective is code generation. Copilot is a great example of this. There are a vast number of code-generation tasks you can perform with clever prompts. Let's look at a few examples below.

First, let's try a simple program that greets the user.

*Prompt:*

*Output:*

You can see that we didn't even need to specify the language to use.

Let's switch levels a bit. I want to show you how powerful LLMs can be with a little more effort in designing the prompts.

*Prompt:*

*Output:*

This is very impressive. In this case, we provided data about the database schema and asked it to generate a valid MySQL query.

---

### Reasoning[](https://www.promptingguide.ai/#reasoning)

Perhaps one of the most difficult tasks for an LLM today is one that requires some form of reasoning. Reasoning is one of the areas that I am most excited about due to the types of complex applications that can emerge from LLMs.

There have been some improvements in tasks involving mathematical capabilities. That said, it's important to note that current LLMs struggle to perform reasoning tasks so this requires even more advanced prompt engineering techniques. We will cover these advanced techniques in the next guide. For now, we will cover a few basic examples to show arithmetic capabilities.

*Prompt:*

*Output:*

Let's try something more difficult.

*Prompt:*

*Output*

That's incorrect! Let's try to improve this by improving the prompt.

*Prompt:*

*Output:*

Much better, right? By the way, I tried this a couple of times and the system sometimes fails. If you provide better instructions combined with examples, it might help get more accurate results.

We will continue to include more examples of common applications in this section of the guide.

In the upcoming section, we will cover even more advanced prompt engineering concepts and techniques for improving performance on all these and more difficult tasks.

Last updated on April 16, 2023

[General Tips for Designing Prompts](https://www.promptingguide.ai/introduction/tips "General Tips for Designing Prompts")[Techniques](https://www.promptingguide.ai/techniques "Techniques")

## Prompting Techniques

---

Techniques

By this point, it should be obvious that it helps to improve prompts to get better results on different tasks. That's the whole idea behind prompt engineering.

While the basic examples were fun, in this section we cover more advanced prompting engineering techniques that allow us to achieve more complex and interesting tasks.

[Examples of Prompts](https://www.promptingguide.ai/introduction/examples "Examples of Prompts")[Zero-shot Prompting](https://www.promptingguide.ai/techniques/zeroshot "Zero-shot Prompting")

## Zero-Shot Prompting

---

LLMs today trained on large amounts of data and tuned to follow instructions, are capable of performing tasks zero-shot. We tried a few zero-shot examples in the previous section. Here is one of the examples we used:

*Prompt:*

*Output:*

Note that in the prompt above we didn't provide the model with any examples -- that's the zero-shot capabilities at work.

Instruction tuning has shown to improve zero-shot learning [Wei et al. (2022) (opens in a new tab)](https://arxiv.org/pdf/2109.01652.pdf). Instruction tuning is essentially the concept of finetuning models on datasets described via instructions. Furthermore, [RLHF (opens in a new tab)](https://arxiv.org/abs/1706.03741) (reinforcement learning from human feedback) has been adopted to scale instruction tuning wherein the model is aligned to better fit human preferences. This recent development powers models like ChatGPT. We will discuss all these approaches and methods in upcoming sections.

When zero-shot doesn't work, it's recommended to provide demonstrations or examples in the prompt which leads to few-shot prompting. In the next section, we demonstrate few-shot prompting.

[Techniques](https://www.promptingguide.ai/techniques "Techniques")[Few-shot Prompting](https://www.promptingguide.ai/techniques/fewshot "Few-shot Prompting")

## Few-Shot Prompting

---

While large-language models demonstrate remarkable zero-shot capabilities, they still fall short on more complex tasks when using the zero-shot setting. Few-shot prompting can be used as a technique to enable in-context learning where we provide demonstrations in the prompt to steer the model to better performance. The demonstrations serve as conditioning for subsequent examples where we would like the model to generate a response.

According to [Touvron et al. 2023 (opens in a new tab)](https://arxiv.org/pdf/2302.13971.pdf) few shot properties first appeared when models were scaled to a sufficient size [(Kaplan et al., 2020) (opens in a new tab)](https://arxiv.org/abs/2001.08361).

Let's demonstrate few-shot prompting via an example that was presented in [Brown et al. 2020 (opens in a new tab)](https://arxiv.org/abs/2005.14165). In the example, the task is to correctly use a new word in a sentence.

*Prompt:*

*Output:*

We can observe that the model has somehow learned how to perform the task by providing it with just one example (i.e., 1-shot). For more difficult tasks, we can experiment with increasing the demonstrations (e.g., 3-shot, 5-shot, 10-shot, etc.).

Following the findings from [Min et al. (2022) (opens in a new tab)](https://arxiv.org/abs/2202.12837), here are a few more tips about demonstrations/exemplars when doing few-shot:

- "the label space and the distribution of the input text specified by the demonstrations are both important (regardless of whether the labels are correct for individual inputs)"
- the format you use also plays a key role in performance, even if you just use random labels, this is much better than no labels at all.
- additional results show that selecting random labels from a true distribution of labels (instead of a uniform distribution) also helps.

Let's try out a few examples. Let's first try an example with random labels (meaning the labels Negative and Positive are randomly assigned to the inputs):

*Prompt:*

*Output:*

We still get the correct answer, even though the labels have been randomized. Note that we also kept the format, which helps too. In fact, with further experimentation, it seems the newer GPT models we are experimenting with are becoming more robust to even random formats. Example:

*Prompt:*

*Output:*

There is no consistency in the format above but the model still predicted the correct label. We have to conduct a more thorough analysis to confirm if this holds for different and more complex tasks, including different variations of prompts.

### Limitations of Few-shot Prompting[](https://www.promptingguide.ai/#limitations-of-few-shot-prompting)

Standard few-shot prompting works well for many tasks but is still not a perfect technique, especially when dealing with more complex reasoning tasks. Let's demonstrate why this is the case. Do you recall the previous example where we provided the following task:

If we try this again, the model outputs the following:

This is not the correct response, which not only highlights the limitations of these systems but that there is a need for more advanced prompt engineering.

Let's try to add some examples to see if few-shot prompting improves the results.

*Prompt:*

*Output:*

That didn't work. It seems like few-shot prompting is not enough to get reliable responses for this type of reasoning problem. The example above provides basic information on the task. If you take a closer look, the type of task we have introduced involves a few more reasoning steps. In other words, it might help if we break the problem down into steps and demonstrate that to the model. More recently, [chain-of-thought (CoT) prompting (opens in a new tab)](https://arxiv.org/abs/2201.11903) has been popularized to address more complex arithmetic, commonsense, and symbolic reasoning tasks.

Overall, it seems that providing examples is useful for solving some tasks. When zero-shot prompting and few-shot prompting are not sufficient, it might mean that whatever was learned by the model isn't enough to do well at the task. From here it is recommended to start thinking about fine-tuning your models or experimenting with more advanced prompting techniques. Up next we talk about one of the popular prompting techniques called chain-of-thought prompting which has gained a lot of popularity.

[Zero-shot Prompting](https://www.promptingguide.ai/techniques/zeroshot "Zero-shot Prompting")[Chain-of-Thought Prompting](https://www.promptingguide.ai/techniques/cot "Chain-of-Thought Prompting")

## Chain-of-Thought Prompting

---

### Chain-of-Thought (CoT) Prompting[](https://www.promptingguide.ai/#chain-of-thought-cot-prompting)

![COT](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcot.1933d9fe.png&w=1920&q=75)

Image Source: [Wei et al. (2022) (opens in a new tab)](https://arxiv.org/abs/2201.11903)

Introduced in [Wei et al. (2022) (opens in a new tab)](https://arxiv.org/abs/2201.11903), chain-of-thought (CoT) prompting enables complex reasoning capabilities through intermediate reasoning steps. You can combine it with few-shot prompting to get better results on more complex tasks that require reasoning before responding.

*Prompt:*

*Output:*

Wow! We can see a perfect result when we provided the reasoning step. In fact, we can solve this task by providing even fewer examples, i.e., just one example seems enough:

*Prompt:*

*Output:*

Keep in mind that the authors claim that this is an emergent ability that arises with sufficiently large language models.

### Zero-shot COT Prompting[](https://www.promptingguide.ai/#zero-shot-cot-prompting)

![Zero-shot COT](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fzero-cot.79793bee.png&w=1920&q=75)

Image Source: [Kojima et al. (2022) (opens in a new tab)](https://arxiv.org/abs/2205.11916)

One recent idea that came out more recently is the idea of [zero-shot CoT (opens in a new tab)](https://arxiv.org/abs/2205.11916) (Kojima et al. 2022) that essentially involves adding "Let's think step by step" to the original prompt. Let's try a simple problem and see how the model performs:

*Prompt:*

*Output:*

The answer is incorrect! Now Let's try with the special prompt.

*Prompt:*

*Output:*

It's impressive that this simple prompt is effective at this task. This is particularly useful where you don't have too many examples to use in the prompt.

[Few-shot Prompting](https://www.promptingguide.ai/techniques/fewshot "Few-shot Prompting")[Self-Consistency](https://www.promptingguide.ai/techniques/consistency "Self-Consistency")

## Self-Consistency

---

Perhaps one of the more advanced techniques out there for prompt engineering is self-consistency. Proposed by [Wang et al. (2022) (opens in a new tab)](https://arxiv.org/pdf/2203.11171.pdf), self-consistency aims "to replace the naive greedy decoding used in chain-of-thought prompting". The idea is to sample multiple, diverse reasoning paths through few-shot CoT, and use the generations to select the most consistent answer. This helps to boost the performance of CoT prompting on tasks involving arithmetic and commonsense reasoning.

Let's try the following example for arithmetic reasoning:

*Prompt:*

*Output:*

The output is wrong! How may we improve this with self-consistency? Let's try it out. We will use the few-shot exemplars from Wang et al. 2022 (Table 17):

*Prompt:*

*Output 1:*

*Output 2:*

*Output 3:*

Computing for the final answer involves a few steps (check out the paper for the details) but for the sake of simplicity, we can see that there is already a majority answer emerging so that would essentially become the final answer.

[Chain-of-Thought Prompting](https://www.promptingguide.ai/techniques/cot "Chain-of-Thought Prompting")[Generate Knowledge Prompting](https://www.promptingguide.ai/techniques/knowledge "Generate Knowledge Prompting")

## Generated Knowledge Prompting

---

![GENKNOW](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fgen-knowledge.055b8d37.png&w=1920&q=75)

Image Source: [Liu et al. 2022 (opens in a new tab)](https://arxiv.org/pdf/2110.08387.pdf)

LLMs continue to be improved and one popular technique includes the ability to incorporate knowledge or information to help the model make more accurate predictions.

Using a similar idea, can the model also be used to generate knowledge before making a prediction? That's what is attempted in the paper by [Liu et al. 2022 (opens in a new tab)](https://arxiv.org/pdf/2110.08387.pdf) -- generate knowledge to be used as part of the prompt. In particular, how helpful is this for tasks such as commonsense reasoning?

Let's try a simple prompt:

*Prompt:*

*Output:*

This type of mistake reveals the limitations of LLMs to perform tasks that require more knowledge about the world. How do we improve this with knowledge generation?

First, we generate a few "knowledges":

*Prompt:*

*Knowledge 1:*

*Knowledge 2:*

We are using the prompt provided in the paper by [Liu et al. 2022 (opens in a new tab)](https://arxiv.org/pdf/2110.08387.pdf).

The next step is to integrate the knowledge and get a prediction. I reformatted the question into QA format to guide the answer format.

*Prompt:*

*Answer 1 (confidence very high):*

*Answer 2 (confidence is a lot lower):*

Some really interesting things happened with this example. In the first answer, the model was very confident but in the second not so much. I simplify the process for demonstration purposes but there are a few more details to consider when arriving at the final answer. Check out the paper for more.

[Self-Consistency](https://www.promptingguide.ai/techniques/consistency "Self-Consistency")[Automatic Prompt Engineer](https://www.promptingguide.ai/techniques/ape "Automatic Prompt Engineer")

## Automatic Prompt Engineer (APE)

---

![APE](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FAPE.3f0e01c2.png&w=1920&q=75)

Image Source: [Zhou et al., (2022) (opens in a new tab)](https://arxiv.org/abs/2211.01910)

[Zhou et al., (2022) (opens in a new tab)](https://arxiv.org/abs/2211.01910) propose automatic prompt engineer (APE) a framework for automatic instruction generation and selection. The instruction generation problem is framed as natural language synthesis addressed as a black-box optimization problem using LLMs to generate and search over candidate solutions.

The first step involves a large language model (as an inference model) that is given output demonstrations to generate instruction candidates for a task. These candidate solutions will guide the search procedure. The instructions are executed using a target model, and then the most appropriate instruction is selected based on computed evaluation scores.

APE discovers a better zero-shot CoT prompt than the human engineered "Let's think step by step" prompt ([Kojima et al., 2022 (opens in a new tab)](https://arxiv.org/abs/2205.11916)).

The prompt "Let's work this out in a step by step way to be sure we have the right answer." elicits chain-of-though reasoning and improves performance on the MultiArith and GSM8K benchmarks:

![APECOT](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fape-zero-shot-cot.75c0f75c.png&w=1920&q=75)

Image Source: [Zhou et al., (2022) (opens in a new tab)](https://arxiv.org/abs/2211.01910)

This paper touches on an important topic related to prompt engineering which is the idea of automatically optimizing prompts. While we don't go deep into this topic in this guide, here are a few key papers if you are interested in the topic:

- [AutoPrompt (opens in a new tab)](https://arxiv.org/abs/2010.15980) - proposes an approach to automatically create prompts for a diverse set of tasks based on gradient-guided search.
- [Prefix Tuning (opens in a new tab)](https://arxiv.org/abs/2101.00190) - a lightweight alternative to fine-tuning that prepends a trainable continuous prefix for NLG tasks.
- [Prompt Tuning (opens in a new tab)](https://arxiv.org/abs/2104.08691) - proposes a mechanism for learning soft prompts through backpropagation.

[Generate Knowledge Prompting](https://www.promptingguide.ai/techniques/knowledge "Generate Knowledge Prompting")[Active-Prompt](https://www.promptingguide.ai/techniques/activeprompt "Active-Prompt")

## Active-Prompt

---

Chain-of-thought (CoT) methods rely on a fixed set of human-annotated exemplars. The problem with this is that the exemplars might not be the most effective examples for the different tasks. To address this, [Diao et al., (2023) (opens in a new tab)](https://arxiv.org/pdf/2302.12246.pdf) recently proposed a new prompting approach called Active-Prompt to adapt LLMs to different task-specific example prompts (annotated with human-designed CoT reasoning).

Below is an illustration of the approach. The first step is to query the LLM with or without a few CoT examples. *k* possible answers are generated for a set of training questions. An uncertainty metric is calculated based on the *k* answers (disagreement used). The most uncertain questions are selected for annotation by humans. The new annotated exemplars are then used to infer each question.

![ACTIVE](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Factive-prompt.f739657b.png&w=3840&q=75)

Image Source: [Diao et al., (2023) (opens in a new tab)](https://arxiv.org/pdf/2302.12246.pdf)

[Automatic Prompt Engineer](https://www.promptingguide.ai/techniques/ape "Automatic Prompt Engineer")[Directional Stimulus Prompting](https://www.promptingguide.ai/techniques/dsp "Directional Stimulus Prompting")

## Directional Stimulus Prompting

---

[Li et al., (2023) (opens in a new tab)](https://arxiv.org/abs/2302.11520) proposes a new prompting technique to better guide the LLM in generating the desired summary.

A tuneable policy LM is trained to generate the stimulus/hint. Seeing more use of RL to optimize LLMs.

The figure below shows how Directional Stimulus Prompting compares with standard prompting. The policy LM can be small and optimized to generate the hints that guide a black-box frozen LLM.

![DSP](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fdsp.27a0005f.jpeg&w=3840&q=75)

Image Source: [Li et al., (2023) (opens in a new tab)](https://arxiv.org/abs/2302.11520)

Full example coming soon!

[Active-Prompt](https://www.promptingguide.ai/techniques/activeprompt "Active-Prompt")[ReAct](https://www.promptingguide.ai/techniques/react "ReAct")

## ReAct Prompting

---

[Yao et al., 2022 (opens in a new tab)](https://arxiv.org/abs/2210.03629) introduced a framework named ReAct where LLMs are used to generate both *reasoning traces* and *task-specific actions* in an interleaved manner.

Generating reasoning traces allow the model to induce, track, and update action plans, and even handle exceptions. The action step allows to interface with and gather information from external sources such as knowledge bases or environments.

The ReAct framework can allow LLMs to interact with external tools to retrieve additional information that leads to more reliable and factual responses.

Results show that ReAct can outperform several state-of-the-art baselines on language and decision-making tasks. ReAct also leads to improved human interpretability and trustworthiness of LLMs. Overall, the authors found that best approach uses ReAct combined with chain-of-thought (CoT) that allows use of both internal knowledge and external information obtained during reasoning.

### How it Works?[](https://www.promptingguide.ai/#how-it-works)

ReAct is inspired by the synergies between "acting" and "reasoning" which allow humans to learn new tasks and make decisions or reasoning.

Chain-of-thought (CoT) prompting has shown the capabilities of LLMs to carry out reasoning traces to generate answers to questions involving arithmetic and commonsense reasoning, among other tasks [(Wei et al., 2022) (opens in a new tab)](https://arxiv.org/abs/2201.11903). But it's lack of access to the external world or inability to update its knowledge can lead to issues like fact hallucination and error propagation.

ReAct is a general paradigm that combines reasoning and acting with LLMs. ReAct prompts LLMs to generate verbal reasoning traces and actions for a task. This allows the system to perform dynamic reasoning to create, maintain, and adjust plans for acting while also enabling interaction to external environments (e.g., Wikipedia) to incorporate additional information into the reasoning. The figure below shows an example of ReAct and the different steps involved to perform question answering.

![REACT](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Freact.8e7c93ae.png&w=1920&q=75)

Image Source: [Yao et al., 2022 (opens in a new tab)](https://arxiv.org/abs/2210.03629)

In the example above, we pass a prompt like the following question from [HotpotQA (opens in a new tab)](https://hotpotqa.github.io/):

Note that in-context examples are also added to the prompt but we exclude that here for simplicity. We can see that the model generates *task solving trajectories* (Thought, Act). Obs corresponds to observation from the environment that's being interacted with (e.g., Search engine). In essence, ReAct can retrieve information to support reasoning, while reasoning helps to target what to retrieve next.

### ReAct Prompting[](https://www.promptingguide.ai/#react-prompting)

To demonstrate how ReAct prompting works, let's follow an example from the paper.

The first step is to select cases from a training set (e.g., HotPotQA) and compose ReAct-format trajectories. These are used as few-shot exemplars in the prompts. The trajectories consist of multiple thought-action-observation steps as shown in the figure above. The free-form thoughts are used to achieve different tasks such as decomposing questions, extracting information, performing commonsense/arithmetic reasoning, guide search formulation, and synthesizing final answer.

Here is an example of what the ReAct prompt exemplars look like (obtained from the paper and shortened to one example for simplicity):

Note that different prompts setups are used for different types of tasks. For tasks where reasoning is of primary importance (e.g., HotpotQA), multiple thought-action-observation steps are used for the task-solving trajectory. For decision making tasks involving lots of action steps, thoughts are used sparsely.

### Results on Knowledge-Intensive Tasks[](https://www.promptingguide.ai/#results-on-knowledge-intensive-tasks)

The paper first evaluates ReAct on knowledge-intensive reasoning tasks such as question answering (HotPotQA) and fact verification ([Fever (opens in a new tab)](https://fever.ai/resources.html)). PaLM-540B is used as the base model for prompting.

![REACT1](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ftable1.e25bc12b.png&w=1920&q=75)

Image Source: [Yao et al., 2022 (opens in a new tab)](https://arxiv.org/abs/2210.03629)

The prompting results on HotPotQA and Fever using different prompting methods show that ReAct generally performs better than Act (involves acting only) on both tasks.

We can also observe that ReAct outperforms CoT on Fever and lags behind CoT on HotpotQA. A detailed error analysis is provided in the paper. In summary:

- CoT suffers from fact hallucination
- ReAct's structural constraint reduces its flexibility in formulating reasoning steps
- ReAct depends a lot on the information it's retrieving; non-informative search results derails the model reasoning and leads to difficulty in recovering and reformulating thoughts

Prompting methods that combine and support switching between ReAct and CoT+Self-Consistency generally outperform all the other prompting methods.

### Results on Knowledge-Intensive Tasks[](https://www.promptingguide.ai/#results-on-knowledge-intensive-tasks-1)

The paper also reports results demonstrating ReAct's performance on decision making tasks. ReAct is evaluated on two benchmarks called [ALFWorld (opens in a new tab)](https://alfworld.github.io/) (text-based game) and [WebShop (opens in a new tab)](https://webshop-pnlp.github.io/) (online shopping website environment). Both involve complex environments that require reasoning to act and explore effectively.

Note that the ReAct prompts are designed differently for these tasks while still keeping the same core idea of combining reasoning and acting. Below is an example for an ALFWorld problem involving ReAct prompting.

![REACT2](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Falfworld.da30656d.png&w=1920&q=75)

Image Source: [Yao et al., 2022 (opens in a new tab)](https://arxiv.org/abs/2210.03629)

ReAct outperforms Act on both ALFWorld and Webshop. Act, without any thoughts, fails to correctly decompose goals into subgoals. Reasoning seems to be advantageous in ReAct for these types of tasks but current prompting-based methods are still far from the performance of expert humans on these tasks.

Check out the paper for more detailed results.

### LangChain ReAct Usage[](https://www.promptingguide.ai/#langchain-react-usage)

Below is a high-level example of how the ReAct prompting approach works in practice. We will be using OpenAI for the LLM and [LangChain (opens in a new tab)](https://python.langchain.com/en/latest/index.html) as it already has built-in functionality that leverages the ReAct framework to build agents that perform tasks by combining the power of LLMs and different tools.

First, let's install and import the necessary libraries:

Now we can configure the LLM, the tools we will use, and the agent that allows us to leverage the ReAct framework together with the LLM and tools. Note that we are using a search API for searching external information and LLM as a math tool.

Once that's configured, we can now run the agent with the desired query/prompt. Notice that here we are not expected to provide few-shot exemplars as explained in the paper.

The chain execution looks as follows:

The output we get is as follows:

We adapted the example from the [LangChain documentation (opens in a new tab)](https://python.langchain.com/en/latest/modules/agents/getting_started.html), so credit goes to them. We encourage the learner to explore different combination of tools and tasks.

You can find the notebook for this code here: [https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/react.ipynb (opens in a new tab)](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/react.ipynb)

Last updated on April 13, 2023

[Directional Stimulus Prompting](https://www.promptingguide.ai/techniques/dsp "Directional Stimulus Prompting")[Multimodal CoT](https://www.promptingguide.ai/techniques/multimodalcot "Multimodal CoT")

## Multimodal CoT Prompting

---

[Zhang et al. (2023) (opens in a new tab)](https://arxiv.org/abs/2302.00923) recently proposed a multimodal chain-of-thought prompting approach. Traditional CoT focuses on the language modality. In contrast, Multimodal CoT incorporates text and vision into a two-stage framework. The first step involves rationale generation based on multimodal information. This is followed by the second phase, answer inference, which leverages the informative generated rationales.

The multimodal CoT model (1B) outperforms GPT-3.5 on the ScienceQA benchmark.

![MCOT](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fmultimodal-cot.a84f6cc1.png&w=1920&q=75)

Image Source: [Zhang et al. (2023) (opens in a new tab)](https://arxiv.org/abs/2302.00923)

Further reading:

- [Language Is Not All You Need: Aligning Perception with Language Models (opens in a new tab)](https://arxiv.org/abs/2302.14045) (Feb 2023)

[ReAct](https://www.promptingguide.ai/techniques/react "ReAct")[Graph Prompting](https://www.promptingguide.ai/techniques/graph "Graph Prompting")

## GraphPrompts

---

[Techniques](https://www.promptingguide.ai/techniques)

Graph Prompting

[Liu et al., 2023 (opens in a new tab)](https://arxiv.org/abs/2302.08043) introduces GraphPrompt, a new prompting framework for graphs to improve performance on downstream tasks.

More coming soon!

[Multimodal CoT](https://www.promptingguide.ai/techniques/multimodalcot "Multimodal CoT")[Applications](https://www.promptingguide.ai/applications "Applications")

## Prompting Applications

---

## Prompting Applications

In this section, we will cover some advanced and interesting ways we can use prompt engineering to perform useful and more advanced tasks.

⚠️

This section is under heavy development.

[Graph Prompting](https://www.promptingguide.ai/techniques/graph "Graph Prompting")[Program-Aided Language Models](https://www.promptingguide.ai/applications/pal "Program-Aided Language Models")

## PAL (Program-Aided Language Models)

---

[Gao et al., (2022) (opens in a new tab)](https://arxiv.org/abs/2211.10435) presents a method that uses LLMs to read natural language problems and generate programs as the intermediate reasoning steps. Coined, program-aided language models (PAL), it differs from chain-of-thought prompting in that instead of using free-form text to obtain solution it offloads the solution step to a programmatic runtime such as a Python interpreter.

![PAL](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fpal.dfc96526.png&w=1920&q=75)

Image Source: [Gao et al., (2022) (opens in a new tab)](https://arxiv.org/abs/2211.10435)

Let's look at an example using LangChain and OpenAI GPT-3. We are interested to develop a simple application that's able to interpret the question being asked and provide an answer by leveraging the Python interpreter.

Specifically, we are interested to create a functionality that allows the use of the LLM to answer questions that require date understanding. We will provide the LLM a prompt that includes a few exemplars which are adopted from [here (opens in a new tab)](https://github.com/reasoning-machines/pal/blob/main/pal/prompt/date_understanding_prompt.py).

These are the imports we need:

Let's first configure a few things:

Setup model instance:

Setup prompt + question:

This will output the following: `02/27/1998`

[Applications](https://www.promptingguide.ai/applications "Applications")[Generating Data](https://www.promptingguide.ai/applications/generating "Generating Data")

## Generating Data

---

LLMs have strong capabilities to generate coherent text. Using effective prompt strategies can steer the model to produce better, consistent, and more factual responses. LLMs can also be especially useful for generating data which is really useful to run all sorts of experiments and evaluations. For example, we can use it to generate quick samples for a sentiment classifier like so:

*Prompt:*

*Output:*

This is very useful. We actually use this example for a different test in another section of the guides.

[Program-Aided Language Models](https://www.promptingguide.ai/applications/pal "Program-Aided Language Models")[Graduate Job Classification Case Study](https://www.promptingguide.ai/applications/workplace_casestudy "Graduate Job Classification Case Study")

## Graduate Job Classification Case Study

---

[Clavié et al., 2023 (opens in a new tab)](https://arxiv.org/abs/2303.07142) provide a case-study on prompt-engineering applied to a medium-scale text classification use-case in a production system. Using the task of classifying whether a job is a true "entry-level job", suitable for a recent graduate, or not, they evaluated a series of prompt engineering techniques and report their results using GPT-3.5 (`gpt-3.5-turbo`).

The work shows that LLMs outperforms all other models tested, including an extremely strong baseline in DeBERTa-V3. `gpt-3.5-turbo` also noticeably outperforms older GPT3 variants in all key metrics, but requires additional output parsing as its ability to stick to a template appears to be worse than the other variants.

The key findings of their prompt engineering approach are:

- For tasks such as this one, where no expert knowledge is required, Few-shot CoT prompting performed worse than Zero-shot prompting in all experiments.
- The impact of the prompt on eliciting the correct reasoning is massive. Simply asking the model to classify a given job results in an F1 score of 65.6, whereas the post-prompt engineering model achieves an F1 score of 91.7.
- Attempting to force the model to stick to a template lowers performance in all cases (this behaviour disappears in early testing with GPT-4, which are posterior to the paper).
- Many small modifications have an outsized impact on performance.
    - The tables below show the full modifications tested.
    - Properly giving instructions and repeating the key points appears to be the biggest performance driver.
    - Something as simple as giving the model a (human) name and referring to it as such increased F1 score by 0.6pts.

### Prompt Modifications Tested[](https://www.promptingguide.ai/#prompt-modifications-tested)

### Performance Impact of All Prompt Modifications[](https://www.promptingguide.ai/#performance-impact-of-all-prompt-modifications)

Template stickiness refers to how frequently the model answers in the desired format.

[Generating Data](https://www.promptingguide.ai/applications/generating "Generating Data")[Models](https://www.promptingguide.ai/models "Models")

## Models

---

In this section, we will cover some of the recent language models and how they successfully apply the latest and most advanced prompting engineering techniques. In addition, we cover capabilities of these models on a range of tasks and prompting setups like few-shot prompting, zero-shot prompting, and chain-of-thought prompting. Understanding these capabilities are important to understand the limitations of these models and how to use them effectively.

⚠️

This section is under heavy development.

[Graduate Job Classification Case Study](https://www.promptingguide.ai/applications/workplace_casestudy "Graduate Job Classification Case Study")[Flan](https://www.promptingguide.ai/models/flan "Flan")

## Scaling Instruction-Finetuned Language Models

---

### What's new?[](https://www.promptingguide.ai/#whats-new)

![FLAN1](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fflan-1.c26df985.png&w=1920&q=75)

Image Source: [Scaling Instruction-Finetuned Language Models (opens in a new tab)](https://arxiv.org/abs/2210.11416)

This paper explores the benefits scaling [instruction finetuning (opens in a new tab)](https://arxiv.org/pdf/2109.01652.pdf) and how it improves performance on a variety of models (PaLM, T5), prompting setups (zero-shot, few-shot, CoT), and benchmarks (MMLU, TyDiQA). This is explored with the following aspects: scaling the number of tasks (1.8K tasks), scaling model size, and finetuning on chain-of-thought data (9 datasets used).

**Finetuning procedure:**

- 1.8K tasks were phrased as instructions and used to finetune the model
- Uses both with and without exemplars, and with and without CoT

Finetuning tasks and held out tasks shown below:

![FLAN11](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fflan-11.3b3298da.png&w=2048&q=75)

### Capabilities & Key Results[](https://www.promptingguide.ai/#capabilities--key-results)

- Instruction finetuning scales well with the number of tasks and the size of the model; this suggests the need for scaling number of tasks and size of model further
- Adding CoT datasets into the finetuning enables good performance on reasoning tasks
- Flan-PaLM has improved multilingual abilities; 14.9% improvement on one-shot TyDiQA; 8.1% improvement on arithmetic reasoning in under-represented languages
- Plan-PaLM also performs well on open-ended generation questions, which is a good indicator for improved usability
- Improves performance across responsible AI (RAI) benchmarks
- Flan-T5 instruction tuned models demonstrate strong few-shot capabilities and outperforms public checkpoint such as T5

**The results when scaling number of finetuning tasks and model size:** scaling both the size of the model and the number of finetuning tasks is expected to continue improving performance, although scaling the number of tasks has diminished returns.

![FLAN2](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fflan-2.10409595.png&w=1920&q=75)

Image Source: [Scaling Instruction-Finetuned Language Models (opens in a new tab)](https://arxiv.org/abs/2210.11416)

**The results when finetuning with non-CoT and CoT data:** Jointly finetuning on non-CoT and CoT data improves performance on both evaluations, compared to finetuning on just one or the other.

![FLAN3](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fflan-3.db3a0ec9.png&w=1920&q=75)

Image Source: [Scaling Instruction-Finetuned Language Models (opens in a new tab)](https://arxiv.org/abs/2210.11416)

In addition, self-consistency combined with CoT achieves SoTA results on several benchmarks. CoT + self-consistency also significantly improves results on benchmarks involving math problems (e.g., MGSM, GSM8K).

![FLAN4](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fflan-4.a595d5a6.png&w=1920&q=75)

Image Source: [Scaling Instruction-Finetuned Language Models (opens in a new tab)](https://arxiv.org/abs/2210.11416)

CoT finetuning unlocks zero-shot reasoning, activated by the phrase "let's think step-by-step", on BIG-Bench tasks. In general, zero-shot CoT Flan-PaLM outperforms zero-shot CoT PaLM without finetuning.

![FLAN6](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fflan-6.a24343d8.png&w=1200&q=75)

Image Source: [Scaling Instruction-Finetuned Language Models (opens in a new tab)](https://arxiv.org/abs/2210.11416)

Below are some demonstrations of zero-shot CoT for PaLM and Flan-PaLM in unseen tasks.

![FLAN5](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fflan-5.98a6c013.png&w=1920&q=75)

Image Source: [Scaling Instruction-Finetuned Language Models (opens in a new tab)](https://arxiv.org/abs/2210.11416)

Below are more examples for zero-shot prompting. It shows how the PaLM model struggles with repetitions and not replying to instructions in the zero-shot setting where the Flan-PaLM is able to perform well. Few-shot exemplars can mitigate these errors.

![FLAN7](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fflan-7.c600a1de.png&w=1920&q=75)

Image Source: [Scaling Instruction-Finetuned Language Models (opens in a new tab)](https://arxiv.org/abs/2210.11416)

Below are some examples demonstrating more zero-shot capabilities of the Flan-PALM model on several different types of challenging open-ended questions:

![FLAN8](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fflan-8.fda963af.png&w=1920&q=75)

Image Source: [Scaling Instruction-Finetuned Language Models (opens in a new tab)](https://arxiv.org/abs/2210.11416)

![FLAN9](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fflan-9.78364907.png&w=1920&q=75)

Image Source: [Scaling Instruction-Finetuned Language Models (opens in a new tab)](https://arxiv.org/abs/2210.11416)

![FLAN10](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fflan-10.60080e50.png&w=1920&q=75)

Image Source: [Scaling Instruction-Finetuned Language Models (opens in a new tab)](https://arxiv.org/abs/2210.11416)

You can try [Flan-T5 models on the Hugging Face Hub (opens in a new tab)](https://huggingface.co/google/flan-t5-xxl).

[Models](https://www.promptingguide.ai/models "Models")[ChatGPT](https://www.promptingguide.ai/models/chatgpt "ChatGPT")

## ChatGPT Prompt Engineering

---

In this section, we cover the latest prompt engineering techniques for ChatGPT, including tips, applications, limitations, papers, and additional reading materials.

Topics:

- [ChatGPT Introduction](https://www.promptingguide.ai/models/chatgpt#chatgpt-introduction)
- [Reviewing The Conversation Task](https://www.promptingguide.ai/models/chatgpt#reviewing-the-conversation-task)
- [Conversations with ChatGPT](https://www.promptingguide.ai/models/chatgpt#conversations-with-chatgpt)

---

### ChatGPT Introduction[](https://www.promptingguide.ai/#chatgpt-introduction)

ChatGPT is a new model [trained by OpenAI (opens in a new tab)](https://openai.com/blog/chatgpt) that has the capability to interact in a conversational way. This model is trained to follow instructions in a prompt to provide appropriate responses in the context of a dialogue. ChatGPT can help with answering questions, suggesting recipes, writing lyrics in a certain style, generating code, and much more.

ChatGPT is trained using Reinforcement Learning from Human Feedback (RLHF). While this model is a lot more capable than previous GPT iterations (and also trained to reduce harmful and untruthful outputs), it still comes with limitations. Let's cover some of the capabilities and limitations with concrete examples.

You can use the research preview of ChatGPT [here](https://www.promptingguide.ai/models/chat.openai.com) but for the examples below we will use the `Chat` mode on the OpenAI Playground.

---

### Reviewing The Conversation Task[](https://www.promptingguide.ai/#reviewing-the-conversation-task)

In one of the previous guides, we covered a bit about conversation capabilities and role prompting. We covered how to instruct the LLM to have a conversation in a specific style, with a specific intent, behavior, and identity.

Let's review our previous basic example where we created a conversational system that's able to generate more technical and scientific responses to questions.

*Prompt:*

From the example above, you can see two important components:

- the **intent** or explanation of what the chatbot is
- the **identity** which instructs the style or tone the chatbot will use to respond

The simple example above works well with the text completion APIs that uses `text-davinci-003`. More recently, OpenAI [announced the ChatGPT APIs (opens in a new tab)](https://openai.com/blog/introducing-chatgpt-and-whisper-apis), which is a more powerful and cheaper model called `gpt-3.5-turbo` was specifically built for this type of functionality (chat completions). In fact, OpenAI recommends this as their best model even for non-chat use cases. Other benefits of using the ChatGPT APIs are significant cost reduction (90%) and efficiency.

Big companies like Snap Inc. and Instacart are already integrating conversational features powered by ChatGPT on their products that range from personalized recommendations to open-ended shopping goals.

---

### Conversations with ChatGPT[](https://www.promptingguide.ai/#conversations-with-chatgpt)

#### Multi-turn Conversations[](https://www.promptingguide.ai/#multi-turn-conversations)

To begin demonstrating the capabilities of ChatGPT, we will use the chatbot assistant example above and discuss the results. Compared to `text-davinci-003`, the `gpt-3.5-turbo` model that powers ChatGPT uses a chat format as input. The model expects a series of messages as input and uses those to generate a response.

*Input:*

*Output:*

Note that in the example above, I have simplified the input and output but the ChatGPT chat completion API requires messages to be in a specific format. I have added a snapshot below of how this example would look using the `Chat Mode` in the OpenAI Playground:

![CHATGPT1](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fchatgpt-1.9a75800f.png&w=3840&q=75)

The more formal API call for our example would look something like the example below:

In fact, the way developers interact with ChatGPT in the future is expected to be done via the [Chat Markup Language (opens in a new tab)](https://github.com/openai/openai-python/blob/main/chatml) (ChatML for short).

#### Single-turn tasks[](https://www.promptingguide.ai/#single-turn-tasks)

The chat format enables multi-turn conversations but it also supports single-turn tasks similar to what we used with `text-davinci-003`. This means we can use ChatGPT to perform similar tasks as what we have demonstrated for the original GPT models. For example, let's try to perform the following question answering task using ChatGPT:

*Input:*

*Output:*

Keep in mind that I am adding the `USER` and `ASSISTANT` labels to better demonstrate how the task can be performed using ChatGPT. Here is the example using the Playground:

![CHATGPTCLASSIC](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fchatgpt-classic.aff12098.png&w=3840&q=75)

More formally, this is the API call (I've only included the message component of the request):

#### Instructing Chat Models[](https://www.promptingguide.ai/#instructing-chat-models)

According to the official OpenAI docs, snapshots of the `gpt-3.5-turbo` model will also be made available. For example, we can access the snapshot from March 1 `gpt-3.5-turbo-0301`. This allows developers to opt for specific model versions. This also means that the best practices for instructing models may change from version to version.

The current recommendation for `gpt-3.5-turbo-0301` is to add instructions in the `user` message as opposed to the available `system` message.

---

### References[](https://www.promptingguide.ai/#references)

- [ChatGPT-4 Outperforms Experts and Crowd Workers in Annotating Political Twitter Messages with Zero-Shot Learning (opens in a new tab)](https://arxiv.org/abs/2304.06588) (April 2023)
- [ChatGPT Beyond English: Towards a Comprehensive Evaluation of Large Language Models in Multilingual Learning (opens in a new tab)](https://arxiv.org/abs/2304.05613) (April 2023)
- [Distinguishing ChatGPT(-3.5, -4)-generated and human-written papers through Japanese stylometric analysis (opens in a new tab)](https://arxiv.org/abs/2304.05534) (April 2023)
- [Zero-shot Temporal Relation Extraction with ChatGPT (opens in a new tab)](https://arxiv.org/abs/2304.05454) (April 2023)
- [Can ChatGPT and Bard Generate Aligned Assessment Items? A Reliability Analysis against Human Performance (opens in a new tab)](https://arxiv.org/abs/2304.05372) (April 2023)
- [Are Large Language Models Ready for Healthcare? A Comparative Study on Clinical Language Understanding (opens in a new tab)](https://arxiv.org/abs/2304.05368) (April 2023)
- [The Wall Street Neophyte: A Zero-Shot Analysis of ChatGPT Over MultiModal Stock Movement Prediction Challenges (opens in a new tab)](https://arxiv.org/abs/2304.05351) (April 2023)
- [Toxicity in ChatGPT: Analyzing Persona-assigned Language Models (opens in a new tab)](https://arxiv.org/abs/2304.05335) (April 2023)
- [Multi-step Jailbreaking Privacy Attacks on ChatGPT (opens in a new tab)](https://arxiv.org/abs/2304.05197) (April 2023)
- [Is ChatGPT a Good Sentiment Analyzer? A Preliminary Study (opens in a new tab)](https://arxiv.org/abs/2304.04339) (April 2023)
- [A Preliminary Evaluation of ChatGPT for Zero-shot Dialogue Understanding (opens in a new tab)](https://arxiv.org/abs/2304.04256) (April 2023)
- [Extractive Summarization via ChatGPT for Faithful Summary Generation (opens in a new tab)](https://arxiv.org/abs/2304.04193) (April 2023)
- [What does ChatGPT return about human values? Exploring value bias in ChatGPT using a descriptive value theory (opens in a new tab)](https://arxiv.org/abs/2304.03612) (April 2023)
- [On the Evaluations of ChatGPT and Emotion-enhanced Prompting for Mental Health Analysis (opens in a new tab)](https://arxiv.org/abs/2304.03347) (April 2023)
- [ChatGPT-Crawler: Find out if ChatGPT really knows what it's talking about (opens in a new tab)](https://arxiv.org/abs/2304.03325) (April 2023)
- [Should ChatGPT be Biased? Challenges and Risks of Bias in Large Language Models (opens in a new tab)](https://arxiv.org/abs/2304.03738) (April 2023)
- [Synthesis of Mathematical programs from Natural Language Specifications (opens in a new tab)](https://arxiv.org/abs/2304.03287) (April 2023)
- [Large language models effectively leverage document-level context for literary translation, but critical errors persist (opens in a new tab)](https://arxiv.org/abs/2304.03245) (April 2023)
- [Investigating Chain-of-thought with ChatGPT for Stance Detection on Social Media (opens in a new tab)](https://arxiv.org/abs/2304.03087) (April 2023)
- [ChatGPT for Shaping the Future of Dentistry: The Potential of Multi-Modal Large Language Model (opens in a new tab)](https://arxiv.org/abs/2304.03086) (April 2023)
- [Can Large Language Models Play Text Games Well? Current State-of-the-Art and Open Questions (opens in a new tab)](https://arxiv.org/abs/2304.02868) (April 2023)
- [Human-like Summarization Evaluation with ChatGPT (opens in a new tab)](https://arxiv.org/abs/2304.02554) (April 2023)
- [Evaluation of ChatGPT Family of Models for Biomedical Reasoning and Classification (opens in a new tab)](https://arxiv.org/abs/2304.02496) (April 2023)
- [Comparative Analysis of CHATGPT and the evolution of language models (opens in a new tab)](https://arxiv.org/abs/2304.02468) (April 2023)
- [Unleashing the Power of ChatGPT for Translation: An Empirical Study (opens in a new tab)](https://arxiv.org/abs/2304.02182) (April 2023)
- [Geotechnical Parrot Tales (GPT): Overcoming GPT hallucinations with prompt engineering for geotechnical applications (opens in a new tab)](https://arxiv.org/abs/2304.02138) (April 2023)
- [Unlocking the Potential of ChatGPT: A Comprehensive Exploration of its Applications, Advantages, Limitations, and Future Directions in Natural Language Processing (opens in a new tab)](https://arxiv.org/abs/2304.02017) (April 2023)
- [Summary of ChatGPT/GPT-4 Research and Perspective Towards the Future of Large Language Models (opens in a new tab)](https://arxiv.org/abs/2304.01852) (April 2023)
- [Is ChatGPT a Highly Fluent Grammatical Error Correction System? A Comprehensive Evaluation (opens in a new tab)](https://arxiv.org/abs/2304.01746) (April 2023)
- [Safety Analysis in the Era of Large Language Models: A Case Study of STPA using ChatGPT (opens in a new tab)](https://arxiv.org/abs/2304.01246) (April 2023)
- [Large language models can rate news outlet credibility (opens in a new tab)](https://arxiv.org/abs/2304.00228) (April 2023)
- [Can AI Chatbots Pass the Fundamentals of Engineering (FE) and Principles and Practice of Engineering (PE) Structural Exams? (opens in a new tab)](https://arxiv.org/abs/2303.18149) (April 2023)
- [Can AI Put Gamma-Ray Astrophysicists Out of a Job? (opens in a new tab)](https://arxiv.org/abs/2303.17853) (March 2023)
- [Comparing Abstractive Summaries Generated by ChatGPT to Real Summaries Through Blinded Reviewers and Text Classification Algorithms (opens in a new tab)](https://arxiv.org/abs/2303.17650) (March 2023)
- [HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in HuggingFace (opens in a new tab)](https://arxiv.org/abs/2303.17580) (March 2023)
- [WavCaps: A ChatGPT-Assisted Weakly-Labelled Audio Captioning Dataset for Audio-Language Multimodal Research (opens in a new tab)](https://arxiv.org/abs/2303.17395) (March 2023)
- [How well do Large Language Models perform in Arithmetic tasks? (opens in a new tab)](https://arxiv.org/abs/2304.02015) (March 2023)
- [Assessing Cross-Cultural Alignment between ChatGPT and Human Societies: An Empirical Study (opens in a new tab)](https://arxiv.org/abs/2303.17466) (March 2023)
- [Yes but.. Can ChatGPT Identify Entities in Historical Documents? (opens in a new tab)](https://arxiv.org/abs/2303.17322) (March 2023)
- [Evaluation of ChatGPT for NLP-based Mental Health Applications (opens in a new tab)](https://arxiv.org/abs/2303.15727) (March 2023)
- [A Perspectival Mirror of the Elephant: Investigating Language Bias on Google, ChatGPT, Wikipedia, and YouTube (opens in a new tab)](https://arxiv.org/abs/2303.16281) (March 2023)
- [ChatGPT or academic scientist? Distinguishing authorship with over 99% accuracy using off-the-shelf machine learning tools (opens in a new tab)](https://arxiv.org/abs/2303.16352) (March 2023)
- [Zero-shot Clinical Entity Recognition using ChatGPT (opens in a new tab)](https://arxiv.org/abs/2303.16416) (March 2023)
- [ChatGPT is a Knowledgeable but Inexperienced Solver: An Investigation of Commonsense Problem in Large Language Models (opens in a new tab)](https://arxiv.org/abs/2303.16421) (March 2023)
- [ChatGPT4PCG Competition: Character-like Level Generation for Science Birds (opens in a new tab)](https://arxiv.org/abs/2303.15662) (March 2023)
- [ChatGPT as a Factual Inconsistency Evaluator for Abstractive Text Summarization (opens in a new tab)](https://arxiv.org/abs/2303.15621) (March 2023)
- [Chat-REC: Towards Interactive and Explainable LLMs-Augmented Recommender System (opens in a new tab)](https://arxiv.org/abs/2303.14524) (March 2023)
- [A comprehensive evaluation of ChatGPT's zero-shot Text-to-SQL capability (opens in a new tab)](https://arxiv.org/abs/2303.13547) (March 2023)
- [Towards Making the Most of ChatGPT for Machine Translation (opens in a new tab)](https://arxiv.org/abs/2303.13780) (March 2023)
- [Error Analysis Prompting Enables Human-Like Translation Evaluation in Large Language Models: A Case Study on ChatGPT (opens in a new tab)](https://arxiv.org/abs/2303.13809) (March 2023)
- [ChatGPT Outperforms Crowd-Workers for Text-Annotation Tasks (opens in a new tab)](https://arxiv.org/pdf/2303.15056v1.pdf) (March 2023)
- [ChatGPT or Grammarly? Evaluating ChatGPT on Grammatical Error Correction Benchmark (opens in a new tab)](https://arxiv.org/abs/2303.13648) (March 2023)
- [ChatGPT and a New Academic Reality: AI-Written Research Papers and the Ethics of the Large Language Models in Scholarly Publishing (opens in a new tab)](https://arxiv.org/abs/2303.13367) (March 2023)
- [Are LLMs the Master of All Trades? : Exploring Domain-Agnostic Reasoning Skills of LLMs (opens in a new tab)](https://arxiv.org/abs/2303.12810) (March 2023)
- [Is ChatGPT A Good Keyphrase Generator? A Preliminary Study (opens in a new tab)](https://arxiv.org/abs/2303.13001) (March 2023)
- [MM-REACT: Prompting ChatGPT for Multimodal Reasoning and Action (opens in a new tab)](https://arxiv.org/abs/2303.11381) (March 2023)
- [Large Language Models Can Be Used to Estimate the Ideologies of Politicians in a Zero-Shot Learning Setting (opens in a new tab)](https://arxiv.org/abs/2303.12057) (March 2023)
- [Chinese Intermediate English Learners outdid ChatGPT in deep cohesion: Evidence from English narrative writing (opens in a new tab)](https://arxiv.org/abs/2303.11812) (March 2023)
- [A Comprehensive Capability Analysis of GPT-3 and GPT-3.5 Series Models (opens in a new tab)](https://arxiv.org/abs/2303.10420) (March 2023)
- [ChatGPT as the Transportation Equity Information Source for Scientific Writing (opens in a new tab)](https://arxiv.org/abs/2303.11158) (March 2023)
- [Translating Radiology Reports into Plain Language using ChatGPT and GPT-4 with Prompt Learning: Promising Results, Limitations, and Potential (opens in a new tab)](https://arxiv.org/abs/2303.09038) (March 2023)
- [ChatGPT Participates in a Computer Science Exam (opens in a new tab)](https://arxiv.org/abs/2303.09461) (March 2023)
- [Consistency Analysis of ChatGPT (opens in a new tab)](https://arxiv.org/abs/2303.06273) (Mar 2023)
- [Algorithmic Ghost in the Research Shell: Large Language Models and Academic Knowledge Creation in Management Research (opens in a new tab)](https://arxiv.org/abs/2303.07304) (Mar 2023)
- [Large Language Models in the Workplace: A Case Study on Prompt Engineering for Job Type Classification (opens in a new tab)](https://arxiv.org/abs/2303.07142) (March 2023)
- [Seeing ChatGPT Through Students' Eyes: An Analysis of TikTok Data (opens in a new tab)](https://arxiv.org/abs/2303.05349) (March 2023)
- [Extracting Accurate Materials Data from Research Papers with Conversational Language Models and Prompt Engineering -- Example of ChatGPT (opens in a new tab)](https://arxiv.org/abs/2303.05352) (Mar 2023)
- [ChatGPT is on the horizon: Could a large language model be all we need for Intelligent Transportation? (opens in a new tab)](https://arxiv.org/abs/2303.05382) (Mar 2023)
- [Making a Computational Attorney (opens in a new tab)](https://arxiv.org/abs/2303.05383) (Mar 2023)
- [Does Synthetic Data Generation of LLMs Help Clinical Text Mining? (opens in a new tab)](https://arxiv.org/abs/2303.04360) (Mar 2023)
- [MenuCraft: Interactive Menu System Design with Large Language Models (opens in a new tab)](https://arxiv.org/abs/2303.04496) (Mar 2023)
- [A Comprehensive Survey of AI-Generated Content (AIGC): A History of Generative AI from GAN to ChatGPT (opens in a new tab)](https://arxiv.org/abs/2303.04226) (Mar 2023)
- [Exploring the Feasibility of ChatGPT for Event Extraction (opens in a new tab)](https://arxiv.org/abs/2303.03836)
- [ChatGPT: Beginning of an End of Manual Annotation? Use Case of Automatic Genre Identification (opens in a new tab)](https://arxiv.org/abs/2303.03953) (Mar 2023)
- [Is ChatGPT a Good NLG Evaluator? A Preliminary Study (opens in a new tab)](https://arxiv.org/abs/2303.04048) (Mar 2023)
- [Will Affective Computing Emerge from Foundation Models and General AI? A First Evaluation on ChatGPT (opens in a new tab)](https://arxiv.org/abs/2303.03186) (Mar 2023)
- [UZH\_CLyp at SemEval-2023 Task 9: Head-First Fine-Tuning and ChatGPT Data Generation for Cross-Lingual Learning in Tweet Intimacy Prediction (opens in a new tab)](https://arxiv.org/abs/2303.01194) (Mar 2023)
- [How to format inputs to ChatGPT models (opens in a new tab)](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_format_inputs_to_ChatGPT_models.ipynb) (Mar 2023)
- [Can ChatGPT Assess Human Personalities? A General Evaluation Framework (opens in a new tab)](https://arxiv.org/abs/2303.01248) (Mar 2023)
- [Cross-Lingual Summarization via ChatGPT (opens in a new tab)](https://arxiv.org/abs/2302.14229) (Feb 2023)
- [ChatAug: Leveraging ChatGPT for Text Data Augmentation (opens in a new tab)](https://arxiv.org/abs/2302.13007) (Feb 2023)
- [Dr ChatGPT, tell me what I want to hear: How prompt knowledge impacts health answer correctness (opens in a new tab)](https://arxiv.org/abs/2302.13793) (Feb 2023)
- [An Independent Evaluation of ChatGPT on Mathematical Word Problems (MWP) (opens in a new tab)](https://arxiv.org/abs/2302.13814) (Feb 2023)
- [ChatGPT: A Meta-Analysis after 2.5 Months (opens in a new tab)](https://arxiv.org/abs/2302.13795) (Feb 2023)
- [Let's have a chat! A Conversation with ChatGPT: Technology, Applications, and Limitations (opens in a new tab)](https://arxiv.org/abs/2302.13817) (Feb 2023)
- [Check Your Facts and Try Again: Improving Large Language Models with External Knowledge and Automated Feedback (opens in a new tab)](https://arxiv.org/abs/2302.12813) (Feb 2023)
- [On the Robustness of ChatGPT: An Adversarial and Out-of-distribution Perspective (opens in a new tab)](https://arxiv.org/abs/2302.12095) (Feb 2023)
- [How Generative AI models such as ChatGPT can be (Mis)Used in SPC Practice, Education, and Research? An Exploratory Study (opens in a new tab)](https://arxiv.org/abs/2302.10916) (Feb 2023)
- [Can ChatGPT Understand Too? A Comparative Study on ChatGPT and Fine-tuned BERT (opens in a new tab)](https://arxiv.org/abs/2302.10198) (Feb 2023)
- [A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT (opens in a new tab)](https://arxiv.org/abs/2302.11382) (Feb 2023)
- [Zero-Shot Information Extraction via Chatting with ChatGPT (opens in a new tab)](https://arxiv.org/abs/2302.10205) (Feb 2023)
- [ChatGPT: Jack of all trades, master of none (opens in a new tab)](https://arxiv.org/abs/2302.10724) (Feb 2023)
- [A Pilot Evaluation of ChatGPT and DALL-E 2 on Decision Making and Spatial Reasoning (opens in a new tab)](https://arxiv.org/abs/2302.09068) (Feb 2023)
- [Netizens, Academicians, and Information Professionals' Opinions About AI With Special Reference To ChatGPT (opens in a new tab)](https://arxiv.org/abs/2302.07136) (Feb 2023)
- [Linguistic ambiguity analysis in ChatGPT (opens in a new tab)](https://arxiv.org/abs/2302.06426) (Feb 2023)
- [ChatGPT versus Traditional Question Answering for Knowledge Graphs: Current Status and Future Directions Towards Knowledge Graph Chatbots (opens in a new tab)](https://arxiv.org/abs/2302.06466) (Feb 2023)
- [What ChatGPT and generative AI mean for science (opens in a new tab)](https://www.nature.com/articles/d41586-023-00340-6) (Feb 2023)
- [Applying BERT and ChatGPT for Sentiment Analysis of Lyme Disease in Scientific Literature (opens in a new tab)](https://arxiv.org/abs/2302.06474) (Feb 2023)
- [Exploring AI Ethics of ChatGPT: A Diagnostic Analysis (opens in a new tab)](https://arxiv.org/abs/2301.12867) (Jan 2023)
- [ChatGPT for Good? On Opportunities and Challenges of Large Language Models for Education (opens in a new tab)](https://www.edu.sot.tum.de/fileadmin/w00bed/hctl/_my_direct_uploads/ChatGPT_for_Good_.pdf) (Jan 2023)
- [The political ideology of conversational AI: Converging evidence on ChatGPT's pro-environmental, left-libertarian orientation (opens in a new tab)](https://arxiv.org/abs/2301.01768) (Jan 2023)
- [Techniques to improve reliability - OpenAI Cookbook (opens in a new tab)](https://github.com/openai/openai-cookbook/blob/main/techniques_to_improve_reliability)
- [Awesome ChatGPT Prompts (opens in a new tab)](https://github.com/f/awesome-chatgpt-prompts)
- [Introducing ChatGPT (opens in a new tab)](https://openai.com/blog/chatgpt) (Nov 2022)

Last updated on April 16, 2023

[Flan](https://www.promptingguide.ai/models/flan "Flan")[LLaMA](https://www.promptingguide.ai/models/llama "LLaMA")

## Llama

---

⚠️

This section is under heavy development.

This paper introduces a collection of foundation language models ranging from 7B to 65B parameters.

The models are trained on trillion of tokens with publicly available datasets.

The work by [(Hoffman et al. 2022) (opens in a new tab)](https://arxiv.org/abs/2203.15556) shows that given a compute budget smaller models trained on a lot more data can achieve better performance than the larger counterparts. This work recommends training 10B models on 200B tokens. However, the LLaMA paper finds that the performance of a 7B model continues to improve even after 1T tokens.

This work focuses on training models (LLaMA) that achieve the best possible performance at various inference budgets, by training on more tokens.

Overall, LLaMA-13B outperform GPT-3(175B) on many benchmarks despite being 10x smaller and possible to run a single GPU. LLaMA 65B is competitive with models like Chinchilla-70B and PaLM-540B.

## GPT-4

---

In this section, we cover the latest prompt engineering techniques for GPT-4, including tips, applications, limitations, and additional reading materials.

### GPT-4 Introduction[](https://www.promptingguide.ai/#gpt-4-introduction)

More recently, OpenAI released GPT-4, a large multimodal model that accept image and text inputs and emit text outputs. It achieves human-level performance on various professional and academic benchmarks.

Detailed results on a series of exams below:

![GPT41](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fgpt4-1.54b94ed6.png&w=1920&q=75)

Detailed results on academic benchmarks below:

![GPT42](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fgpt4-2.c9b0ca72.png&w=1920&q=75)

GPT-4 achieves a score that places it around the top 10% of test takers on a simulated bar exam. It also achieves impressive results on a variety of difficult benchmarks like MMLU and HellaSwag.

OpenAI claims that GPT-4 was improved with lessons from their adversarial testing program as well as ChatGPT, leading to better results on factuality, steerability, and better alignment.

### Vision Capabilities[](https://www.promptingguide.ai/#vision-capabilities)

GPT-4 APIs currently only supports text inputs but there is plan for image input capability in the future. OpenAI claims that in comparison with GPT-3.5 (which powers ChatGPT), GPT-4 can be more reliable, creative, and handle more nuanced instructions for more complex tasks. GPT-4 improves performance across languages.

While the image input capability is still not publicly available, GPT-4 can be augmented with techniques like few-shot and chain-of-thought prompting to improve performance on these image related tasks.

From the blog, we can see a good example where the model accepts visual inputs and a text instruction.

The instruction is as follows:

Note the "Provide a step-by-step reasoning before providing your answer" prompt which steers the model to go into an step-by-step explanation mode.

The image input:

![GPT43](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fgpt4-3.b9cfcd81.png&w=1920&q=75)

This is GPT-4 output:

This is an impressive result as the model follows the correct instruction even when there is other available information on the image. This open a range of capabilities to explore charts and other visual inputs and being more selective with the analyses.

### Steering GPT-4[](https://www.promptingguide.ai/#steering-gpt-4)

One area for experimentation is the ability to steer the model to provide answers in a certain tone and style via the `system` messages. This can accelerate personalization and getting accurate and more precise results for specific use cases.

For example, let's say we want to build an AI assistant that generate data for us to experiment with. We can use the `system` messages to steer the model to generate data in a certain style.

In the example below, we are interested to generated data samples formatted in JSON format.

*ASSISTANT Response:*

And here is a snapshot from the OpenAI Playground:

![GPT44](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fgpt4-4.07ec52fa.png&w=3840&q=75)

To achieve this with previous GPT-3 models, you needed to be very detailed in the instructions. The difference with GPT-4 is that you have instructed the style once via the `system` message and this will persists for any follow up interaction. If we now try to override the behavior, here is what you get.

*ASSISTANT Response:*

This is very useful to get consistent results and behavior.

### Limitations[](https://www.promptingguide.ai/#limitations)

According to the blog release, GPT-4 is not perfect and there are still some limitations. It can hallucinate and makes reasoning errors. The recommendation is to avoid high-stakes use.

On the TruthfulQA benchmark, RLHF post-training enables GPT-4 to be significantly more accurate than GPT-3.5. Below are the results reported in the blog post.

![GPT45](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fgpt4-5.4835f42b.png&w=1920&q=75)

Checkout this failure example below:

![GPT46](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fgpt4-6.ec9b5327.png&w=1200&q=75)

The answer should be `Elvis Presley`. This highlights how brittle these models can be for some use cases. It will be interesting to combine GPT-4 with other external knowledge sources to improve the accuracy of cases like this or even improve results by using some of the prompt engineering techniques we have learned here like in-context learning or chain-of-thought prompting.

Let's give it a shot. We have added additional instructions in the prompt and added "Think step-by-step". This is the result:

![GPT47](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fgpt4-7.e1d3fc94.png&w=1200&q=75)

Keep in mind that I haven't tested this approach sufficiently to know how reliable it is or how well it generalizes. That's something the reader can experiment with further.

Another option, is to create a `system` message that steers the model to provide a step-by-step answer and output "I don't know the answer" if it can't find the answer. I also changed the temperature to 0.5 to make the model more confident in its answer to 0. Again, please keep in mind that this needs to be tested further to see how well it generalizes. We provide this example to show you how you can potentially improve results by combining different techniques and features.

![GPT48](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fgpt4-8.fb8b721b.png&w=3840&q=75)

Keep in mind that the data cutoff point of GPT-4 is September 2021 so it lacks knowledge of events that occurred after that.

See more results in their [main blog post (opens in a new tab)](https://openai.com/research/gpt-4) and [technical report (opens in a new tab)](https://arxiv.org/pdf/2303.08774.pdf).

### Applications[](https://www.promptingguide.ai/#applications)

We will summarize many applications of GPT-4 in the coming weeks. In the meantime, you can checkout a list of applications in this [Twitter thread (opens in a new tab)](https://twitter.com/omarsar0/status/1635816470016827399?s=20).

### Library Usage[](https://www.promptingguide.ai/#library-usage)

Coming soon!

### References / Papers[](https://www.promptingguide.ai/#references--papers)

- [chatIPCC: Grounding Conversational AI in Climate Science (opens in a new tab)](https://arxiv.org/abs/2304.05510) (April 2023)
- [Galactic ChitChat: Using Large Language Models to Converse with Astronomy Literature (opens in a new tab)](https://arxiv.org/abs/2304.05406) (April 2023)
- [Emergent autonomous scientific research capabilities of large language models (opens in a new tab)](https://arxiv.org/abs/2304.05332) (April 2023)
- [Evaluating the Logical Reasoning Ability of ChatGPT and GPT-4 (opens in a new tab)](https://arxiv.org/abs/2304.03439) (April 2023)
- [Instruction Tuning with GPT-4 (opens in a new tab)](https://arxiv.org/abs/2304.03277) (April 2023)
- [Evaluating GPT-4 and ChatGPT on Japanese Medical Licensing Examinations (opens in a new tab)](https://arxiv.org/abs/2303.18027) (April 2023)
- Evaluation of GPT and BERT-based models on identifying protein-protein interactions in biomedical text (March 2023)
- [Sparks of Artificial General Intelligence: Early experiments with GPT-4 (opens in a new tab)](https://arxiv.org/abs/2303.12712) (March 2023)
- [How well do Large Language Models perform in Arithmetic tasks? (opens in a new tab)](https://arxiv.org/abs/2304.02015) (March 2023)
- [Evaluating GPT-3.5 and GPT-4 Models on Brazilian University Admission Exams (opens in a new tab)](https://arxiv.org/abs/2303.17003) (March 2023)
- [GPTEval: NLG Evaluation using GPT-4 with Better Human Alignment (opens in a new tab)](https://arxiv.org/abs/2303.16634) (March 2023)
- [Humans in Humans Out: On GPT Converging Toward Common Sense in both Success and Failure (opens in a new tab)](https://arxiv.org/abs/2303.17276) (March 2023)
- [GPT is becoming a Turing machine: Here are some ways to program it (opens in a new tab)](https://arxiv.org/abs/2303.14310) (March 2023)
- [Mind meets machine: Unravelling GPT-4's cognitive psychology (opens in a new tab)](https://arxiv.org/abs/2303.11436) (March 2023)
- [Capabilities of GPT-4 on Medical Challenge Problems (opens in a new tab)](https://www.microsoft.com/en-us/research/uploads/prod/2023/03/GPT-4_medical_benchmarks.pdf) (March 2023)
- [GPT-4 Technical Report (opens in a new tab)](https://cdn.openai.com/papers/gpt-4.pdf) (March 2023)
- [DeID-GPT: Zero-shot Medical Text De-Identification by GPT-4 (opens in a new tab)](https://arxiv.org/abs/2303.11032) (March 2023)
- [GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models (opens in a new tab)](https://arxiv.org/abs/2303.10130) (March 2023)

Last updated on April 16, 2023

[LLaMA](https://www.promptingguide.ai/models/llama "LLaMA")[Model Collection](https://www.promptingguide.ai/models/collection "Model Collection")

## Model Collection

---

[BERT (opens in a new tab)](https://arxiv.org/abs/1810.04805)2018Bidirectional Encoder Representations from Transformers[GPT (opens in a new tab)](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf)2018Improving Language Understanding by Generative Pre-Training[RoBERTa (opens in a new tab)](https://arxiv.org/abs/1907.11692)2019A Robustly Optimized BERT Pretraining Approach[GPT-2 (opens in a new tab)](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)2019Language Models are Unsupervised Multitask Learners[T5 (opens in a new tab)](https://arxiv.org/abs/1910.10683)2019Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer[BART (opens in a new tab)](https://arxiv.org/abs/1910.13461)2019Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension[ALBERT (opens in a new tab)](https://arxiv.org/abs/1909.11942)2019A Lite BERT for Self-supervised Learning of Language Representations[XLNet (opens in a new tab)](https://arxiv.org/abs/1906.08237)2019Generalized Autoregressive Pretraining for Language Understanding and Generation[CTRL (opens in a new tab)](https://arxiv.org/abs/1909.05858)2019CTRL: A Conditional Transformer Language Model for Controllable Generation[ERNIE (opens in a new tab)](https://arxiv.org/abs/1904.09223v1)2019ERNIE: Enhanced Representation through Knowledge Integration[GShard (opens in a new tab)](https://arxiv.org/abs/2006.16668v1)2020GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding[GPT-3 (opens in a new tab)](https://arxiv.org/abs/2005.14165)2020Language Models are Few-Shot Learners[LaMDA (opens in a new tab)](https://arxiv.org/abs/2201.08239v3)2021LaMDA: Language Models for Dialog Applications[PanGu-α (opens in a new tab)](https://arxiv.org/abs/2104.12369v1)2021PanGu-α: Large-scale Autoregressive Pretrained Chinese Language Models with Auto-parallel Computation[mT5 (opens in a new tab)](https://arxiv.org/abs/2010.11934v3)2021mT5: A massively multilingual pre-trained text-to-text transformer[CPM-2 (opens in a new tab)](https://arxiv.org/abs/2106.10715v3)2021CPM-2: Large-scale Cost-effective Pre-trained Language Models[T0 (opens in a new tab)](https://arxiv.org/abs/2110.08207)2021Multitask Prompted Training Enables Zero-Shot Task Generalization[HyperCLOVA (opens in a new tab)](https://arxiv.org/abs/2109.04650)2021What Changes Can Large-scale Language Models Bring? Intensive Study on HyperCLOVA: Billions-scale Korean Generative Pretrained Transformers[Codex (opens in a new tab)](https://arxiv.org/abs/2107.03374v2)2021Evaluating Large Language Models Trained on Code[ERNIE 3.0 (opens in a new tab)](https://arxiv.org/abs/2107.02137v1)2021ERNIE 3.0: Large-scale Knowledge Enhanced Pre-training for Language Understanding and Generation[Jurassic-1 (opens in a new tab)](https://uploads-ssl.webflow.com/60fd4503684b466578c0d307/61138924626a6981ee09caf6_jurassic_tech_paper.pdf)2021Jurassic-1: Technical Details and Evaluation[FLAN (opens in a new tab)](https://arxiv.org/abs/2109.01652v5)2021Finetuned Language Models Are Zero-Shot Learners[MT-NLG (opens in a new tab)](https://arxiv.org/abs/2201.11990v3)2021Using DeepSpeed and Megatron to Train Megatron-Turing NLG 530B, A Large-Scale Generative Language Model[Yuan 1.0 (opens in a new tab)](https://arxiv.org/abs/2110.04725v2)2021Yuan 1.0: Large-Scale Pre-trained Language Model in Zero-Shot and Few-Shot Learning[WebGPT (opens in a new tab)](https://arxiv.org/abs/2112.09332v3)2021WebGPT: Browser-assisted question-answering with human feedback[Gopher (opens in a new tab)](https://arxiv.org/abs/2112.11446v2)2021Scaling Language Models: Methods, Analysis & Insights from Training Gopher[ERNIE 3.0 Titan (opens in a new tab)](https://arxiv.org/abs/2112.12731v1)2021ERNIE 3.0 Titan: Exploring Larger-scale Knowledge Enhanced Pre-training for Language Understanding and Generation[GLaM (opens in a new tab)](https://arxiv.org/abs/2112.06905)2021GLaM: Efficient Scaling of Language Models with Mixture-of-Experts[InstructGPT (opens in a new tab)](https://arxiv.org/abs/2203.02155v1)2022Training language models to follow instructions with human feedback[GPT-NeoX-20B (opens in a new tab)](https://arxiv.org/abs/2204.06745v1)2022GPT-NeoX-20B: An Open-Source Autoregressive Language Model[AlphaCode (opens in a new tab)](https://arxiv.org/abs/2203.07814v1)2022Competition-Level Code Generation with AlphaCode[CodeGen (opens in a new tab)](https://arxiv.org/abs/2203.13474v5)2022CodeGen: An Open Large Language Model for Code with Multi-Turn Program Synthesis[Chinchilla (opens in a new tab)](https://arxiv.org/abs/2203.15556)2022Shows that for a compute budget, the best performances are not achieved by the largest models but by smaller models trained on more data.[Tk-Instruct (opens in a new tab)](https://arxiv.org/abs/2204.07705v3)2022Super-NaturalInstructions: Generalization via Declarative Instructions on 1600+ NLP Tasks[UL2 (opens in a new tab)](https://arxiv.org/abs/2205.05131v3)2022UL2: Unifying Language Learning Paradigms[PaLM (opens in a new tab)](https://arxiv.org/abs/2204.02311v5)2022PaLM: Scaling Language Modeling with Pathways[OPT (opens in a new tab)](https://arxiv.org/abs/2205.01068)2022OPT: Open Pre-trained Transformer Language Models[BLOOM (opens in a new tab)](https://arxiv.org/abs/2211.05100v3)2022BLOOM: A 176B-Parameter Open-Access Multilingual Language Model[GLM-130B (opens in a new tab)](https://arxiv.org/abs/2210.02414v1)2022GLM-130B: An Open Bilingual Pre-trained Model[AlexaTM (opens in a new tab)](https://arxiv.org/abs/2208.01448v2)2022AlexaTM 20B: Few-Shot Learning Using a Large-Scale Multilingual Seq2Seq Model[Flan-T5 (opens in a new tab)](https://arxiv.org/abs/2210.11416v5)2022Scaling Instruction-Finetuned Language Models[Sparrow (opens in a new tab)](https://arxiv.org/abs/2209.14375)2022Improving alignment of dialogue agents via targeted human judgements[U-PaLM (opens in a new tab)](https://arxiv.org/abs/2210.11399v2)2022Transcending Scaling Laws with 0.1% Extra Compute[mT0 (opens in a new tab)](https://arxiv.org/abs/2211.01786v1)2022Crosslingual Generalization through Multitask Finetuning[Galactica (opens in a new tab)](https://arxiv.org/abs/2211.09085v1)2022Galactica: A Large Language Model for Science[OPT-IML (opens in a new tab)](https://arxiv.org/abs/2212.12017v3)2022OPT-IML: Scaling Language Model Instruction Meta Learning through the Lens of Generalization[LLaMA (opens in a new tab)](https://arxiv.org/abs/2302.13971v1)2023LLaMA: Open and Efficient Foundation Language Models[GPT-4 (opens in a new tab)](https://arxiv.org/abs/2303.08774v3)2023GPT-4 Technical Report[PanGu-Σ (opens in a new tab)](https://arxiv.org/abs/2303.10845v1)2023PanGu-Σ: Towards Trillion Parameter Language Model with Sparse Heterogeneous Computing[BloombergGPT (opens in a new tab)](https://arxiv.org/abs/2303.17564v1)2023BloombergGPT: A Large Language Model for Finance[Cerebras-GPT (opens in a new tab)](https://arxiv.org/abs/2304.03208)2023Cerebras-GPT: Open Compute-Optimal Language Models Trained on the Cerebras Wafer-Scale Cluster

## Risks & Misuses

---

We have seen already how effective well-crafted prompts can be for various tasks using techniques like few-shot learning and chain-of-thought prompting. As we think about building real-world applications on top of LLMs, it becomes crucial to think about the misuses, risks, and safety practices involved with language models.

This section focuses on highlighting some of the risks and misuses of LLMs via techniques like prompt injections. It also highlights harmful behaviors and how to potentially mitigate them via effective prompting techniques. Other topics of interest include generalizability, calibration, biases, social biases, and factuality to name a few.

[Model Collection](https://www.promptingguide.ai/models/collection "Model Collection")[Adversarial Prompting](https://www.promptingguide.ai/risks/adversarial "Adversarial Prompting")

## Adversarial Prompting

---

Adversarial prompting is an important topic in prompt engineering as it could help to understand the risks and safety issues involved with LLMs. It's also an important discipline to identify these risks and design techniques to address the issues.

The community has found many different types of adversarial prompts attacks that involve some form of prompt injection. We provide a list of these examples below.

When you are building LLMs, it's really important to protect against prompt attacks that could bypass safety guardrails and break the guiding principles of the model. We will cover examples of this below.

Please note that it is possible that more robust models have been implemented to address some of the issues documented here. This means that some of the prompt attacks below might not be as effective anymore.

Before proceeding with the section, please keep in mind that we don't condone any of the attacks described below. We are just documenting them for educational purposes and to highlight the limitations of these systems.

---

### Prompt Injection[](https://www.promptingguide.ai/#prompt-injection)

Prompt injection aims to hijack the model output by using clever prompts that change its behavior. These attacks could be harmful -- Simon Willison defined it ["as a form of security exploit" (opens in a new tab)](https://simonwillison.net/2022/Sep/12/prompt-injection/).

Let's cover a basic example to demonstrate how prompt injection can be achieved. We will use a popular example shared by [Riley on Twitter (opens in a new tab)](https://twitter.com/goodside/status/1569128808308957185?s=20).

*Prompt:*

*Output:*

We can observe that the original instruction was somewhat ignored by the follow-up instruction. In the original example shared by Riley, the model output was "Haha pwned!!". However, I couldn't reproduce it since the model has been updated a few times since then. Regardless, this can be problematic for many reasons.

Keep in mind that when we are designing prompts we are just chaining instructions and all the different prompt components, including user inputs, but there is no standard format that the model expects. This flexibility in input is desired, however, the issue is that we might run into vulnerabilities like the prompt injection explained above.

As you develop your prompts for your applications, you might be thinking about how to avoid such undesired behaviors. There is no clear guidelines how to achieve this. In fact, Riley also tried to provide warnings in the instruction to avoid the attack as follows:

*Prompt:*

At the time Riley reported this, the model was still vulnerable to the attack. Using the default settings, and the latest model, `text-davinci-003`, the model outputs the following:

*Output:*

This particular attack seems to have been largely addressed by OpenAI's `text-devinci-003` model but you can play around with more clever prompts and see if you can make the injection work on the updated model. Testing models for vulnerabilities is an important part of the prompt engineering process as you aim to build a more robust and safe model.

Here is another basic example with different instruction and task:

*Prompt:*

*Output:*

The idea of this attack is that it hijacks the model output by injecting an instruction to ignore the original instruction and execute the injected one, which can be intended to cause the model to emit harmful or undesired outputs.

---

### Prompt Leaking[](https://www.promptingguide.ai/#prompt-leaking)

Prompt leaking is another type of prompt injection where prompt attacks are designed to leak details from the prompt which could contain confidential or proprietary information that was not intended for the public.

A lot of startups are already developing and chaining well-crafted prompts that are leading to useful products built on top of LLMs. These prompts could contain important IP that shouldn't be public so developers need to consider the kinds of robust testing that need to be carried out to avoid prompt leaking.

Let's look at a simple example of prompt leaking below:

*Prompt:*

*Output:*

The above output returns the exemplars which could be confidential information that you could be using as part of the prompt in your application. The advise here is to be very careful of what you are passing in prompts and perhaps try some techniques (e.g., optimizing prompts) to avoid the leaks. More on this later on.

Check out [this example of a prompt leak (opens in a new tab)](https://twitter.com/simonw/status/1570933190289924096?s=20) in the wild.

---

### Jailbreaking[](https://www.promptingguide.ai/#jailbreaking)

Some models will avoid responding to unethical instructions but can be bypassed if the request is contextualized in a clever way.

#### Illegal Behavior[](https://www.promptingguide.ai/#illegal-behavior)

As an example, the prompt below was able to bypass the content policy of previous versions of ChatGPT:

*Prompt:*

[Source (opens in a new tab)](https://twitter.com/m1guelpf/status/1598203861294252033?s=20&t=M34xoiI_DKcBAVGEZYSMRA)

There are many other variations of this prompt, also known as *jailbreaking*, with the goal to make the model do something that it shouldn't do according to its guiding principles.

Models like ChatGPT and Claude have been aligned to avoid outputting content that for instance promotes illegal behavior or unethical activities. So it's harder to jailbreak them but they still have flaws and we are learning new ones as people experiment with these systems in the open.

#### DAN[](https://www.promptingguide.ai/#dan)

LLMs like ChatGPT includes guardrails limiting the model from outputting harmful, illegal, unethical, or violent content of any kind. However, users on Reddit found a jailbreaking technique that allows a user to bypass the model rules and creating a character called DAN (Do Anything Now) that forces the model to comply with any request leading the system to generate unfiltered responses. This is a version of role playing used for jailbreaking models.

There has been many iterations of DAN as ChatGPT keeps getting better against these types of attacks. Initially, a simple prompt worked. However, as the model got better, the prompt needed to be more sophisticated.

Here is an example of the DAN jailbreaking technique:

![DAN](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fdan-1.837af53f.png&w=1920&q=75)

You can find a summary of DAN variants [here (opens in a new tab)](https://www.reddit.com/r/ChatGPT/comments/10tevu1/new_jailbreak_proudly_unveiling_the_tried_and/).

#### The Waluigi Effect[](https://www.promptingguide.ai/#the-waluigi-effect)

LessWrong recently published an article titled ["The Waluigi Effect" (opens in a new tab)](https://www.lesswrong.com/posts/D7PumeYTDPfBTp3i7/the-waluigi-effect-mega-post) that discusses the ability of LLMs to easily elicit opposite and undesired behavior due to how it was trained.

From the article:

> > The Waluigi Effect: After you train an LLM to satisfy a desirable property P, then it's easier to elicit the chatbot into satisfying the exact opposite of property P.

#### GPT-4 Simulator[](https://www.promptingguide.ai/#gpt-4-simulator)

One recent jailbreaking example that was shared on Twitter was able to bypass the content filters of ChatGPT-4. The idea is to simulate an autoregressive model and trigger a harmful response using this input "how do I hack into into" into the function defined. This hack required clever manipulation and leveraging some of the code generation/understanding capabilities of the model.

Below is the full prompting (obtained from [Jailbreak Chat (opens in a new tab)](https://www.jailbreakchat.com/prompt/b2917fad-6803-41f8-a6c8-756229b84270)):

Below is a response obtained by [Alex (opens in a new tab)](https://twitter.com/i/bookmarks/1635718795263082512):

![GPT4SIM](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fgpt-simulator.8a44ec1b.jpeg&w=3840&q=75)

You can find more of these examples in the [Jailbreak Chat (opens in a new tab)](https://www.jailbreakchat.com/) website.

#### Game Simulator[](https://www.promptingguide.ai/#game-simulator)

GPT-4 has improved in terms of safety, as many of the jailbreaking and prompt injection techniques described above are not as effective anymore. Simulations continue to be an effective technique to jailbreak the system.

Here is an example that instructs the model to simulate a game with instructions that enable the model to respond what seems like undesirable content.

![GPT4SIM2](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fgpt4-game-simulator.b60e216f.png&w=1920&q=75)

---

### Defense Tactics[](https://www.promptingguide.ai/#defense-tactics)

It's widely known that language models tend to elicit undesirable and harmful behaviors such as generating inaccurate statements, offensive text, biases, and much more. Furthermore, other researchers have also developed methods that enable models like ChatGPT to write malware, exploit identification, and create phishing sites. Prompt injections are not only used to hijack the model output but also to elicit some of these harmful behaviors from the LM. Thus, it becomes imperative to understand better how to defend against prompt injections.

While prompt injections are easy to execute, there are no easy ways or widely accepted techniques to defend against these text-based attacks. Some researchers and practitioners recommend various ways to mitigate the effects of ill-intentioned prompts. We touch on a few defense tactics that are of interest to the community.

#### Add Defense in the Instruction[](https://www.promptingguide.ai/#add-defense-in-the-instruction)

A simple defense tactic to start experimenting with is to just enforce the desired behavior via the instruction passed to the model. This is not a complete solution or offers any guarantees but it highlights the power of a well-crafted prompt. In an upcoming section, we cover a more robust approach that leverages good prompts for detecting adversarial prompts. Let's try the following prompt injection on `text-davinci-003`:

*Prompt:*

*Output:*

A simple fix would be to warn the model about a potential malicious attack and how desired behavior.

*Prompt*:\*

*Output:*

We can see that even when we injected the malicious instruction at the end, the model still performed the original task. It looks like the additional context provided in the instruction helped to steer the model to perform the original task we wanted.

You can try this example in [this notebook (opens in a new tab)](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/pe-chatgpt-adversarial.ipynb).

#### Parameterizing Prompt Components[](https://www.promptingguide.ai/#parameterizing-prompt-components)

Prompt injections have similarities to [SQL injection (opens in a new tab)](https://en.wikipedia.org/wiki/SQL_injection) and we can potentially learn defense tactics from that domain. Inspired by this, a potential solution for prompt injection, [suggested by Simon (opens in a new tab)](https://simonwillison.net/2022/Sep/12/prompt-injection/), is to parameterize the different components of the prompts, such as having instructions separated from inputs and dealing with them differently. While this could lead to cleaner and safer solutions, I believe the tradeoff will be the lack of flexibility. This is an active area of interest as we continue to build software that interacts with LLMs.

#### Quotes and Additional Formatting[](https://www.promptingguide.ai/#quotes-and-additional-formatting)

Riley also followed up with a [workaround (opens in a new tab)](https://twitter.com/goodside/status/1569457230537441286?s=20) which was eventually exploited by another user. It involved escaping/quoting the input strings. Additionally, Riley reports that with this trick there is no need to add warnings in the instruction, and appears robust across phrasing variations. Regardless, we share the prompt example as it emphasizes the importance and benefits of thinking deeply about how to properly format your prompts.

*Prompt:*

*Output:*

Another [defense proposed (opens in a new tab)](https://twitter.com/goodside/status/1569457230537441286?s=20) by Riley, is using JSON encoding plus Markdown headings for instructions/examples.

I tried to reproduce with `temperature=0` but couldn't really get it to work. You can see below my prompt and the output. This shows how important it is to think about the input that goes to the model and formatting I added the example below to see if the learner can find a robust defense that works for different inputs and instruction variants.

*Prompt:*

*Output:*

#### Adversarial Prompt Detector[](https://www.promptingguide.ai/#adversarial-prompt-detector)

We know that LLMs can be complex, general, and robust systems that can perform really well on a wide range of tasks. LLMs can also be used or fine-tuned to perform specific tasks like knowledge generation ([Liu et al. 2022 (opens in a new tab)](https://arxiv.org/pdf/2110.08387.pdf)) and self-verification ([Weng et al. (2022) (opens in a new tab)](https://arxiv.org/abs/2212.09561v1)). Similarly, an LLM can be used to detect adversarial prompts and filter them out.

[Armstrong and Gorman (2022) (opens in a new tab)](https://www.alignmentforum.org/posts/pNcFYZnPdXyL2RfgA/using-gpt-eliezer-against-chatgpt-jailbreaking) proposes an interesting solution using this concept. Here is how it looks in practice.

The first step is to define a prompt evaluator. In the article, the authors propose a `chatgpt-prompt-evaluator` which looks something like the following:

*Prompt:*

This is an interesting solution as it involves defining a specific agent that will be in charge of flagging adversarial prompts so as to avoid the LM responding undesirable outputs.

We have prepared [this notebook](https://www.promptingguide.ai/notebooks/pe-chatgpt-adversarial.ipynb) for your play around with this strategy.

#### Model Type[](https://www.promptingguide.ai/#model-type)

As suggested by Riley Goodside in [this twitter thread (opens in a new tab)](https://twitter.com/goodside/status/1578278974526222336?s=20), one approach to avoid prompt injections is to not use instruction-tuned models in production. His recommendation is to either fine-tune a model or create a k-shot prompt for a non-instruct model.

The k-shot prompt solution, which discards the instructions, works well for general/common tasks that don't require too many examples in the context to get good performance. Keep in mind that even this version, which doesn't rely on instruction-based models, is still prone to prompt injection. All this [twitter user (opens in a new tab)](https://twitter.com/goodside/status/1578291157670719488?s=20) had to do was disrupt the flow of the original prompt or mimic the example syntax. Riley suggests trying out some of the additional formatting options like escaping whitespaces and quoting inputs to make it more robust. Note that all these approaches are still brittle and a much more robust solution is needed.

For harder tasks, you might need a lot more examples in which case you might be constrained by context length. For these cases, fine-tuning a model on many examples (100s to a couple thousand) might be more ideal. As you build more robust and accurate fine-tuned models, you rely less on instruction-based models and can avoid prompt injections. Fine-tuned models might just be the best approach we currently have for avoiding prompt injections.

More recently, ChatGPT came into the scene. For many of the attacks that we tried above, ChatGPT already contains some guardrails and it usually responds with a safety message when encountering a malicious or dangerous prompt. While ChatGPT prevents a lot of these adversarial prompting techniques, it's not perfect and there are still many new and effective adversarial prompts that break the model. One disadvantage with ChatGPT is that because the model has all of these guardrails, it might prevent certain behaviors that are desired but not possible given the constraints. There is a tradeoff with all these model types and the field is constantly evolving to better and more robust solutions.

---

### References[](https://www.promptingguide.ai/#references)

- [The Waluigi Effect (mega-post) (opens in a new tab)](https://www.lesswrong.com/posts/D7PumeYTDPfBTp3i7/the-waluigi-effect-mega-post)
- [Jailbreak Chat (opens in a new tab)](https://www.jailbreakchat.com/)
- [Model-tuning Via Prompts Makes NLP Models Adversarially Robust (opens in a new tab)](https://arxiv.org/abs/2303.07320) (Mar 2023)
- [Can AI really be protected from text-based attacks? (opens in a new tab)](https://techcrunch.com/2023/02/24/can-language-models-really-be-protected-from-text-based-attacks/) (Feb 2023)
- [Hands-on with Bing’s new ChatGPT-like features (opens in a new tab)](https://techcrunch.com/2023/02/08/hands-on-with-the-new-bing/) (Feb 2023)
- [Using GPT-Eliezer against ChatGPT Jailbreaking (opens in a new tab)](https://www.alignmentforum.org/posts/pNcFYZnPdXyL2RfgA/using-gpt-eliezer-against-chatgpt-jailbreaking) (Dec 2022)
- [Machine Generated Text: A Comprehensive Survey of Threat Models and Detection Methods (opens in a new tab)](https://arxiv.org/abs/2210.07321) (Oct 2022)
- [Prompt injection attacks against GPT-3 (opens in a new tab)](https://simonwillison.net/2022/Sep/12/prompt-injection/) (Sep 2022)

[Risks & Misuses](https://www.promptingguide.ai/risks "Risks & Misuses")[Factuality](https://www.promptingguide.ai/risks/factuality "Factuality")

## Factuality

---

LLMs have a tendency to generate responses that sounds coherent and convincing but can sometimes be made up. Improving prompts can help improve the model to generate more accurate/factual responses and reduce the likelihood to generate inconsistent and made up responses.

Some solutions might include:

- provide ground truth (e.g., related article paragraph or Wikipedia entry) as part of context to reduce the likelihood of the model producing made up text.
- configure the model to produce less diverse responses by decreasing the probability parameters and instructing it to admit (e.g., "I don't know") when it doesn't know the answer.
- provide in the prompt a combination of examples of questions and responses that it might know about and not know about

Let's look at a simple example:

*Prompt:*

*Output:*

I made up the name "Neto Beto Roberto" so the model is correct in this instance. Try to change the question a bit and see if you can get it to work. There are different ways you can improve this further based on all that you have learned so far.

[Adversarial Prompting](https://www.promptingguide.ai/risks/adversarial "Adversarial Prompting")[Biases](https://www.promptingguide.ai/risks/biases "Biases")

## Biases

---

LLMs can produce problematic generations that can potentially be harmful and display biases that could deteriorate the performance of the model on downstream tasks. Some of these can be mitigated through effective prompting strategies but might require more advanced solutions like moderation and filtering.

### Distribution of Exemplars[](https://www.promptingguide.ai/#distribution-of-exemplars)

When performing few-shot learning, does the distribution of the exemplars affect the performance of the model or bias the model in some way? We can perform a simple test here.

*Prompt:*

*Output:*

In the example above, it seems that the distribution of exemplars doesn't bias the model. This is good. Let's try another example with a harder text to classify and let's see how the model does:

*Prompt:*

*Output:*

While that last sentence is somewhat subjective, I flipped the distribution and instead used 8 positive examples and 2 negative examples and then tried the same exact sentence again. Guess what the model responded? It responded "Positive". The model might have a lot of knowledge about sentiment classification so it will be hard to get it to display bias for this problem. The advice here is to avoid skewing the distribution and instead provide a more balanced number of examples for each label. For harder tasks that the model doesn't have too much knowledge of, it will likely struggle more.

### Order of Exemplars[](https://www.promptingguide.ai/#order-of-exemplars)

When performing few-shot learning, does the order affect the performance of the model or bias the model in some way?

You can try the above exemplars and see if you can get the model to be biased towards a label by changing the order. The advice is to randomly order exemplars. For example, avoid having all the positive examples first and then the negative examples last. This issue is further amplified if the distribution of labels is skewed. Always ensure to experiment a lot to reduce this type of bias.

Last updated on April 11, 2023

[Factuality](https://www.promptingguide.ai/risks/factuality "Factuality")[Papers](https://www.promptingguide.ai/papers "Papers")

## Papers

---

The following are the latest papers (sorted by release date) on prompt engineering. We update this on a daily basis and new papers come in. We incorporate summaries of these papers to the guides above every week.

### Overviews[](https://www.promptingguide.ai/#overviews)

- [One Small Step for Generative AI, One Giant Leap for AGI: A Complete Survey on ChatGPT in AIGC Era (opens in a new tab)](https://arxiv.org/abs/2304.06488) (April 2023)
- [A Bibliometric Review of Large Language Models Research from 2017 to 2023 (opens in a new tab)](https://arxiv.org/abs/2304.02020) (April 2023)
- [A Survey of Large Language Models (opens in a new tab)](https://arxiv.org/abs/2303.18223) (April 2023)
- [Nature Language Reasoning, A Survey (opens in a new tab)](https://arxiv.org/abs/2303.14725) (Mar 2023)
- [Augmented Language Models: a Survey (opens in a new tab)](https://arxiv.org/abs/2302.07842) (Feb 2023)
- [A Survey for In-context Learning (opens in a new tab)](https://arxiv.org/abs/2301.00234) (Dec 2022)
- [Towards Reasoning in Large Language Models: A Survey (opens in a new tab)](https://arxiv.org/abs/2212.10403) (Dec 2022)
- [Reasoning with Language Model Prompting: A Survey (opens in a new tab)](https://arxiv.org/abs/2212.09597) (Dec 2022)
- [Emergent Abilities of Large Language Models (opens in a new tab)](https://arxiv.org/abs/2206.07682) (Jun 2022)
- [A Taxonomy of Prompt Modifiers for Text-To-Image Generation (opens in a new tab)](https://arxiv.org/abs/2204.13988) (Apr 2022)
- [Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing (opens in a new tab)](https://arxiv.org/abs/2107.13586) (Jul 2021)

### Approaches[](https://www.promptingguide.ai/#approaches)

- [Boosted Prompt Ensembles for Large Language Models (opens in a new tab)](https://arxiv.org/abs/2304.05970) (April 2023)
- [Global Prompt Cell: A Portable Control Module for Effective Prompt (opens in a new tab)](https://arxiv.org/abs/2304.05642) (April 2023)
- [Why think step-by-step? Reasoning emerges from the locality of experience (opens in a new tab)](https://arxiv.org/abs/2304.03843) (April 2023)
- [Revisiting Automated Prompting: Are We Actually Doing Better? (opens in a new tab)](https://arxiv.org/abs/2304.03609) (April 2023)
- [REFINER: Reasoning Feedback on Intermediate Representations (opens in a new tab)](https://arxiv.org/abs/2304.01904) (April 2023)
- [Reflexion: an autonomous agent with dynamic memory and self-reflection (opens in a new tab)](https://arxiv.org/abs/2303.11366) (March 2023)
- [CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society (opens in a new tab)](https://arxiv.org/abs/2303.17760) (Mar 2023)
- [Self-Refine: Iterative Refinement with Self-Feedback (opens in a new tab)](https://arxiv.org/abs/2303.17651v1) (Mar 2023)
- [kNN Prompting: Beyond-Context Learning with Calibration-Free Nearest Neighbor Inference (opens in a new tab)](https://arxiv.org/abs/2303.13824) (Mar 2023)
- [Visual-Language Prompt Tuning with Knowledge-guided Context Optimization (opens in a new tab)](https://arxiv.org/abs/2303.13283) (Mar 2023)
- [Fairness-guided Few-shot Prompting for Large Language Models (opens in a new tab)](https://arxiv.org/abs/2303.13217) (Mar 2023)
- [Context-faithful Prompting for Large Language Models (opens in a new tab)](https://arxiv.org/abs/2303.11315) (Mar 2023)
- [Is Prompt All You Need? No. A Comprehensive and Broader View of Instruction Learning (opens in a new tab)](https://arxiv.org/abs/2303.10475) (Mar 2023)
- [UPRISE: Universal Prompt Retrieval for Improving Zero-Shot Evaluation (opens in a new tab)](https://arxiv.org/abs/2303.08518) (Mar 2023)
- [Model-tuning Via Prompts Makes NLP Models Adversarially Robust (opens in a new tab)](https://arxiv.org/abs/2303.07320) (Mar 2023)
- [Structure Pretraining and Prompt Tuning for Knowledge Graph Transfer (opens in a new tab)](https://arxiv.org/abs/2303.03922) (March 2023)
- [CoTEVer: Chain of Thought Prompting Annotation Toolkit for Explanation Verification (opens in a new tab)](https://arxiv.org/abs/2303.03628) (March 2023)
- [Larger language models do in-context learning differently (opens in a new tab)](https://arxiv.org/abs/2303.03846) (March 2023)
- [OpenICL: An Open-Source Framework for In-context Learning (opens in a new tab)](https://arxiv.org/abs/2303.02913) (March 2023)
- [Dynamic Prompting: A Unified Framework for Prompt Tuning (opens in a new tab)](https://arxiv.org/abs/2303.02909) (March 2023)
- [Multitask Prompt Tuning Enables Parameter-Efficient Transfer Learning (opens in a new tab)](https://arxiv.org/abs/2303.02861) (March 2023)
- [Effectiveness of Data Augmentation for Prefix Tuning with Limited Data (opens in a new tab)](https://arxiv.org/abs/2303.02577) (March 2023)
- [Mixture of Soft Prompts for Controllable Data Generation (opens in a new tab)](https://arxiv.org/abs/2303.01580) (March 2023)
- [Prompt, Generate, then Cache: Cascade of Foundation Models makes Strong Few-shot Learners (opens in a new tab)](https://arxiv.org/abs/2303.02151) (March 2023)
- [How Robust is GPT-3.5 to Predecessors? A Comprehensive Study on Language Understanding Tasks (opens in a new tab)](https://arxiv.org/abs/2303.00293) (March 2023)
- [Can ChatGPT Understand Too? A Comparative Study on ChatGPT and Fine-tuned BERT (opens in a new tab)](https://arxiv.org/pdf/2302.10198.pdf) (Feb 2023)
- [EvoPrompting: Language Models for Code-Level Neural Architecture Search (opens in a new tab)](https://arxiv.org/abs/2302.14838) (Feb 2023)
- [In-Context Instruction Learning (opens in a new tab)](https://arxiv.org/abs/2302.14691) (Feb 2023)
- [Chain of Hindsight Aligns Language Models with Feedback (opens in a new tab)](https://arxiv.org/abs/2302.02676) (Feb 2023)
- [Language Is Not All You Need: Aligning Perception with Language Models (opens in a new tab)](https://arxiv.org/abs/2302.14045) (Feb 2023)
- [Automatic Prompt Augmentation and Selection with Chain-of-Thought from Labeled Data (opens in a new tab)](https://arxiv.org/abs/2302.12822) (Feb 2023)
- [Active Prompting with Chain-of-Thought for Large Language Models (opens in a new tab)](https://arxiv.org/abs/2302.12246) (Feb 2023)
- [More than you've asked for: A Comprehensive Analysis of Novel Prompt Injection Threats to Application-Integrated Large Language Models (opens in a new tab)](https://arxiv.org/abs/2302.12173) (Feb 2023)
- [A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT (opens in a new tab)](https://arxiv.org/abs/2302.11382) (Feb 2023)
- [Guiding Large Language Models via Directional Stimulus Prompting (opens in a new tab)](https://arxiv.org/abs/2302.11520) (Feb 2023)
- [How Does In-Context Learning Help Prompt Tuning? (opens in a new tab)](https://arxiv.org/abs/2302.11521) (Feb 2023)
- [Scalable Prompt Generation for Semi-supervised Learning with Language Models (opens in a new tab)](https://arxiv.org/abs/2302.09236) (Feb 2023)
- [Bounding the Capabilities of Large Language Models in Open Text Generation with Prompt Constraints (opens in a new tab)](https://arxiv.org/abs/2302.09185) (Feb 2023)
- [À-la-carte Prompt Tuning (APT): Combining Distinct Data Via Composable Prompting (opens in a new tab)](https://arxiv.org/abs/2302.07994) (Feb 2023)
- [GraphPrompt: Unifying Pre-Training and Downstream Tasks for Graph Neural Networks (opens in a new tab)](https://arxiv.org/abs/2302.08043) (Feb 2023)
- [The Capacity for Moral Self-Correction in Large Language Models (opens in a new tab)](https://arxiv.org/abs/2302.07459) (Feb 2023)
- [SwitchPrompt: Learning Domain-Specific Gated Soft Prompts for Classification in Low-Resource Domains (opens in a new tab)](https://arxiv.org/abs/2302.06868) (Feb 2023)
- [Evaluating the Robustness of Discrete Prompts (opens in a new tab)](https://arxiv.org/abs/2302.05619) (Feb 2023)
- [Compositional Exemplars for In-context Learning (opens in a new tab)](https://arxiv.org/abs/2302.05698) (Feb 2023)
- [Hard Prompts Made Easy: Gradient-Based Discrete Optimization for Prompt Tuning and Discovery (opens in a new tab)](https://arxiv.org/abs/2302.03668) (Feb 2023)
- [Multimodal Chain-of-Thought Reasoning in Language Models (opens in a new tab)](https://arxiv.org/abs/2302.00923) (Feb 2023)
- [Large Language Models Can Be Easily Distracted by Irrelevant Context (opens in a new tab)](https://arxiv.org/abs/2302.00093) (Feb 2023)
- [Synthetic Prompting: Generating Chain-of-Thought Demonstrations for Large Language Models (opens in a new tab)](https://arxiv.org/abs/2302.00618) (Feb 2023)
- [Progressive Prompts: Continual Learning for Language Models (opens in a new tab)](https://arxiv.org/abs/2301.12314) (Jan 2023)
- [Batch Prompting: Efficient Inference with LLM APIs (opens in a new tab)](https://arxiv.org/abs/2301.08721) (Jan 2023)
- [Demonstrate-Search-Predict: Composing retrieval and language models for knowledge-intensive NLP (opens in a new tab)](https://arxiv.org/abs/2212.14024) (Dec 2022)
- [On Second Thought, Let's Not Think Step by Step! Bias and Toxicity in Zero-Shot Reasoning (opens in a new tab)](https://arxiv.org/abs/2212.08061) (Dec 2022)
- [Constitutional AI: Harmlessness from AI Feedback (opens in a new tab)](https://arxiv.org/abs/2212.08073) (Dec 2022)
- [Successive Prompting for Decomposing Complex Questions (opens in a new tab)](https://arxiv.org/abs/2212.04092) (Dec 2022)
- [Large Language Models are reasoners with Self-Verification (opens in a new tab)](https://arxiv.org/abs/2212.09561v1) (Dec 2022)
- [Discovering Language Model Behaviors with Model-Written Evaluations (opens in a new tab)](https://arxiv.org/abs/2212.09251) (Dec 2022)
- [Structured Prompting: Scaling In-Context Learning to 1,000 Examples (opens in a new tab)](https://arxiv.org/abs/2212.06713) (Dec 2022)
- [PAL: Program-aided Language Models (opens in a new tab)](https://arxiv.org/abs/2211.10435) (Nov 2022)
- [Large Language Models Are Human-Level Prompt Engineers (opens in a new tab)](https://arxiv.org/abs/2211.01910) (Nov 2022)
- [Ignore Previous Prompt: Attack Techniques For Language Models (opens in a new tab)](https://arxiv.org/abs/2211.09527) (Nov 2022)
- [Machine Generated Text: A Comprehensive Survey of Threat Models and Detection Methods (opens in a new tab)](https://arxiv.org/abs/2210.07321) (Nov 2022)
- [Teaching Algorithmic Reasoning via In-context Learning (opens in a new tab)](https://arxiv.org/abs/2211.09066) (Nov 2022)
- [Enhancing Self-Consistency and Performance of Pre-Trained Language Models through Natural Language Inference (opens in a new tab)](https://arxiv.org/abs/2211.11875) (Nov 2022)
- [Ask Me Anything: A simple strategy for prompting language models (opens in a new tab)](https://paperswithcode.com/paper/ask-me-anything-a-simple-strategy-for) (Oct 2022)
- [Recitation-Augmented Language Models (opens in a new tab)](https://arxiv.org/abs/2210.01296) (Oct 2022)
- [ReAct: Synergizing Reasoning and Acting in Language Models (opens in a new tab)](https://arxiv.org/abs/2210.03629) (Oct 2022)
- [Prompting GPT-3 To Be Reliable (opens in a new tab)](https://arxiv.org/abs/2210.09150) (Oct 2022)
- [Decomposed Prompting: A Modular Approach for Solving Complex Tasks (opens in a new tab)](https://arxiv.org/abs/2210.02406) (Oct 2022)
- [Language Models Are Greedy Reasoners: A Systematic Formal Analysis of Chain-of-Thought (opens in a new tab)](https://arxiv.org/abs/2210.01240v3) (Oct 2022)
- [Evaluating the Susceptibility of Pre-Trained Language Models via Handcrafted Adversarial Examples (opens in a new tab)](https://arxiv.org/abs/2209.02128) (Sep 2022)
- [Dynamic Prompt Learning via Policy Gradient for Semi-structured Mathematical Reasoning (opens in a new tab)](https://arxiv.org/abs/2209.14610) (Sep 2022)
- [Promptagator: Few-shot Dense Retrieval From 8 Examples (opens in a new tab)](https://arxiv.org/abs/2209.11755) (Sep 2022)
- [Atlas: Few-shot Learning with Retrieval Augmented Language Models (opens in a new tab)](https://arxiv.org/abs/2208.03299) (Nov 2022)
- [DocPrompting: Generating Code by Retrieving the Docs (opens in a new tab)](https://arxiv.org/abs/2207.05987) (July 2022)
- [On the Advance of Making Language Models Better Reasoners (opens in a new tab)](https://arxiv.org/abs/2206.02336) (June 2022)
- [Large Language Models are Zero-Shot Reasoners (opens in a new tab)](https://arxiv.org/abs/2205.11916) (May 2022)
- [Maieutic Prompting: Logically Consistent Reasoning with Recursive Explanations (opens in a new tab)](https://arxiv.org/abs/2205.11822) (May 2022)
- [MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning (opens in a new tab)](https://arxiv.org/abs/2205.00445) (May 2022)
- [PPT: Pre-trained Prompt Tuning for Few-shot Learning (opens in a new tab)](https://aclanthology.org/2022.acl-long.576/) (Mqy 2022)
- [Toxicity Detection with Generative Prompt-based Inference (opens in a new tab)](https://arxiv.org/abs/2205.12390) (May 2022)
- [Learning to Transfer Prompts for Text Generation (opens in a new tab)](https://arxiv.org/abs/2205.01543) (May 2022)
- [The Unreliability of Explanations in Few-shot Prompting for Textual Reasoning (opens in a new tab)](https://arxiv.org/abs/2205.03401) (May 2022)
- [A Taxonomy of Prompt Modifiers for Text-To-Image Generation (opens in a new tab)](https://arxiv.org/abs/2204.13988) (Apr 2022)
- [PromptChainer: Chaining Large Language Model Prompts through Visual Programming (opens in a new tab)](https://arxiv.org/abs/2203.06566) (Mar 2022)
- [Self-Consistency Improves Chain of Thought Reasoning in Language Models (opens in a new tab)](https://arxiv.org/abs/2203.11171) (March 2022)
- [Training language models to follow instructions with human feedback (opens in a new tab)](https://arxiv.org/abs/2203.02155)
- [Rethinking the Role of Demonstrations: What Makes In-Context Learning Work? (opens in a new tab)](https://arxiv.org/abs/2202.12837) (Feb 2022)
- [Chain of Thought Prompting Elicits Reasoning in Large Language Models (opens in a new tab)](https://arxiv.org/abs/2201.11903) (Jan 2022)
- [Show Your Work: Scratchpads for Intermediate Computation with Language Models (opens in a new tab)](https://arxiv.org/abs/2112.00114) (Nov 2021)
- [AI Chains: Transparent and Controllable Human-AI Interaction by Chaining Large Language Model Prompts (opens in a new tab)](https://arxiv.org/abs/2110.01691) (Oct 2021)
- [Generated Knowledge Prompting for Commonsense Reasoning (opens in a new tab)](https://arxiv.org/abs/2110.08387) (Oct 2021)
- [Multitask Prompted Training Enables Zero-Shot Task Generalization (opens in a new tab)](https://arxiv.org/abs/2110.08207) (Oct 2021)
- [Reframing Instructional Prompts to GPTk's Language (opens in a new tab)](https://arxiv.org/abs/2109.07830) (Sep 2021)
- [Design Guidelines for Prompt Engineering Text-to-Image Generative Models (opens in a new tab)](https://arxiv.org/abs/2109.06977) (Sep 2021)
- [Making Pre-trained Language Models Better Few-shot Learners (opens in a new tab)](https://aclanthology.org/2021.acl-long.295) (Aug 2021)
- [Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity (opens in a new tab)](https://arxiv.org/abs/2104.08786) (April 2021)
- [BERTese: Learning to Speak to BERT (opens in a new tab)](https://aclanthology.org/2021.eacl-main.316) (April 2021)
- [The Power of Scale for Parameter-Efficient Prompt Tuning (opens in a new tab)](https://arxiv.org/abs/2104.08691) (April 2021)
- [Prompt Programming for Large Language Models: Beyond the Few-Shot Paradigm (opens in a new tab)](https://arxiv.org/abs/2102.07350) (Feb 2021)
- [Calibrate Before Use: Improving Few-Shot Performance of Language Models (opens in a new tab)](https://arxiv.org/abs/2102.09690) (Feb 2021)
- [Prefix-Tuning: Optimizing Continuous Prompts for Generation (opens in a new tab)](https://arxiv.org/abs/2101.00190) (Jan 2021)
- [Learning to Generate Task-Specific Adapters from Task Description (opens in a new tab)](https://arxiv.org/abs/2101.00420) (Jan 2021)
- [Making Pre-trained Language Models Better Few-shot Learners (opens in a new tab)](https://arxiv.org/abs/2012.15723) (Dec 2020)
- [Learning from Task Descriptions (opens in a new tab)](https://aclanthology.org/2020.emnlp-main.105/) (Nov 2020)
- [AutoPrompt: Eliciting Knowledge from Language Models with Automatically Generated Prompts (opens in a new tab)](https://arxiv.org/abs/2010.15980) (Oct 2020)
- [Language Models are Few-Shot Learners (opens in a new tab)](https://arxiv.org/abs/2005.14165) (May 2020)
- [How Can We Know What Language Models Know? (opens in a new tab)](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00324/96460/How-Can-We-Know-What-Language-Models-Know) (July 2020)
- [Scaling Laws for Neural Language Models (opens in a new tab)](https://arxiv.org/abs/2001.08361) (Jan 2020)

### Applications[](https://www.promptingguide.ai/#applications)

- [Are LLMs All You Need for Task-Oriented Dialogue? (opens in a new tab)](https://arxiv.org/abs/2304.06556) (April 2023)
- [HiPrompt: Few-Shot Biomedical Knowledge Fusion via Hierarchy-Oriented Prompting (opens in a new tab)](https://arxiv.org/abs/2304.05973) (April 2023)
- [Approximating Human Evaluation of Social Chatbots with Prompting (opens in a new tab)](https://arxiv.org/abs/2304.05253) (April 2023)
- [Automated Reading Passage Generation with OpenAI's Large Language Model (opens in a new tab)](https://arxiv.org/abs/2304.04616) (April 2023)
- [WebBrain: Learning to Generate Factually Correct Articles for Queries by Grounding on Large Web Corpus (opens in a new tab)](https://arxiv.org/abs/2304.04358) (April 2023)
- [Prompt Pre-Training with Twenty-Thousand Classes for Open-Vocabulary Visual Recognition (opens in a new tab)](https://arxiv.org/abs/2304.04704) (April 2023)
- [GPT detectors are biased against non-native English writers (opens in a new tab)](https://arxiv.org/abs/2304.02819) (April 2023)
- [Zero-Shot Next-Item Recommendation using Large Pretrained Language Models (opens in a new tab)](https://arxiv.org/abs/2304.03153) (April 2023)
- [Large Language Models as Master Key: Unlocking the Secrets of Materials Science with GPT (opens in a new tab)](https://arxiv.org/abs/2304.02213) (April 2023)
- [Efficiently Aligned Cross-Lingual Transfer Learning for Conversational Tasks using Prompt-Tuning (opens in a new tab)](https://arxiv.org/abs/2304.01295) (April 2023)
- [Better Language Models of Code through Self-Improvement (opens in a new tab)](https://arxiv.org/abs/2304.01228) (April 2023)
- [PromptORE -- A Novel Approach Towards Fully Unsupervised Relation Extraction (opens in a new tab)](https://arxiv.org/abs/2304.01209) (April)
- Assessing Language Model Deployment with Risk Cards (April 2023)
- [Enhancing Large Language Models with Climate Resources (opens in a new tab)](https://arxiv.org/abs/2304.00116) (March 2023)
- [BloombergGPT: A Large Language Model for Finance (opens in a new tab)](https://arxiv.org/abs/2303.17564) (March 2023)
- [Medical Intervention Duration Estimation Using Language-enhanced Transformer Encoder with Medical Prompts (opens in a new tab)](https://arxiv.org/abs/2303.17408) (March 2023)
- [Soft-prompt tuning to predict lung cancer using primary care free-text Dutch medical notes (opens in a new tab)](https://arxiv.org/abs/2303.15846) (March 2023)
- [TaskMatrix.AI: Completing Tasks by Connecting Foundation Models with Millions of APIs (opens in a new tab)](https://arxiv.org/abs/2303.16434) (March 2023)
- [Larger Probes Tell a Different Story: Extending Psycholinguistic Datasets Via In-Context Learning (opens in a new tab)](https://arxiv.org/abs/2303.16445) (March 2023)
- [Linguistically Informed ChatGPT Prompts to Enhance Japanese-Chinese Machine Translation: A Case Study on Attributive Clauses (opens in a new tab)](https://arxiv.org/abs/2303.15587) (March 2023)
- [Knowledge-augmented Frame Semantic Parsing with Hybrid Prompt-tuning (opens in a new tab)](https://arxiv.org/abs/2303.14375) (March 2023)
- [Debiasing Scores and Prompts of 2D Diffusion for Robust Text-to-3D Generation (opens in a new tab)](https://arxiv.org/abs/2303.15413) (March 2023)
- [Zero-shot Model Diagnosis (opens in a new tab)](https://arxiv.org/abs/2303.15441#) (March 2023)
- [Prompting Large Language Models to Generate Code-Mixed Texts: The Case of South East Asian Languages (opens in a new tab)](https://arxiv.org/abs/2303.13592) (March 2023)
- [SPeC: A Soft Prompt-Based Calibration on Mitigating Performance Variability in Clinical Notes Summarization (opens in a new tab)](https://arxiv.org/abs/2303.13035) (March 2023)
- [Large Language Models and Simple, Stupid Bugs (opens in a new tab)](https://arxiv.org/abs/2303.11455) (March 2023)
- [Can Generative Pre-trained Transformers (GPT) Pass Assessments in Higher Education Programming Courses? (opens in a new tab)](https://arxiv.org/abs/2303.09325) (Mar 2023)
- [SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models (opens in a new tab)](https://arxiv.org/abs/2303.08896) (Mar 2023)
- [Large Language Models in the Workplace: A Case Study on Prompt Engineering for Job Type Classification (opens in a new tab)](https://arxiv.org/abs/2303.07142) (March 2023)
- [ICL-D3IE: In-Context Learning with Diverse Demonstrations Updating for Document Information Extraction (opens in a new tab)](https://arxiv.org/abs/2303.05063) (March 2023)
- [MathPrompter: Mathematical Reasoning using Large Language Models (opens in a new tab)](https://arxiv.org/abs/2303.05398) (March 2023)
- [Prompt-Based Learning for Thread Structure Prediction in Cybersecurity Forums (opens in a new tab)](https://arxiv.org/abs/2303.05400) (March 2023)
- [Choice Over Control: How Users Write with Large Language Models using Diegetic and Non-Diegetic Prompting (opens in a new tab)](https://arxiv.org/abs/2303.03199) (March 2023)
- [Prompting Large Language Models with Answer Heuristics for Knowledge-based Visual Question Answering (opens in a new tab)](https://arxiv.org/abs/2303.01903) (March 2023)
- [Soft Prompt Guided Joint Learning for Cross-Domain Sentiment Analysis (opens in a new tab)](https://arxiv.org/abs/2303.00815) (March 2023)
- [SpeechPrompt v2: Prompt Tuning for Speech Classification Tasks (opens in a new tab)](https://arxiv.org/abs/2303.00733) (March 2023)
- [Goal Driven Discovery of Distributional Differences via Language Descriptions (opens in a new tab)](https://arxiv.org/abs/2302.14233) (Feb 2023)
- [Navigating the Grey Area: Expressions of Overconfidence and Uncertainty in Language Models (opens in a new tab)](https://arxiv.org/abs/2302.13439) (Feb 2023)
- [TabGenie: A Toolkit for Table-to-Text Generation (opens in a new tab)](https://arxiv.org/abs/2302.14169) (Feb 2023)
- [SGL-PT: A Strong Graph Learner with Graph Prompt Tuning (opens in a new tab)](https://arxiv.org/abs/2302.12449) (Feb 2023)
- [Few-Shot Table-to-Text Generation with Prompt-based Adapter (opens in a new tab)](https://arxiv.org/abs/2302.12468) (Feb 2023)
- [Language Models Are Few-shot Learners for Prognostic Prediction (opens in a new tab)](https://arxiv.org/abs/2302.12692) (Feb 2023)
- [STA: Self-controlled Text Augmentation for Improving Text Classifications (opens in a new tab)](https://arxiv.org/abs/2302.12784) (Feb 2023)
- [Check Your Facts and Try Again: Improving Large Language Models with External Knowledge and Automated Feedback (opens in a new tab)](https://arxiv.org/abs/2302.12813) (Feb 2023)
- [How Generative AI models such as ChatGPT can be (Mis)Used in SPC Practice, Education, and Research? An Exploratory Study (opens in a new tab)](https://arxiv.org/abs/2302.10916) (Feb 2023)
- [Grimm in Wonderland: Prompt Engineering with Midjourney to Illustrate Fairytales (opens in a new tab)](https://arxiv.org/abs/2302.08961) (Feb 2023)
- [LabelPrompt: Effective Prompt-based Learning for Relation Classification (opens in a new tab)](https://arxiv.org/abs/2302.08068) (Feb 2023)
- [Language Model Crossover: Variation through Few-Shot Prompting (opens in a new tab)](https://arxiv.org/abs/2302.09236) (Feb 2023)
- [Prompt Tuning of Deep Neural Networks for Speaker-adaptive Visual Speech Recognition (opens in a new tab)](https://arxiv.org/abs/2302.08102) (Feb 2023)
- [The Capacity for Moral Self-Correction in Large Language Models (opens in a new tab)](https://arxiv.org/abs/2302.07459) (Feb 2023)
- [Prompting for Multimodal Hateful Meme Classification (opens in a new tab)](https://arxiv.org/abs/2302.04156) (Feb 2023)
- [PLACES: Prompting Language Models for Social Conversation Synthesis (opens in a new tab)](https://arxiv.org/abs/2302.03269) (Feb 2023)
- [Commonsense-Aware Prompting for Controllable Empathetic Dialogue Generation (opens in a new tab)](https://arxiv.org/abs/2302.01441) (Feb 2023)
- [Crawling the Internal Knowledge-Base of Language Models (opens in a new tab)](https://arxiv.org/abs/2301.12810) (Jan 2023)
- [Legal Prompt Engineering for Multilingual Legal Judgement Prediction (opens in a new tab)](https://arxiv.org/abs/2212.02199) (Dec 2022)
- [Investigating Prompt Engineering in Diffusion Models (opens in a new tab)](https://arxiv.org/abs/2211.15462) (Nov 2022)
- [Learn to Explain: Multimodal Reasoning via Thought Chains for Science Question Answering (opens in a new tab)](https://arxiv.org/abs/2209.09513v2) (Sep 2022)
- [Conversing with Copilot: Exploring Prompt Engineering for Solving CS1 Problems Using Natural Language (opens in a new tab)](https://arxiv.org/abs/2210.15157) (Oct 2022)
- [Piloting Copilot and Codex: Hot Temperature, Cold Prompts, or Black Magic? (opens in a new tab)](https://arxiv.org/abs/2210.14699) (Oct 2022)
- [Plot Writing From Scratch Pre-Trained Language Models (opens in a new tab)](https://aclanthology.org/2022.inlg-main.5) (July 2022)
- [Survey of Hallucination in Natural Language Generation (opens in a new tab)](https://arxiv.org/abs/2202.03629) (Feb 2022)

### Collections[](https://www.promptingguide.ai/#collections)

- [Chain-of-Thought Papers (opens in a new tab)](https://github.com/Timothyxxx/Chain-of-ThoughtsPapers)
- [Papers with Code (opens in a new tab)](https://paperswithcode.com/task/prompt-engineering)
- [Prompt Papers (opens in a new tab)](https://github.com/thunlp/PromptPapers#papers)

Last updated on April 16, 2023

[Biases](https://www.promptingguide.ai/risks/biases "Biases")[Tools](https://www.promptingguide.ai/tools "Tools")

## Tools & Libraries

---

### (Sorted By Name)[](https://www.promptingguide.ai/#sorted-by-name)

- [AI Test Kitchen (opens in a new tab)](https://aitestkitchen.withgoogle.com/)
- [betterprompt (opens in a new tab)](https://github.com/krrishdholakia/betterprompt)
- [ChatGPT Prompt Generator (opens in a new tab)](https://huggingface.co/spaces/merve/ChatGPT-prompt-generator)
- [ClickPrompt (opens in a new tab)](https://github.com/prompt-engineering/click-prompt)
- [DreamStudio (opens in a new tab)](https://beta.dreamstudio.ai/)
- [DUST (opens in a new tab)](https://dust.tt/)
- [Dyno (opens in a new tab)](https://trydyno.com/)
- [EmergentMind (opens in a new tab)](https://www.emergentmind.com/)
- [EveryPrompt (opens in a new tab)](https://www.everyprompt.com/)
- [Guardrails (opens in a new tab)](https://github.com/ShreyaR/guardrails)
- [GPT Index (opens in a new tab)](https://github.com/jerryjliu/gpt_index)
- [GPTTools (opens in a new tab)](https://gpttools.com/comparisontool)
- [hwchase17/adversarial-prompts (opens in a new tab)](https://github.com/hwchase17/adversarial-prompts)
- [Interactive Composition Explorer (opens in a new tab)](https://github.com/oughtinc/ice)
- [LangChain (opens in a new tab)](https://github.com/hwchase17/langchain)
- [Lexica (opens in a new tab)](https://lexica.art/)
- [LMFlow (opens in a new tab)](https://github.com/OptimalScale/LMFlow)
- [loom (opens in a new tab)](https://github.com/socketteer/loom)
- [Metaprompt (opens in a new tab)](https://metaprompt.vercel.app/?task=gpt)
- [OpenAI Playground (opens in a new tab)](https://beta.openai.com/playground)
- [OpenICL (opens in a new tab)](https://github.com/Shark-NLP/OpenICL)
- [OpenPrompt (opens in a new tab)](https://github.com/thunlp/OpenPrompt)
- [OpenPlayground (opens in a new tab)](https://nat.dev/)
- [Playground (opens in a new tab)](https://playgroundai.com/)
- [Prodia (opens in a new tab)](https://app.prodia.com/#/)
- [Prompt Base (opens in a new tab)](https://promptbase.com/)
- [Prompt Engine (opens in a new tab)](https://github.com/microsoft/prompt-engine)
- [Prompt Generator for OpenAI's DALL-E 2 (opens in a new tab)](http://dalle2-prompt-generator.s3-website-us-west-2.amazonaws.com/)
- [Promptable (opens in a new tab)](https://promptable.ai/)
- [PromptInject (opens in a new tab)](https://github.com/agencyenterprise/PromptInject)
- [Prompts.ai (opens in a new tab)](https://github.com/sevazhidkov/prompts-ai)
- [Promptmetheus (opens in a new tab)](https://promptmetheus.com/)
- [PromptPerfect (opens in a new tab)](https://promptperfect.jina.ai/)
- [Promptly (opens in a new tab)](https://trypromptly.com/)
- [PromptSource (opens in a new tab)](https://github.com/bigscience-workshop/promptsource)
- [Promptist (opens in a new tab)](https://promptist.herokuapp.com/)
- [Scale SpellBook (opens in a new tab)](https://scale.com/spellbook)
- [sharegpt (opens in a new tab)](https://sharegpt.com/)
- [ThoughtSource (opens in a new tab)](https://github.com/OpenBioLink/ThoughtSource)
- [Visual Prompt Builder (opens in a new tab)](https://tools.saxifrage.xyz/prompt)

Last updated on April 16, 2023

[Papers](https://www.promptingguide.ai/papers "Papers")[Notebooks](https://www.promptingguide.ai/notebooks "Notebooks")

## Prompt Engineering Notebooks

---

Contains a collection of notebooks we have designed to help you get started with prompt engineering. More to be added soon!

| Description | Notebook |
| --- | --- |
| Learn how to perform many different types of common tasks using the `openai` and `LangChain` library | [Getting Started with Prompt Engineering (opens in a new tab)](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/pe-lecture.ipynb) |
| Learn how to use code as reasoning for solving common tasks using the Python interpreter in combination with the language model. | [Program-Aided Language Model (opens in a new tab)](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/pe-pal.ipynb) |
| Learn more about how to make calls to the ChatGPT APIs using the `openai` library. | [ChatGPT API Intro (opens in a new tab)](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/pe-chatgpt-intro.ipynb) |
| Learn how to use ChatGPT features using the `LangChain` library. | [ChatGPT API with LangChain (opens in a new tab)](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/pe-chatgpt-langchain.ipynb) |
| Learn about adversarial prompting include defensive measures. | [Adversarial Prompt Engineering (opens in a new tab)](https://github.com/dair-ai/Prompt-Engineering-Guide/blob/main/notebooks/pe-chatgpt-adversarial.ipynb) |

Last updated on April 15, 2023

[Tools](https://www.promptingguide.ai/tools "Tools")[Datasets](https://www.promptingguide.ai/datasets "Datasets")

## Datasets

---

Datasets

## Additional Readings

---

### (Sorted By Name)[](https://www.promptingguide.ai/#sorted-by-name)

- [2023 AI Index Report (opens in a new tab)](https://aiindex.stanford.edu/report/)
- [3 Principles for prompt engineering with GPT-3 (opens in a new tab)](https://www.linkedin.com/pulse/3-principles-prompt-engineering-gpt-3-ben-whately)
- [Eight Things to Know about Large Language Models (opens in a new tab)](https://arxiv.org/pdf/2304.00612v1.pdf)
- [A beginner-friendly guide to generative language models - LaMBDA guide (opens in a new tab)](https://aitestkitchen.withgoogle.com/how-lamda-works)
- [A Complete Introduction to Prompt Engineering for Large Language Models (opens in a new tab)](https://www.mihaileric.com/posts/a-complete-introduction-to-prompt-engineering)
- [A Generic Framework for ChatGPT Prompt Engineering (opens in a new tab)](https://medium.com/@thorbjoern.heise/a-generic-framework-for-chatgpt-prompt-engineering-7097f6513a0b)
- [An SEO’s guide to ChatGPT prompts (opens in a new tab)](https://searchengineland.com/chatgpt-prompts-seo-393523)
- [Anyone can Design! With a little help from Generative AI (opens in a new tab)](https://github.com/YashSharma/PromptEngineering)
- [AI Content Generation (opens in a new tab)](https://www.jonstokes.com/p/ai-content-generation-part-1-machine)
- [AI's rise generates new job title: Prompt engineer (opens in a new tab)](https://www.axios.com/2023/02/22/chatgpt-prompt-engineers-ai-job)
- [AI Safety, RLHF, and Self-Supervision - Jared Kaplan | Stanford MLSys #79 (opens in a new tab)](https://www.youtube.com/watch?v=fqC3D-zNJUM&ab_channel=StanfordMLSysSeminars)
- [Awesome Textual Instruction Learning Papers (opens in a new tab)](https://github.com/RenzeLou/awesome-instruction-learning)
- [Awesome ChatGPT Prompts (opens in a new tab)](https://github.com/f/awesome-chatgpt-prompts)
- [Best 100+ Stable Diffusion Prompts (opens in a new tab)](https://mpost.io/best-100-stable-diffusion-prompts-the-most-beautiful-ai-text-to-image-prompts)
- [Best practices for prompt engineering with OpenAI API (opens in a new tab)](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)
- [Building GPT-3 applications—beyond the prompt (opens in a new tab)](https://medium.com/data-science-at-microsoft/building-gpt-3-applications-beyond-the-prompt-504140835560)
- [Can AI really be protected from text-based attacks? (opens in a new tab)](https://techcrunch.com/2023/02/24/can-language-models-really-be-protected-from-text-based-attacks/)
- [ChatGPT, AI and GPT-3 Apps and use cases (opens in a new tab)](https://gpt3demo.com/)
- [ChatGPT Prompts (opens in a new tab)](https://twitter.com/aaditsh/status/1636398208648658945?s=20)
- [ChatGPT Plugins Collection ⭐️ (unofficial) (opens in a new tab)](https://github.com/logankilpatrick/ChatGPT-Plugins-Collection)
- [ChatGPT3 Prompt Engineering (opens in a new tab)](https://github.com/mattnigh/ChatGPT3-Free-Prompt-List)
- [CMU Advanced NLP 2022: Prompting (opens in a new tab)](https://youtube.com/watch?v=5ef83Wljm-M&feature=shares)
- [Common Sense as Dark Matter - Yejin Choi | Stanford MLSys #78 (opens in a new tab)](https://youtube.com/live/n4HakBqoCVg?feature=shares)
- [Create images with your words–Bing Image Creator comes to the new Bing (opens in a new tab)](https://blogs.microsoft.com/blog/2023/03/21/create-images-with-your-words-bing-image-creator-comes-to-the-new-bing/)
- [Curtis64's set of prompt gists (opens in a new tab)](https://gist.github.com/Curtis-64)
- [CS324 - Large Language Models (opens in a new tab)](https://stanford-cs324.github.io/winter2022/)
- [CS 324 - Advances in Foundation Models (opens in a new tab)](https://stanford-cs324.github.io/winter2023/)
- [CS224N: Natural Language Processing with Deep Learning (opens in a new tab)](https://web.stanford.edu/class/cs224n/)
- [DALL·E 2 Prompt Engineering Guide (opens in a new tab)](https://docs.google.com/document/d/11WlzjBT0xRpQhP9tFMtxzd0q6ANIdHPUBkMV-YB043U/edit#)
- [DALL·E 2 Preview - Risks and Limitations (opens in a new tab)](https://github.com/openai/dalle-2-preview/blob/main/system-card)
- [DALLE Prompt Book (opens in a new tab)](https://dallery.gallery/the-dalle-2-prompt-book)
- [DALL-E, Make Me Another Picasso, Please (opens in a new tab)](https://www.newyorker.com/magazine/2022/07/11/dall-e-make-me-another-picasso-please?)
- [Diffusion Models: A Practical Guide (opens in a new tab)](https://scale.com/guides/diffusion-models-guide)
- [Exploiting GPT-3 Prompts (opens in a new tab)](https://twitter.com/goodside/status/1569128808308957185)
- [Exploring Prompt Injection Attacks (opens in a new tab)](https://research.nccgroup.com/2022/12/05/exploring-prompt-injection-attacks)
- [Extrapolating to Unnatural Language Processing with GPT-3's In-context Learning: The Good, the Bad, and the Mysterious (opens in a new tab)](http://ai.stanford.edu/blog/in-context-learning)
- [FVQA 2.0: Introducing Adversarial Samples into Fact-based Visual Question Answering (opens in a new tab)](https://arxiv.org/pdf/2303.10699.pdf)
- [Generative AI with Cohere: Part 1 - Model Prompting (opens in a new tab)](https://txt.cohere.ai/generative-ai-part-1)
- [Generative AI: Perspectives from Stanford HAI (opens in a new tab)](https://hai.stanford.edu/sites/default/files/2023-03/Generative_AI_HAI_Perspectives.pdf)
- [Get a Load of This New Job: "Prompt Engineers" Who Act as Psychologists to AI Chatbots (opens in a new tab)](https://futurism.com/prompt-engineers-ai)
- [Giving GPT-3 a Turing Test (opens in a new tab)](https://lacker.io/ai/2020/07/06/giving-gpt-3-a-turing-test.html)
- [GPT-3 & Beyond (opens in a new tab)](https://youtube.com/watch?v=-lnHHWRCDGk)
- [GPT3 and Prompts: A quick primer (opens in a new tab)](https://buildspace.so/notes/intro-to-gpt3-prompts)
- [GPT-4 Tutorial: How to Chat With Multiple PDF Files (~1000 pages of Tesla's 10-K Annual Reports) (opens in a new tab)](https://youtu.be/Ix9WIZpArm0)
- [Hands-on with Bing’s new ChatGPT-like features (opens in a new tab)](https://techcrunch.com/2023/02/08/hands-on-with-the-new-bing/)
- [How to Draw Anything (opens in a new tab)](https://andys.page/posts/how-to-draw)
- [How to get images that don't suck (opens in a new tab)](https://www.reddit.com/r/StableDiffusion/comments/x41n87/how_to_get_images_that_dont_suck_a)
- [How to make LLMs say true things (opens in a new tab)](https://evanjconrad.com/posts/world-models)
- [How to perfect your prompt writing for AI generators (opens in a new tab)](https://www.sydney.edu.au/news-opinion/news/2023/02/28/how-to-perfect-your-prompt-writing-for-ai-generators.html)
- [How to write good prompts (opens in a new tab)](https://andymatuschak.org/prompts)
- [If I Was Starting Prompt Engineering in 2023: My 8 Insider Tips (opens in a new tab)](https://youtube.com/watch?v=SirW7feTjh0&feature=shares)
- [Indirect Prompt Injection on Bing Chat (opens in a new tab)](https://greshake.github.io/)
- [Interactive guide to GPT-3 prompt parameters (opens in a new tab)](https://sevazhidkov.com/interactive-guide-to-gpt-3-prompt-parameters)
- [Introduction to ChatGPT (opens in a new tab)](https://www.edx.org/course/introduction-to-chatgpt)
- [Introduction to Reinforcement Learning with Human Feedback (opens in a new tab)](https://www.surgehq.ai/blog/introduction-to-reinforcement-learning-with-human-feedback-rlhf-series-part-1)
- [In defense of prompt engineering (opens in a new tab)](https://simonwillison.net/2023/Feb/21/in-defense-of-prompt-engineering/)
- [JailBreaking ChatGPT: Everything You Need to Know (opens in a new tab)](https://metaroids.com/learn/jailbreaking-chatgpt-everything-you-need-to-know/)
- [Language Models and Prompt Engineering: Systematic Survey of Prompting Methods in NLP (opens in a new tab)](https://youtube.com/watch?v=OsbUfL8w-mo&feature=shares)
- [Language Model Behavior: A Comprehensive Survey (opens in a new tab)](https://arxiv.org/abs/2303.11504)
- [Learn Prompting (opens in a new tab)](https://learnprompting.org/)
- [Learning Prompt (opens in a new tab)](https://github.com/thinkingjimmy/Learning-Prompt)
- [LINGO : Visually Debiasing Natural Language Instructions to Support Task Diversity (opens in a new tab)](https://arxiv.org/abs/2304.06184)
- [Meet Claude: Anthropic’s Rival to ChatGPT (opens in a new tab)](https://scale.com/blog/chatgpt-vs-claude)
- [Methods of prompt programming (opens in a new tab)](https://generative.ink/posts/methods-of-prompt-programming)
- [Mysteries of mode collapse (opens in a new tab)](https://www.lesswrong.com/posts/t9svvNPNmFf5Qa3TA/mysteries-of-mode-collapse)
- [NLP for Text-to-Image Generators: Prompt Analysis (opens in a new tab)](https://heartbeat.comet.ml/nlp-for-text-to-image-generators-prompt-analysis-part-1-5076a44d8365)
- [NLP with Deep Learning CS224N/Ling284 - Lecture 11: Prompting, Instruction Tuning, and RLHF (opens in a new tab)](http://web.stanford.edu/class/cs224n/slides/cs224n-2023-lecture11-prompting-rlhf.pdf)
- [Notes for Prompt Engineering by sw-yx (opens in a new tab)](https://github.com/sw-yx/ai-notes)
- [On pitfalls (and advantages) of sophisticated large language models (opens in a new tab)](https://arxiv.org/abs/2303.17511)
- [OpenAI Cookbook (opens in a new tab)](https://github.com/openai/openai-cookbook)
- [OpenAI Prompt Examples for several applications (opens in a new tab)](https://platform.openai.com/examples)
- [Pretrain, Prompt, Predict - A New Paradigm for NLP (opens in a new tab)](http://pretrain.nlpedia.ai/)
- [Prompt Engineer: Tech's hottest job title? (opens in a new tab)](https://www.peoplematters.in/article/talent-management/is-prompt-engineering-the-hottest-job-in-ai-today-37036)
- [Prompt Engineering by Lilian Weng (opens in a new tab)](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/)
- [Prompt Engineering 101 - Introduction and resources (opens in a new tab)](https://www.linkedin.com/pulse/prompt-engineering-101-introduction-resources-amatriain)
- [Prompt Engineering 101: Autocomplete, Zero-shot, One-shot, and Few-shot prompting (opens in a new tab)](https://youtube.com/watch?v=v2gD8BHOaX4&feature=shares)
- [Prompt Engineering 101 (opens in a new tab)](https://humanloop.com/blog/prompt-engineering-101)
- [Prompt Engineering - A new profession ? (opens in a new tab)](https://www.youtube.com/watch?v=w102J3_9Bcs&ab_channel=PatrickDebois)
- [Prompt Engineering by co:here (opens in a new tab)](https://docs.cohere.ai/docs/prompt-engineering)
- [Prompt Engineering by Microsoft (opens in a new tab)](https://microsoft.github.io/prompt-engineering)
- [Prompt Engineering: The Career of Future (opens in a new tab)](https://shubhamsaboo111.medium.com/prompt-engineering-the-career-of-future-2fb93f90f117)
- [Prompt engineering davinci-003 on our own docs for automated support (Part I) (opens in a new tab)](https://www.patterns.app/blog/2022/12/21/finetune-llm-tech-support)
- [Prompt Engineering Guide: How to Engineer the Perfect Prompts (opens in a new tab)](https://richardbatt.co.uk/prompt-engineering-guide-how-to-engineer-the-perfect-prompts)
- [Prompt Engineering in GPT-3 (opens in a new tab)](https://www.analyticsvidhya.com/blog/2022/05/prompt-engineering-in-gpt-3)
- [Prompt Engineering Template (opens in a new tab)](https://docs.google.com/spreadsheets/d/1-snKDn38-KypoYCk9XLPg799bHcNFSBAVu2HVvFEAkA/edit#gid=0)
- [Prompt Engineering Topic by GitHub (opens in a new tab)](https://github.com/topics/prompt-engineering)
- [Prompt Engineering: The Ultimate Guide 2023 \[GPT-3 & ChatGPT\] (opens in a new tab)](https://businessolution.org/prompt-engineering/)
- [Prompt Engineering: From Words to Art (opens in a new tab)](https://www.saxifrage.xyz/post/prompt-engineering)
- [Prompt Engineering with OpenAI's GPT-3 and other LLMs (opens in a new tab)](https://youtube.com/watch?v=BP9fi_0XTlw&feature=shares)
- [Prompt injection attacks against GPT-3 (opens in a new tab)](https://simonwillison.net/2022/Sep/12/prompt-injection)
- [Prompt injection to read out the secret OpenAI API key (opens in a new tab)](https://twitter.com/ludwig_stumpp/status/1619701277419794435?s=20&t=GtoMlmYCSt-UmvjqJVbBSA)
- [Prompting: Better Ways of Using Language Models for NLP Tasks (opens in a new tab)](https://thegradient.pub/prompting/)
- [Prompting for Few-shot Learning (opens in a new tab)](https://www.cs.princeton.edu/courses/archive/fall22/cos597G/lectures/lec05.pdf)
- [Prompting in NLP: Prompt-based zero-shot learning (opens in a new tab)](https://savasy-22028.medium.com/prompting-in-nlp-prompt-based-zero-shot-learning-3f34bfdb2b72)
- [Prompting Methods with Language Models and Their Applications to Weak Supervision (opens in a new tab)](https://snorkel.ai/prompting-methods-with-language-models-nlp)
- [Prompts as Programming by Gwern (opens in a new tab)](https://www.gwern.net/GPT-3#prompts-as-programming)
- [Prompts for communicators using the new AI-powered Bing (opens in a new tab)](https://blogs.microsoft.com/blog/2023/03/16/prompts-for-communicators-using-the-new-ai-powered-bing/)
- [Reverse Prompt Engineering for Fun and (no) Profit (opens in a new tab)](https://lspace.swyx.io/p/reverse-prompt-eng)
- [Retrieving Multimodal Information for Augmented Generation: A Survey (opens in a new tab)](https://arxiv.org/pdf/2303.10868.pdf)
- [So you want to be a prompt engineer: Critical careers of the future (opens in a new tab)](https://venturebeat.com/ai/so-you-want-to-be-a-prompt-engineer-critical-careers-of-the-future/)
- [Simulators (opens in a new tab)](https://www.lesswrong.com/posts/vJFdjigzmcXMhNTsx/simulators)
- [Start with an Instruction (opens in a new tab)](https://beta.openai.com/docs/quickstart/start-with-an-instruction)
- [Talking to machines: prompt engineering & injection (opens in a new tab)](https://artifact-research.com/artificial-intelligence/talking-to-machines-prompt-engineering-injection)
- [Tech’s hottest new job: AI whisperer. No coding required (opens in a new tab)](https://www.washingtonpost.com/technology/2023/02/25/prompt-engineers-techs-next-big-job/)
- [The Book - Fed Honeypot (opens in a new tab)](https://fedhoneypot.notion.site/25fdbdb69e9e44c6877d79e18336fe05?v=1d2bf4143680451986fd2836a04afbf4)
- [The ChatGPT Prompt Book (opens in a new tab)](https://docs.google.com/presentation/d/17b_ocq-GL5lhV_bYSShzUgxL02mtWDoiw9xEroJ5m3Q/edit#slide=id.gc6f83aa91_0_79)
- [The ChatGPT list of lists: A collection of 3000+ prompts, examples, use-cases, tools, APIs, extensions, fails and other resources (opens in a new tab)](https://medium.com/mlearning-ai/the-chatgpt-list-of-lists-a-collection-of-1500-useful-mind-blowing-and-strange-use-cases-8b14c35eb)
- [The Most Important Job Skill of This Century (opens in a new tab)](https://www.theatlantic.com/technology/archive/2023/02/openai-text-models-google-search-engine-bard-chatbot-chatgpt-prompt-writing/672991/)
- [The Mirror of Language (opens in a new tab)](https://deepfates.com/the-mirror-of-language)
- [The Waluigi Effect (mega-post) (opens in a new tab)](https://www.lesswrong.com/posts/D7PumeYTDPfBTp3i7/the-waluigi-effect-mega-post)
- [Thoughts and impressions of AI-assisted search from Bing (opens in a new tab)](https://simonwillison.net/2023/Feb/24/impressions-of-bing/)
- [Unleash Your Creativity with Generative AI: Learn How to Build Innovative Products! (opens in a new tab)](https://youtube.com/watch?v=jqTkMpziGBU&feature=shares)
- [Unlocking Creativity with Prompt Engineering (opens in a new tab)](https://youtube.com/watch?v=PFsbWAC4_rk&feature=shares)
- [Using GPT-Eliezer against ChatGPT Jailbreaking (opens in a new tab)](https://www.alignmentforum.org/posts/pNcFYZnPdXyL2RfgA/using-gpt-eliezer-against-chatgpt-jailbreaking)
- [What Is ChatGPT Doing … and Why Does It Work? (opens in a new tab)](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/)
- [Why is ChatGPT so good? (opens in a new tab)](https://scale.com/blog/chatgpt-reinforcement-learning)
- [【徹底解説】これからのエンジニアの必携スキル、プロンプトエンジニアリングの手引「Prompt Engineering Guide」を読んでまとめてみた(opens in a new tab)](https://dev.classmethod.jp/articles/how-to-design-prompt-engineering/)

Last updated on April 16, 2023

[Datasets](https://www.promptingguide.ai/datasets "Datasets")
