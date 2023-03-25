---
created: 2023-01-30T16:28:23 (UTC -05:00)
tags: []
source: https://stable-diffusion-art.com/install-windows/
author: 
---

# How to Install Stable Diffusion on Windows (AUTOMATIC1111) - Stable Diffusion Art

> ## Excerpt
> We will go through how to install the popular Stable Diffusion software AUTOMATIC1111 on Windows step-by-step.

---

We will go through how to install the popular Stable Diffusion software AUTOMATIC1111 on Windows step-by-step.

Stable Diffusion is a text-to-image AI that can be run on consumer-grade PC with a GPU. After this tutorial, you will be able to generate AI images on your own PC.

Contents \[[hide](https://stable-diffusion-art.com/install-windows/#)\]

- [Systems requirements](https://stable-diffusion-art.com/install-windows/#Systems_requirements)
- [Installation steps](https://stable-diffusion-art.com/install-windows/#Installation_steps)
    - [Step 1: Install python](https://stable-diffusion-art.com/install-windows/#Step_1_Install_python)
    - [Step 2: Install git](https://stable-diffusion-art.com/install-windows/#Step_2_Install_git)
    - [Step 3: Clone web-ui](https://stable-diffusion-art.com/install-windows/#Step_3_Clone_web-ui)
    - [Step 4: Download model file](https://stable-diffusion-art.com/install-windows/#Step_4_Download_model_file)
    - [Step 5: Run webui](https://stable-diffusion-art.com/install-windows/#Step_5_Run_webui)
- [Options](https://stable-diffusion-art.com/install-windows/#Options)
- [Next Step](https://stable-diffusion-art.com/install-windows/#Next_Step)
- [Frequently Asked Questions](https://stable-diffusion-art.com/install-windows/#Frequently_Asked_Questions)

## Systems Requirements

Your PC should be running Windows 10 or higher with a **discrete Nvidia video card** (GPU) with 4 GB VRAM or more. An integrated GPU will not work.

If your PC does not meet these requirements, alternatives are

- Cloud service–[Google Colab](https://stable-diffusion-art.com/automatic1111-colab/).
- [Mac Apple Silicon M1/M2](https://stable-diffusion-art.com/install-mac/).

## Installation Steps

### Step 1: Install Python

You will need [Python 3.10.6](https://www.python.org/downloads/release/python-3106/) to run Stable Diffusion. Select 64-bit windows installer, or use this [direct download link](https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe).

[![windows installer for Python.](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-48.png?resize=480%2C288&ssl=1)](https://stable-diffusion-art.com/install-windows/image-48-2/)

Download Python Windows installer.

Open the Python installer to start install.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-49.png?resize=480%2C297&ssl=1)](https://stable-diffusion-art.com/install-windows/image-49-2/)

Make sure **“Add Python 3.10 to PATH” is checked**. Click **“Install Now”** to start install.

If you encounter error, it’s most likely because you have previously installed Python. Remove any previously installed Python versions before re-installing 3.10.6. You can do that in **Control Panel** → **Add or remove programs**.

### Step 2: Install Git

[Git](https://git-scm.com/) is a code repository management system. You will need it to install and update AUTOMATIC1111.

Go to [this page](https://git-scm.com/download/win) to download the windows version.

Open the installer. Click **Install** to accept the license and install the software.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/Screenshot_20221215_060231.png?resize=480%2C368&ssl=1)](https://stable-diffusion-art.com/install-windows/screenshot_20221215_060231/)

Follow the instruction to complete the install.

### Step 3: Clone Web-ui

This is the most difficult step…

Press the **Window** key (Should be on the left of the space bar on your keyboard), a search window should pop up. Type `cmd`.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-50.png?resize=480%2C379&ssl=1)](https://stable-diffusion-art.com/install-windows/image-50-2/)

Click on **Command Prompt**. The command prompt window would show up.

First make sure you are in your home folder by typing the following command and press Enter. (Tip: You should be able to use right click to paste in Command Prompt.)

```
cd %userprofile%
```

You should see your prompt shows something like `C:\Users\YOUR_USER_NAME`\>.

Next type the following command and press Enter to clone the AUTOMATIC1111 repository.

```
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
```

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-51.png?resize=480%2C278&ssl=1)](https://stable-diffusion-art.com/install-windows/image-51-2/)

A folder called `stable-diffusion-webui` should be created in your home directory.

It’s ok to clone the repository in a different folder instead of `%userprofile%`, as long as you can find the newly created `stable-diffusion-webui` folder. You will need to change the folder location accordingly in the following steps.

### Step 4: Download Model File

Next, go to the newly created folder in **File Explorer**. Put in

```
%userprofile%\stable-diffusion-webui
```

in the address bar and press enter.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-52.png?resize=480%2C241&ssl=1)](https://stable-diffusion-art.com/install-windows/image-52-2/)

Navigate to the folder **models** and then **Stable-diffusion**. You should see a file `Put Stable Diffusion checkpoints here.txt` like below.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-53.png?resize=480%2C368&ssl=1)](https://stable-diffusion-art.com/install-windows/image-53-2/)

Download the [Stable Diffusion v1.5](https://stable-diffusion-art.com/models/#Stable_diffusion_v15) model checkpoint file ([download link](https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.ckpt)). Put it in that folder.

### Step 5: Run Webui

Now in File Explorer, go back to the `stable-diffusion-webui` folder. That is go back up two levels, or type

```
%userprofile%\stable-diffusion-webui
```

again in the address bar.

Find a file called `webui-user.bat`. **Double click** to run and complete the install.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-54.png?resize=480%2C361&ssl=1)](https://stable-diffusion-art.com/install-windows/image-54-2/)

This last step is going to take a while. When it is done, you will see a message

> Running on local URL: http://127.0.0.1:7860

like below.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-55.png?resize=480%2C273&ssl=1)](https://stable-diffusion-art.com/install-windows/image-55/)

In your web browser, go to the URL

> http://127.0.0.1:7860/

You should see the AUTOMATIC1111 webui! Put in a prompt (e.g. “a cat”) and hit **Generate** to test if Stable Diffusion is running correctly.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-56.png?resize=480%2C215&ssl=1)](https://stable-diffusion-art.com/install-windows/image-56/)

When you are done using Stable Diffusion, close the `cmd` black window to shut down Stable Diffusion.

To run Stable Diffusion again, you just need to double click the `webui-user.bat`.

## Options

You should be able to speed up Stable Diffusion with the `--xformers` option. If you have less than 8 GB VRAM on GPU, it is a good idea to turn on `--medvram` option to conserve memory, so that you can generate more images at a time.

To enable them, right click on the file `webui-user.bat` and select **Edit**. (You may need to select “Show more Options” first if you are using Windows 11).

Replace the line

```
set COMMANDLINE_ARGS=
```

With

```
set COMMANDLINE_ARGS=--xformers --medvram
```

Save and close the file.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-57.png?resize=480%2C243&ssl=1)](https://stable-diffusion-art.com/install-windows/image-57/)

Double click the `webui-user.bat` file to run Stable Diffusion.

## Next Step

That’s it! Hope you will have fun making AI images.

If you are new to Stable Diffusion, check out the [Quick Start Guide](https://andrewongai.gumroad.com/l/stable_diffusion_quick_start) for some quick tips to use Stable Diffusion.

Head to our [beginner’s series](https://stable-diffusion-art.com/beginners-guide/) to learn Stable Diffusion step by step.

Check out this [prompt generator](https://andrewongai.gumroad.com/l/stable_diffusion_prompt_generator) for building high-quality prompts.

## Frequently Asked Questions

**Does it work on AMD GPU?**  
No, you have to have an NVIDIA GPU.

**Is there a easier way to install AUTOMATIC1111?**  
The above are from the official install instructions. Two alternatives:

- Recently they started to tag [release builds](https://github.com/AUTOMATIC1111/stable-diffusion-webui/tags). They are supposed to work after download and unzip.
- There’s an unofficial easy [installer for Windows](https://github.com/EmpireMediaScience/A1111-Web-UI-Installer) you can try.

**I tried everything but still does not work.**  
You can use [Google Colab](https://stable-diffusion-art.com/automatic1111-colab/) to run AUTOMATIC1111. In fact this is what I use most of the time. The notebook launches AUTOMATIC1111 with 1 mouse click.  

---

#AI #article
