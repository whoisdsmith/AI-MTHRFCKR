---
created: 2023-01-30T16:26:18 (UTC -05:00)
tags: []
source: https://stable-diffusion-art.com/models/
author: 
---

# Beginner's Guide to Stable Diffusion Models and the Ones You Should Know - Stable Diffusion Art

> ## Excerpt
> How to install, use and merge stable diffusion models: F222, Anything v3, Open Journey v4, v1.4 and v1.5.

---

**Models**, sometimes called **checkpoint files**, are pre-trained Stable Diffusion weights intended for generating general or a particular genre of images.

What images a model can generate depends on the data used to trained them. A model won’t be able to generate a cat’s image if there’s never a cat in the training data. Likewise, if you only train a model with cat images, it will only generate cats.

We will go introduce what models are, some common ones ([v1.4](https://stable-diffusion-art.com/models/#Stable_diffusion_v14), [v1.5](https://stable-diffusion-art.com/models/#Stable_diffusion_v15), [F222](https://stable-diffusion-art.com/models/#F222), [Anything V3](https://stable-diffusion-art.com/models/#Anything_V3), [Open Journey v4](https://stable-diffusion-art.com/models/#Open_Journey)), how to install, use and merge them.

This is part 4 of the beginner’s guide series.  
Read part 1: [Absolute beginner’s guide](https://stable-diffusion-art.com/beginners-guide/).  
Read part 2: [Prompt building](https://stable-diffusion-art.com/how-to-come-up-with-good-prompts-for-ai-image-generation/).  
Read part 3: [Inpainting](https://stable-diffusion-art.com/inpainting_basics/).

Contents \[[hide](https://stable-diffusion-art.com/models/#)\]

- [Fine-tuned models](https://stable-diffusion-art.com/models/#Fine-tuned_models)
    - [What is fine tuning?](https://stable-diffusion-art.com/models/#What_is_fine_tuning)
    - [Why do people make them?](https://stable-diffusion-art.com/models/#Why_do_people_make_them)
    - [How are they made?](https://stable-diffusion-art.com/models/#How_are_they_made)
- [Models](https://stable-diffusion-art.com/models/#Models)
    - [Stable diffusion v1.4](https://stable-diffusion-art.com/models/#Stable_diffusion_v14)
    - [Stable diffusion v1.5](https://stable-diffusion-art.com/models/#Stable_diffusion_v15)
    - [F222](https://stable-diffusion-art.com/models/#F222)
    - [Anything V3](https://stable-diffusion-art.com/models/#Anything_V3)
    - [Open Journey](https://stable-diffusion-art.com/models/#Open_Journey)
    - [Model comparison](https://stable-diffusion-art.com/models/#Model_comparison)
    - [Other models](https://stable-diffusion-art.com/models/#Other_models)
        - [Waifu-diffusion](https://stable-diffusion-art.com/models/#Waifu-diffusion)
        - [Arcane Diffusion](https://stable-diffusion-art.com/models/#Arcane_Diffusion)
        - [Robo Diffusion](https://stable-diffusion-art.com/models/#Robo_Diffusion)
        - [Mo-di-diffusion](https://stable-diffusion-art.com/models/#Mo-di-diffusion)
        - [Inkpunk Diffusion](https://stable-diffusion-art.com/models/#Inkpunk_Diffusion)
    - [Finding more models](https://stable-diffusion-art.com/models/#Finding_more_models)
- [v2 models](https://stable-diffusion-art.com/models/#v2_models)
- [How to install and use a model](https://stable-diffusion-art.com/models/#How_to_install_and_use_a_model)
- [Merging two models](https://stable-diffusion-art.com/models/#Merging_two_models)
    - [Example of a merged model](https://stable-diffusion-art.com/models/#Example_of_a_merged_model)
- [Summary](https://stable-diffusion-art.com/models/#Summary)

## Fine-tuned Models

### What is Fine Tuning?

**Fine tuning** in a common technique in machine learning of taking a model that is trained on a wide dataset, and train a bit more on the narrow dataset that you are interested in.

A fine-tuned model will be biased towards generating images similar to your dataset, while maintaining the versatility of the original model.

### Why Do People Make Them?

Stable diffusion is great but is not good at everything. For example, it can and will generate anime style images with the keyword “anime” in prompt. But it could be difficult to generate images of a sub-genre of anime. Instead of tinkering with the prompt, you can fine tune the model with images of that sub-genre.

### How Are They Made?

There are two main fine tuning methods: (1) Additional training and (2) Dreambooth. They both start with a base model like Stable Diffusion [v1.4](https://stable-diffusion-art.com/wp-admin/post.php?post=806&action=edit#Stable_diffusion_v14) or [v1.5](https://stable-diffusion-art.com/wp-admin/post.php?post=806&action=edit#Stable_diffusion_v15).

**Additional training** is achieved by training a base model with an additional dataset that you are interested in. For example, you can train Stable Diffusion v1.5 with an additional dataset of vintage cars to bias the aesthetic of cars towards the sub-genre.

[**Dreambooth**](https://arxiv.org/abs/2208.12242), originally developed by Google, is a technique to inject custom subjects into text-to-image models. It works with as few as 3-5 custom images. You can take a few pictures of yourself and use Dreambooth to put yourself into the model. A model trained with Dreambooth requires a special keyword to condition the model.

There’s another less popular fine tuning technique called **[textual inversion](https://textual-inversion.github.io/)** (sometimes called **embedding**). The goal is similar to Dreambooth: Inject a custom subject into the model with only a few examples. A new keyword is created specifically for the new object. Only the text embedding network is fine tuned, while keeping the rest of the model unchanged. In layman’s term, it’s like using existing words to describe a new concept.

There are two group of models: v1 and v2. I will cover v1 models in this section and v2 models in the next section.

There are hundreds of fine-tuned Stable Diffusion models and the number is increasing everyday. Below is a list of model that can be used for general purpose.

### Stable Diffusion v1.4

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-11.png?resize=480%2C660&ssl=1)

v1.4 image

[Model Page](https://huggingface.co/CompVis/stable-diffusion-v-1-4-original)

[Download link](https://huggingface.co/CompVis/stable-diffusion-v-1-4-original/resolve/main/sd-v1-4.ckpt)

Released in August 2022 by Stability AI, v1.4 model is considered to be the first publicly available Stable Diffusion model.

You can treat v1.4 as a general-purpose model. Most of the time, it is enough to use it as is unless you are really picky about certain styles.

### Stable Diffusion v1.5

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00911-1930667104-A-digital-painting-of-blade-lively_Ana-de-Armas_0.8-full-body-contemporary-white-top-red-dress-by-Artgerm-Guangjian-a.png?resize=480%2C780&ssl=1)

v1.5 image.

[Model Page](https://huggingface.co/runwayml/stable-diffusion-v1-5)

[Download link](https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.ckpt)

v1.5 is released in Oct 2022 by Runway ML, a partner of Stability AI. The model is based on v1.2 with further trainings.

The [model page](https://huggingface.co/runwayml/stable-diffusion-v1-5) does not mention what the improvement is. It produces slightly different results compared to v1.4 but it is unclear if they are better.

Like v1.4, you can treat v1.5 as a general-purpose model.

In my experience, v1.5 is a fine choice as the initial model and can be used interchangeably with v1.4.

### F222

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-47.png?resize=402%2C497&ssl=1)

F222

[Model Page](https://ai.zeipher.com/)

[Download link](https://mega.nz/file/0c8hkagB#ER-Lz6Wwb3y2BXko4ZzA0kfusnGYk-EYsz3E3vugfqo)

**F222** is trained originally for generating nudes but people found it useful in generating beautiful female portraits with correct body part relations. Interestingly, contrary to what you might think, it’s quite good at generating aesthetically pleasing clothings.

F222 is a special purpose model but it is quite useful for portraits. It has a high tendency of generating nudes but it can be suppressed by keywords like “dress”.

Read [recommended keyword](https://ai.zeipher.com/f.html) list.

### Anything V3

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-25.png?resize=480%2C600&ssl=1)](https://stable-diffusion-art.com/models/image-25-2/)

Anything v3 model.

[Model Page](https://huggingface.co/Linaqruf/anything-v3.0)

[Download Link](https://huggingface.co/Linaqruf/anything-v3.0/resolve/main/Anything-V3.0-pruned.ckpt)

**Anything V3** is a special-purpose model trained to produce high-quality anime-style images. You can use [danbooru tags](https://danbooru.donmai.us/tags) (like 1girl, white hair) in text prompt.

It’s useful for casting celebrities to amine style, which can then be blended seamlessly with illustrative elements.

One drawback (as least to me) is that it produces females with disproportional body shapes. I like to tone it down with F222.

### Open Journey

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-26.png?resize=480%2C360&ssl=1)](https://stable-diffusion-art.com/models/image-26-2/)

Open Journey model.

[Model Page](https://huggingface.co/prompthero/openjourney)

[Download link](https://huggingface.co/prompthero/openjourney/resolve/main/mdjrny-v4.ckpt)

Open Journey is a model fine-tuned with images generated by [Mid Journey v4](https://www.midjourney.com/). It has a different aesthetic and is a good general purpose model.

### Model Comparison

Here’s a comparison of these models with the same prompt and seed. All but Anything v3 generate realistic images but with different aesthetics.

[![Compare commonly used models.](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/merged-1.png?resize=480%2C288&ssl=1)](https://stable-diffusion-art.com/models/merged-1/)

Images generated with the same seed and steps.

### Other Models

There are hundreds of Stable Diffusion models available. Many of them are special-purpose models designed to generate a particular style. Some notable ones are:

#### Waifu-diffusion

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-20.png?resize=480%2C148&ssl=1)](https://stable-diffusion-art.com/models/image-20-2/)

waifu-diffusion on right.

[Download link](https://huggingface.co/hakurei/waifu-diffusion)

Waifu Diffusion is Japanese anime style.

#### Arcane Diffusion

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-21.png?resize=480%2C330&ssl=1)](https://stable-diffusion-art.com/models/image-21-2/)

Arcane diffusion

[Download link](https://huggingface.co/nitrosocke/Arcane-Diffusion)

Arcane Diffusion is TV show Arcane style. Use keywords ***arcane style*** to trigger the effect.

#### Robo Diffusion

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-22.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/models/image-22-2/)

Robo diffusion

[Download link](https://huggingface.co/nousr/robo-diffusion)

Robot Diffusion is an interesting robot style model that will turn everything your subject into robot!

#### Mo-di-diffusion

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-23.png?resize=480%2C360&ssl=1)](https://stable-diffusion-art.com/models/image-23-2/)

Mo-di-diffusion is modern Disney style.

[Download link](https://huggingface.co/nitrosocke/mo-di-diffusion)

This is the model for you if you want to generate some Pixar-like style.

Use keywords: ***modern disney style***

#### Inkpunk Diffusion

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-24.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/models/image-24-2/)

Inkpunk diffusion

[Download link](https://huggingface.co/Envvi/Inkpunk-Diffusion)

Inkpunk Diffusion is a Dreambooth-trained model with a very distinct illustration style.

Use keyword: ***nvinkpunk***

### Finding More Models

You can find more models in [Huggingface](https://huggingface.co/models?other=stable-diffusion).

[Civitai](https://civitai.com/) is another great resources to search for models.

## v2 Models

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00003-RESRGAN.png?resize=480%2C349&ssl=1)

Sample 2.1 image.

Stability AI released a new series of models version 2. So far [2.0](https://stable-diffusion-art.com/how-to-run-stable-diffusion-2-0/) and [2.1](https://stable-diffusion-art.com/install-stable-diffusion-2-1/) models are released. The main change in v2 models are

- In addition to 512×512 pixels, a higher resolution version 768×768 pixels is available.
- You can no longer generate explicit contents because pornographic materials were removed from training.

You may assume that everyone has moved on to using the v2 models. However, the Stable Diffusion community found that the images looked worse in the [2.0](https://stable-diffusion-art.com/how-to-run-stable-diffusion-2-0/) model. People also have difficulty in using power keywords like celebrity names and artist names.

The [2.1](https://stable-diffusion-art.com/install-stable-diffusion-2-1/) model has partially addressed these issues. The images looks better out of box. It’s easier to generate artistic style.

As of now, most people not have completely moved on to 2.1 model. Many use them occasionally but spend most of the time with v1 models.

If you decided to try out v2 models, be sure to check out [these tips](https://stable-diffusion-art.com/install-stable-diffusion-2-1/#Tips_for_using_21) to avoid some common frustrations.

## How to Install and Use a Model

These instructions are only applicable to v1 models. See the instructions for [v2.0](https://stable-diffusion-art.com/how-to-run-stable-diffusion-2-0/) and [v2.1](https://stable-diffusion-art.com/install-stable-diffusion-2-1/).

To install a model in AUTOMATIC1111 GUI, download and place the checkpoint (.ckpt) file in the following folder

```
stable-diffusion-webui/models/Stable-diffusion/
```

Press **reload** button next to the checkpoint drop box

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/image-44.png?resize=444%2C115&ssl=1)](https://stable-diffusion-art.com/models/image-44/)

You should see the checkpoint file you just put in available for selection. Select the new checkpoint file to use the model.

If you are new to AUTOMATIC1111 GUI, some models are preloaded in Colab notebook included in the [Quick Start Guide](https://andrewongai.gumroad.com/l/stable_diffusion_quick_start?layout=profile).

## Merging Two Models

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/image-47.png?resize=480%2C317&ssl=1)](https://stable-diffusion-art.com/models/image-47/)

Settings for merging two models.

To merge two models using AUTOMATIC1111 GUI, go to the **Checkpoint Merger** tab and select the two models you want to merge in **Primary model (A)** and **Secondary model (B)**.

Adjust the multiplier (M) to adjust the relative weight of the two models. Setting it to 0.5 would merge the two models with equal importance.

After pressing **Run**, the new merged model will be available for use.

### Example of a Merged Model

Here are sample images from merging [F222](https://stable-diffusion-art.com/models/#F222) and [Anything V3](https://stable-diffusion-art.com/models/#Anything_V3) with equal weight (0.5):

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/merged2.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/models/merged2/)

Compare F222, Anything V3 and Merged (50% each)

The merged model sits in between the realistic F222 and the anime Anything V3 styles. It is a very good model for generating illustration arts with human figures.

## Summary

In this article, I have introduced what Stable Diffusion models are, how they are made, a few common ones, and how to merge them. Using models can make your life easier when you have a specific style in mind.

---

#AI #article
