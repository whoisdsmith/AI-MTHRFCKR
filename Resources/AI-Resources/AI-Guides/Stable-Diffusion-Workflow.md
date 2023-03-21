---
created: 2023-01-30T16:23:10 (UTC -05:00)
tags: []
source: https://stable-diffusion-art.com/workflow/
author: 
---

# Stable Diffusion Workflow (step-by-step example) - Stable Diffusion Art

> ## Excerpt
> A stunning Stable Diffusion artwork is not created by a simple prompt. The workflow is a multiple-step process. In this post, I will go through the workflow

---

A stunning Stable Diffusion artwork is not created by a simple prompt. The workflow is a multiple-step process. In this post, I will go through the workflow step-by-step.

The steps in this workflow are:

1. Build a base prompt.
2. Choose a model.
3. Refinement prompt and generate image with good composition.
4. Fix defects with inpainting.
5. Upscale the image.
6. Final adjustment with photo-editing software.

Contents \[[hide](https://stable-diffusion-art.com/workflow/#)\]

- [Software used in this workflow](https://stable-diffusion-art.com/workflow/#Software_used_in_this_workflow)
- [1\. Build a base prompt](https://stable-diffusion-art.com/workflow/#1_Build_a_base_prompt)
- [2\. Select a model](https://stable-diffusion-art.com/workflow/#2_Select_a_model)
    - [Stable Diffusion v1.5](https://stable-diffusion-art.com/workflow/#Stable_Diffusion_v15)
    - [F222](https://stable-diffusion-art.com/workflow/#F222)
    - [OpenJourney](https://stable-diffusion-art.com/workflow/#OpenJourney)
- [3\. Refine prompt and get a good composition](https://stable-diffusion-art.com/workflow/#3_Refine_prompt_and_get_a_good_composition)
    - [Refine prompt](https://stable-diffusion-art.com/workflow/#Refine_prompt)
    - [Select a good composition](https://stable-diffusion-art.com/workflow/#Select_a_good_composition)
        - [Squint your eyes](https://stable-diffusion-art.com/workflow/#Squint_your_eyes)
        - [Invoke emotion](https://stable-diffusion-art.com/workflow/#Invoke_emotion)
        - [Pick one image to work with](https://stable-diffusion-art.com/workflow/#Pick_one_image_to_work_with)
- [4\. Fix defects with inpainting](https://stable-diffusion-art.com/workflow/#4_Fix_defects_with_inpainting)
    - [Touch up the subject](https://stable-diffusion-art.com/workflow/#Touch_up_the_subject)
    - [Touch up the background](https://stable-diffusion-art.com/workflow/#Touch_up_the_background)
- [5\. Upscale the image](https://stable-diffusion-art.com/workflow/#5_Upscale_the_image)
- [6\. Final adjustment](https://stable-diffusion-art.com/workflow/#6_Final_adjustment)
    - [Adjust levels](https://stable-diffusion-art.com/workflow/#Adjust_levels)
    - [Adjust curves](https://stable-diffusion-art.com/workflow/#Adjust_curves)
    - [Crop](https://stable-diffusion-art.com/workflow/#Crop)
    - [Resize (optional)](https://stable-diffusion-art.com/workflow/#Resize_optional)
- [Final result](https://stable-diffusion-art.com/workflow/#Final_result)

## Software Used in This Workflow

I will use AUTOMATIC1111 GUI in this workflow because I want to tap into some [advanced prompting techniques](https://stable-diffusion-art.com/fine-tune-your-ai-images-with-these-simple-prompting-techniques/) and test multiple [models](https://stable-diffusion-art.com/models/). The Colab notebook in the [Quick Start Guide](https://andrewongai.gumroad.com/l/stable_diffusion_quick_start) runs this GUI and includes all the models used in this tutorial. Check out [install guide for Windows](https://stable-diffusion-art.com/install-windows/) if you want to install this GUI locally.

In the post-processing stages, I will use [GIMP](https://www.gimp.org/), a free and open-source photo editor, for making small final adjustments.

## 1\. Build a Base Prompt

The first task is to search for a prompt that roughly matches what you want. This includes two aspects: (1) **Subject** and (2) **Style**.

You should describe the **subject** in as much detail as possible. Next, include multiple keywords that influence the **styles and aesthetics**.

Let’s say I want to create a **digital illustration of a woman**. Using the [prompt generator](https://andrewongai.gumroad.com/l/stable_diffusion_prompt_generator) (you can also find a list of keywords in this [post](https://stable-diffusion-art.com/how-to-come-up-with-good-prompts-for-ai-image-generation/)), I get the following initial prompt

> A digital painting of \[blake lively:Ana de Armas:0.8 \] , full-body, contemporary white top, red dress, by Artgerm, Guangjian, artstation, soft eyes, extremely detailed face, stunningly beautiful, highly detailed, sharp focus, radiant light rays

Putting a standard negative prompt “just in case”…

> ugly, disfigured, deformed, cropped

I have used [keyword blending](https://stable-diffusion-art.com/fine-tune-your-ai-images-with-these-simple-prompting-techniques/#Blend_two_keywords) to control how my model looks.

This is just a draft prompt. We will make changes to it in the workflow. Let’s move on to the next step.

## 2\. Select a Model

Testing the base prompt is also a good time to pick a **model**. (Read [this post](https://stable-diffusion-art.com/models/) for instructions to install and use models.)

For digital portraits, I would test these three models:

1. [**Stable Diffusion 1.5**](https://stable-diffusion-art.com/models/#Stable_diffusion_v15): The base model
2. [**F222**](https://stable-diffusion-art.com/models/#F222): Specialized in females (Caution: this is a NSFW model)
3. [**OpenJourney**](https://stable-diffusion-art.com/models/#Open_Journey): MidJourney v4 Style

Here are samples from each model. We will pick a model based on the style. Don’t worry about getting a perfect image. Defects can be fixed later.

I am going to use portrait size 512×832 pixels to increase the chance of generating a [full-body portrait](https://stable-diffusion-art.com/common-problems-in-ai-images-and-how-to-fix-them/#Use_portrait_size). The rest of the parameters are pretty standard: 25 [sampling steps](https://stable-diffusion-art.com/know-these-important-parameters-for-stunning-ai-images/#Sampling_steps) of Euler a [sampler](https://stable-diffusion-art.com/know-these-important-parameters-for-stunning-ai-images/#Sampling_methods), [CFG scale](https://stable-diffusion-art.com/know-these-important-parameters-for-stunning-ai-images/#CFG_Scale) 7.

### Stable Diffusion v1.5

[Stable Diffusion v1.5](https://stable-diffusion-art.com/models/#Stable_diffusion_v15) generates a mix of digital and photograph styles. Some of them are nice but many of them have bad anatomy that it will be hard to fix.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00916-2501611548-A-digital-painting-of-blade-lively_Ana-de-Armas_0.8-full-body-contemporary-white-top-red-dress-by-Artgerm-Guangjian-a.png?resize=480%2C780&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00917-2501611549-A-digital-painting-of-blade-lively_Ana-de-Armas_0.8-full-body-contemporary-white-top-red-dress-by-Artgerm-Guangjian-a.png?resize=480%2C780&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00919-2501611551-A-digital-painting-of-blade-lively_Ana-de-Armas_0.8-full-body-contemporary-white-top-red-dress-by-Artgerm-Guangjian-a.png?resize=480%2C780&ssl=1)

Sample images from Stable Diffusion v1.5.

### F222

It’s a safe bet to use [F222](https://stable-diffusion-art.com/models/#F222) to generate portrait-style images. Being fine-tuned with large amount of female images, body parts are usually generated correctly. It generates a pretty standard digital art style with this prompt.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00909-1930667102-A-digital-painting-of-blade-lively_Ana-de-Armas_0.8-full-body-contemporary-white-top-red-dress-by-Artgerm-Guangjian-a.png?resize=480%2C780&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00910-1930667103-A-digital-painting-of-blade-lively_Ana-de-Armas_0.8-full-body-contemporary-white-top-red-dress-by-Artgerm-Guangjian-a.png?resize=480%2C780&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00911-1930667104-A-digital-painting-of-blade-lively_Ana-de-Armas_0.8-full-body-contemporary-white-top-red-dress-by-Artgerm-Guangjian-a.png?resize=480%2C780&ssl=1)

Sample images from F222.

### OpenJourney

[OpenJourney](https://stable-diffusion-art.com/models/#Open_Journey) was trained with images generated by MidJourney v4, a paid AI image generation service. The images have a distinct feel and look.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00915-2456508445-A-digital-painting-of-blade-lively_Ana-de-Armas_0.8-full-body-contemporary-white-top-red-dress-by-Artgerm-Guangjian-a.png?resize=480%2C780&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00913-2456508443-A-digital-painting-of-blade-lively_Ana-de-Armas_0.8-full-body-contemporary-white-top-red-dress-by-Artgerm-Guangjian-a.png?resize=480%2C780&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00912-2456508442-A-digital-painting-of-blade-lively_Ana-de-Armas_0.8-full-body-contemporary-white-top-red-dress-by-Artgerm-Guangjian-a.png?resize=480%2C780&ssl=1)

Sample images from OpenJourney.

I like both F222 and OpenJourney’s styles. But **let’s pick OpenJourney to continue with the workflow**.

## 3\. Refine Prompt and Get a Good Composition

### Refine Prompt

Now you have picked a model, let’s **refine the prompt by adding or removing keywords** until you get an image you can use for the next stage.

When testing new prompts, I would generate at least 4 images at a time. Some prompts just do not work all the time. You don’t want to write off a prompt because of one bad image.

I would add a few keywords to generate a more interesting background and lighting effects.

### Select a Good Composition

The goal at this stage is **not** to pick a perfect image, but to pick one with a **good composition**. Any small defects can be fixed later using inpainting.

But **don’t pick one with many defects**. You will spend an insane amount of time inpainting.

#### Squint Your Eyes

How to pick a good composition? It’s no different from any other artworks. A common trick is to **squint your eyes** when you look at an image. You see a blurry version of it, removing any distracting details. It’s a good composition if the color and shape are still pleasing to you.

#### Invoke Emotion

Have you ever seen an artwork that you cannot take your eyes off? More often than not, it was not because of the technical execution but because the art conveys a message that touches you emotionally.

Good artworks deliver a message and invoke emotions. Pick an image that resonates with you.

#### Pick One Image to Work with

I keep the [batch size](https://stable-diffusion-art.com/know-these-important-parameters-for-stunning-ai-images/#Batch_size) to 4 and the [seed](https://stable-diffusion-art.com/know-these-important-parameters-for-stunning-ai-images/#Seed) to -1 (random). I keep modifying the prompt, generating a batch of 4 images while keeping an eye on composition.

Now, I see this image that *totally* resonates with me…. Let’s use it for the rest of the tutorial…

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00900-808108648-A-digital-painting-of-blade-lively_Ana-de-Armas_0.8-in-street-cityscape-background-happy-full-body-contemporary-white-top.png?resize=480%2C780&ssl=1)](https://stable-diffusion-art.com/workflow/00900-808108648-a-digital-painting-of-blade-lively_ana-de-armas_0-8-in-street-cityscape-background-happy-full-body-contemporary-white-top/)

An image with good composition.

And this is the final prompt:

> A digital painting of \[blake lively:Ana de Armas:0.8\] in street cityscape background, happy, full-body, contemporary white top, red dress, (stocking:1.2), by Artgerm, Guangjian, artstation, soft eyes, extremely detailed face, stunningly beautiful, highly detailed, sharp focus, radiant light rays, cinematic lighting, colorful, volumetric light

The negative prompt is still the same:

> ugly, disfigured, deformed, cropped

## 4\. Fix Defects with Inpainting

### Touch up the Subject

The upper half of this image is in good shape but the lower half is not quite coherent. Let’s use [inpainting](https://stable-diffusion-art.com/inpainting_basics/) to fix it.

If you have just generated this image in **txt2img** tab with AUTOMATIC1111, use **Send to inpaint** button to send the image and parameters to the **Inpaint** tab.

If you have saved the image on your local storage, go to **PNG info** tab, drag and drop the image to the image canvas. The generation parameters will be populated in the text box. Press **Send to inpaint**.

Navigate to **img2img** tab. Select the Inpaint sub-tab. Use the paint brush tool to draw the mask for the area you want to regenerate.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-66.png?resize=480%2C406&ssl=1)](https://stable-diffusion-art.com/workflow/image-66/)

Create the mask for the area you wanted to regenerate.

Inpaint with **mask content** as **original** and **denoising strength 0.66**. I want a red dress so I delete the keyword “white” and increase the emphasis of red dress to 1.3 in the prompt:

> A digital painting of \[blade lively:Ana de Armas:0.8 \] in street cityscape background, happy, full-body, contemporary top, (red dress: 1.3), (stocking:1.2), by Artgerm, Guangjian, artstation, soft eyes, extremely detailed face, stunningly beautiful, highly detailed, sharp focus, radiant light rays, cinematic lighting, colorful, volumetric light

When inpainting clothings or other body parts, inpaint in full resolution is usually not neccesary. So I leave this option unchecked.

Here’s the inpainting result I picked:

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00332-808108650-A-digital-painting-of-blade-lively_Ana-de-Armas_0.8-in-street-cityscape-background-happy-full-body-contemporary-top-red.png?resize=480%2C780&ssl=1)](https://stable-diffusion-art.com/workflow/00332-808108650-a-digital-painting-of-blade-lively_ana-de-armas_0-8-in-street-cityscape-background-happy-full-body-contemporary-top-red/)

Let’s fix up the belt and the dress a bit more. The prompt can stay the same. Denoising strength can be adjusted depending on how much change you want. For this inpainting it stays the same at 0.66.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-67.png?resize=480%2C392&ssl=1)](https://stable-diffusion-art.com/workflow/image-67/)

Now we get:

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-68.png?resize=480%2C780&ssl=1)](https://stable-diffusion-art.com/workflow/image-68/)

I found keeping **mask content** as **original** but adjusting **denoising strength** up and down worked most of the time.

### Touch up the Background

Finally, touch up the background to remove any distracting details. Again, a good way to do this is to **squint your eyes** to see the blurry version of the image. Remove anything in the background that stands out.

[![Use inpainting to touch up the background in Stable Diffusion workflow.](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-69.png?resize=480%2C399&ssl=1)](https://stable-diffusion-art.com/workflow/image-69/)

Use inpainting to touch up the background.

Now with the background got fixed up, the image is in a pretty good shape!

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-70.png?resize=480%2C780&ssl=1)](https://stable-diffusion-art.com/workflow/image-70/)

Image after inpainting.

## 5\. Upscale the Image

This part of the workflow is to make the image larger since it is pretty small: only 512×832 pixels. We will enlarge it 4 times with an [AI upscaler](https://stable-diffusion-art.com/ai-upscaler/).

In AUTOMATIC1111, under the inpainting results, click **Send to extras**.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-71.png?resize=480%2C399&ssl=1)](https://stable-diffusion-art.com/workflow/image-71/)

Go to **Extras** tab. You can experiment with different upscalers and settings. Be sure to save the resulting image to your local computer and zoom in to inspect the details, especially the face.

After some experimentation, here’s the setting I settled with:

- Resize: 4
- Upscaler: R-ESRGAN 4x+
- CodeFormer visibility: ~0.5
- CodeFormer weight: ~0.5
- Upscale before restoring faces: Yes

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-72.png?resize=480%2C477&ssl=1)](https://stable-diffusion-art.com/workflow/image-72/)

The general rule is to apply the least amount of face restoration you can get away with. This can be achieved by lowering the **CodeFomer visibility** and/or increasing the **CodeFormer weight**. **Upscale before restoring faces** could reduce artifact introduced by the upscaler.

Here’s the upcaled image:

[![Image upscaled with R-ESRGAN with face restoration.](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00015.png?resize=480%2C780&ssl=1)](https://stable-diffusion-art.com/workflow/attachment/00015/)

Image upscaled with R-ESRGAN with face restoration.

## 6\. Final Adjustment

The final step is to do some **small adjustments in luminosity and contrast** using [GIMP](https://www.gimp.org/), or any photo editing software of your choice. There’s a lot more you can do to touch up an image. I will only mention the very basics: **levels, curves and crop**.

### Adjust Levels

In GIMP, click **Colors** → **Levels** in the top menu. Adjust the left and right up-arrow so that they cover the tails of the histogram. This is to make sure the image is using the whole range of intensity values.

Then adjust the middle up-arrow to the level of brightness to your taste.

[![Adjust levels in GIMP for Stable Diffusion workflow.](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-74.png?resize=480%2C374&ssl=1)](https://stable-diffusion-art.com/workflow/image-74/)

Adjust levels in GIMP.

### Adjust Curves

In GIMP, click **Colors** → **Curves** in the top menu. Adjust the upper part and lower part of the curve separately to control the contrast applied to the bright part and the shadow independently.

[![Adjust curves in GIMP for Stable Diffusion workflow.](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-75.png?resize=480%2C399&ssl=1)](https://stable-diffusion-art.com/workflow/image-75/)

Adjust curves in GIMP.

### Crop

Like real photos, AI images may need to be cropped to improve composition. This has something to do with the [simple automated cropping](https://github.com/NovelAI/novelai-aspect-ratio-bucketing#description) applied to the training data.

To crop an image in GIMP, click **Tools** → **Transform tool** → **Crop**.

Since this image looks pretty good already, I am not going to crop it.

### Resize (optional)

You can optionally resize the image for different usages. To resize, click **Image** → **Scale Image**. Enter the new width and height.

[![Resize image in GIMP.](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-76.png?resize=480%2C392&ssl=1)](https://stable-diffusion-art.com/workflow/image-76/)

Resize image in GIMP.

## Final Result

So here we get the final result.

[![Final resulting image of Stable Diffusion workflow.](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00015_final.png?resize=480%2C780&ssl=1)](https://stable-diffusion-art.com/workflow/00015_final/)

Final image.

See more images from the same workflow [here](https://stable-diffusion-art.com/portraits-in-midjourney-style/).

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00157.png?resize=480%2C780&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00124.png?resize=480%2C780&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00097.png?resize=480%2C780&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00052.png?resize=480%2C780&ssl=1)

To recap, the steps in this Stable Diffusion workflow are

1. Build a base prompt.
2. Choose a model.
3. Refinement prompt and generate image with good composition.
4. Fix defects with inpainting.
5. Upscale the image.
6. Final adjustment with photo-editing software.


---

#AI #article
