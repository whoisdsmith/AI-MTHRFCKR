---
created: 2023-01-30T16:26:49 (UTC -05:00)
tags: []
source: https://stable-diffusion-art.com/how-to-use-negative-prompts/
author: 
---

# How to Use Negative Prompts? - Stable Diffusion Art

> ## Excerpt
> Negative prompt gives you an additional way to control text-to-image generation. Many people treat it as an optional feature in Stable Diffusion 1.4 or 1.5

---

Negative prompt gives you an additional way to control text-to-image generation. Many people treat it as an optional feature in Stable Diffusion 1.4 or 1.5 models. Things changed with release of Stable Diffusion v2. Negative prompt becomes indispensable.

In this post, I will walkthrough a few use cases of negative prompt including modifying contents and modifying style. Then I will demonstrate the importance of negative prompts in v2 models. I will demonstrate how to search for a **universal negative prompt**.

*This is the second part of a series on negative prompt. Read the first part: [How does negative prompt work](https://stable-diffusion-art.com/how-negative-prompt-work/).*

Contents \[[hide](https://stable-diffusion-art.com/how-to-use-negative-prompts/#)\]

- [Enter negative prompt](https://stable-diffusion-art.com/how-to-use-negative-prompts/#Enter_negative_prompt)
- [Use cases](https://stable-diffusion-art.com/how-to-use-negative-prompts/#Use_cases)
    - [Removing things](https://stable-diffusion-art.com/how-to-use-negative-prompts/#Removing_things)
    - [Modifying images](https://stable-diffusion-art.com/how-to-use-negative-prompts/#Modifying_images)
    - [Negative prompt with keyword switching](https://stable-diffusion-art.com/how-to-use-negative-prompts/#Negative_prompt_with_keyword_switching)
    - [Modifying styles](https://stable-diffusion-art.com/how-to-use-negative-prompts/#Modifying_styles)
        - [Sharpening](https://stable-diffusion-art.com/how-to-use-negative-prompts/#Sharpening)
        - [Photorealistic](https://stable-diffusion-art.com/how-to-use-negative-prompts/#Photorealistic)
- [Negative prompt is important for v2 models](https://stable-diffusion-art.com/how-to-use-negative-prompts/#Negative_prompt_is_important_for_v2_models)
    - [Negative prompt with Stable Diffusion v2.1](https://stable-diffusion-art.com/how-to-use-negative-prompts/#Negative_prompt_with_Stable_Diffusion_v21)
    - [Negative prompt with Stable Diffusion v1.5](https://stable-diffusion-art.com/how-to-use-negative-prompts/#Negative_prompt_with_Stable_Diffusion_v15)
    - [Why does negative prompt become more important in v2?](https://stable-diffusion-art.com/how-to-use-negative-prompts/#Why_does_negative_prompt_become_more_important_in_v2)
- [Boilerplate negative prompts in v2 model](https://stable-diffusion-art.com/how-to-use-negative-prompts/#Boilerplate_negative_prompts_in_v2_model)
    - [Search for a good negative prompt](https://stable-diffusion-art.com/how-to-use-negative-prompts/#Search_for_a_good_negative_prompt)
    - [Universal negative prompt](https://stable-diffusion-art.com/how-to-use-negative-prompts/#Universal_negative_prompt)
    - [Photograph style](https://stable-diffusion-art.com/how-to-use-negative-prompts/#Photograph_style)
    - [Amine style](https://stable-diffusion-art.com/how-to-use-negative-prompts/#Amine_style)
    - [Oil painting style](https://stable-diffusion-art.com/how-to-use-negative-prompts/#Oil_painting_style)
    - [Conclusion](https://stable-diffusion-art.com/how-to-use-negative-prompts/#Conclusion)

## Enter Negative Prompt

Many Stable Diffusion GUI or web services offer negative prompts. In AUTOMATIC1111 (install instruction [here](https://stable-diffusion-art.com/install-windows/)), you enter negative prompt right under where you put in the prompt.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-10.png?resize=480%2C221&ssl=1)

Negative prompt input box in AUTOMATIC1111

However, don’t be surprised if you cannot find a way to enter negative prompt in other GUI or services. It was an unofficial feature in v1 model.

## Use Cases

I will go through a few examples of using negative prompts, so you can get some idea what can be done and how to tweak it. I will be using the [v1.5 base model](https://stable-diffusion-art.com/models/#Stable_diffusion_v15) in this section but the techniques are applicable to v2 models.

### Removing Things

The first obvious usage is to remove anything you don’t want to see in the image. Let’s say you have generated a painting of Paris in a rainy day.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/00993-1923936260-autumn-in-paris-ornate-beautiful-atmosphere-vibe-mist-smoke-fire-chimney-rain-wet-pristine-puddles-melting-drippin.png?resize=480%2C320&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/00993-1923936260-autumn-in-paris-ornate-beautiful-atmosphere-vibe-mist-smoke-fire-chimney-rain-wet-pristine-puddles-melting-drippin/)

**Prompt**: autumn in paris, ornate, beautiful, atmosphere, vibe, mist, smoke, fire, chimney, rain, wet, pristine, puddles, melting, dripping, snow, creek, lush, ice, bridge, forest, roses, flowers, by stanley artgerm lau, greg rutkowski, thomas kindkade, alphonse mucha, loish, norman rockwell. **Seed**: 1923936260

You want to generate another one but an empty street. What you can do is to use the same [seed value](https://stable-diffusion-art.com/know-these-important-parameters-for-stunning-ai-images/#Seed), which specifies the image, and add the negative prompt “people”. You get an image with most people removed.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/01003-1923936260-autumn-in-paris-ornate-beautiful-atmosphere-vibe-mist-smoke-fire-chimney-rain-wet-pristine-puddles-melting-drippin.png?resize=480%2C320&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/01003-1923936260-autumn-in-paris-ornate-beautiful-atmosphere-vibe-mist-smoke-fire-chimney-rain-wet-pristine-puddles-melting-drippin/)

Adding negative prompt “people” but keeping the same prompt and seed.

Note that the scene is very similar but not completely the same as the original one. If you really **need** the original one, you will need to use [inpainting](https://stable-diffusion-art.com/inpainting_basics/) to painstakingly removing the people while keeping the scene coherent.

You may have noticed that there’s one person left in the above image. You can tell Stable Diffusion to try harder by adding [emphasis](https://stable-diffusion-art.com/fine-tune-your-ai-images-with-these-simple-prompting-techniques/#Adjust_keyword_strength_using_weight) to the negative prompt `(people:1.3)`. That tells Stable Diffusion that the keyword `people` is 30% more important now.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-12.png?resize=480%2C320&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/image-12-3/)

Adding 30% more emphasis to negative prompt `people` removes the last person.

Keep in mind that while you can use keyword emphasis in [AUTOMATIC1111](https://stable-diffusion-art.com/install-windows/), it is not universally supported by all services. Be sure to check with the one you are using before writing me an angry email…

### Modifying Images

You can nudge Stable Diffusion to make subtle changes with negative prompts. You don’t exactly want to remove anything but to make slight changes to the subjects.

Let’s work on this base image:

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/base.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/base/)

**Prompt**: emma watson as nature magic celestial, top down pose, long hair, soft pink and white transparent cloth, space, D&D, shiny background, intricate, elegant, highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustration, artgerm, bouguereau. **Seed**: 479804672

Looks like it’s windy and the hairs are floating. Let’s use the **negative prompt “windy” to keep the hair down**.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/neg-windy.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/neg-windy/)

Adding negative prompt “windy” keeps the hair down.

Emma in the original image looked a bit… underdeveloped. Using the **negative prompt “underage” makes her look more adult-like**.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/neg-underage.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/neg-underage/)

Negative prompt: underage.

What if we are ok with the wind but want the hair to cover the ear? Let’s add **negative prompt “ear”** with different emphasis factors. Below are with three increasing emphasis 1.3, 1.6 and 1.9.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/neg-ear-1.3.png?resize=300%2C300&ssl=1)

(ear:1.3)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/neg-ear-1.6.png?resize=300%2C300&ssl=1)

(ear:1.6)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/neg-ear-1.9.png?resize=300%2C300&ssl=1)

(ear:1.9)

The ears are covered more by hair with in all emphasis factors but when the factor reaches 1.9, the composition of the image changed. Negative prompt could affect the diffusion process strongly.

### Negative Prompt with Keyword Switching

**Now what if you really want to use a high emphasis `(ear:1.9)`?** I don’t know what’s your problem with ears but I have a trick for you. You can use [keyword switching](https://stable-diffusion-art.com/fine-tune-your-ai-images-with-these-simple-prompting-techniques/#Blend_two_keywords) to first use a meaningless word as negative prompt, and then switching to `(ear:1.9)` at a later sampling step.

Let’s pick `the` as the meaningless, dud negative prompt. You can verify its uselessness by putting it in the negative prompt. You will get the same image as if you didn’t put anything. Now use this as negative prompt:

> \[the: (ear:1.9): 0.5\]

Since, I am using 20 sampling steps, what this means is using `the` as the negative prompt in steps 1–10, and `(ear:1.9)` in steps 11-20.

The reasoning behind this is that the diffusion process is most important in the beginning steps. Later steps are only finer adjustment to details, such as hairs covering ears.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-13.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/image-13-3/)

Switching to the negative prompt only at a later step.

Now what we have accomplished is nothing short of amazing.

- We can now use the much stronger emphasis `(ear:1.9)` without changing the composition.
- We get an image much closer to the original one.
- The ear is covered.

### Modifying Styles

Negative prompts are not only useful for modifying the content but also modifying the style. Why use negative prompt to change style? Sometimes adding too much to positive prompt just confuses the diffuser. Imagine someone tell you to go to 77 (the token limit) places at the same time. It helps if they tell you what areas to **avoid** instead.

#### Sharpening

Instead of using keywords “sharp”, ‘focused’ in prompt, you can use **“blurry”** in the negative prompt. The image does gets sharper.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/neg-blurry.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/neg-blurry/)

Using “blurry” in negative prompt sharpens the image.

#### Photorealistic

Using the **negative prompt `painting, cartoon`** makes it more photo-like.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/neg-painting-cartoon.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/neg-painting-cartoon/)

If you want to keep the original composition, you can experiment with keyword switching I mentioned earlier. Using `[the: (painting cartoon:1.9): 0.3]` we get:

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-14.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/image-14-3/)

It’s much closer to the original but with added photorealism style.

## Negative Prompt is Important for v2 Models

### Negative Prompt with Stable Diffusion v2.1

Consistent with [Max Woolf’s finding](https://minimaxir.com/2022/11/stable-diffusion-negative-prompt/), my own experience is that negative prompt is very important for v2 models. Below I used the positive prompt for generating [realistic humans](https://stable-diffusion-art.com/realistic-human-street-portrait/) but with Stable Diffusion 2.1 model.

> a young female, highlights in hair, sitting outside restaurant, brown eyes, wearing a dress, side light

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-4.png?resize=480%2C277&ssl=1)](https://stable-diffusion-art.com/how-negative-prompt-work/image-4-3/)

Stable Diffusion 2.1. Adding more negative prompts improve images.

Adding just two to three negative prompts progressively improves the aesthetic of the images. I would say this is pretty near the quality of v1 models.

### Negative Prompt with Stable Diffusion v1.5

Let’s repeat the exercise on [v1.5 model](https://stable-diffusion-art.com/models/#Stable_diffusion_v15).

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-5.png?resize=480%2C285&ssl=1)](https://stable-diffusion-art.com/how-negative-prompt-work/image-5-3/)

Adding negative prompt to v1.5. Improvements are not clear.

The images comes out pretty good without any negative prompts in v1.5. Adding the negative prompt `ugly, deformed and disfigured` **may** improve things but it is not as clear as in v2.1. It is as if v1.5 model does not understand these words.

### Why Does Negative Prompt Become More Important in v2?

This is an area I can only speculate… but why not? The two [changes in v2](https://stable-diffusion-art.com/how-stable-diffusion-work/#Stable_Diffusion_v1_vs_v2) are

1. Use a larger OpenCLIP language model.
2. Filtered out NSFW contents in training data.

The first suspect is switching from Open AI’s CLIP model to OpenCLIP. This affects the [embeddings](https://stable-diffusion-art.com/how-stable-diffusion-work/#Embedding) of the model. Open AI trained the CLIP model with proprietary data. If the data is highly curated that every single person looks way above average, prompting “woman” would be the same as prompting “beautiful woman”. That would make prompting easier.

My second speculation is that what are deemed NSFW could also be highly aesthetic. It could be a failure of the filter, or its just be the nature of the NSFW images. Excluding NSFW images also unintentionally biases the data towards the bad and ugly.

## Boilerplate Negative Prompts in v2 Model

We have already touched on the importance of negative prompts in v2. Now let’s find a good universal negative prompt.

### Search for a Good Negative Prompt

I will use [2.1 model](https://stable-diffusion-art.com/install-stable-diffusion-2-1/) (512-pixel) for this test. The originals without negative prompt are

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/grid-0611.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/grid-0611/)

Originals.

Not bad, but could be improved. Using our minimalist negative prompt, we immediately see improvements:

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/ugly-disfigured-deformed.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/ugly-disfigured-deformed/)

**Negative prompt:** ugly, disfigured, deformed

Adding `underexposed` and `overexposed` helps to make the images less flat.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-16.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/image-16-3/)

**Negative prompt**: underexposed, overexposed, ugly, disfigured, deformed.

It doesn’t hurt to add `low contrast`.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-17.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/image-17-3/)

**Negative prompt**: low contrast, underexposed, overexposed, ugly, disfigured, deformed

Next, let’s test this popular negative prompt for v2 floating around on the internet:

> ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, blurry, bad anatomy, blurred, watermark, grainy, signature, cut off, draft

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-18.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/image-18-3/)

I think it’s doing a decent job although it may have modified the style slightly. This could be caused by the negative keywords `blurry, blurred, grainy, draft`. Some styles could look just that. Deleting these keywords seems to get back closer to the original style.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-19.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/image-19-3/)

**Negative prompt**: ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, bad anatomy, watermark, signature, cut off

Next, add the lighting keywords we just used (`low contrast, underexposed, overexposed`). It does help the contrast and dynamic range.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-20.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/image-20-3/)

**Negative prompt:** ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, bad anatomy, watermark, signature, cut off, low contrast, underexposed, overexposed

Now adding a few more negative keywords to avoid sampling bad art or newbies drawings, we arrive at the last negative prompt below. **This is a pretty decent boilerplate negative prompt without affecting styles.**

> ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, bad anatomy, watermark, signature, cut off, low contrast, underexposed, overexposed, bad art, beginner, amateur, distorted face

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-21.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/image-21-3/)

This is a huge improvement over the without negative prompts. You may want to take out low contrast, underexpose or overexpose if it is the style.

### Universal Negative Prompt

We will put the **universal negative prompt for v2** we just found to a battery of test to see how well it performs. As a recap, the universal negative prompt is

> **ugly, tiling, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, disfigured, deformed, body out of frame, bad anatomy, watermark, signature, cut off, low contrast, underexposed, overexposed, bad art, beginner, amateur, distorted face**

### Photograph Style

Prompt:

> A man walking around her neighborhood, highlight hair, detailed eyes, sharp focus, young face, perfect symmetric face, pupil reflecting surroundings, realistic skin, soft healthy skin

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/03597-173725244-A-man-walking-around-her-neighborhood-highlight-hair-detailed-eyes-sharp-focus-young-face-perfect-symmetric-face-pupil-ref.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/03597-173725244-a-man-walking-around-her-neighborhood-highlight-hair-detailed-eyes-sharp-focus-young-face-perfect-symmetric-face-pupil-ref/)

Without negative prompt.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/03593-173725244-A-man-walking-around-her-neighborhood-highlight-hair-detailed-eyes-sharp-focus-young-face-perfect-symmetric-face-pupil-ref.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/03593-173725244-a-man-walking-around-her-neighborhood-highlight-hair-detailed-eyes-sharp-focus-young-face-perfect-symmetric-face-pupil-ref/)

With negative prompt.

The universal negative prompt works nicely with photograph style image. The guy looks a league higher and definitely had spent more time on his hair in the morning…

### Amine Style

Prompt:

> anime style girl on battleground, holding a ninja sword, detailed eyes, perfect face

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-22.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/image-22-3/)

Without negative prompt.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/03611-173725246-anime-style-girl-on-battleground-holding-a-ninja-sword-detailed-eyes-perfect-face.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/03611-173725246-anime-style-girl-on-battleground-holding-a-ninja-sword-detailed-eyes-perfect-face/)

With negative prompt.

The universal negative prompt helped characters equally well in anime style. The subject stands better, more handsome, and more ready to fight as it seems. The ninja sword is straighten up and looks more dangerous.

### Oil Painting Style

> impressionist oil painting of a young man standing right next to a red tesla roadster by john sargent

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-23.png?resize=480%2C375&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/image-23-3/)

Without negative prompt.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/03665-4036291972-impressionist-oil-painting-of-a-young-man-standing-right-next-to-a-red-tesla-roadster-by-john-sargent.png?resize=480%2C375&ssl=1)](https://stable-diffusion-art.com/how-to-use-negative-prompts/03665-4036291972-impressionist-oil-painting-of-a-young-man-standing-right-next-to-a-red-tesla-roadster-by-john-sargent/)

With negative prompt.

The universal negative prompt helps both the Tesla and the guy. Instead of showing a flat-tired beat-up car with a troubled teenager, now it shows a shinny new car with a young man who looks a million bucks.

### Conclusion

Looks like this v2 universal negative prompt works well under variety of styles! This concludes our two-part series of negative prompt.

---

#AI #article
