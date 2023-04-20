## Include direct instructions in prompts

For simple tasks (at least simple for GPT-3) the best prompt is a clear, direct, and concise one that tells the LLM the exact task we are trying to solve. Let’s take a simple example asking GPT-3 (which is instruction tuned) to translate a sentence from English to Spanish. Our prompt will consist of three elements:

1. A clear, concise, and direct instruction: “**Translate.**”
2. The English phrase we want translated preceded by “**English:** ”
3. A clearly designated space for the LLM to answer preceded by the intentionally similar prefix “**Spanish:** ”

These three elements are all part of a direct set of instructions with an organized answer area. By giving GPT-3 this clearly constructed prompt, it will be able to recognize the task being asked of it and fill in the answer correctly.

![Example of a translation task using GPT-3 where the prompt includes a direct instruction “Translate.” followed by a clear area for the model to respond.](https://humanloop.com/_next/image?url=%2Fblog%2Fprompt-engineering-101%2F2.png&w=3840&q=75)

If in doubt, just ask. Here's an example of a translation task using GPT-3 where the prompt includes a direct instruction “Translate.” followed by a clear area for the model to respond.

Without clear instructions, LLMs are likely to behave erratically and be more likely to give an answer we were not expecting. Let’s take the same prompt and remove the one word instruction preceding the English sentence: “Translate.”. We can see how just one word being removed from our prompt makes GPT-3 misinterpret the task entirely and instead responds to the question “How do you reset your password” with a generic customer support response in Spanish.

![Example of the same Spanish to English translation task without the direct instruction “Translate.” which GPT-3 then incorrectly responds to.](https://humanloop.com/_next/image?url=%2Fblog%2Fprompt-engineering-101%2F3.png&w=3840&q=75)

Without a direct instruction (such as “Translate”), GPT-3 then incorrectly interprets the task.

---