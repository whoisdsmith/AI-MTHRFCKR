---
created: 2023-01-30T16:25:24 (UTC -05:00)
tags: []
source: https://stable-diffusion-art.com/how-to-come-up-with-good-prompts-for-ai-image-generation/
author: 
---

# How to Come up with Good Prompts for Stable Diffusion - Stable Diffusion Art

> ## Excerpt
> In this post, I’ll teach you how to create good prompts for generating AI art work images for Stable Diffusion.

---

In this post, I’ll teach you how to create good prompts for generating AI art work images for Stable Diffusion.

This is part 2 of the beginner’s guide series.  
Read part 1: [Absolute beginner’s guide](https://stable-diffusion-art.com/beginners-guide/).  
Read part 3: [Inpainting](https://stable-diffusion-art.com/inpainting_basics/).  
Read part 4: [Models](https://stable-diffusion-art.com/models/).

Contents \[[hide](https://stable-diffusion-art.com/how-to-come-up-with-good-prompts-for-ai-image-generation/#)\]

- [What is Stable Diffusion?](https://stable-diffusion-art.com/how-to-come-up-with-good-prompts-for-ai-image-generation/#What_is_Stable_Diffusion)
    - [Where can I try my prompts?](https://stable-diffusion-art.com/how-to-come-up-with-good-prompts-for-ai-image-generation/#Where_can_I_try_my_prompts)
- [Anatomy of a good prompt](https://stable-diffusion-art.com/how-to-come-up-with-good-prompts-for-ai-image-generation/#Anatomy_of_a_good_prompt)
- [Tips for good prompts](https://stable-diffusion-art.com/how-to-come-up-with-good-prompts-for-ai-image-generation/#Tips_for_good_prompts)
- [Some good keywords for you](https://stable-diffusion-art.com/how-to-come-up-with-good-prompts-for-ai-image-generation/#Some_good_keywords_for_you)
    - [Medium](https://stable-diffusion-art.com/how-to-come-up-with-good-prompts-for-ai-image-generation/#Medium)
    - [Style](https://stable-diffusion-art.com/how-to-come-up-with-good-prompts-for-ai-image-generation/#Style)
    - [Artist](https://stable-diffusion-art.com/how-to-come-up-with-good-prompts-for-ai-image-generation/#Artist)
    - [Website](https://stable-diffusion-art.com/how-to-come-up-with-good-prompts-for-ai-image-generation/#Website)
    - [Resolution](https://stable-diffusion-art.com/how-to-come-up-with-good-prompts-for-ai-image-generation/#Resolution)
    - [Additional details](https://stable-diffusion-art.com/how-to-come-up-with-good-prompts-for-ai-image-generation/#Additional_details)
    - [Color](https://stable-diffusion-art.com/how-to-come-up-with-good-prompts-for-ai-image-generation/#Color)
- [Summary](https://stable-diffusion-art.com/how-to-come-up-with-good-prompts-for-ai-image-generation/#Summary)

## What is Stable Diffusion?

Stable Diffusion is a text-to-image AI model. It is trained on millions of image and text description pairs found on the internet. Because it has seen so much, the model understands what text description associates with what images.

As a result, if you put in a prompt like “A Photo of a cat sitting on top of a building”, it would give you images like these:

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/stablediffusion_cat.png?resize=480%2C272&ssl=1)

Cat images generated with Stable Diffusion.

You may be thinking what’s the big deal? Couldn’t we get millions of them in a Google search? What’s intriguing about this technology is that you can **prompt** the model to generate high quality images that **do not exist before**. For example, you can ask for a portrait painting of Emma Watson by the 19th century American painter [John Singer Sargent](https://www.johnsingersargent.org/):

![Prompt stable diffusion to generate portrait of Emma Watson in John Sargent's style.](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/stablediffusion_john_sargent_emma_watson.png?resize=480%2C273&ssl=1)

John Sargent’s painting of Emma Watson.

It is incredible that such images can be produced from keyword-pixel correlations! What’s mind-boggling is that it gets the artistic style, faces (which our brains are very unforgiving of tiny mistakes) and shadows correct, and blends them all together in an aesthetically pleasing manner. The wonder of large numbers is beyond the comprehension of human minds.

### Where Can I Try My Prompts?

Check out our list of [free sites](https://stable-diffusion-art.com/free-ai-image-generator-sites/) offering free images generations. Read the [Quick Start Guide](https://andrewongai.gumroad.com/l/stable_diffusion_quick_start) for other setups.

## Anatomy of a Good Prompt

There are proven techniques to generate high quality, specific images. Your prompt should cover most if not all of these areas

1. Subject (required)
2. Medium
3. Style
4. Artist
5. Website
6. Resolution
7. Additional details
8. Color

First you will need a description of the **subject** with as much detail as possible. E.g.

`Subject`

> A young woman with light blue dress sitting next to a wooden window reading a book.

We got the following image, which matches the prompt pretty well.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/stablediffusion_woman1.png?resize=480%2C480&ssl=1)

We can be more specific. Let’s add a **medium**. Some examples are: digital painting, photograph, oil painting. Let’s use

`Medium`

> Digital painting

The new prompt is

> Digital painting of a young woman with light blue dress sitting next to a wooden window reading a book

The resulting image is

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/stablediffusion_woman2.png?resize=480%2C480&ssl=1)

You can see the image changes from a photograph to a digital art.

You get the idea. Let’s add the rest of them

`Artist`

> by Stanley Artgerm Lau

`Website`

> artstation

`Resolution`

> 8k

`Additional details`

> extremely detailed, ornate, cinematic lighting

`color`

> vivid

Putting them all together, the prompt is

> Digital painting of a young woman with light blue dress sitting next to a wooden window reading a book, by Stanley Artgerm Lau, artstation, 8k, extremely detailed, ornate, cinematic lighting, vivid.

which generates this image:

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/stablediffusion_woman3.png?resize=480%2C480&ssl=1)

By adding keywords to the prompt, we can engineer the image to get the style we want.

- Be detailed and specific when describing the subject.
- Use multiple brackets () to increase its strength and \[\] to reduce.
- Use an appropriate medium type consistent with the artist. E.g. photograph should not be used with van Gogh.
- Artist name is a very strong style modifier. Use wisely.
- Experiment with blending styles.
- Head to the [prompt section](https://stable-diffusion-art.com/prompts/) to study the high-quality prompts. If you like a particular image, use the prompt as a starting point.

## Some Good Keywords for You

Below are some of my favorite keywords and their effects. (Used with Stable Diffusion [v1.4](https://stable-diffusion-art.com/models/#Stable_diffusion_v14) and [v1.5](https://stable-diffusion-art.com/models/#Stable_diffusion_v15))

Enjoy!

### Medium

Medium defines a category of the artwork.

| keyword | Note |
| --- | --- |
| **Portrait** | Focuses image on the face / headshot. |
| **Digital painting** | Digital art style |
| **Concept art** | Illustration style, 2D |
| **Ultra realistic illustration** | drawing that are very realistic. Good to use with people |
| **Underwater portrait** | Use with people. Underwater. Hair floating |
| **Underwater steampunk** | underwater with wash color |

### Style

These keywords further refine the art style.

| keyword | Note |
| --- | --- |
| **hyperrealistic** | Increases details and resolution |
| **pop-art** | Pop-art style |
| **Modernist** | vibrant color, high contrast |
| **art nouveau** | Add ornaments and details, building style |

### Artist

Mentioning the artist in the prompt is a strong effect. Study their work and choose wisely.

| keyword | Note |
| --- | --- |
| **John Collier** | 19th century portrait painter. Add elegancy |
| **Stanley Artgerm Lau** | Strong realistic modern drawing. |
| **Frida Kahlo** | Quite strong effect following Kahlo’s portrait style. Sometimes result in picture frame |
| **John Singer Sargent** | Good to use with woman portrait, generate 19th delicate clothings, some impressionism |
| **Alphonse Mucha** | 2D portrait painting in style of Alphonse Mucha |

### Website

Mentioning an art or photo site is a strong effect, probably because each site has its niche genre.

| keyword | Note |
| --- | --- |
| **pixiv** | Japanese anime style |
| **pixabay** | Commercial stock photo style |
| **artstation** | Modern illustration, fantasy |

### Resolution

| keyword | Note |
| --- | --- |
| **unreal engine** | Very realistic and detailed 3D |
| **sharp focus** | Increase resolution |
| **8k** | Increase resolution, though can lead to it looking more fake. Makes the image more camera like and realistic |
| **vray** | 3D rendering best for objects, landscape and building. |

### Additional Details

Add specific details to your image.

| keyword | Note |
| --- | --- |
| **dramatic** | Increases the emotional expressivity of the face. Overall substantial increase in photo potential / variability. +1 for variability, important for getting the max hit. |
| **silk** | Add silk to clothing |
| **expansive** | More open background, smaller subject |
| **low angle shot** | shot from low angle \*\* |
| **god rays** | sunlight breaking through the cloud |
| **psychedelic** | vivid color with distortion |

### Color

Add additional color scheme to the image.

| keyword | Note |
| --- | --- |
| **iridescent gold** | Shinny gold |
| **silver** | Silver color |
| **vintage** | vintage effect |

## Summary

We have gone through the basic structure of a good prompt. This should be used as a guide rather than rules. The Stable Diffusion model is very flexible. Let it surprise you with some creative combination of keywords!

If you have problem generating stunning artworks, this [Stable Diffusion prompt generator](https://andrewongai.gumroad.com/l/stable_diffusion_prompt_generator) would be able to help you.

This is part 2 of the beginner’s guide series.  
Read part 1: [Absolute beginner’s guide](https://stable-diffusion-art.com/beginners-guide/).  
Read part 3: [Inpainting](https://stable-diffusion-art.com/inpainting_basics/).  
Read part 4: [Models](https://stable-diffusion-art.com/models/).

---

#AI #article
