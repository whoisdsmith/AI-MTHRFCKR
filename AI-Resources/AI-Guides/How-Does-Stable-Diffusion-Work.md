---
created: 2023-01-30T16:23:18 (UTC -05:00)
tags: []
source: https://stable-diffusion-art.com/how-stable-diffusion-work/
author: 
---

# How Does Stable Diffusion Work? - Stable Diffusion Art

> ## Excerpt
> Stable Diffusion is a deep learning model. We will dig deep into understanding how Stable Diffusion work under the hood.

---

Stable Diffusion is a deep learning model. We will dig deep into understanding how Stable Diffusion work under the hood.

Why do you need to know? Apart from being a fascinating subject on its own right, some understanding of the inner mechanics will make you a better artist. You will be able to use the tool correctly to achieve results in higher precision.

How does text-to-image different from image-to-image? What’s CFG value? What’s denoising strength? You will find the answer in this article.

Let’s dive in.

Contents \[[hide](https://stable-diffusion-art.com/how-stable-diffusion-work/#)\]

- [What can Stable Diffusion do?](https://stable-diffusion-art.com/how-stable-diffusion-work/#What_can_Stable_Diffusion_do)
- [Diffusion model](https://stable-diffusion-art.com/how-stable-diffusion-work/#Diffusion_model)
    - [Forward diffusion](https://stable-diffusion-art.com/how-stable-diffusion-work/#Forward_diffusion)
    - [Reverse diffusion](https://stable-diffusion-art.com/how-stable-diffusion-work/#Reverse_diffusion)
- [How training is done](https://stable-diffusion-art.com/how-stable-diffusion-work/#How_training_is_done)
    - [Reverse diffusion](https://stable-diffusion-art.com/how-stable-diffusion-work/#Reverse_diffusion-2)
- [Stable Diffusion model](https://stable-diffusion-art.com/how-stable-diffusion-work/#Stable_Diffusion_model)
    - [Latent diffusion model](https://stable-diffusion-art.com/how-stable-diffusion-work/#Latent_diffusion_model)
    - [Variational Autoencoder](https://stable-diffusion-art.com/how-stable-diffusion-work/#Variational_Autoencoder)
    - [Why is latent space possible](https://stable-diffusion-art.com/how-stable-diffusion-work/#Why_is_latent_space_possible)
    - [Reverse diffusion in latent space](https://stable-diffusion-art.com/how-stable-diffusion-work/#Reverse_diffusion_in_latent_space)
    - [What is VAE file?](https://stable-diffusion-art.com/how-stable-diffusion-work/#What_is_VAE_file)
- [Conditioning](https://stable-diffusion-art.com/how-stable-diffusion-work/#Conditioning)
    - [Text conditioning (text-to-image)](https://stable-diffusion-art.com/how-stable-diffusion-work/#Text_conditioning_text-to-image)
        - [Tokenizer](https://stable-diffusion-art.com/how-stable-diffusion-work/#Tokenizer)
        - [Embedding](https://stable-diffusion-art.com/how-stable-diffusion-work/#Embedding)
        - [Feeding embeddings to noise predictor](https://stable-diffusion-art.com/how-stable-diffusion-work/#Feeding_embeddings_to_noise_predictor)
- [Stable Diffusion step-by-step](https://stable-diffusion-art.com/how-stable-diffusion-work/#Stable_Diffusion_step-by-step)
    - [Text-to-image](https://stable-diffusion-art.com/how-stable-diffusion-work/#Text-to-image)
    - [Image-to-image](https://stable-diffusion-art.com/how-stable-diffusion-work/#Image-to-image)
    - [Inpainting](https://stable-diffusion-art.com/how-stable-diffusion-work/#Inpainting)
    - [Depth-to-image](https://stable-diffusion-art.com/how-stable-diffusion-work/#Depth-to-image)
- [What is CFG value?](https://stable-diffusion-art.com/how-stable-diffusion-work/#What_is_CFG_value)
    - [Classifier guidance](https://stable-diffusion-art.com/how-stable-diffusion-work/#Classifier_guidance)
    - [Classifier-free guidance](https://stable-diffusion-art.com/how-stable-diffusion-work/#Classifier-free_guidance)
        - [CFG value](https://stable-diffusion-art.com/how-stable-diffusion-work/#CFG_value)
- [Stable Diffusion v1 vs v2](https://stable-diffusion-art.com/how-stable-diffusion-work/#Stable_Diffusion_v1_vs_v2)
    - [Model difference](https://stable-diffusion-art.com/how-stable-diffusion-work/#Model_difference)
    - [Training data difference](https://stable-diffusion-art.com/how-stable-diffusion-work/#Training_data_difference)
    - [Outcome difference](https://stable-diffusion-art.com/how-stable-diffusion-work/#Outcome_difference)
    - [Some interesting reads](https://stable-diffusion-art.com/how-stable-diffusion-work/#Some_interesting_reads)

## What Can Stable Diffusion Do?

In the simplest form, Stable Diffusion is a **text-to-image mode**l. Give it a **text prompt**, it will return an image matching the text.

![Example of stable diffusion prompt and images.](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-77.png?resize=480%2C206&ssl=1)

Stable diffusion turns text prompt into images.

## Diffusion Model

Stable Diffusion belongs to a class of deep learning models called **Diffusion model**. They are **generative models**, meaning they are designed to generate new data similar to what they have seen in training. In case of Stable Diffusion, the data are images.

Why is it called diffusion model? Because its math looks very much like diffusion in physics. Let’s go through the idea.

Let’s say I trained a diffusion model with only two kinds of images: cats and dogs. In the figure below, the two peaks on left represent the groups of cat and dog images.

### Forward Diffusion

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-79.png?resize=480%2C209&ssl=1)

Forward diffusion turn a photo into noise. (Figure modified from [this article](https://arxiv.org/abs/2011.13456))

A **forward diffusion** process adds noise to a training image, gradually turning it to an uncharacteristic noise image. The forward process will turn **any** cat or dog image into a noise image. At the end, you won’t be able to tell whether they are originally a dog or a cat. (This is important)

This is similar to a drop of ink fell into a glass of water. The ink drop **diffuses** in water. After a few minutes, It randomly distributes itself throughout the water. You can no longer tell wether it originally fell at the center or near the rim.

Below is an example of image undergoing forward diffusion. The cat image turns to random noise.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-81.png?resize=480%2C210&ssl=1)

Forward diffusion of a cat image.

### Reverse Diffusion

Now comes the interesting part. What if we can **reverse** the diffusion? Like playing a video backward. Going backward in time. We will see where the ink drop was originally added.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-80.png?resize=480%2C225&ssl=1)

Reverse diffusion process recovers an image.

Starting from a noisy, meaningless image, **reverse diffusion** recovers a cat **OR** a dog image. This is the main idea.

On a technical level, every diffusion process has two parts: (1) drift or directed motion, and (2) random motion. The reverse diffusion drifts towards **either** cat or dog images, but nothing in between. That’s why the result can either be a cat or a dog.

## How Training is Done

The idea of reverse diffusion is surely clever and elegant. But the million-dollar question is “How can it be done?”.

In order to reverse diffusion, we need to know how much noise is added to an image. The answer is teaching a **neural network model to predict the noise added**. It is called the **noise predictor** in Stable Diffusion. It is a [U-Net model](https://en.wikipedia.org/wiki/U-Net). The training goes as follows.

1. Pick a training image like a photo of a cat.
2. Generate a random noise image.
3. Corrupt the training image by adding this noisy image up to a certain number of steps.
4. Teach the noise predictor to tell us the total noise added from the corrupted image. This is done by tuning its weights and showing it the correct answer.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-82.png?resize=480%2C275&ssl=1)

Noise is sequentially added at each step. Noise predictor estimates the total noise added up to each step.

After training, **we have a noise predictor capable of estimating the noise added to an image.**

### Reverse Diffusion

Now we have the noise predictor. How to use it?

We first **generate a completely random image and ask the noise predictor to tell us the noise**. We then subtract this estimated noise from the original image. Repeat this process for a few times. You will get an image of either a cat or a dog.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-84.png?resize=480%2C179&ssl=1)

Reverse diffusion works by subtracting the predicted noise from the image successively.

You may notice we have no control of generating a cat or dog’s image. We will address this when we talk about **conditioning**. For now, the image generation is **unconditioned**.

Now I need to tell you a bad news: What we just talked about is NOT how Stable Diffusion works! The reason is that the above diffusion process is in image space. **It is computationally very very slow.** You won’t be able to run on *any* single GPU, let alone the crappy GPU on your laptop.

**Image space is huge**. Think about it: a 512×512 image with 3 color channels (red, green and blue) is a 786,432 dimensional space! (You need to specify that many values for ONE image.)

Diffusion models like Google’s [Imagen](https://imagen.research.google/) and Open AI’s [DALL-E](https://openai.com/dall-e-2/) are in pixel space. They have used some tricks to make the model faster but still not enough.

### Latent Diffusion Model

Stable Diffusion is designed to solve the speed problem. Here’s how.

**Stable Diffusion is a latent diffusion model**. Instead of operating in the high-dimensional image space, it first compresses the image into the **latent space**. The latent space is 48 times smaller so it reaps the benefit of crunching a lot fewer numbers. That’s why its a lot faster.

### Variational Autoencoder

It is done using a technique called **variational autoencoder**. Yes, that’s exactly what the [VAE files](https://stable-diffusion-art.com/how-to-use-vae/) are but I will make it crystal clear later.

The Variational Autoencoder (VAE) neural network has two parts: (1) an encoder and (2) a decoder. Encoder compresses an image to a lower dimensional representation in the latent space. The decoder restores the image from the latent space.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-85.png?resize=480%2C224&ssl=1)

Variational autoencoder transforms the image to and from the latent space.

**The latent space of Stable Diffusion model is 4x64x64, 48 times smaller than the image pixel space.** All the forward and reverse diffusions we talked about are actually done in the latent space.

So during training, **instead of generating a noisy image, it generates a random tensor in latent space** (latent noise). Instead of corrupting an image with noise, it corrupts the representation of the image in latent space with the latent noise. **The reason for doing that is it is a lot faster since the latent space is smaller.**

### Why is Latent Space Possible

You may ask why can the VAE compress an image into the much smaller latent space without losing information? The reason is, unsurprisingly, natural images are not random. They have high regularity: A face follows certain spatial relationship between eyes, nose, cheek and mouth. A dog has 4 legs and in a certain shape.

In other words, the high dimensionality of images are artifactual. Natural images can be readily compressed into the much smaller latent space without losing any information. This is called the [manifold hypothesis](https://en.wikipedia.org/wiki/Manifold_hypothesis) in machine learning.

### Reverse Diffusion in Latent Space

Here’s how latent reverse diffusion in Stable Diffusion works.

1. A random latent space matrix is generated.
2. The **noise predictor** estimate the noise of the latent matrix.
3. The estimated noise is then subtracted from the latent matrix.
4. Step 2 and 3 is repeated up to a certain [sampling steps](https://stable-diffusion-art.com/know-these-important-parameters-for-stunning-ai-images/#Sampling_steps).
5. The **decoder** of VAE converts the latent matrix to the final image.

### What is VAE File?

[VAE files](https://stable-diffusion-art.com/how-to-use-vae/) are used in Stable Diffusion v1 to improve eyes and faces. They are the **decoder of the autoencoder** we just talked about. By further fine tuning the decoder, the model is able to paint finer details.

You may realize what I have mentioned previously is not entirely true. Compressing an image into the latent space *does* lose information, since the fine details was not recovered by the original VAE. Instead, the VAE decoder is responsible for painting fine details.

## Conditioning

Our understanding is still not complete: Where does the text prompt enter the picture? Without it, Stable Diffusion is not a text-to-image model. You will either get an image of a cat or a dog, without any ways to control it.

This is where **conditioning** comes in. The purpose of conditioning is to **steer the noise predictor so that the predicted noise will give us what we want,** after subtracting from the image.

### Text Conditioning (text-to-image)

Below is an overview of how a **text prompt** is processed and fed into the noise predictor. **Tokenizer** first converts each word in the prompt to a number called **token**. Each token is then converted to a 768-value vector called **embedding**. (Yes, this is the same [embedding](https://stable-diffusion-art.com/embedding/) you used in AUTOMATIC1111) The embeddings are then processed by the **text transformer** and are ready to be consumed by the noise predictor.

![In Stable Diffusion, text prompt is tokenized and converted to embedding. It is then processed by the text transformer and consumed by the noise predictor.](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-86.png?resize=480%2C199&ssl=1)

How text prompt is processed and fed into the noise predictor to steer image generation.

Now let’s look closer into each part. You can [skip to the next section](https://stable-diffusion-art.com/how-stable-diffusion-work/#Stable_Diffusion_step-by-step) if the above high-level overview is good enough for you.

Check tokens and embeddings of any prompt with [this notebook](https://colab.research.google.com/github/sagiodev/stablediffusion_webui/blob/master/Stable_Diffusion_tokenizer_and_embedding_SDA.ipynb).

#### Tokenizer

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-88.png?resize=357%2C263&ssl=1)

Tokenizer.

Text prompt is first **tokenized** by a [CLIP tokenizer](https://huggingface.co/docs/transformers/model_doc/clip). CLIP is a deep learning model developed by Open AI to produce text description of any images. Stable Diffusion v1 uses CLIP’s tokenizer.

**Tokenization is computer’s way to understand words**. We human can read words, but computer can only read numbers. That’s why words in a text prompt are first converted to numbers.

A tokenizer can only tokenize words it has seen during training. For example, there are “dream” and “beach” in the CLIP model but not “dreambeach”. Tokenizer would break up the word “dreambeach” into two tokens “dream” and “beach”. So **one word does not always mean one token**!

Another fine print is the space character is also part of a token. In the above case, the phrase “dream beach” produces two token “dream” and “\[space\]beach”. These tokens are not the same as that produced by “dreambeach” which is “dream” and “beach” (without space before beach).

Stable Diffusion model is limited to using 75 tokens in a prompt. (Now you know it is not the same as 75 words!)

#### Embedding

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-89.png?resize=316%2C255&ssl=1)

Embedding.

Stable diffusion v1 uses Open AI’s [ViT-L/14](https://github.com/CompVis/stable-diffusion) Clip model. Embedding is a 768-value vector. Each token has its own unique embedding vector. Embedding is fixed by the CLIP model which learned during training.

Why do we need embedding? It’s because some words are closely related to each other and we want to take advantage of this information. For example, the embeddings of “man”, “gentleman” and “guy” are nearly identical because they can be used almost interchangeably. Monet, Manet and Degas all painted in impressionist style but in different ways. The names have close but not identical embeddings.

This is the same [embedding](https://stable-diffusion-art.com/embedding/) we talked about for triggering a style with a keyword. Embeddings can do magic. Scientists has shown that finding the right embeddings can trigger arbitrary objects and styles, a fine-tuning process called [textual inversion](https://textual-inversion.github.io/).

#### Feeding Embeddings to Noise Predictor

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-91.png?resize=449%2C298&ssl=1)

From embeddings to noise predictor.

The embedding needs to be further processed by the **text transformer** before feeding into the noise predictor. The transformer is like a universal adapter for conditioning. In this case, its input is text embedding vectors, but it could as well be something else like class labels, images and [depth map](https://stable-diffusion-art.com/depth-to-image/). The transformer not only further processes the data, but also **provides a mechanism to include different conditioning modalities**.

The output of text transformer are used **multiple times** by the noise predictor throughout the U-Net. The U-Net consumes it by a **cross-attention mechanism**. That’s how the words in the prompt come together and got related to each other. For example, the prompt “A man with blue eyes” needs cross-attention between “blue” and “eyes” so that Stable Diffusion knows to paint a man with blue eyes, not a blue man with eyes…

A side note: Hypernetwork, a technique to fine-tune Stable Diffusion models, hijacks the cross-attention network to insert styles.

## Stable Diffusion Step-by-step

Now you know all the inner mechanics of Stable Diffusion, let’s go through some examples of what happen under the hood.

### Text-to-image

In text-to-image, you give Stable Diffusion a text prompt and it returns an image.

**Step 1**. Stable Diffusion generates a random tensor in the latent space. You control this tensor by setting the [seed](https://stable-diffusion-art.com/know-these-important-parameters-for-stunning-ai-images/#Seed) of the random number generator. If you set the seed to a certain value, you will always get the same random tensor. **This is your image in latent space**. But it is all noise for now.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-92.png?resize=335%2C173&ssl=1)

Random tensor is generated in latent space.

**Step 2**. The noise predictor U-Net takes the latent noisy image and text prompt as input, and **predicts** the noise, also in latent space (a 4x64x64 tensor).

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-94.png?resize=480%2C237&ssl=1)

**Step 3**. Subtract the latent noise from the latent image. This becomes your **new latent image**.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-95.png?resize=370%2C160&ssl=1)

Steps 2 and 3 are repeated for certain number of [sampling steps](https://stable-diffusion-art.com/know-these-important-parameters-for-stunning-ai-images/#Sampling_steps), for example 20 times.

**Step 4**. Finally, decoder of VAE converts the latent image back to pixel space. This is the image you get after running Stable Diffusion.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-96.png?resize=421%2C247&ssl=1)

Here’s how to image evolve with each sampling step.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/ezgif-1-74fb1d90ed.gif?resize=480%2C480&ssl=1)

### Image-to-image

Image-to-image is a method first proposed in [SDEdit](https://arxiv.org/abs/2108.01073). SDEdit can applied to any diffusion model so here we have image-to-image for Stable Diffusion (a latent diffusion model).

In [image-to-image](https://stable-diffusion-art.com/how-to-use-img2img-to-turn-an-amateur-drawing-to-professional-with-stable-diffusion-image-to-image/), an **input image** and a **text prompt** are supplied as the input. The generated image will be conditioned by both the input image and text prompt. for example, using this amateur drawing and the prompt “photo of perfect green apple with stem, water droplets, dramatic lighting” as inputs, image-to-image can turn it into a professional drawing:

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-97.png?resize=480%2C244&ssl=1)

Image-to-image

Now here’s the step-by-step process.

**Step 1**. The input image is encoded to latent space.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-99.png?resize=387%2C253&ssl=1)

**Step 2**. Noise is added to the latent image. **[Denoising strength](https://stable-diffusion-art.com/inpainting_basics/#Denoising_strength)** controls how much noise is added. If it is 0, no noise is added. If it is 1, maximum amount of noise is added so that the latent image becomes a complete random tensor.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-100.png?resize=480%2C231&ssl=1)

**Step 3**. The noise predictor U-Net takes the latent noisy image and text prompt as input, and predicts the noise in latent space (a 4x64x64 tensor).

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-94.png?resize=480%2C237&ssl=1)

**Step 4**. Subtract the latent noise from the latent image. This becomes your **new latent image**.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-95.png?resize=370%2C160&ssl=1)

Steps 3 and 4 are repeated for certain number of [sampling steps](https://stable-diffusion-art.com/know-these-important-parameters-for-stunning-ai-images/#Sampling_steps), for example 20 times.

**Step 5**. Finally, decoder of VAE converts the latent image back to pixel space. This is the image you get after running image-to-image.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-105.png?resize=356%2C238&ssl=1)

So now you know what image-to-image is: All it does is to set the initial latent image with a bit of noise and a bit of input image. Setting denoising strength to 1 is equivalent to text-to-image because the initial latent image is a completely random noise.

### Inpainting

Inpainting is really just a special case of image-to-image. Noise is added to the parts of the image you wanted to inpaint. The amount of noise is similarly controlled by denoising strength.

### Depth-to-image

[Depth-to-image](https://stable-diffusion-art.com/depth-to-image/) is an enhancement to image-to-image, it generates new images with additional conditioning using a depth map.

**Step 1**. Input image is encoded to latent state

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-101.png?resize=436%2C271&ssl=1)

**Step 2**. [MiDaS](https://github.com/isl-org/MiDaS) (an AI depth model) estimates the depth map from the input image.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-102.png?resize=480%2C162&ssl=1)

**Step 3**. Noise is added to the latent image. Denoising strength controls how much noise is added. If denoising strength is 0, no noise is added. If denoising strength is 1, maximum amount of noise is added so that the latent image becomes a complete random tensor.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-100.png?resize=480%2C231&ssl=1)

**Step 4**. Noise predictor estimates noise of the latent space, **conditioned by the text prompt and the depth map**.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-103.png?resize=480%2C280&ssl=1)

**Step** 5\. Subtract the latent noise from the latent image. This becomes your **new latent image**.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-95.png?resize=370%2C160&ssl=1)

Steps 4 and 5 are repeated for the number of sampling steps.

**Step 6**. Latent image is decoded by the decoder of VAE. Now you get the final image from depth-to-image.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-104.png?resize=472%2C300&ssl=1)

## What is CFG Value?

This write-up won’t be complete without explaining what Classifier-Free Guidance (CFG) is, a value that AI artists tinker with everyday. To understand what it is, we will need to first touch on its predecessor, **classifier guidance**…

### Classifier Guidance

[Classifier guidance](https://arxiv.org/abs/2105.05233) is a way to incorporate **image labels** in diffusion models, so that you can use a label to guide the diffusion process. For example, you can use the class label “cat” to steer the reverse diffusion process towards generating photos of cat.

**Classifier guidance scale** is a parameter for controlling how closely should the diffusion process follow the label.

Below is an example I stole from this [paper](https://arxiv.org/abs/2207.12598). Suppose there are 3 groups of images with label “cat”, “dog” and “human”. If the diffusion is unguided, the model will draw samples from each group’s total population, but sometimes it may draw images that could fit two labels, e.g. a boy petting a dog.

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-106.png?resize=480%2C148&ssl=1)

Classifier guidance. Left: unguided. Middle: small guidance scale. Right: large guidance scale.

With classifier guidance, the images produced by the diffusion model would be biased towards **extreme/unambiguous examples** of that group. For example, if you ask the model for a cat, it will return an image that is unambiguously a cat and nothing else.

How strong this guidance is is controlled by the parameter **classifier guidance scale**. In figure above, the sampling on the right has a higher classifier guidance scale than the one in the middle. In practice, this scale value is simply the multiplier to the drift term towards the data with that label.

### Classifier-free Guidance

Although classifier guidance achieved record-breaking performance, it needs an extra model to provide that guidance. This has presented some difficulties in training.

**[Classifier-free guidance](https://arxiv.org/abs/2207.12598)**, in its authors’ term, is a way to achieve “classifier guidance without a classifier”. Instead of using class labels and a separate model for guidance, they proposed to use image captions and train a **conditional diffusion model**, exactly like the one we [discussed](https://stable-diffusion-art.com/how-stable-diffusion-work/#Text_conditioning_text-to-image) in text-to-image.

They put the classifier part as **conditioning of the noise predictor U-Net**, achieving the so-called “classifier-free” (i.e. without a separate image classifier) guidance in image generation.

In text-to-image, this guidance is with text prompt.

#### CFG Value

Now we have a classifier-free diffusion process via conditioning, how do we control how much the guidance should be followed?

**Classifier-free guidance (CFG) scale is a value that controls how much the diffusion process is conditioned** by the text prompt. The image generation is **unconditioned** (i.e. the prompt is ignored) when it is set to 0. A higher value steers the diffusion towards the prompt.

## Stable Diffusion v1 Vs v2

This is already a long post but it won’t be complete without comparing the difference between v1 and [v2](https://stable-diffusion-art.com/how-to-run-stable-diffusion-2-0/) models.

### Model Difference

Stable Diffusion v2 uses [OpenClip](https://stability.ai/blog/stable-diffusion-v2-release) for text embedding. Stable Diffusion v1 uses Open AI’s CLIP [ViT-L/14](https://github.com/CompVis/stable-diffusion) for text embedding. The reasons for this change are

- OpenClip is up 5 times larger. Larger text encoder model improves image quality.
- Although Open AI’s CLIP models are open-source, the models were trained with proprietary data. Switching to OpenClip model gives researchers more transparency in studying and optimizing the model. It is better for long term development.

### Training Data Difference

Stable Diffusion v1.4 is [trained](https://huggingface.co/CompVis) with

- 237k steps at resolution 256×256 on [laion2B-en](https://huggingface.co/datasets/laion/laion2B-en) dataset.
- 194k steps at resolution 512×512 on [laion-high-resolution](https://huggingface.co/datasets/laion/laion-high-resolution).
- 225k steps at 512×512 on “[laion-aesthetics v2 5+](https://laion.ai/blog/laion-aesthetics/)“,  
    with 10% dropping of text conditioning.

Stable Diffusion v2 is [trained with](https://huggingface.co/stabilityai/stable-diffusion-2-base)

- 550k steps at resolution `256x256` on a subset of [LAION-5B](https://laion.ai/blog/laion-5b/) filtered for explicit pornographic material, using the [LAION-NSFW classifier](https://github.com/LAION-AI/CLIP-based-NSFW-Detector) with `punsafe=0.1` and an [aesthetic score](https://github.com/christophschuhmann/improved-aesthetic-predictor) >= `4.5`. 
- 850k steps at resolution `512x512` on the same dataset on images with resolution `>= 512x512`.
- 150k steps using a [v-objective](https://arxiv.org/abs/2202.00512) on the same dataset.
- Resumed for another 140k steps on `768x768` images.

[Stable Diffusion v2.1](https://huggingface.co/stabilityai/stable-diffusion-2-1) is fine-tuned on v2.0

- additional 55k steps on the same dataset (with `punsafe=0.1`)
- another 155k extra steps with `punsafe=0.98`

So basically they **turned off the NSFW filter in the last training steps.**

### Outcome Difference

Users generally find it harder to use Stable Diffusion v2 to control styles and generate celebrities. Although Stability AI did not explicitly filter out artist and celebrity names, their effects are much weaker in v2. This is likely due to difference in training data. Open AI’s proprietary data may have more artworks and celebrity photos. Their data is probably highly filtered so that everything and everyone looks fine and pretty.

### Some Interesting Reads

- [Stable Diffusion v1.4 press release](https://stability.ai/blog/stable-diffusion-public-release)
- [Stable Diffusion v2 press release](https://stability.ai/blog/stable-diffusion-v2-release)
- [Stable Diffusion v2.1 press release](https://stability.ai/blog/stablediffusion2-1-release7-dec-2022)
- [High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752)–research paper introducing Stable Diffusion
- [The Illustrated Stable Diffusion](https://jalammar.github.io/illustrated-stable-diffusion/)–Some good details in model architecture
- [Stable Diffusion 2](https://huggingface.co/stabilityai/stable-diffusion-2)–Official model page
- [Diffusion Models Beat GANs on Image Synthesis](https://arxiv.org/abs/2105.05233)–Research paper introducing classifier guidance
- [Classifier-Free Diffusion Guidance](https://arxiv.org/abs/2207.12598)–Research paper introducing classifier-free guidance
- [Deep Unsupervised Learning using Nonequilibrium Thermodynamics](https://arxiv.org/abs/1503.03585)–Reverse diffusion process


---

#AI #article
