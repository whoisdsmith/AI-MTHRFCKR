---
created: 2023-01-30T16:25:06 (UTC -05:00)
tags: []
source: https://stable-diffusion-art.com/inpainting_basics/
author: 
---

# Beginner's Guide to Inpainting (step-by-step examples) - Stable Diffusion Art

> ## Excerpt
> Inpainting is an indispensable way to fix small defects. In this post, I will go through a few basic examples to use inpainting for fixing defects.

---

No matter how good your prompt and model are, it is rare to get a perfect image in one shot.

Inpainting is an indispensable way to fix small defects. In this post, I will go through a few basic examples to use **inpainting** for fixing defects.

If you are new to AI images, you may want to read the [beginner’s guide](https://stable-diffusion-art.com/beginners-guide/) first.

This is part 3 of the beginner’s guide series.  
Read part 1: [Absolute beginner’s guide](https://stable-diffusion-art.com/beginners-guide/).  
Read part 2: [Prompt building](https://stable-diffusion-art.com/how-to-come-up-with-good-prompts-for-ai-image-generation/).  
Read part 4: [Models](https://stable-diffusion-art.com/models/).

Contents \[[hide](https://stable-diffusion-art.com/inpainting_basics/#)\]

- [Image model and GUI](https://stable-diffusion-art.com/inpainting_basics/#Image_model_and_GUI)
- [Basic inpainting settings](https://stable-diffusion-art.com/inpainting_basics/#Basic_inpainting_settings)
    - [Use an inpainting model (optional)](https://stable-diffusion-art.com/inpainting_basics/#Use_an_inpainting_model_optional)
    - [Creating an inpaint mask](https://stable-diffusion-art.com/inpainting_basics/#Creating_an_inpaint_mask)
    - [Settings for inpainting](https://stable-diffusion-art.com/inpainting_basics/#Settings_for_inpainting)
        - [Prompt](https://stable-diffusion-art.com/inpainting_basics/#Prompt)
        - [Image size](https://stable-diffusion-art.com/inpainting_basics/#Image_size)
        - [Face restoration](https://stable-diffusion-art.com/inpainting_basics/#Face_restoration)
        - [Inpaint in Full resolution](https://stable-diffusion-art.com/inpainting_basics/#Inpaint_in_Full_resolution)
        - [Mask content](https://stable-diffusion-art.com/inpainting_basics/#Mask_content)
        - [Denoising strength](https://stable-diffusion-art.com/inpainting_basics/#Denoising_strength)
        - [Batch size](https://stable-diffusion-art.com/inpainting_basics/#Batch_size)
    - [Inpainting results](https://stable-diffusion-art.com/inpainting_basics/#Inpainting_results)
    - [One more round of inpainting](https://stable-diffusion-art.com/inpainting_basics/#One_more_round_of_inpainting)
- [Adding new objects](https://stable-diffusion-art.com/inpainting_basics/#Adding_new_objects)
- [Explanation of inpainting parameters](https://stable-diffusion-art.com/inpainting_basics/#Explanation_of_inpainting_parameters)
    - [Denoising strength](https://stable-diffusion-art.com/inpainting_basics/#Denoising_strength-2)
    - [CFG scale](https://stable-diffusion-art.com/inpainting_basics/#CFG_scale)
    - [Masked content](https://stable-diffusion-art.com/inpainting_basics/#Masked_content)
    - [Inpaint at full resolution](https://stable-diffusion-art.com/inpainting_basics/#Inpaint_at_full_resolution)
- [Tips for inpainting](https://stable-diffusion-art.com/inpainting_basics/#Tips_for_inpainting)

## Image Model and GUI

We will use Stable Diffusion AI and AUTOMATIC1111 GUI. See my [quick start guide](https://andrewongai.gumroad.com/l/stable_diffusion_quick_start) for setting up in Google’s cloud server.

## Basic Inpainting Settings

In this section, I will show you step-by-step how to use inpainting to fix small defects.

I will use an original image from the [Lonely Palace](https://stable-diffusion-art.com/lonely-palace/) prompt:

> \[emma watson: amber heard: 0.5\], (long hair:0.5), headLeaf, wearing stola, vast roman palace, large window, medieval renaissance palace, ((large room)), 4k, arstation, intricate, elegant, highly detailed
>
> (Detailed settings can be found [here](https://stable-diffusion-art.com/lonely-palace/).)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/01644-3083470266-emma-watson_-amber-heard_-0.5-long-hair_0.5-headLeaf-wearing-stola-vast-roman-palace-large-window-medieval-renaissan.png?resize=480%2C349&ssl=1)

Original image

It’s a fine image but I would like to fix the following issues

- The face looks unnatural.
- The right arm is missing.

### Use an Inpainting Model (optional)

Do you know there are Stable Diffusion models specially trained for inpainting? You can use it if you want to get the best result. But usually its fine using the same model you generated the image with for inpainting.

To install the [v1.5 inpainting model](https://huggingface.co/runwayml/stable-diffusion-inpainting), download the model [checkpoint file](https://huggingface.co/runwayml/stable-diffusion-inpainting/resolve/main/sd-v1-5-inpainting.ckpt) and put it in the folder

```
stable-diffusion-webui/models/Stable-diffusion
```

In AUTOMATIC1111, press the refresh icon next to the checkpoint selection dropbox at the top left. Select `sd-v1-5-inpainting.ckpt` to enable the model.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-46.png?resize=480%2C83&ssl=1)

### Creating an Inpaint Mask

In AUTOMATIC1111 GUI, Select the **img2img** tab and select the **Inpaint** sub-tab. Upload the image to the inpainting canvas.

![inpainting canvas](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/image-6.png?resize=480%2C435&ssl=1)

We will inpaint both the right arm and the face at the same time. Using the paintbrush tool to create a **mask** to be inpainted. This is the area you want Stable Diffusion to regenerate.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/image-7.png?resize=480%2C435&ssl=1)

Create mask use the paintbrush tool.

### Settings for Inpainting

#### Prompt

You can **reuse the original prompt** for fixing defects. This is similar to generating multiple images but you can select a particular area and with different settings.

#### Image Size

The image size need to be adjusted to be the same as the original image. (704 x 512 in this case).

#### Face Restoration

If your are inpainting faces, make sure to turn on **restore faces**. (You will also need to select and apply the **face restoration model** to be used in the **Settings** tab. **CodeFormer** is a good one.)

#### Inpaint in Full Resolution

When inpainting small area with fine details, it is important to select **inpaint in full resolution**. Doing so would enlarge your masked area , perform inpainting, and scale it back down. The end result is an inpainting with finer details.

#### Mask Content

The next important setting is **Mask Content**.

Select **original** if you want the result guided by the color and shape of the original content. **Original is used when inpainting faces** because the general shape and anatomy were ok. We just want it to look a bit different.

If you want to regenerate something completely different from the original, for example removing a limb or hiding a hand, **latent noise** and **latent nothing** should be selected. These options initialize the masked area with something other than the original image. It will produce something completely different.

#### Denoising Strength

**Denoising strength** controls how much changes it will make compared with the original image. Nothing will change when you set it to 0. You will get an unrelated inpainting when you set it to 1.

0.4 is usually a good starting point. Increase if you want more changes.

#### Batch Size

Make sure to **generate a few images at a time** so that you can choose the best ones. Set the **seed** to -1 so that every image is different.

<table><tbody><tr><td>Prompt</td><td>(Same as original)</td></tr><tr><td>Sampling steps</td><td>20</td></tr><tr><td>Seed</td><td>-1</td></tr><tr><td>Image size</td><td>704 x 512</td></tr><tr><td>Face restoration</td><td>Codeformer</td></tr><tr><td>Sampling method</td><td>Euler a</td></tr><tr><td>Model</td><td>Stable Diffusion v1.5 inpainting</td></tr><tr><td>Mask content</td><td>latent noise or latent nothing</td></tr><tr><td>Inpaint at full resolution</td><td>On</td></tr><tr><td>Denoising strength</td><td>0.75</td></tr></tbody></table>

### Inpainting Results

Below are some of the inpainted images.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/tmp1enh7xr0-1.png?resize=480%2C349&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/tmpm_6azlsf.png?resize=480%2C349&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/tmp4dhbazk1-1.png?resize=480%2C349&ssl=1)

Inpainted images

### One More Round of Inpainting

I like the last one but there’s an extra hand under the newly inpainted arm. Follow similar steps of uploading this image and creating a mask. **Masked content** needs to be set to **latent noise** to generate something completely different.

The hand under the arm is removed with the second round of inpainting:

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/tmp77hnb1kr.png?resize=480%2C349&ssl=1)](https://stable-diffusion-art.com/inpainting_basics/tmp77hnb1kr/)

Use inpainting to remove the extra hand under the arm.

And this is my final image.

A side-by-side comparison

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/image-12.png?resize=480%2C245&ssl=1)](https://stable-diffusion-art.com/inpainting_basics/image-12/)

Left: original. Right: inpainted 2 times.

Inpainting is an iterative process. You can apply it as many time you want to refine an image.

See this [post](https://stable-diffusion-art.com/how-to-remove-a-person-with-ai-inpainting/) for another more extreme example of inpainting.

## Adding New Objects

Sometimes you want to add something new to the image.

Let’s try adding a hand fan to the picture.

First upload the image to inpainting canvas and create a mask around the chest and right arm.

Add prompt “holding a hand fan” to the beginning of the original prompt. The prompt for inpainting is

> (holding a hand fan: 1.2), \[emma watson: amber heard: 0.5\], (long hair:0.5), headLeaf, wearing stola, vast roman palace, large window, medieval renaissance palace, ((large room)), 4k, arstation, intricate, elegant, highly detailed

Adding new objects to the original prompt ensures consistency in style. You can adjust the [keyword weight](https://stable-diffusion-art.com/fine-tune-your-ai-images-with-these-simple-prompting-techniques/#Adjust_keyword_strength_using_weight) (1.2 above) to make the fan show.

Set **masked content** as **latent noise**.

Adjust **denoising strength** and **CFG scale** to fine-tune the inpainted images.

After some experimentation, our mission is accomplished:

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/image-13.png?resize=480%2C349&ssl=1)

Adding a hand fan with inpainting.

## Explanation of Inpainting Parameters

### Denoising Strength

Denoising strength controls how much respect the final image should pay to the original content. Setting it to 0 changes nothing. Setting to 1 you got an unrelated image.

Set to a low value if you want small change and high value if you want big change.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/image-9.png?resize=480%2C272&ssl=1)

Changing denoising strength. Set to low value if you want small change and high value if you want big change.

### CFG Scale

Similar to usage in [text-to-image](https://stable-diffusion-art.com/know-these-important-parameters-for-stunning-ai-images/#CFG_Scale), **Classifier Free Guidance scale** is a parameter to control how much the model should respect your prompt.

1–Mostly ignore your prompt.  
3–Be more creative.  
7–A good balance between following the prompt and freedom.  
15–Adhere more to prompt.  
30–Strictly follow the prompt.

### Masked Content

Masked content controls how the masked area are initialized.

- **Fill**: Initialize with a highly blurred of the original image.
- **Original**: Unmodified.
- **Latent noise**: Masked area initialized with **fill** and random noise is added to the latent space.
- **Latent zero**: Like latent noise except no noise is added to the latent space.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/image-10.png?resize=480%2C453&ssl=1)

Masked content.

### Inpaint at Full Resolution

Inpaint the masked area at full resolution, then scale down to the original size. This helps to increase the quality of the inpainting.

When inpainting a small area, turning on full resolution is critical to the quality of the final image.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/11/image-11.png?resize=314%2C316&ssl=1)

Inpaint at full resolution: Left: Off. Right: On.

## Tips for Inpainting

Successful inpainting requires patient and skill. Here are some take homes for using inpainting

- Inpaint one small area at a time.
- Inpaint at full resolution when inpainting faces or objects with fine details.
- Play with **masked content** to see which one works the best.
- If nothing works well within AUTOMATIC1111’s settings, use software like Photoshop or GIMP to paint the area of interest with the rough shape and color you wanted. Upload that image and inpaint with original content.

---

#AI #article
