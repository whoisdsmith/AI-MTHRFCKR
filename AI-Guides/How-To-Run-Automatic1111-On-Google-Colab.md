---
created: 2023-01-30T16:26:36 (UTC -05:00)
tags: []
source: https://stable-diffusion-art.com/automatic1111-colab/
author: 
---

# How to Run AUTOMATIC1111 on Google Colab - Stable Diffusion Art

> ## Excerpt
> This is a step-by-step guide for using the Google Colab notebook in the Quick Start Guide to run AUTOMATIC1111. This is one of the easiest way to use

---

This is a step-by-step guide for using the Google Colab notebook in the [Quick Start Guide](https://andrewongai.gumroad.com/l/stable_diffusion_quick_start) to run AUTOMATIC1111. This is one of the easiest way to use AUTOMATIC1111 because you don’t need to deal with install.

See install instructions on [Windows PC](https://stable-diffusion-art.com/install-windows/) and [Mac](https://stable-diffusion-art.com/install-mac/) if you prefer to run locally.

## What is AUTOMATIC1111?

You should know what [AUTOMATIC1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui) is if you want to be a serious user of Stable Diffusion. You can choose not to use it. But you need to know what it can do because it is the gold standard in terms of features, though not necessarily software stability…

Stable Diffusion is a machine learning model. By itself is not very user-friendly. You will need to write codes to use it. It’s kind of a hassle. Most users use a **GUI** (Graphical User Interface) to use Stable Diffusion. Instead of writing codes, we write prompt in a text box and click some buttons to generate images.

AUTOMATIC1111 was one of the first GUI developed for Stable Diffusion. Although it associates with AUTOMATIC1111’s GitHub account, it has been a community effort to develop this software.

AUTOMATIC1111 is feature-rich: You can use text-to-image, image-to-image, upscaling, depth-to-image, run and train custom models all within this GUI. Many of the tutorials in this site are demonstrated with this GUI.

## What is Google Colab?

[Google Colab](https://colab.research.google.com/) is an interactive computing service offered by Google. You can use it if you have a free Google account. You can use Colab for free but you may get disconnected during busy hours or have been using too much lately.

They have three paid plans–**Pay As You Go, Colab Pro and Colab Pro+**. If you decided to pay, **I recommend using the Colab Pro plan**. It gives you 100 compute unit per month which is about 50 hours on a standard GPU. (It’s a steal) You can also request high RAM machines which may come handy if you need to generate large or many images.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-34.png?resize=480%2C256&ssl=1)](https://stable-diffusion-art.com/automatic1111-colab/image-34-3/)

With a paid plan, you can choose to use **Premium GPU**, which is a A100 processor. That comes in handy when you need to train Dreambooth models fast.

If you use Colab for AUTOMATIC1111, be sure to disconnect and shut down the notebook when you are done. It will consume compute units when notebook is kept open.

## Step-by-step Instructions to Run Colab Notebook

**Step 1**. Open the Colab notebook in [Quick Start Guide](https://andrewongai.gumroad.com/l/stable_diffusion_quick_start). You should see the notebook with the second cell like below.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-36.png?resize=480%2C351&ssl=1)](https://stable-diffusion-art.com/automatic1111-colab/image-36-3/)

**Step 2.** Review username and password. You will need the credential after you start AUTOMATIC11111.

**Step 3.** Check `SAVE_IN_GOOGLE_DRIVE` will save the followings automatically in your Google Drive

- All images generated
- GUI Settings

They will be saved under the directory name specified in `output_path`. You will need to grant permission to access Google Drive if you check this option.

**Step 4**. Check the models you want to load. Currently we offer v1.4, v1.5, v1.5 inpainting, F222, anything v3, inkpunk diffusion, Mo Di diffusion, v2.1-512, v2.1-768 and v2 depth model.

If you are a first time user, you can just select v1.5 model.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-37.png?resize=464%2C453&ssl=1)](https://stable-diffusion-art.com/automatic1111-colab/image-37-3/)

**Step 5.** You can optionally include models in your Google Drive, such as the ones created from the [Dreambooth notebook](https://stable-diffusion-art.com/dreambooth/). You can include multiple models. Separate them with commas.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-38.png?resize=480%2C105&ssl=1)

**Step 6.** Click the Play button on left of the cell to start.

**Step 7.** Start up should complete within a few minutes. How long it takes depends on how many models you include. When it is done, you should see the message like below.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-39.png?resize=480%2C213&ssl=1)](https://stable-diffusion-art.com/automatic1111-colab/image-39-3/)

**Step 8**. Follow the `gradio.live` link to start AUTOMATIC1111.

**Step 9**. Enter username and password you specified in the notebook.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-40.png?resize=350%2C308&ssl=1)](https://stable-diffusion-art.com/automatic1111-colab/image-40-3/)

**Step 10**. You should see the AUTOMATIC1111 GUI after you login.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-41.png?resize=480%2C223&ssl=1)](https://stable-diffusion-art.com/automatic1111-colab/image-41-3/)

Put in “a cat” in the prompt text box and press **Generate** to test using Stable Diffusion. You should see it generates an image of a cat.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-45.png?resize=480%2C242&ssl=1)](https://stable-diffusion-art.com/automatic1111-colab/image-45-3/)

## Ngrok (Optional)

If you run into display issues with the GUI, you can try using ngrok instead of Gradio to estabish the public connection.

You will need to setup a free account and get an **authoken**.

1. Go to [https://ngrok.com/](https://ngrok.com/)
2. create an account
3. verify email
4. Copy the authoken from [https://dashboard.ngrok.com/get-started/your-authtoken](https://dashboard.ngrok.com/get-started/your-authtoken) and paste in ngrok field in the notebook

The Stable Diffusion cell in the notebook should look like below after you put in your ngrok authtoken.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-42.png?resize=480%2C221&ssl=1)](https://stable-diffusion-art.com/automatic1111-colab/image-42-3/)

Click the play button on the left to start running. When it is done loading, you will see a link to  ngrok.io in the output under the cell. **Click the ngrok.io link to start AUTOMATIC1111.** The first link in the example output below is the ngrok.io link.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-43.png?resize=480%2C139&ssl=1)](https://stable-diffusion-art.com/automatic1111-colab/image-43-3/)

When you visit the ngrok link, it should show a message like below

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-44.png?resize=480%2C217&ssl=1)](https://stable-diffusion-art.com/automatic1111-colab/image-44-3/)

 Click on Visit Site to Start AUOTMATIC1111 GUI. Occasionally, you will see a warning message about the site is not safe to visit. It was likely because someone used ngrok to put up something malicious with the same link before. Since you are the one who created this link, you can ignore the safety warning and proceed.

## Next Step

If you are new to Stable Diffusion, check out the [Absolute beginner’s guide](https://stable-diffusion-art.com/beginners-guide/).

---

#AI #article
