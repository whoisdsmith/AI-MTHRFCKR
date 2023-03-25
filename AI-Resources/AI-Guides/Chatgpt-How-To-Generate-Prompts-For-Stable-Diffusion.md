---
created: 2023-01-30T16:22:05 (UTC -05:00)
tags: []
source: https://stable-diffusion-art.com/chatgpt-prompt/
author: 
---

# ChatGPT: How to Generate Prompts for Stable Diffusion - Stable Diffusion Art

> ## Excerpt
> Can ChatGPT generate high-quality prompts for Stable Diffusion? The answer is yes. But you will need special methods to tease them out. Once you learn how to

---

Can ChatGPT generate high-quality prompts for Stable Diffusion? The answer is yes. But you will need special methods to tease them out. Once you learn how to do it, the results will surprise you. In this article, I will show you how to do that step-by-step.

Contents \[[hide](https://stable-diffusion-art.com/chatgpt-prompt/#)\]

- [What is ChatGPT?](https://stable-diffusion-art.com/chatgpt-prompt/#What_is_ChatGPT)
- [How was ChatGPT trained?](https://stable-diffusion-art.com/chatgpt-prompt/#How_was_ChatGPT_trained)
- [Does ChatGPT know anything about Stable Diffusion?](https://stable-diffusion-art.com/chatgpt-prompt/#Does_ChatGPT_know_anything_about_Stable_Diffusion)
- [How to use ChatGPT](https://stable-diffusion-art.com/chatgpt-prompt/#How_to_use_ChatGPT)
- [Asking for prompts](https://stable-diffusion-art.com/chatgpt-prompt/#Asking_for_prompts)
    - [Close-up illustration](https://stable-diffusion-art.com/chatgpt-prompt/#Close-up_illustration)
    - [Full-body illustration](https://stable-diffusion-art.com/chatgpt-prompt/#Full-body_illustration)
    - [Ask for more](https://stable-diffusion-art.com/chatgpt-prompt/#Ask_for_more)
- [Summary](https://stable-diffusion-art.com/chatgpt-prompt/#Summary)

## What is ChatGPT?

[ChatGPT](https://openai.com/blog/chatgpt/) is a chatbot released by Open AI in November 2022. It is built on the [GPT-3](https://en.wikipedia.org/wiki/GPT-3) family of Large Language Model which was trained with text containing *hundreds of billions of words* on the internet.

How long is a book with hundreds of billions words? It would take a person more than five thousand years to read it all out.

As a result, ChatGPT contains vast amount of human knowledge. it can generate essays, poems, fictions and even computer codes.

## How Was ChatGPT Trained?

ChatGPT was fine-tuned on top of GPT-3.5. GPT-3 itself is a powerful large language model. **It operates like autocomplete**. You type in a few words or a few sentences, the model predicts the most likely next words. Because the large amount of data it was trained on, the autocomplete of GPT-3 is supercharged. It can produce an essay of coherent and (sometimes) accurate content.

Human trainers played an important role in fine-tuning ChatGPT’s response. The model was trained to provide answers human trainers would give. Human trainers also ranked ChatGPT’s answers during the training phase so that it would prioritize answers humans prefer.

## Does ChatGPT Know Anything About Stable Diffusion?

Unfortunately, the answer is no. You can easily check by asking ChatGPT the question “What is Stable Diffusion?”. Its answer is

> Stable diffusion refers to a type of stochastic process that describes the spread of a certain quantity, such as information or a disease, through a network of individuals or nodes. The term “stable” is used to indicate that the process reaches a steady state, in which the rate at which the quantity spreads through the network is balanced by the rate at which it decays. The most common example of stable diffusion is the spread of a rumor through a social network.

We can debate whether this is complete nonsense, but we should all agree this is NOT Stable Diffusion. Its training data likely predates the release of Stable Diffusion.

Luckily, it knows what **text-to-image models** and **DALL·E** are (You can verify). So we can piggy-back on them in our prompt engineering.

To start using ChatGPT, go to [chat.openai.com](http://chat.openai.com/). Type a question in the input box at the bottom to start a conversation.

![ChatGPT dialog page. Get Stable Diffusion prompts.](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-48.png?resize=480%2C305&ssl=1)

ChatGPT page.

ChatGPT is aware of the history of your current conversation. Press “+ New Chat” button on the left panel to start a new conversation.

## Asking for Prompts

I am going to test ChatGPT by asking prompts for illustration portrait, one of the hardest to get right. Let’s see how it does.

### Close-up Illustration

There are **three important techniques** to tease out high-quality prompts for Stable Diffusion from ChatGPT:

- **Specify image style**. You need to ask for a specific kind of image. In my example, I will ask for “photorealistic close-up illustration”.
- **Fix the subject**. I will fix the subject as the actress “Ana de Armas”. I am not (too) obsessed with Ana de Armas. Reason for doing this is actress name is a strong keyword. Not only will it change the face (intended) but it will also heavily influence the style (not intended). If the subject is not fixed, ChatGPT will use a different actress in each prompt. The style and composition can be changed simply due to that.
- **Prime with examples**. Finally, give two example prompts.

Putting these together, the ChatGPT prompt is

> Examples of high quality prompt for stunning close-up photorealistic illustration of Ana de Armas for text-to-image models (Stable Diffusion, midjourney or Dalle2) are
>
>–portrait of beautiful happy young ana de armas, ethereal, realistic anime, trending on pixiv, detailed, clean lines, sharp lines, crisp lines, award winning illustration, masterpiece, 4k, eugene de blaas and ross tran, vibrant color scheme, intricately detailed
>
>–alberto seveso and geo2099 style, A highly detailed and hyper realistic portrait of a gorgeous young ana de armas, lisa frank, trending on artstation, butterflies, floral, sharp focus, studio photo, intricate details, highly detailed, by Tvera and wlop and artgerm
>
> Give me more examples.

ChatGPT’s response:

> - A stunning close-up illustration of Ana de Armas in a dramatic, dark and moody style, inspired by the work of Simon Stålenhag, with intricate details and a sense of mystery.
> - A photorealistic, highly detailed illustration of Ana de Armas in a vintage Hollywood style, reminiscent of the golden age of cinema, with a focus on glamour and elegance.
> - A close-up illustration of Ana de Armas in a neo-noir style, reminiscent of the film noir genre, with a focus on shadows, contrasts, and a sense of danger.

Let’s put these prompts in [Stable Diffusion v1.5](https://stable-diffusion-art.com/models/#Stable_diffusion_v15). I will use 25 steps of DPM++ 2M Karras sampler, CFG scale 7, image size 512×704. I will use the following [universal negative prompt](https://stable-diffusion-art.com/how-to-use-negative-prompts/).

> ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, bad anatomy, watermark, signature, cut off, low contrast, underexposed, overexposed, bad art, beginner, amateur, distorted face

**ChatGPT Prompt #1**: A stunning close-up illustration of Ana de Armas in a **dramatic, dark and moody** style, inspired by the work of Simon Stålenhag, with intricate details and a sense of mystery.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/03892-3783748869-A-stunning-close-up-illustration-of-Ana-de-Armas-in-a-dramatic-dark-and-moody-style-inspired-by-the-work-of-Simon-Stalenhag-w.png?resize=480%2C660&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/03889-3783748866-A-stunning-close-up-illustration-of-Ana-de-Armas-in-a-dramatic-dark-and-moody-style-inspired-by-the-work-of-Simon-Stalenhag-w.png?resize=480%2C660&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/03895-1055889230-A-stunning-close-up-illustration-of-Ana-de-Armas-in-a-dramatic-dark-and-moody-style-inspired-by-the-work-of-Simon-Stalenhag-w.png?resize=480%2C660&ssl=1)

**ChatGPT Prompt #2**: A photorealistic, highly detailed illustration of Ana de Armas in a **vintage Hollywood style**, reminiscent of the golden age of cinema, with a focus on glamour and elegance.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/03903-2685639187-A-photorealistic-highly-detailed-illustration-of-Ana-de-Armas-in-a-vintage-Hollywood-style-reminiscent-of-the-golden-age-of-ci.png?resize=480%2C660&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/03899-3581820967-A-photorealistic-highly-detailed-illustration-of-Ana-de-Armas-in-a-vintage-Hollywood-style-reminiscent-of-the-golden-age-of-ci.png?resize=480%2C660&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/03898-3581820966-A-photorealistic-highly-detailed-illustration-of-Ana-de-Armas-in-a-vintage-Hollywood-style-reminiscent-of-the-golden-age-of-ci.png?resize=480%2C660&ssl=1)

**ChatGPT Prompt #3**: A close-up illustration of Ana de Armas in a **neo-noir style**, reminiscent of the film noir genre, with a focus on shadows, contrasts, and a sense of danger.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/03924-3350896149-A-close-up-illustration-of-Ana-de-Armas-in-a-neo-noir-style-reminiscent-of-the-film-noir-genre-with-a-focus-on-shadows-contra.png?resize=480%2C660&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/03918-1508399388-A-close-up-illustration-of-Ana-de-Armas-in-a-neo-noir-style-reminiscent-of-the-film-noir-genre-with-a-focus-on-shadows-contra.png?resize=480%2C660&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/03917-1508399387-A-close-up-illustration-of-Ana-de-Armas-in-a-neo-noir-style-reminiscent-of-the-film-noir-genre-with-a-focus-on-shadows-contra.png?resize=480%2C660&ssl=1)

These are all good stuffs! I am pleasantly surprised by how creative the prompts are, and how diverse the styles it gives.

And I surely learned some new keywords that I am going to put in the [prompt generator](https://andrewongai.gumroad.com/l/stable_diffusion_prompt_generator).

### Full-body Illustration

Now let’s refine the ChatGPT prompt to tease out prompts for **full-body portrait**. All you need to do is to add “full-body” in your question and prompt examples.

> Examples of high quality prompt for stunning photorealistic **full body** illustration of ana de armas for text-to-image models (Stable Diffusion, midjourney or Dalle2) are
>
> - full body portrait of beautiful happy young ana de armas, ethereal, realistic anime, trending on pixiv, detailed, clean lines, sharp lines, crisp lines, award winning illustration, masterpiece, 4k, eugene de blaas and ross tran, vibrant color scheme, intricately detailed
> - full body portrait of a gorgeous young ana de armas, A highly detailed and hyper realistic lisa frank, trending on artstation, butterflies, floral, sharp focus, studio photo, intricate details, highly detailed, by Tvera and wlop and artgerm, alberto seveso and geo2099 style,
>
>     Give me more examples
>

There are the prompts ChatGPT generated.

**ChatGPT Prompt #**4: Full body illustration of Ana de Armas in a stunning red dress, posing elegantly against a beautiful sunset background, with realistic lighting and shadows, by a master digital artist known for their photorealistic style, such as Jomaro Kindred or Gleb Alexandrov

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/03985-553253989-Full-body-illustration-of-Ana-de-Armas-in-a-stunning-red-dress-posing-elegantly-against-a-beautiful-sunset-background-with-rea.png?resize=480%2C660&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/03983-168510972-Full-body-illustration-of-Ana-de-Armas-in-a-stunning-red-dress-posing-elegantly-against-a-beautiful-sunset-background-with-rea.png?resize=480%2C660&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/03981-168510970-Full-body-illustration-of-Ana-de-Armas-in-a-stunning-red-dress-posing-elegantly-against-a-beautiful-sunset-background-with-rea.png?resize=480%2C660&ssl=1)

**ChatGPT Prompt #**5: A full body illustration of Ana de Armas as a powerful warrior queen, with intricate armor and weapons, in a dynamic and action-packed pose, rendered in a highly detailed and photorealistic style by top fantasy artists such as Simon Stålenhag or Jora Vision

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/03989-939795629-A-full-body-illustration-of-Ana-de-Armas-as-a-powerful-warrior-queen-with-intricate-armor-and-weapons-in-a-dynamic-and-action-.png?resize=480%2C660&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/03998-229608173-A-full-body-illustration-of-Ana-de-Armas-as-a-powerful-warrior-queen-with-intricate-armor-and-weapons-in-a-dynamic-and-action-.png?resize=480%2C660&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/03999-229608174-A-full-body-illustration-of-Ana-de-Armas-as-a-powerful-warrior-queen-with-intricate-armor-and-weapons-in-a-dynamic-and-action-.png?resize=480%2C660&ssl=1)

**ChatGPT Prompt #6**: A full body illustration of Ana de Armas as a sultry and mysterious sorceress, with detailed and realistic clothing and accessories, in a dramatic and captivating pose, by leading fantasy and sci-fi artists such as Yoshitaka Amano or Dave Rapoza.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/04003-17444026-A-full-body-illustration-of-Ana-de-Armas-as-a-sultry-and-mysterious-sorceress-with-detailed-and-realistic-clothing-and-accessor.png?resize=480%2C660&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/04012-1527840054-A-full-body-illustration-of-Ana-de-Armas-as-a-sultry-and-mysterious-sorceress-with-detailed-and-realistic-clothing-and-accessor.png?resize=480%2C660&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/04013-3504716504-A-full-body-illustration-of-Ana-de-Armas-as-a-sultry-and-mysterious-sorceress-with-detailed-and-realistic-clothing-and-accessor.png?resize=480%2C660&ssl=1)

These are good, stylish full-body portraits!

### Ask for More

If you like a particular prompt ChatGPT gave, you can ask for more by something like

> I like the third one. Can you give me more examples like that?

ChatGPT will give you more variants of the same style.

## Summary

Can ChatGPT generate high-quality prompts for Stable Diffusion? The answer is a solid YES. But you need to follow these three guidelines: (1) Specify the image style, (2) fix the subject, and (3) prime with examples.

ChatGPT is still free to use as of time of writing. Go generate some prompts before they start charging!

---

#AI #article
