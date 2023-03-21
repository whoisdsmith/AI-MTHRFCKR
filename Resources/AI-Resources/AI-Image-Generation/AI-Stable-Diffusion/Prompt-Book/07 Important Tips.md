# 07 Important Tips

Prompt

	Tiny duck playing on guitar toy, standing character, soft smooth lighting, soft pastel colors, skottie young, 3d blender render, polycount, modular constructivism, pop surrealism, physically based rendering, square image

When to use different CFG values?

- CFG 2 - 6: Creative, but might not follow the Prompt
- CFG 7 - 10: Recommended for most Prompts. Good balance between creativity and guided generation
- CFG 10 - 15: When you’re sure that your Prompts good/specific enough.
- CFG 16 - 20: Not generally recommended unless the Prompt is well detailed. Might affect coherence and quality

---

## When to Use Different CFG Values? - Examples

CFG: 2  
CFG: 7  
CFG: 12  
CFG: 19

Complete mess We have a rabbit now  
We got all 3 subjects!  
Composition seems forced  
anime illustration of a blue rabbit, riding a scooter near a lake, with the sun in the sky

In a Prompt with multiple subjects, it’s a good idea to increase the CFG scale

## The Power of Seeds

Some seeds are just better for a Prompt, so try to save a good seed and slightly tweak the Prompt to get what you’re looking for while keeping the same composition. This can also be used to test the effect of different modifiers.

All these images used the same seed and parameters, only change was the Prompt

Photo of a cute dog

	Photo of a cute cat holding an umbrella holding an umbrella

	Painting of a cute cat holding an umbrella Photo of a cute cat holding an umbrella, at night

## Token Efficiency

Your Prompt is limited effectively to 75 tokens.

If you are working with a long Prompt try to be efficient with words that do not significantly add to your meaning.

A typical example is when using an artist as a modifier to get a particular style. Here are a few Prompts and their token counts. They all will produce a piece that looks like it was created by Vincent Van Gogh with their associated token counts,

● A horse in the style of Vincent Van Gogh (11)  
● A horse in the style of Van Gogh (10)  
● A horse by Vincent Van Gogh (7)  
● A horse by Van Gogh (6)  
● Horse by Van Gogh (6)  
● Horse Van Gogh (5)

All will accomplish the result but are not exactly the same.  
The order of words can be as important as the words themselves

This trick is especially useful when trying to make unusual creations. Machine gun mounted

Pink ice cream truck with machine gun mounted on it, technical  
on top of a pink ice cream truck, technical “Using the same seed and sampler”

In the above example, the machine gun doesn’t appear unless you put it in the start of the Prompt

## Don’t Forget About Conventional Tools!

You got a great generation with a messed-up facial features?

Use GFP-GAN to fix it ( use it online )

Close-up portrait photo of a blonde woman on her wedding day  
Close-up portrait photo of an elderly middle eastern woman smiling, bokeh  
Portrait photo of a female army soldier during WW1

---
