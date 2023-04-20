## Give examples in prompts to get the best response

If clear and direct instructions aren’t enough for a task to be solved consistently and accurately, it is usually a good idea to give the LLM a few examples. This can be as simple as giving an LLM a single example of our task and letting the model figure out the rest.

Let’s see an example on our English to Spanish translation task. We’ll replace the instruction, “Translate.”, with a single example of an English to Spanish translation instead. We should format the example in the exact same way as the final pair except the Spanish translation will be filled in for our example to tell the LLM what we are trying to do.

![An example of few-shot learning with GPT-3 is where the English to Spanish translation task's direct instruction has been replaced with a single example. The model was able to recognize and respond accordingly.](https://humanloop.com/_next/image?url=%2Fblog%2Fprompt-engineering-101%2F4.png&w=3840&q=75)

Few-shot learning can help clarify the task, and especially help with things like tone, syntax or style. Here a single example of translation is enough for the the model respond correctly.

We can see that by giving the model an example of what we want, the model can figure out the task as if we gave it a direct set of instructions. Including examples in prompts is called **few-shot learning.** This is such a breakthrough capability with GPT-3, that it was the main focus in the the title of its research paper: “Language models are few-shot learners”. The creators of GPT-3 knew that few-shot learning was so powerful that it would be one of the dominant ways people interacted with their model.

By using few-shot learning, we can provide an LLM with an understanding of our task without explicitly providing instructions. This can be especially helpful when the task is specific to a certain field or when the response language must be tailored to a particular organization (e.g. using P1, P2, and P3 instead of High, Medium, and Low priority).

---