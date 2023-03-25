---
created: 2023-01-30T16:26:41 (UTC -05:00)
tags: []
source: https://stable-diffusion-art.com/install-mac/
author: 
---

# How to Install and Run Stable Diffusion on Apple Silicon M1/M2 Macs - Stable Diffusion Art

> ## Excerpt
> Stable Diffusion is a text-to-image AI that can be run on personal computer such as Mac M1 or M2. In this article, I will provide a step-by-step guide for

---

Stable Diffusion is a text-to-image AI that can be run on personal computer such as Mac M1 or M2. In this article, I will provide a step-by-step guide for installing and running Stable Diffusion on Mac.

You will need a Mac with Apple Silicon (M1 or M2) for reasonable speed. Ideally you will have 16 GB memory. You will likely need to wait longer for an image compared to using a similarly priced Windows PC with a discrete graphic card.

I will go through two install options

1. **[DiffusionBee](https://stable-diffusion-art.com/install-mac/#DiffusionBee)**. Easy to install but with smaller set of functions.
2. **[AUTOMATIC1111](https://stable-diffusion-art.com/install-mac/#AUTOMATIC1111)**. Feature-rich but a bit harder to install if you are not tech savvy.

Alternatively you can run Stable Diffusion in Google Colab. Check the [Quick Start Guide](https://andrewongai.gumroad.com/l/stable_diffusion_quick_start) for details.

Read this [install guide](https://stable-diffusion-art.com/install-windows/) if you want to install Stable Diffusion on a Windows PC.

Contents \[[hide](https://stable-diffusion-art.com/install-mac/#)\]

- [DiffusionBee](https://stable-diffusion-art.com/install-mac/#DiffusionBee)
    - [Install DiffusionBee on Mac](https://stable-diffusion-art.com/install-mac/#Install_DiffusionBee_on_Mac)
    - [Run DiffusionBee on Mac](https://stable-diffusion-art.com/install-mac/#Run_DiffusionBee_on_Mac)
- [AUTOMATIC1111](https://stable-diffusion-art.com/install-mac/#AUTOMATIC1111)
    - [Install AUTOMATIC1111 on Mac](https://stable-diffusion-art.com/install-mac/#Install_AUTOMATIC1111_on_Mac)
    - [Run AUTOMATIC1111 on Mac](https://stable-diffusion-art.com/install-mac/#Run_AUTOMATIC1111_on_Mac)
- [Next Steps](https://stable-diffusion-art.com/install-mac/#Next_Steps)

## DiffusionBee

This section shows you how to install and run DiffusionBee on Mac step-by-step.

### Install DiffusionBee on Mac

[DiffusionBee](https://diffusionbee.com/) is one of the easiest ways to run Stable Diffusion on Mac. It’s install process is no different from any other apps.

**Step 1:** Go to DiffusionBee’s [download page](https://diffusionbee.com/download) and download the installer for **MacOS–Apple Silicon**. A dmg file should be downloaded.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-24.png?resize=480%2C233&ssl=1)](https://stable-diffusion-art.com/install-mac/image-24-3/)

**Step 2:** Double click to run the downloaded **dmg** file in Finder. The following windows will show up.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-25.png?resize=480%2C332&ssl=1)](https://stable-diffusion-art.com/install-mac/image-25-3/)

**Step 3:** Drag the **DiffusionBee** icon on the left to the **Applications** folder on the right. Installation is now complete!

### Run DiffusionBee on Mac

You can use spotlight search bar to start StableBee. Press `command` + `spacebar` to bring up spotlight search. Type “DiffusionBee” and press `return` to start DiffusionBee.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-27.png?resize=480%2C100&ssl=1)](https://stable-diffusion-art.com/install-mac/image-27-3/)

It will download some models when it starts for the very first time.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-26.png?resize=480%2C367&ssl=1)](https://stable-diffusion-art.com/install-mac/image-26-3/)

When it is done, you can start using Stable Diffusion! Let’s try putting the prompt “a cat” in the prompt box and hit **Generate**.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-28.png?resize=480%2C287&ssl=1)](https://stable-diffusion-art.com/install-mac/image-28-3/)

Works pretty well! You can click the **option** button to customize your images such as image size and [CFG scale](https://stable-diffusion-art.com/know-these-important-parameters-for-stunning-ai-images/#CFG_Scale).

Go to the [Next Step](https://stable-diffusion-art.com/install-mac/#Next_Steps) section to see what to do next.

## AUTOMATIC1111

This section show you how to install and run AUTOMATIC1111 on Mac step-by-step.

DiffusionBee is easy to install but the functionality is pretty limited. If you are (or aspired to be) an advanced user, you will want to use an advanced GUI like [AUTOMATIC1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui). You will need this GUI if you want to follow my tutorials.

### Install AUTOMATIC1111 on Mac

**Step 1**: Install [Homebrew](https://brew.sh/), a package manager for Mac, if you haven’t already. Open the **Terminal** app, type the following command and press return.

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Step 2**: Install a few required packages. Open a new terminal and run the following command

```
brew install cmake protobuf rust python@3.10 git wget
```

**Step 3**: Clone the AUTOMATIC1111 repository by running the following command in the terminal

```
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui
```

A new folder `stable-diffusion-webui` should be created under your home directory.

**Step 5**: You will need a [model](https://stable-diffusion-art.com/models) to run Stable Diffusion. Use the following link to download the [v1.5 model](https://stable-diffusion-art.com/models/#Stable_diffusion_v15).

[Download link](https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.ckpt)

Put the file in the folder `stable-diffusion-webui/models/Stable-diffusion`. You can get there in the **Finder** app. In top menu, click **Go** and then **Home**. Double Click to the folders `stable-diffusion-webui`, and then `models`, and then `Stable-diffusion`.

When you are done with this step, the `Stable-diffusion` folder should two files like below.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-29.png?resize=480%2C258&ssl=1)](https://stable-diffusion-art.com/install-mac/image-29-3/)

### Run AUTOMATIC1111 on Mac

Follow the steps in this section to start AUTOMATIC1111 GUI for Stable Diffusion.

In terminal, run the following command

```
cd ~/stable-diffusion-webui;./webui.sh 
```

It will take a while when you run it for the very first time.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-31.png?resize=480%2C327&ssl=1)](https://stable-diffusion-art.com/install-mac/image-31-3/)

Open a web browser and go to the following URL to start Stable Diffusion.

```
http://127.0.0.1:7860/
```

You should see the AUTOMATIC1111 GUI. Put in a prompt “a cat” and press **Generate** to test using the GUI.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2023/01/image-32.png?resize=480%2C213&ssl=1)](https://stable-diffusion-art.com/install-mac/image-32-3/)

Close the terminal when you are done. Follow the steps in this section the next time when you want to run Stable Diffusion.

## Next Steps

Now you are able to run Stable Diffusion, below are some suggestions on what to learn next

- Check out how to [build good prompts](https://stable-diffusion-art.com/how-to-come-up-with-good-prompts-for-ai-image-generation/).
- Check out [this article](https://stable-diffusion-art.com/know-these-important-parameters-for-stunning-ai-images/) to learn what the parameters in GUI mean.
- Download [some new models](https://stable-diffusion-art.com/know-these-important-parameters-for-stunning-ai-images/) and have fun!


---

#AI #article
