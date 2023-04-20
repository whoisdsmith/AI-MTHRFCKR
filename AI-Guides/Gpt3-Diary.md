# Thread by @michellehuang42 on Thread Reader App

---

> ## Excerpt
> @michellehuang42: i've received a lot of requests on how to replicate my AI experiment so here goes -- [tutorial] how to create your own "inner child" chatbot using GPT-3 step 1: acquire some source material this……

---

![michelle huang Profile picture](https://pbs.twimg.com/profile_images/1511104560546422790/mL9nG_lP_bigger.png)

i've received a lot of requests on how to replicate my AI experiment so here goes --

\[tutorial\] how to create your own "inner child" chatbot using GPT-3

step 1: acquire some source material

this can range from diaries, personal narrative, any kind of written content that shows your personality / voice / values

if you have no diaries to reference … do not fear! archived chats should work just as well

side note for those who are looking to do this with diaries

i took pictures + scanned some some entries via an OCR app, but primarily just spent hours typing due to my messy handwriting

(unfortunately this was of the things that has stayed constant since my childhood)

congrats, you have now finished the most grueling part of the process.

\*\*i would advise to just start off with a few samples instead of transcribing everything\*\* - you'll see why later in this post

step 2: after you have some source material, go to the GPT-3 playground here [beta.openai.com/playground/](https://beta.openai.com/playground/)

this playground is basically where you can add your prompts + diary entries, and set training parameters for your model

[![](https://threadreaderapp.com/images/sticky-note-regular.png)](https://beta.openai.com/playground/)

note that you will need to have an open ai account, as well as have a payment method to run the model

as reference, i personally trained my inner child used the da vinci model, the most powerful one offered, about 2 cents per 1k tokens (about 750 words)

step 3: next, you'll want to start prompt-crafting in the playground

i referenced the open-ai docs, which i've linked below

go to this website, scroll down to the conversation sub-header, and you'll see an example of a conversation prompt sample  

[![](https://threadreaderapp.com/images/sticky-note-regular.png)](https://beta.openai.com/docs/guides/completion/prompt-design)

here is the specific prompt i used to train on diary entries:

side note -- if you're terrified that your younger self is going to roast you and cause more psychological damage than helpfulness, you can also adjust the tone / sentiment / attitude [![Image](https://pbs.twimg.com/media/FiwrZvRWIAYhwYo.png)](https://pbs.twimg.com/media/FiwrZvRWIAYhwYo.png)

so, to receive more gentle / kind responses for healing use cases, you can add "young \[your name\] is loving, gentle, and very friendly" or something along those lines to soften the responses

step 4: add parameters

i cranked the temp settings + character count up, and used the da vinci model-002 to train (003 wasn't out yet at this time of writing)

of course, you can alter based on your own needs, but these are the settings i used [![Image](https://pbs.twimg.com/media/FiwslXHWIAE7aMW.png)](https://pbs.twimg.com/media/FiwslXHWIAE7aMW.png)[![Image](https://pbs.twimg.com/media/Fiwss9aWYAEj_zN.png)](https://pbs.twimg.com/media/Fiwss9aWYAEj_zN.png)

for those interested in the code or running it via a program, you can also do the following: [![Image](https://pbs.twimg.com/media/Fiws22GXgAEA8ky.png)](https://pbs.twimg.com/media/Fiws22GXgAEA8ky.png)

note that for gpt-3 playground, is that there’s a content maximum: even for the most robust modelwhich processes up to 4k tokens per request

you can increase these limits with fine-tuning, but i ended up just using the playground for simplicity

so it might be better to just pick and choose which specific entries feel the most poignant for you, or represent your attitude and values most during that time and go with those -- which is why i mentioned starting with just a few samples at the beginning of this post

step 5: hit submit, and now you should be able to start the conversation with your younger self :)

hope everyone has a fun time healing, interacting, and learning from previous versions + states of themselves

there are many other use cases / instances that you can train this ai bot to do in therapy settings, specifically for parts work, or internal family systems therapy (IFS)

for instance, you can have your child-self respond angrily, and then try to console your younger self

feel free to share what you find -- there are so many more use cases for mental health, career counseling, and beyond!

---

#AI #article
