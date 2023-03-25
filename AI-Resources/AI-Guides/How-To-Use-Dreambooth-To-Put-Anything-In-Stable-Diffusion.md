---
created: 2023-01-30T16:16:05 (UTC -05:00)
tags: []
source: https://stable-diffusion-art.com/dreambooth/
author: 
---

# How to Use Dreambooth to Put Anything in Stable Diffusion - Stable Diffusion Art

> ## Excerpt
> Dreambooth is a way to put anything -- your loved one, your dog, your favorite toy -- into a Stable Diffusion model. We will introduce what Dreambooth is, how

---

Dreambooth is a way to put anything—your loved one, your dog, your favorite toy—into a Stable Diffusion model. We will introduce what Dreambooth is, how does it work, and how to perform the training.

This tutorial is aim for people who have used Stable Diffusion but have not used Dreambooth before.

Do you know many [custom models](https://stable-diffusion-art.com/models/) are trained using Dreambooth? After completing this tutorial, you will know how to make your own.

You can skip to the [training part](https://stable-diffusion-art.com/dreambooth/#Step-by-step_guide) if you are only interested in the training.

Contents \[[hide](https://stable-diffusion-art.com/dreambooth/#)\]

- [What is Dreambooth?](https://stable-diffusion-art.com/dreambooth/#What_is_Dreambooth)
    - [How does Dreambooth work?](https://stable-diffusion-art.com/dreambooth/#How_does_Dreambooth_work)
    - [What you need to train Dreambooth](https://stable-diffusion-art.com/dreambooth/#What_you_need_to_train_Dreambooth)
- [Step-by-step guide](https://stable-diffusion-art.com/dreambooth/#Step-by-step_guide)
    - [Get training images](https://stable-diffusion-art.com/dreambooth/#Get_training_images)
    - [Resize your images](https://stable-diffusion-art.com/dreambooth/#Resize_your_images)
    - [Training](https://stable-diffusion-art.com/dreambooth/#Training)
    - [Testing the model](https://stable-diffusion-art.com/dreambooth/#Testing_the_model)
- [Using the model](https://stable-diffusion-art.com/dreambooth/#Using_the_model)
- [Further readings](https://stable-diffusion-art.com/dreambooth/#Further_readings)

## What is Dreambooth?

Published in 2022 by Google research team, [Dreambooth](https://dreambooth.github.io/) is a technique to fine-tune diffusion models (like Stable Diffusion) by injecting a custom subject to the model.

Why does it call Dreambooth? According to the Google research team,

> It’s like a photo booth, but once the subject is captured, it can be synthesized wherever your dreams take you.

Sounds great! But how well does it work? Below is an example in the research article. Using just 3 images of a particular dog (Let’s call her **Devora**) as input, the dreamboothed model can generate images of Devora in different context.

[![dreambooth examples from the dreambooth research article](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-13.png?resize=480%2C247&ssl=1)](https://stable-diffusion-art.com/?attachment_id=1118)

With as few as 3 training images, Dreambooth injects a custom subject to a diffusion model seamlessly.

### How Does Dreambooth Work?

You may ask, why can’t you simply train the model with additional steps with those images? The issue is that doing so is known to cause catastrophic failure due to *overfitting* (since the dataset is quite small) and *[language drift](https://arxiv.org/abs/1909.04499)*.

Dreambooth resolves these problems by

1. Using a **rare word** for the new subject (Notice I used a rare name **Devora** for the dog) so that it does not have a lot of meaning in the model in the first place.
2. **Prior preservation** on class: In order to preserve the meaning of the **class** (dog in the above case), the model is fine-tuned in a way that the subject (Devora) is injected while the image generation of the class (dog) is preserved.

There’s another similar technique called [textual inversion](https://textual-inversion.github.io/). The difference is that Dreambooth fine-tunes the whole model, while textual inversion injects a new word, instead of reusing a rare one, and fine-tunes only the text embedding part of the model.

### What You Need to Train Dreambooth

You will need three things

1. A few custom images
2. An unique identifier
3. A class name

In the above example. The unique identifier is **Devora**. The class name is **dog**.

Then you will need to construct your **instance prompt**:

> a photo of \[unique identifier\] \[class name\]

And a **class prompt**:

> a photo of \[class name\]

In the above example, **instance prompt** is

> a photo of Devora dog

Since Devora is a dog, the **class prompt** is

> a photo of a dog

Now you understand what you need, let’s dive into the training!

## Step-by-step Guide

### Get Training Images

As in any machine learning tasks, high-quality training data is the single most important factor to your success.

Take 3-10 picture of your custom subject. The picture should be taken from different angles.

The subject should also be in a variety of background so that the model can differentiate the subject against the background.

I will use this toy in the tutorial.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/3E0FD8C0-2A5B-4F60-AB75-46E7E4A54A39_1_105_c.jpeg?resize=480%2C480&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/0E5AFC83-B759-4FE9-8E16-A60774E1DEDF_1_105_c.jpeg?resize=480%2C480&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/7BFAC61C-85ED-4E82-8B8D-F518F9C54BA8_1_105_c.jpeg?resize=480%2C480&ssl=1)

Images of the subject.

### Resize Your Images

In order to use the images in training, you will first need to resize them to 512×512 pixels for training with v1 models.

[BIRME](https://www.birme.net/?target_width=512&target_height=512) is a convenient site for resizing images.

1. Drop your images to the BIRME page.
2. Adjust the canvas of each image so that it shows the subject adequately.
3. Make sure the width and height are both 512 px.
4. Press **SAVE FILES** to save the resized images to your computer.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-14.png?resize=480%2C270&ssl=1)](https://stable-diffusion-art.com/?attachment_id=1122)

Alternatively, you can download my resized images if you just want to go through the tutorial.

### Training

I recommend using Google Colab for training because it saves you trouble of setting up. The following notebook is modified from [Shivam Shrirao](https://github.com/ShivamShrirao)‘s repository but is made more user-friendly. Follow the repository’s instruction if you prefer other setups.

The whole training takes about 30 minutes. If you don’t use Google Colab much, you probably can complete the training without getting disconnected. Purchase some compute credits to avoid the frustration of getting disconnected. As of Dec 2022, $10 USD will get you 50 hours so its not much of a cost.

The notebook will save the model to your [Google Drive](https://drive.google.com/drive/my-drive). Make sure you have at least 2GB if you choose `fp16` (recommended) and 4GB if you don’t.

1. Open the [Colab notebook](https://colab.research.google.com/github/sagiodev/stablediffusion_webui/blob/master/DreamBooth_Stable_Diffusion_SDA.ipynb).
2. You don’t need to change MODEL\_NAME if you want to train from [Stable Diffusion v1.5](https://stable-diffusion-art.com/models/#Stable_diffusion_v15) model (Recommended).
3. Put in **instance prompt** and **class prompt**. For my images, I name my toy rabbit zwx so my instance prompt is “photo of zwx toy” and my class prompt is “photo of a toy”.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-15.png?resize=480%2C381&ssl=1)](https://stable-diffusion-art.com/?attachment_id=1123)

4\. Click the Play button ( ![▶️](https://s.w.org/images/core/emoji/14.0.0/svg/25b6.svg) ) on the left of the cell to start processing.

5\. Grant permission to access Google Drive. Currently there’s no easy way to download the model file except through saving to Google Drive.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-16.png?resize=480%2C155&ssl=1)](https://stable-diffusion-art.com/?attachment_id=1124)

6\. Press **Choose Files** to upload the resized images.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-17.png?resize=480%2C284&ssl=1)](https://stable-diffusion-art.com/?attachment_id=1125)

7\. It should take about 30 minutes to complete the training. When it is done, you should see a few sample images generated from the new model.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-19.png?resize=480%2C115&ssl=1)](https://stable-diffusion-art.com/?attachment_id=1133)

8\. Your custom model will be saved in your [Google Drive](https://drive.google.com/drive/my-drive), under the folder `Dreambooth_model`. Download the model checkpoint file and [install](https://stable-diffusion-art.com/models/#How_to_install_and_use_a_model) it in your favorite GUI.

That’s it!

### Testing the Model

You can also use the second cell of the notebook to test using the model.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-18.png?resize=480%2C336&ssl=1)](https://stable-diffusion-art.com/?attachment_id=1127)

Using the prompt

> oil painting of zwx in style of van gogh

with my newly trained model, I am happy with what I got:

![This image has an empty alt attribute; its file name is download-6.png](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/download-6.png?w=480&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/download-7.png?resize=480%2C480&ssl=1)

Images from dreambooth model.

## Using the Model

You can use the model checkpoint file in AUTOMATIC1111 GUI. It is a free and full-feature GUI you can install on [Windows](https://stable-diffusion-art.com/install-windows/), [Mac](https://stable-diffusion-art.com/install-mac/) or running on [Google Colab](https://stable-diffusion-art.com/automatic1111-colab/).

If you have not used the GUI and the model file has been saved in your Google Drive, the easiest way is the Google Colab option. All you need to do is to put in the path to the model in Google Drive to use it. See the step-by-step [tutorial](https://stable-diffusion-art.com/automatic1111-colab/#Step-by-step_instructions_to_run_Colab_notebook) for more details.

## Further Readings

I recommend the following articles if you want to dive deeper into Dreambooth.

- [Training Stable Diffusion with Dreambooth using Diffusers–Huggingface blog](https://huggingface.co/blog/dreambooth)
- [Dreambooth training guide–nitrosocke](https://github.com/nitrosocke/dreambooth-training-guide)
- [BlueFaux’s dreamBooth guide](https://docs.google.com/document/d/1xHSHEohmCOLlhdCY0ox4EARFKKU29XbFd8ji8UgjGn4/edit)
- [The research paper](https://arxiv.org/abs/2208.12242)


---

#AI #article
