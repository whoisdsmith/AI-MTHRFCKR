# 05 Stable Diffusion Parameters

Prompt

	Tiny robot scratching his head toy, standing character, soft smooth lighting, soft pastel colors, skottie young, 3d blender render, polycount, modular constructivism, pop surrealism, physically based rendering, square image 

## Resolution–Default is 512x512

This parameter is straight forward. You choose the Width and Height of the generated images. But it’s important to know that the model was trained on 512x512 images, and in general these dimensions provide the best quality and composition, so it is recommended you stick to them as a beginner. 576x448 Even with all parameters fixed, changing the 512x512 resolution will completely change the generated image. Although it may have similar colors and composition This parameter increases the required VRAM, and the time needed to generate

## Classifier Free Guidance (CFG)–Default is 7

You can see this parameter as a “Creativity vs. Prompt

” scale. Lower numbers give the AI more freedom to be creative, while higher numbers force it to stick to the Prompt

Prompt

	a red bird drinking water from a lake, children's book painting

CFG: 0 Completely ignores the Prompt  
CFG: 4 Missing the red color  
CFG: 7 Good balance  
CFG: 15 Too high Starts creating artifacts

This parameter does not affect the VRAM needed, or the generation time.

## Step Count–Default is 50

Stable Diffusion creates an image by starting with a canvas full of noise and denoise it gradually to reach the final output, this parameter controls the number of these denoising steps. Usually, higher is better but to a certain degree, for beginners it’s recommended to stick with the default.

- Steps: 1
- Steps: 2
- Steps: 3
- Steps: 4
- Steps: 5
- Steps: 40
- Steps: 30
- Steps: 20
- Steps: 10

This parameter does not affect the VRAM needed, but increasing it is directly proportional to the time it takes to generate an image

## Seed–Default is “random”

Seed is a number that controls the initial noise. The seed is the reason that you get a different image each time you generate when all the parameters are fixed. By default, on most implementations of Stable Diffusion, the seed automatically changes every time you generate an image. You can get the same result back if you keep the Prompt the seed and all other parameters the same.

Prompt

	photo of a rabbit driving a bicycle, in Tokyo at night

Seed: 0  
Seed: 8  
Seed: 18

## Sampler Diffusion

samplers are the method used to denoise the image during generation, and since they differ in the way of calculating the next step in the image production, they take different durations and different number of steps to reach a usable image. We suggest beginners to use DDIM since it's fast and can usually generate good images with only 10 steps, making it easy and fast to experiment and improve

Sampler: PLMS Steps: 10  
Sampler: DDIM Steps: 10

	kawaii tiny cute unicorn emoji made of clay, iOS emoji, 3D clay blender render, rich vivid colors, smooth gradients, isometric front view, diffuse lighting, octane render, unreal engine

---
