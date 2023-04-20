# The Fine Art of Prompting

---

Once upon a time, the glory and terror of computers was that they would do exactly what you told them to do. One of the most remarkable things about the rise of AI is that this is no longer the case. Interacting with a large language model (aka LLM) like ChatGPT, or a text-to-image diffusion model like Stable Diffusion, is more like making a deal with a [perverse imp](https://twitter.com/rezendi/status/1600583273679183872) than like programming. Sure, you give it instructions, known as *prompts* … but those aren't really *commands*. Instead they suggest, they cajole, they negotiate, they hint.

The extraordinary capabilities of modern AI can only be fully unlocked by giving them the right—and right *kind*—of prompts. This “capability overhang” has led to the entirely new field of “prompt engineering.” Bad news: effective prompts are often quite complex and elaborate. Good news: prompting is indeed more a science than an art, and there are a whole slew of effective techniques.

Invisibly fundamental to all of them, I think, is a better mental model of what the AI is actually doing. The naïve assumption is that ChatGPT *answers,* and Stable Diffusion *creates*. This is not correct. Large language models are actually trained to take blocks of text and *continue* them. ChatGPT channels this into dialectical Q&A, but under the hood, it really “wants” to *extend* whatever prompt you give it, not *respond*. (This is why, for instance, telling it what *not* to do almost never leads to better output.)

Similarly, it’s better to think of diffusion models like Stable Diffusion not as generators, but as infinite art museums containing all imaginable images, à la Borges. They use your prompt not to *create* but to *guide* you, through their endless chambers, to the nearest with art that matches your prompt.

That’s all pretty abstract. Fortunately, many people have come up with very concrete guidelines of how to prompt. Below is an overview of that good stuff, followed by a brief discussion of chains of thought, using prompts to generate prompts, and more.

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8d647671-54a8-49ef-85e7-2d5afdd57614_1024x1024.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8d647671-54a8-49ef-85e7-2d5afdd57614_1024x1024.png)

In which I perpetuate the incorrect mental model.

First things first: to follow the bleeding edge of prompt engineering, follow Riley Goodside, [@goodside](https://twitter.com/goodside), on Twitter. Most text prompts are maybe a paragraph of prose. Riley pushes the form to its limits, prompting [entire preprints of scientific papers](https://twitter.com/goodside/status/1609041139100749824), [Wikipedia content](https://twitter.com/goodside/status/1608329313425686530), [your own ChatGPT](https://twitter.com/goodside/status/1607487283782995968), and even [getting GPT-3 to run Python code](https://twitter.com/goodside/status/1581805503897735168) to calculate the kinds of answers it usually gets wrong. He’s also the de-facto inventor of using [prompt injection](https://simonwillison.net/2022/Sep/12/prompt-injection/) to [hack](https://artifact-research.com/artificial-intelligence/talking-to-machines-prompt-engineering-injection/) large language models.

That said, you probably want to start with the basics. First read OpenAI’s “[best practices for prompt engineering](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api).” Then proceed to the excellent free online course at [learnprompting.org](https://learnprompting.org/docs/intro). Finally, refer to the collective wisdom of “[Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts).”

For those inclined to merely gaze into rather than dive down this rabbit hole, though, I’ll cite a few essential patterns and examples here:

- My favorite is “role prompting”—telling the AI to play the role of a particular expert before asking questions relevant to that expertise. For instance, if you tell it it’s a brilliant mathematician, it is far more likely to get math questions correct! An example borrowed from learnprompting.org:  
    `You are a brilliant mathematician who can solve any problem in the world. Attempt to solve the following problem: What is 100*100/400*56?   `GPT-3.5 will get the answer *wrong* without that role prefix … but *right* with it.
    
- Similarly, you can get ChatGPT to take on a whole multitude of roles, such as that of a math teacher (from [@devisasasari](https://github.com/devisasari)):  
    `I want you to act as a math teacher. I will provide some mathematical equations or concepts, and it will be your job to explain them in easy-to-understand terms. This could include providing step-by-step instructions for solving a problem, demonstrating various techniques with visuals or suggesting online resources for further study. My first request is "I need help understanding how probability works."`
    

For whatever reason—we are a visual species living in a visual world; generative art is far more controversial than generative language; AI art’s effort-reward feedback loop is tighter and more visceral; its prompts tend to be somewhat less complex, chained and dialectical—there are far more guides to DALL-E and Stable Diffusion prompting than guides to large language models.

The embarrassment of riches includes, first, an excellent overview of the state of AI art, including a thoughtful analysis of legality and morality, at “[AI Art Panic](https://opguides.info/posts/aiartpanic/).” But if you want to just get to the prompts, go straight to two really excellent pages of examples: you can learn a lot just from scanning through “[Best 100+ Stable Diffusion Prompts](https://mpost.io/best-100-stable-diffusion-prompts-the-most-beautiful-ai-text-to-image-prompts/)” and “[Top 50 Prompts for Midjourney and DALL-E](https://mpost.io/top-50-text-to-image-prompts-for-ai-art-generators-midjourney-and-dall-e/).”

More formal analysis is also increasingly available, such as the scientific papers “[Prompt Engineering for Text-Based Generative Art](https://www.arxiv-vanity.com/papers/2204.13988/)” and “[Investigating Prompt Engineering in Diffusion Models](https://www.arxiv-vanity.com/papers/2211.15462/).” You probably want to work your way up to those, though, beginning with the step-by-step “[4.2 Gigabytes, or: How to Draw Anything](https://andys.page/posts/how-to-draw/)” and “[A Beginner’s Guide to Prompt Design for Text-to-Image](https://towardsdatascience.com/a-beginners-guide-to-prompt-design-for-text-to-image-generative-models-8242e1361580).”

Some more specific guides include“[Prompt Design for DALL·E: Photorealism — Emulating Reality](https://medium.com/merzazine/prompt-design-for-dall-e-photorealism-emulating-reality-6f478df6f186),” “[How to get images that don't suck: a Beginner/Intermediate Guide to Getting Cool Images from Stable Diffusion](https://www.reddit.com/r/StableDiffusion/comments/x41n87/how_to_get_images_that_dont_suck_a/),” and a [tutorial](https://www.reddit.com/r/StableDiffusion/comments/x8szj9/tutorial_seed_selection_and_the_impact_on_your/) on using “seed images” (i.e. using both text *and* an image as an input to Stable Diffusion.)

Once again, though, perhaps the best/most gems of wisdom will come from the accumulated wisdom of the crowd: the “[DALL·E 2 Prompt Engineering Guide](https://docs.google.com/document/d/11WlzjBT0xRpQhP9tFMtxzd0q6ANIdHPUBkMV-YB043U/)” is a whopping 34-page Google Doc of DALL-E tips, hints, and tricks. Finally, in case this list is insufficiently exhaustive, here is a very thorough “[List of tools for creating prompts for text-to-image AI generators](https://pixexid.com/read/how-to-create-prompts-to).”

I know, I know: in a list of tools and guides, I just linked you to a page which is just a list of yet *more* links to tools and guides, it’s all very indirect. As such I will once again cite a few especially good examples and patterns from the above:

- One amusing tip is just to tell the model that the output should be really good! You can do this by including prompt terms like `award winning`, `gorgeous`, `masterpiece`, `amazing`, `wonderful`, `beautiful`, etc.
    
- Another is to add stylistic terms: `hyper-realistic`, `impressionist`, `soft focus`, `cinematic`, `detailed`, `abstract`, `photograph`, `Sigma 85mm f/1.4`, `oil painting`, `vector graphics`, `rendered in Unreal Engine`, etc.
    
- Repetition can be important: “*the prompt ‘‘space whale. a whale in space’’ will likely produce subjectively better results than either term alone.*”
    
- Add specific directorial directions re lighting and subject position such as `ambient lighting`, `dark shadows`, `golden hour`, `looking away`, `kneeling`, `arms wide`, etc.
    
- Personally, I like to *not* do any of the above, instead prompt with a string of abstract concepts and weird narrative fragments, and hope to be pleasantly surprised … but I’m weird that way. If you actually have a specific image in mind, you can usually iterate pretty close to it with the above tips.
    

[

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F7d3f87c7-ed8f-4882-a436-f82e460eab5f_1024x1024.png)

Never break the chain of thought.

Let’s get back to large language models for a moment. One of the strange and interesting things about them is that you can “cue” them to think better about your particular prompt, often by giving them an example or two. In the argot of the industry, a model’s response to a prompt with no setup is called a “zero-shot” output. A response to a prompt after you give the LLM a single example of what you want is “one-shot,” and a response after giving it a few examples is “few-shot.”

Until fairly recently, LLMs were considered to do their best work in “few-shot” cases. However, as described by the Google Brain team in “[Language Models Perform Reasoning via Chain of Thought](https://ai.googleblog.com/2022/05/language-models-perform-reasoning-via.html),” it turns out that if you can get them to “stretch out” their outputs into multiple steps—the “chain of thought” of that title—then zero-shot results can be just as good. And, in fact, as “[Large Language Models are Zero-Shot Reasoners](https://www.arxiv-vanity.com/papers/2205.11916/)” by Google Brain and the University of Tokyo establishes, this can be as easy as telling it “let’s think step by step.”

This is fascinating and extraordinary … but it also highlights that, while it may be theoretically possible to come up with the perfect prompt that generates the perfect answer, it’s often easier to “stack” prompts, i.e. use several prompts sequentially, often including the previous output in the next prompt. ChatGPT is especially good at this, because it automatically maintains conversational context. So don’t be afraid to tell LLMs, and in particular ChatGPT, to iterate on their suboptimal output from a previous prompt. This can be a whole lot easier than finding the One True Prompt, even if that might exist somewhere.

(Are chain-of-thought and few-shot prompts ultimately just a special case of “fine-tuning,” i.e. formally training an LLM on a slew of new data specific to your particular task before using it? And if so, does that suggest that “fine-tuning,” even though it actually adjusts model weights, is *also* unnecessary, at least in theory, because it’s used not to add any additional capabilities to the LLM but to orient it towards your task, something one could also do with the platonic ideal of a single prompt? I’m no theoretician, but I also don’t think theoreticians actually know the answer, so: maybe?)

But why just *chain* prompts when you can *meta-chain* them? This whole blog post is about the fact that we have to generate very specific language to optimize the outputs of both LLMs and diffusion models. Aaaaaaand what’s the best available tool humanity has for generating very specific (or any other forms of) language? That’s right: LLMs themselves! As such, “[Large Language Models are Human-Level Prompt Engineers](https://www.arxiv-vanity.com/papers/2211.01910/),” one can even tweak prompts to edit generated images in real time, and I’m confident a great deal of further work is underway on prompting LLMs to generate prompts (for) themselves [and for diffusion models](https://www.timothybrooks.com/instruct-pix2pix).

[

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F1d28df87-02a9-47de-8843-334ed3fb0daa_1024x1024.png)

Hard at work in the prompt factory.

The above is barely an introduction to the topic of prompting. Let me suggest a few more in-depth resources. First, the inimitable Gwern’s [GPT-3 Creative Fiction](https://www.gwern.net/GPT-3) page, especially “[Prompts As Programming](https://www.gwern.net/GPT-3#prompts-as-programming)” but really everything. Second, “[GPT-3 and prompts: a quick primer](https://buildspace.so/notes/intro-to-gpt3-prompts).” Third, “[A Complete Introduction to Prompt Engineering For Large Language Models](https://www.mihaileric.com/posts/a-complete-introduction-to-prompt-engineering/).”

The sheer speed of AI today is breathtaking, and also discombobulating. The above applies to the current generation of AI models; but I got a sneak preview of OpenAI’s still-not-yet-released GPT-4 a few months ago, and it was mindblowing. (And now already several months old, an eternity in modern AI.) It’s unclear whether today’s generation of prompt engineering will be effective, or necessary, or supplanted by a whole new set of techniques. My guess is it will mostly remain effective and required.

As you can see, while the core idea of “train an AI to respond to text inputs” is pretty simple … the repercussions are not. Even today’s models are both opaque and very powerful, meaning that finding the right prompts, and the right techniques, feels a little like inventing magical spells. It’s an open question whether AIs will become more comprehensible, meaning “prompt engineering” will be a brief phase we pass through en route to much simpler and more deterministic instruction … or whether working with them will feel ever more like wizardry than like programming.
