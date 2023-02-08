# The Day The AGI Was Born

---

What were you doing the evening of November 30th, 2022—the day AGI was born?

I imagine most regular folks were going about their usual routine - hobbies, TV, family, work stuff. This isn’t a judgment; I was *sleeping*. I may even have thought to myself: “[Nothing much happened today](https://www.npr.org/2007/07/04/11703583/reading-the-declaration-of-independence).” I’ve been covering the new AI Summer here on this blog and, like the apocryphal story of King George III on July 4 1776, I *slept through* what probably will be viewed in history as the biggest change to the world since the Internet, and woke up to an absolute *torrent* of tweets and jailbreaks and jokes and discoveries I should’ve been on top of.  

If you’re feeling the FOMO, you aren’t alone - [even AI researchers are feeling it](https://twitter.com/kevin_zakka/status/1599037443004850177) - and this is the blogpost for you. **ChatGPT is as big a jump from GPT3, as GPT3 itself was a jump from GPT2** - but it has been extremely hard to get up to speed live because of the extreme quantity and variety of discoveries. Each tweet is a rabbit hole, which contributes to the FOMO. Every newsletter author furiously writing this up this weekend will add to it by linking out to dozens of tweets and hyperbolic comments.

  

So I will tackle this differently: you can [view my notes](https://github.com/sw-yx/ai-notes/blob/main/TEXT.md#chatgpt) live anytime, but here, I’ll attempt to give a cohesive, concise executive summary of ChatGPT here that you can use in your conversations and thinking. Longtime readers will know this isn’t my normal style, but I think the importance of this topic deserves clarity and concision.

*last updated Dec 3 2022*

ChatGPT is OpenAI’s latest large language model, released on Nov 30 2022 as a [chat app](https://chat.openai.com/chat) open to the public. Its simple interface

hints at its capabilities and limitations.

Like GPT3, it can explain scientific and technical concepts in a desired style or programming language, and brainstorm basically anything you need.

However, there are three very important differences you should know:

- **Better at Zero Shot**: As a fine-tuned “[GPT-3.5 series](https://beta.openai.com/docs/model-index-for-researchers/models-referred-to-as-gpt-3-5)” model *and* an [InstructGPT](https://openai.com/blog/instruction-following/) sibling, it is a *LOT* better at [zero-shot](https://en.wikipedia.org/wiki/Zero-shot_learning) generation of text that follows your instructions, whether it is generating rhyming poetry ([Shakespearean sonnets](https://twitter.com/AndrewGlassner/status/1598749865768792065), [Limericks](https://twitter.com/typesfast/status/1598438721791361024), [Song parodies](https://twitter.com/raphaelmilliere/status/1598469100535259136)), emulating people ([AI experts](https://twitter.com/raphaelmilliere/status/1598469100535259136), [Gangster movies](https://twitter.com/goodside/status/1598129631609380864), [Seinfeld](https://twitter.com/goodside/status/1598077257498923010)), or writing ([college essays that get A’s and B’s from real professors](https://twitter.com/TimKietzmann/status/1598230759118376960), [writing LaTeX](https://twitter.com/jdjkelly/status/1598021488795586561), [podcast intros](https://twitter.com/gilbert/status/1598446084279652353)).
    
    - It has long term **memory** of [up to 8192 tokens](https://twitter.com/goodside/status/1598874674204618753), and can take input and generate output about twice as long
        

        as GPT3.

    - It *still* [can’t do math, generates false information about the real world, and writes bad code](https://github.com/sw-yx/ai-notes/blob/main/TEXT.md#fails), and does not pass [Turing](https://twitter.com/emollick/status/1598516535038861313), [SAT](https://twitter.com/davidtsong/status/1598767389390573569), or [IQ](https://twitter.com/SergeyI49013776/status/1598430479878856737) tests.
        
    - If you only need zero-shot textgen, you may be able to use the recently released [text-davinci-003](https://scale.com/blog/gpt-3-davinci-003-comparison) instead. However, you’d be losing out on…
        
- **New Chat capability**: ChatGPT is also the first **chat**\-focused large language model, and it is *astoundingly* good at it, meaning you can **talk back** to it and **modify what it generates** or have it **continue an existing conversation**.
    

    Previous attempts at creating chat experiences in GPT3 involved hacky, unreliable prompt engineering to create contextual memory and extensive software engineering to allow follow-up corrections. This is now a “solved” problem and means you can [write blogs iteratively and with ~unlimited length](https://twitter.com/goodside/status/1598235521675038722).

- **Notable, but flawed, but improving safety**: To most people, “[ChatGPT feels much more filtered, reserved, and somehow judgmental than GPT-3](https://news.ycombinator.com/item?id=33808731)”.
    
    - OpenAI clearly invested a great deal of time in making ChatGPT “safe”, specifically by attempting to disable responses related to violence, terrorism, drugs, hate speech, dating, sentience, and eradicating humanity, and also purporting to disable web browsing and knowledge of current dates.
        
    - However, **every single one of these precautions were compromised** in the first 48 hours, using [many “jailbreaks” found](https://github.com/sw-yx/ai-notes/blob/main/TEXT.md#jailbreaks)
        

        soon after public release, causing commentators to observe that the danger signs are “[like watching an Asimov novel come to life](https://news.ycombinator.com/item?id=33832358)”.

    - Still, OpenAI placed clear warnings
        

        that this is a test, encourages reporting of results, and have [been](https://twitter.com/pensharpiero/status/1598731292278865920) [observed](https://twitter.com/sleepdensity/status/1598233414683197441) **patching** these discoveries in real time.

As we have [previously explored](https://twitter.com/goodside/status/1598235521675038722), **the best usecases are where creativity is more valued than precision**: brainstorming, drafting, presenting information in creative ways. The biggest unresolved debate is how much a ChatGPT-like experience can **replace Google**: on one hand, ChatGPT answers questions far more directly and legibly than a Google results page

; on the other, its answers are often [incorrect](https://twitter.com/SeaRyanC/status/1598515753942384640) and unsourced

. The unsatisfying outcome will likely be “it depends” — yet disruptive tech tends to be worse than existing tech in almost every way but one.

The final notable development this week has been in the distribution. There is no official ChatGPT API yet, however Daniel Gross [demonstrated](https://twitter.com/danielgross/status/1598735800497119232) that you can automate it, using Playwright browser automation, to create an unofficial API and hook it up for a WhatsApp chatbot. This technique has been cloned to a [Telegram bot](https://twitter.com/altryne/status/1598822052760195072), [Chrome extension](https://github.com/kazuki-sf/ChatGPT_Extension), [Python script](https://github.com/taranjeet/chatgpt-api), and [Nodejs script](https://github.com/transitive-bullshit/chatgpt-api).

Some people have concluded that [ChatGPT is AGI](https://twitter.com/MichaelTrazzi/status/1599073962582892546?s=20&t=rGJQIdjB8sCvmy-WJUBr6A), which Sam Altman dismisses as “[obviously not close, lol](https://twitter.com/sama/status/1599111626191294464?s=20&t=rGJQIdjB8sCvmy-WJUBr6A)”, but I do agree that this is the birth of something that *looks like* AGI. The main factor is learning that we have somehow gone much faster with **Reinforcement Learning via Human Feedback** than I knew in October (“[What is AGI-Hard](https://lspace.swyx.io/p/agi-hard)?”)

. RLHF is essentially Chat, and this is **the first actually good Chat AI that humanity has ever seen**: it understands when you want to make edits to prior generations versus when you want to continue on with the conversation; it knows to [remember information](https://twitter.com/goodside/status/1598874674204618753) and retain context, so you can talk naturally to it and it can keep up with you; it demonstrably knows what it can’t do and can generate code to get the information it needs, making it a good central brain for [an agentic AI system](https://twitter.com/amasad/status/1598089698534395924):

That means that ChatGPT is likely the first

LLM you can present to a regular human (without any prompt engineering training) that could accomplish any particular commodity task - a general feat that meets some definitions of AGI.

This is my attempt at being concise so I have to cut it short, but I am open to whatever I may have missed and would love your questions! Fire away below!

---

#ai #article
