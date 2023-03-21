---
created: 2023-01-30T16:28:28 (UTC -05:00)
tags: []
source: https://stable-diffusion-art.com/install-stable-diffusion-2-1/
author: 
---

# How to Install Stable Diffusion 2.1 in AUTOMATIC1111 GUI - Stable Diffusion Art

> ## Excerpt
> Stable diffusion 2.1 was released on Dec 7, 2022.

---

Stable diffusion 2.1 was [released](https://stability.ai/blog/stablediffusion2-1-release7-dec-2022) on Dec 7, 2022.

Those who have used [2.0](https://stable-diffusion-art.com/how-to-run-stable-diffusion-2-0/) has been scratching their head on how to make the most out of it. While we see some good images here or there, most of us went back to [v1.5](https://stable-diffusion-art.com/models/#Stable_diffusion_v15) for their business.

See step-by-step guide for [installing AUTOMATIC1111 on Windows](https://stable-diffusion-art.com/install-windows/).

The difficulty was in part caused by (1) using a new language model that is trained from scratch, and (2) the training dataset was heavily censored with NSFW filter.

The second part would have been fine, but the filter was quite inclusive and has removed substantial amount of good-quality data. 2.1 promised to bring them back.

This tutorial will cover installing and using 2.1 models in [AUTOMATIC1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui) GUI, so that you can make your judgement by using it.

Contents \[[hide](https://stable-diffusion-art.com/install-stable-diffusion-2-1/#)\]

- [2.1 models variants](https://stable-diffusion-art.com/install-stable-diffusion-2-1/#21_models_variants)
- [Install base software](https://stable-diffusion-art.com/install-stable-diffusion-2-1/#Install_base_software)
- [Download Stable diffusion 2.1 model](https://stable-diffusion-art.com/install-stable-diffusion-2-1/#Download_Stable_diffusion_21_model)
    - [2.1 base model (512-base)](https://stable-diffusion-art.com/install-stable-diffusion-2-1/#21_base_model_512-base)
    - [2.1 model (768)](https://stable-diffusion-art.com/install-stable-diffusion-2-1/#21_model_768)
- [How to use 2.1 model](https://stable-diffusion-art.com/install-stable-diffusion-2-1/#How_to_use_21_model)
- [Troubleshooting](https://stable-diffusion-art.com/install-stable-diffusion-2-1/#Troubleshooting)
- [Tips for using 2.1](https://stable-diffusion-art.com/install-stable-diffusion-2-1/#Tips_for_using_21)
    - [Tip 1: Write more](https://stable-diffusion-art.com/install-stable-diffusion-2-1/#Tip_1_Write_more)
    - [Tip 2: Use negative prompt](https://stable-diffusion-art.com/install-stable-diffusion-2-1/#Tip_2_Use_negative_prompt)
    - [Tip 3: Use correct image size](https://stable-diffusion-art.com/install-stable-diffusion-2-1/#Tip_3_Use_correct_image_size)

## 2.1 Models Variants

There are two text-to-image models available:

- [**2.1 base model**](https://huggingface.co/stabilityai/stable-diffusion-2-1-base): Default image size is 512×512 pixels
- [**2.1 model**](https://huggingface.co/stabilityai/stable-diffusion-2-1): Default image size is 768×768 pixels

The 768 model is capable of generating larger images. You can set the image size to 768×768 without worrying about the infamous [two heads](https://stable-diffusion-art.com/common-problems-in-ai-images-and-how-to-fix-them/#Two-head_problems) issue.

This is especially useful for generating larger scene with small characters. The faces can be generated a bit clearer than the 512 model, increasing the chance of success of the downstream [upscaling](https://stable-diffusion-art.com/ai-upscaler/) and [face restoration](https://stable-diffusion-art.com/common-problems-in-ai-images-and-how-to-fix-them/#Garbled_faces_and_eyes_problems).

The downside of the 768 model is it takes longer to generate images. The larger images may limit the batch size, depending on how much VRAM your GPU has.

## Install Base Software

We will go through how to use Stable Diffusion 2.0 in AUTOMATIC1111 GUI.

This GUI can be installed quite easily in [Windows systems](https://stable-diffusion-art.com/install-windows/), or follow the [installation instruction](https://github.com/AUTOMATIC1111/stable-diffusion-webui#automatic-installation-on-windows) on your respective environment. Ideally, you should have a dedicated GPU card with at least 6GB VRAM.

If you have already have this GUI, make sure it is up-to-date by running the following command in terminal under its installation location (`stable-diffusion-webui` folder).

```
git pull
```

## Download Stable Diffusion 2.1 Model

### 2.1 Base Model (512-base)

1. Download the model file ([v2-1\_512-ema-pruned.ckpt](https://huggingface.co/stabilityai/stable-diffusion-2-1-base/resolve/main/v2-1_512-ema-pruned.ckpt))
2. Download the [config file](https://raw.githubusercontent.com/Stability-AI/stablediffusion/main/configs/stable-diffusion/v2-inference.yaml), rename it to `v2-1_512-ema-pruned.yaml`

Put both of them in the model directory:

```
stable-diffusion-webui/models/Stable-diffusion
```

### 2.1 Model (768)

1. Download the model file ([v2-1\_768-ema-pruned.ckpt](https://huggingface.co/stabilityai/stable-diffusion-2-1/resolve/main/v2-1_768-ema-pruned.ckpt))
2. Download the [config file](https://raw.githubusercontent.com/Stability-AI/stablediffusion/main/configs/stable-diffusion/v2-inference-v.yaml), rename it to `v2-1_768-ema-pruned.yaml`

Put both of them in the model directory:

```
stable-diffusion-webui/models/Stable-diffusion
```

## How to Use 2.1 Model

To use the 768 version of Stable Diffusion 2.1 model, select `v2-1_768-ema-pruned.ckpt` in the **Stable Diffusion checkpoint** dropdown menu on top left.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-38.png?resize=480%2C82&ssl=1)

The model is designed to generate 768×768 images. So set the image width and/or height to 768 to get the best result.

To use the base model, select `v2-1_512-ema-pruned.ckpt` instead.

## Troubleshooting

Something you can try if your install doesn’t work.

- See if your AUTOMATIC1111 GUI is outdated. In terminal, use the command `git pull` under the `stable-diffusion-webui` directory and restart the GUI.
- Check if the yaml file is downloaded correctly. Its content should be a simple text file, not with HTML tags.
- Check if the yaml file is correctly renamed as described in the previous section.
- If 2.0 or 2.1 is generating black images, enable full precision with startup arguments `--no-half` or `--xformers` optimization.

## Tips for Using 2.1

I definitely think 2.1 is an improvement over 2.0. The images look better and require less effort in engineering the prompt.

So I am deleting my 2.0 models.

Here are some tips I found using when using 2.1.

### Tip 1: Write More

Similar to [2.0](https://stable-diffusion-art.com/how-to-run-stable-diffusion-2-0/), **prompt needs to be very specific and detailed** to get the image you want. Unlike v1 models, simple prompt usually won’t go well with 2.1.

### Tip 2: Use Negative Prompt

Many have already found that **negative prompt** is very important for v2 models. I would suggest to keep a boilerplate negative prompt for portraits where many things can go wrong. In fact, Stability uses

> *cropped, lowres, poorly drawn face, out of frame, poorly drawn hands, blurry, bad art, blurred, text, watermark, disfigured, deformed, closed eyes*

in a demo image in their press release.

### Tip 3: Use Correct Image Size

Finally, **set the correct image size**. Set at least one side to be 512 px for 512-base model and 768 px for the 768 model.

Have fun with 2.1!

---

#AI #article
