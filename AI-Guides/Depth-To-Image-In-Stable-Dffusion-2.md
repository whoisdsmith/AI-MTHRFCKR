---
created: 2023-01-30T16:23:03 (UTC -05:00)
tags: []
source: https://stable-diffusion-art.com/depth-to-image/
author: 
---

# Depth-to-image in Stable Diffusion 2: All You Need to Know - Stable Diffusion Art

> ## Excerpt
> Depth-to-image (Depth2img) is an under-appreciated model in Stable Diffusion v2. It is an enhancement to image-to-image (img2img) which takes advantage of the

---

Depth-to-image (Depth2img) is an under-appreciated model in Stable Diffusion v2. It is an enhancement to [image-to-image](https://stable-diffusion-art.com/how-to-use-img2img-to-turn-an-amateur-drawing-to-professional-with-stable-diffusion-image-to-image/) (img2img) which takes advantage of the depth information when generating new images.

In this tutorial, we will look under the hood to see what it is, how to install and use it, and what it can do for you.

Contents \[[hide](https://stable-diffusion-art.com/depth-to-image/#)\]

- [What can depth-to-image do](https://stable-diffusion-art.com/depth-to-image/#What_can_depth-to-image_do)
- [So what is depth-to-image?](https://stable-diffusion-art.com/depth-to-image/#So_what_is_depth-to-image)
    - [Depth map](https://stable-diffusion-art.com/depth-to-image/#Depth_map)
- [Install depth-to-image model](https://stable-diffusion-art.com/depth-to-image/#Install_depth-to-image_model)
    - [How to install](https://stable-diffusion-art.com/depth-to-image/#How_to_install)
    - [How to use](https://stable-diffusion-art.com/depth-to-image/#How_to_use)
- [Some usage ideas](https://stable-diffusion-art.com/depth-to-image/#Some_usage_ideas)
    - [An alternative to img2img](https://stable-diffusion-art.com/depth-to-image/#An_alternative_to_img2img)
    - [Inpainting](https://stable-diffusion-art.com/depth-to-image/#Inpainting)
    - [Style transfer](https://stable-diffusion-art.com/depth-to-image/#Style_transfer)
    - [Steal a pose](https://stable-diffusion-art.com/depth-to-image/#Steal_a_pose)
- [Summary](https://stable-diffusion-art.com/depth-to-image/#Summary)

## What Can Depth-to-image Do

With depth-to-image, you have better control of synthesizing subject and background separately.

Let’s say I want to do turn this romantic scene in *La La Land* into a wrestling match…

[![Original image to be used for depth-to-image.](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/lala-land.png?resize=480%2C330&ssl=1)](https://stable-diffusion-art.com/depth-to-image/lala-land/)

Original image.

We will go into more details later, but for now just **treat depth-to-image as an enhanced version of image-to-image**. They can be used in exactly the same way—given an image and a text prompt, it will generate a new image.

Let’s say I use the prompt

> photo of two men wrestling

for both image-to-image and depth-to-image. Below are the results with [denoising strength](https://stable-diffusion-art.com/inpainting_basics/#Denoising_strength) varying from 0.4 to 1.0. (Remember the higher the denoising strength, the more the image would change.)

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-60.png?resize=480%2C225&ssl=1)](https://stable-diffusion-art.com/depth-to-image/image-60/)

Comparing image-to-image and depth-to-image.

Let’s look at the image-to-image generations (top row). We ran into a problem: At low denoising strength, the image didn’t change enough. At high denoising strength, we do see two wrestlers but the original composition is lost.

**Depth-to-image resolves this problem**. You can crank up denoising strength all the way to 1 (the maximum) without losing the original composition!

Now you know what depth-to-image can do, let’s see how it works.

## So What is Depth-to-image?

Recall that in image-to-image, Stable Diffusion takes an image and a prompt as inputs. The image generation is based on BOTH the image and the prompt. The final image resembles the input image in color and shapes.

In depth-to-image, Stable Diffusion similarly takes an image and a prompt as inputs. The model first estimates the **depth map** of the input image using [MIDaS](https://github.com/isl-org/MiDaS), an AI model developed in 2019 for estimating [monocular depth perception](https://en.wikipedia.org/wiki/Depth_perception) (that is estimating depth from a single view). The depth map is then used by Stable Diffusion as an extra **conditioning** to image generation.

In other words, depth-to-image uses *three* conditionings to generate a new image: (1) text prompt, (2) original image and (3) depth map.

Equipped with the depth map, the model has *some* knowledge of the three-dimensional composition of the scene. **Image generations of foreground objects and the background can be separated.**

### Depth Map

You don’t need to supply a depth map to use depth-to-image. This section reproduces the depth map for educational purpose.

A depth map is a simple gray scale image of the same size of the original image encoding the depth information. Complete white means the object is closest to you. More black means further away.

Here’s an example of an image and its depth map estimated by MIDaS.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00702-854471792-Amber-Heard_-Ana-de-Armas-_0.6Victorian-FemininePerfect-Face-arms-outstretched-above-head-Aype-Beven-.png?resize=480%2C600&ssl=1)

Original

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/depthmap-00702-854471792-Amber-Heard_-Ana-de-Armas-_0.6Victorian-FemininePerfect-Face-arms-outstretched-above-head-Aype-Beven-.png?resize=480%2C600&ssl=1)

Depth map

Let’s combine the image and the depth map (using [Depthy](https://depthy.stamina.pl/#/)). Hover the pointer over the image to see the effect.

See [model architecture](https://stable-diffusion-art.com/how-stable-diffusion-work/#Depth-to-image) if you want to learn more about how the depth-to-image works in deeper level.

## Install Depth-to-image Model

### How to Install

To install the depth-to-image model in AUTOMATIC1111 GUI:

1. Download the model file ([512-depth-ema.ckpt](https://huggingface.co/stabilityai/stable-diffusion-2-depth/resolve/main/512-depth-ema.ckpt))
2. Download the [config file](https://raw.githubusercontent.com/Stability-AI/stablediffusion/main/configs/stable-diffusion/v2-midas-inference.yaml), rename it to `512-depth-ema.yaml`

Put both of them in the model directory:

```
stable-diffusion-webui/models/Stable-diffusion
```

### How to Use

To use the model, press the refresh button next to the checkpoint dropbox at the top left. Select `512-depth-ema.ckpt` to load the model.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-61.png?resize=456%2C73&ssl=1)

Note that the depth model can be used for **image-to-image** and **inpainting**, but not text-to-image. You will see an error if you try to do that.

To use the model, go to **img2img** tab. Follow instructions for [img2img](https://stable-diffusion-art.com/how-to-use-img2img-to-turn-an-amateur-drawing-to-professional-with-stable-diffusion-image-to-image/) and [inpainting](https://stable-diffusion-art.com/inpainting_basics/) to use.

As evident from the model name, this is a 512 model. That means it works best when at least one side of the new image is 512 pixels.

## Some Usage Ideas

Now that’s go through some use cases.

### An Alternative to img2img

Let’s say you have an portrait photo like this.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/joseph-gonzalez-iFgRcqHznqg-unsplash.jpg?resize=389%2C583&ssl=1)](https://stable-diffusion-art.com/depth-to-image/joseph-gonzalez-ifgrcqhznqg-unsplash/)

Original portrait image.

You want to have some variety by including an asian woman. But you have already designed additional elements surrounding him so you don’t want the shape of the person to change.

You can kind of do that with img2img, but you cannot set denoising strength too high because you will lose the original shape.

With img2img, this is the best you can do:

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/2.1-img2img-denoise-0.58-00128-2882469290-a-beautiful-happy-asian-woman-with-perfect-detailed-eyes-detailed-facial-feature-detailed-skin-natural-lighting-long-hair.png?resize=375%2C562&ssl=1)](https://stable-diffusion-art.com/depth-to-image/2-1-img2img-denoise-0-58-00128-2882469290-a-beautiful-happy-asian-woman-with-perfect-detailed-eyes-detailed-facial-feature-detailed-skin-natural-lighting-long-hair/)

Image-to-image. Prompt: a beautiful happy asian woman with perfect detailed eyes, detailed facial feature, detailed skin, natural lighting, long hair. Denoising strength: 0.58

There’s some change in shape but not too bad. However, the denoising strength is still too low to deviate from the original man’s skin color. Also the *long hair* prompt was not followed.

Now the dilemma: Increasing denoising strength to 1 would result in what we want but we will lose the original shape:

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/2.1-img2img-long-hair-00126-458374445-a-beautiful-happy-asian-woman-with-perfect-detailed-eyes-detailed-facial-feature-detailed-skin-natural-lighting-long-hair.png?resize=364%2C546&ssl=1)](https://stable-diffusion-art.com/depth-to-image/2-1-img2img-long-hair-00126-458374445-a-beautiful-happy-asian-woman-with-perfect-detailed-eyes-detailed-facial-feature-detailed-skin-natural-lighting-long-hair/)

Image-to-image with the same prompt but denoising strength is set to 1.

Using depth-to-image model would allow us to set denoising strength to 1 without losing the original shape:

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/long-hair-00124-2487370671-a-beautiful-happy-asian-woman-with-perfect-detailed-eyes-detailed-facial-feature-detailed-skin-natural-lighting-long-hair.png?resize=377%2C565&ssl=1)](https://stable-diffusion-art.com/depth-to-image/long-hair-00124-2487370671-a-beautiful-happy-asian-woman-with-perfect-detailed-eyes-detailed-facial-feature-detailed-skin-natural-lighting-long-hair/)

Depth-to-image with the same prompt and denoising strength set to 1.

Note that the man’s shape is *completely* preserved, and Stable Diffusion somehow figure out how to render the long hair.

### Inpainting

You can similarly use depth-to-image in inpainting, either for [fixing defects](https://stable-diffusion-art.com/inpainting_basics/) or creating something new.

You want to use depth-to-image if you care about preserving the original composition.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/W14ShotToHERO.jpg?resize=480%2C270&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00098-1555620215-two-lions-holding-each-other.png?resize=480%2C320&ssl=1)

Inpainting with the depth-to-image model.

### Style Transfer

An advantage of depth-to-image is you can dial denoising strength all the way up to 1 without losing composition. That makes transforming a scene to a different style easy.

Here are some examples:

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00190-4163774329-cubism-painting_1.5-a-man-with-white-shirt-dark-pant-and-a-tie-and-a-woman-with-yellow-dress-dancing-on-a-street-at-night-wit.png?resize=480%2C320&ssl=1)

cubism

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00183-694140991-unreal-engine-a-man-with-white-shirt-dark-pant-and-a-tie-and-a-woman-with-yellow-dress-dancing-on-a-street-at-night-with-a-city.png?resize=480%2C320&ssl=1)

Unreal engine

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00182-362111397-Aype-Beven-scott-williams-jim-leeLeinil-Francis-Yu-Salva-Espin-oil-painting-Matteo-Lolli-Sop.png?resize=480%2C320&ssl=1)

OIl painting

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00178-124542128-in-art-nouveau-painting_1.4-style-a-man-with-white-shirt-dark-pant-and-a-tie-and-a-woman-with-yellow-dress-dancing-on-a-stree.png?resize=480%2C320&ssl=1)

Illustration

Style transfer with Depth-to-image.

### Steal a Pose

It’s difficult to generate a particular human pose with Stable Diffusion. With depth-to-image, you can use a photo with the pose you want as the base image. Set denoising strength to 1 and you are in business! The pose will be completely preserved with depth-to-image. The photo can be a movie scene, a painting or a picture you take with your phone.

No more extra limbs, weird hands and endless [inpainting](https://stable-diffusion-art.com/inpainting_basics/) to fix poses!

## Summary

Depth-to-image is a great alternative to image-to-image, especially when you want to preserve the composition of the scene.

This powerful tool hasn’t got much attention since its release. I hope this article would inspire you to think about including it in your workflow.

---

#AI #article
