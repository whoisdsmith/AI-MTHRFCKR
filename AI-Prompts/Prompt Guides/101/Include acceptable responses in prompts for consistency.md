## Include acceptable responses in prompts for consistency

Another way to form prompts is as a “complete this sentence” prompt. In this style of prompt, we are asking the LLM to complete a sentence with the answer we are seeking which generally leads to more natural language. Here is an example prompt run through GPT-3 asking for the sentiment of a movie review:

![A sentiment task that provides a response that is arguably too natural to be considered a response to, say, a strict sentiment classification task.](https://humanloop.com/_next/image?url=%2Fblog%2Fprompt-engineering-101%2F8.png&w=3840&q=75)

Without specifying the format of the output, you'll likely get a natural language response which can be hard to use for downstream tasks

Technically GPT-3 answered correctly here. The sentiment of the review was that they didn’t like the movie. But If we wanted to narrow down the universe of possible results with prompt engineering to make our response more like a sentiment classifier we could tweak this prompt slightly and give it a list of possible answers directly in the instruction of the prompt. In this case, let’s guide GPT-3 to only respond with either “positive” or “negative”.

![https://lh6.googleusercontent.com/nETgOlRLA4RPghTzEfeEtZLOZUtGLbyFKSXHEbAZc1_I57wYyx3H8OUxSikSfOp_HHzlc_ojdxWe_d2Zj7txbOM-QkGEBR1qysicA9BKEmB2Aw6iKPJ2FbdTBBqjNwtXsprHiPElKtnRm9s1R_ourV4H8reyYKcCVsDAoYUz0h-D4JEMAf5om1D8XrhaRA](https://humanloop.com/_next/image?url=%2Fblog%2Fprompt-engineering-101%2F9.png&w=3840&q=75)

Including the options of possible responses in our instruction (in this case a binary choice) nudges GPT-3 to respond only using one of the two options instead of the previously overly natural response

The result is much more aligned with a binary classifier where GPT-3 is now only responding using the two given options. From here we can alter the label names as long as they are semantically appropriate.

![LLMs can decipher and assign semantically appropriate labels as long as they make semantic sense](https://humanloop.com/_next/image?url=%2Fblog%2Fprompt-engineering-101%2F10.png&w=3840&q=75)

LLMs can decipher and assign semantically appropriate labels as long as they make semantic sense

Could we have achieved similar results using few-shot learning? Probably but this prompt is much more concise and we don’t need to spend the time coming up with examples.

---