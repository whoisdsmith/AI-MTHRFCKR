---
created: 2023-01-30T16:25:17 (UTC -05:00)
tags: []
source: https://stable-diffusion-art.com/fine-tune-your-ai-images-with-these-simple-prompting-techniques/
author: 
---

# Fine-tune Your AI Images With These Simple Prompting Techniques - Stable Diffusion Art

> ## Excerpt
> Generated a Stable Diffusion AI image but not quite what you want? In this article, I will teach you a few simple prompt techniques to let you dial-in your

---

Generated a Stable Diffusion AI image but not quite what you want? In this article, I will teach you a few simple prompt techniques to let you dial-in your images.

Contents \[[hide](https://stable-diffusion-art.com/fine-tune-your-ai-images-with-these-simple-prompting-techniques/#)\]

- [Stable Diffusion Software](https://stable-diffusion-art.com/fine-tune-your-ai-images-with-these-simple-prompting-techniques/#Stable_Diffusion_Software)
- [Adjust keyword strength with () and \[\]](https://stable-diffusion-art.com/fine-tune-your-ai-images-with-these-simple-prompting-techniques/#Adjust_keyword_strength_with_and)
- [Adjust keyword strength using weight](https://stable-diffusion-art.com/fine-tune-your-ai-images-with-these-simple-prompting-techniques/#Adjust_keyword_strength_using_weight)
- [Use \[\] to suppress unwanted objects](https://stable-diffusion-art.com/fine-tune-your-ai-images-with-these-simple-prompting-techniques/#Use_to_suppress_unwanted_objects)
- [Suppress unwanted objects with negative prompts](https://stable-diffusion-art.com/fine-tune-your-ai-images-with-these-simple-prompting-techniques/#Suppress_unwanted_objects_with_negative_prompts)
- [Blend two keywords](https://stable-diffusion-art.com/fine-tune-your-ai-images-with-these-simple-prompting-techniques/#Blend_two_keywords)
- [Summary](https://stable-diffusion-art.com/fine-tune-your-ai-images-with-these-simple-prompting-techniques/#Summary)

## Stable Diffusion Software

We will use [this](https://github.com/AUTOMATIC1111/stable-diffusion-webui) Stable Diffusion GUI for this tutorial. See my [quick start guide](https://andrewongai.gumroad.com/l/stable_diffusion_quick_start) for setting up in Google’s cloud server. Note that many of the techniques outlined in this article only works on this software.

## Adjust Keyword Strength with () and \[\]

Use `()` to increase the weight of a keyword. Use `[]` to decrease. Below is a famous example taken from Web UI’s [feature showcase](https://github.com/AUTOMATIC1111/stable-diffusion-webui-feature-showcase). This is the original image:

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/sdprompt_egg_and_bacon.jpg?resize=374%2C512&ssl=1)

Starting image with equal amount of eggs and bacons.

You can increase the emphasis of egg in the image by adding `()` to the keyword **egg**:

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/sdprompt_more_egg_and_bacon.jpg?resize=480%2C224&ssl=1)

Generate more eggs by putting () around “eggs”.

Likewise, you can do the same for **bacon**:

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/sdprompt_egg_and_more_bacon.jpg?resize=480%2C216&ssl=1)

Generate more bacons by putting () around “bacons”.

As you can see, the more weight you put on a keyword, the more bias the image towards the keyword. The effect of multiple parenthesis is multiplicative. Each parenthesis represents 1.1 times increase in weight. In other words:

> (keyword): 1.1  
> ((keyword)): 1.21  
> (((keyword))): 1.33

Similarly, the effect of multiple brackets is

> \[keyword\]: 0.9  
> \[\[keyword\]\]: 0.81  
> \[\[\[keyword\]\]\]: 0.73

## Adjust Keyword Strength Using Weight

In AUTOMATIC1111 GUI, instead of using brackets, you can assign a weight to a keyword directly. The syntax is

> (keyword: weight)

For example, the followings are equivalent

> (keyword)  
> ((keyword))  
> (((keyword)))

> (keyword: 1.1)  
> (keyword: 1.21)  
> (keyword: 1.33)

The weight can also be negative to replace the usage of square brackets.

## Use \[\] to Suppress Unwanted Objects

Celebrity time is a strong effect. Some names are strongly associated with certain objects. For example, Steve Jobs is highly associated with the Apple logo (see image example below) because they often appear together in the training data.

What if you just want to generate a portrait of Steve Jobs? One method is to generate a lot of them. By shear chance, you will get an image you want AND without the Apple logo. But this could unnecessarily take up resources. Alternatively, you can suppress the keyword *Steve Jobs* to reduce the chance of generating the Apple logo, an association, in the hope that the main effect, Steve Jobs, still remains. You would usually need to play with how many `[]` to achieve the desired effect.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/sdprompt_steve_jobs2.png?resize=480%2C483&ssl=1)

Steve Jobs is highly correlated with the Apple logo.

## Suppress Unwanted Objects with Negative Prompts

Another way to suppress objects or styles you do not want is to use **negative prompts**. In fact, many practitioners use boilerplate negative prompts. Below is an example for portraits.

> ((((ugly)))), (((duplicate))), ((morbid)), ((mutilated)), \[out of frame\], extra fingers, mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))), out of frame, ugly, extra limbs, (bad anatomy), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck)))

All you need to do is to list *everything* you do not want to see.

## Blend Two Keywords

Want to blend two faces? Keyword swapping is designed for that. In fact, this is an important technique to create new looks. Celebrity name is a strong effect. By using names of actors and actresses, it is easy to generate good-looking faces. But the downside is the faces are too recognizable. Everyone can tell who he or she was, and you lost novelty. Keyword swapping allows you to blend two readily recognizable faces together to form a new one.

Use syntax

> \[person1 : person2: amount\]

to blend two faces at different degree. Below is an example

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/sdprompt_more_joe_and_trump-1.jpg?resize=480%2C196&ssl=1)

Blending two keywords to mix two faces.

The last number ranges from 0 to 1. As an example, if the number of sampling steps is 40, specifying amount = 0.75 swaps the keyword `joe biden` to `donald trump` at step 40\*0.75=30 steps.

This technique can be used to generate novel faces. Below is an example.

\[Emma Watson: Amber heard: 0.85\], 40 steps:

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/sdprompt_emma_watson_ember_heard.png?resize=480%2C480&ssl=1)

Blending Emma Watson and Amber Heard.

Full prompt is

> \[Emma Watson: Amber heard: 0.85\],((Victorian)) , Feminine,((Perfect Face)), ((arms outstretched above head)), ((Aype Beven)), ((scott williams)) ((jim lee)),((Leinil Francis Yu)), ((Salva Espin)), ((oil painting)), ((Matteo Lolli)), ((Sophie Anderson)), ((Kris Anka)), (Intricate),(High Detail), (bokeh)

You can go one step further and blend 4 names together:

\[Evan Rachel Wood: Jennifer Lawrence: 0.75\], \[Jennifer Aniston: Jennifer Connelly: 0.85\], 40 steps:

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/sdprompt_4actresses.png?resize=480%2C480&ssl=1)

Blending Evan Rachel Wood, Jennifer Lawrence, Jennifer Aniston and Jennifer Connelly.

Full prompt:

> \[Evan Rachel Wood: Jennifer Lawrence: 0.75\], \[Jennifer Aniston: Jennifer Connelly: 0.85\], Feminine,((Perfect Face)), ((arms outstretched above head)), ((Aype Beven)), ((scott williams)) ((jim lee)),((Leinil Francis Yu)), ((Salva Espin)), ((oil painting)), ((Matteo Lolli)), ((Sophie Anderson)), ((Kris Anka)), (Intricate),(High Detail), (bokeh)

You got the idea. This technique allows you to generate novel faces with precise facial features you want. Just pick the celebrities with certain looks and blend them together with keyword swapping!

## Summary

We have gone through techniques to control image generation by adjusting strength of keywords, adding negative keywords and blending keywords. These are invaluable tools to dial-in your image. Hope you find these techniques useful. In the next post, I will cover how to redraw an area of the image with *inpainting*. Stay tuned!

---

#AI #article
