# Part 1: Crafting the prompt

Files & media: 122.Idea_13.png

For this idea, we need to create a prompt that will give us a good cold email. To do that we will use the OpenAI playground.

The prompt requires some experimentation to get it right. Make changes to the context, temperature, and other settings till you get a sufficient response. [Refer to the Playground section](../30%20Days%20Action%20Plan%20(1)%204e7aaffbc4084860889660effa8c406e/OpenAI%20Playground%200970fdff0eb9491786ecbc4c36532827.md) to understand the various components to craft the prompt.

[OpenAI Playground](../30%20Days%20Action%20Plan%20(1)%204e7aaffbc4084860889660effa8c406e/OpenAI%20Playground%200970fdff0eb9491786ecbc4c36532827.md)

For the cold email write, this is the prompt we will be using:

model: text-davinci-003
Prompt: "Write a long cold email in a friendly but professional tone. Mention the purpose in the introduction, and experience in the middle and ask as a conclusion and follow the below information:

From: <Writer>

Purpose: <Why>

To: <Receiver>

Company Description: <Company>

Expereience: <Experience>

Ask: <Action>

temperature: 0.81,
max_tokens: 3312,
top_p: 0.29,
frequency_penalty: 0.59,
presence_penalty: 0.57

![Screen Shot 2023-01-29 at 11.57.53 PM.png](Part%201%20Crafting%20the%20prompt%20d8d7967439fa445189cef7340ed7a2e5/Screen_Shot_2023-01-29_at_11.57.53_PM.png)