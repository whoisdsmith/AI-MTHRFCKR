## Align prompt instructions with the task’s end goal

When engineering a prompt, we need to put ourselves in the shoes of the LLM and ask: what will the model think the end goal of my task is?

For example, if we want the model to respond to a customer with a single response in a friendly way, we might write a prompt like:

"This is a conversation between a customer and a polite, helpful customer support service agent."

This provides a clear and direct instruction to the model. However, we must consider what GPT-3 will think the task actually is.

![Saying “this is a conversation” in a prompt makes GPT-3 think the task is to generate a full transcript of a conversation vs just giving a single response](https://humanloop.com/_next/image?url=%2Fblog%2Fprompt-engineering-101%2F5.png&w=3840&q=75)

GPT-3 will take things literally. Saying “this is a conversation” in the prompt makes GPT-3 makes GPT-3 generate a full dialogue (the most likely continuation) rather than just giving a single response

We can see that GPT-3 thought the task was to create an entire conversation transcript given the customer’s initial input and not simply to just respond once to the customer. GPT-3 was not wrong necessarily but it was misaligned with the original specific task intention. Let’s instead change our prompt to “Respond to a customer as a polite, helpful customer service agent.”.

![Changing the prompt to say “Respond to ...” is more aligned with the end goal of what we wanted from the LLM.](https://humanloop.com/_next/image?url=%2Fblog%2Fprompt-engineering-101%2F6.png&w=3840&q=75)

Changing the prompt to say “Respond to …” is more aligned with the end goal of what we wanted from the LLM.

The small change from "this is a conversation…" to "respond to a…" aligned GPT-3's response with our desired outcome. Prompts must be both direct and tailored to the task; when they are not, the model will respond with what it believes is the correct task, regardless of our intention.

---