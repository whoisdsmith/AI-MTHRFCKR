---
created: 2023-01-30T16:24:59 (UTC -05:00)
tags: []
source: https://stable-diffusion-art.com/embedding/
author: 
---

# How to Use Embeddings in Stable Diffusion - Stable Diffusion Art

> ## Excerpt
> Embedding, the product of textual inversion, is an alternative way to control the style of your images in Stable Diffusion. We will go over what embedding is,

---

Embedding, the product of textual inversion, is an alternative way to control the style of your images in Stable Diffusion. We will go over [what embedding is](https://stable-diffusion-art.com/embedding/#What_is_embedding), [where to find them](https://stable-diffusion-art.com/embedding/#Where_to_find_embeddings), and [how to use them](https://stable-diffusion-art.com/embedding/#How_to_use_embeddings).

Contents \[[hide](https://stable-diffusion-art.com/embedding/#)\]

- [What is embedding?](https://stable-diffusion-art.com/embedding/#What_is_embedding)
    - [How does textual inversion work?](https://stable-diffusion-art.com/embedding/#How_does_textual_inversion_work)
    - [Examples of embeddings](https://stable-diffusion-art.com/embedding/#Examples_of_embeddings)
- [Where to find embeddings](https://stable-diffusion-art.com/embedding/#Where_to_find_embeddings)
- [How to use embeddings](https://stable-diffusion-art.com/embedding/#How_to_use_embeddings)
    - [Web interface](https://stable-diffusion-art.com/embedding/#Web_interface)
    - [AUTOMATIC1111](https://stable-diffusion-art.com/embedding/#AUTOMATIC1111)
    - [Note on using embeddings in AUTOMATIC1111](https://stable-diffusion-art.com/embedding/#Note_on_using_embeddings_in_AUTOMATIC1111)
- [Some embeddings I like](https://stable-diffusion-art.com/embedding/#Some_embeddings_I_like)
    - [wlop\_style](https://stable-diffusion-art.com/embedding/#wlop_style)
    - [Kuvshinov](https://stable-diffusion-art.com/embedding/#Kuvshinov)
- [Difference between embedding, dreambooth and hypernetwork](https://stable-diffusion-art.com/embedding/#Difference_between_embedding_dreambooth_and_hypernetwork)
- [Pros and Cons of using embedding](https://stable-diffusion-art.com/embedding/#Pros_and_Cons_of_using_embedding)

## What is Embedding?

Embedding is the result of [textual inversion](https://textual-inversion.github.io/), a method to define new keywords in a model without modifying it. The method has gained attention because its capable of injecting new **styles** or **objects** to a model with as few as 3 -5 sample images.

### How Does Textual Inversion Work?

The amazing thing about textual inversion is NOT the ability to add new styles or objects—other fine-tuning methods can do that as well or better. It is the fact that it can do so *without* changing the model.

The diagram from the original research article reproduced below illustrates how it works.

[![how does embedding work.](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-40.png?resize=480%2C417&ssl=1)](https://stable-diffusion-art.com/embedding/image-40-2/)

New embedding is found for the new token S\* through textual inversion.

First you define a **new** **keyword** that’s **not** in the model for the new object or style. That new keyword will get **tokenized** (that is represented by a number) just like any other keywords in the prompt.

Each token is then converted to a unique **embedding vector** to be used by the model for image generation.

Textual inversion finds the embedding vector of the new keyword that best represents the new style or object, without changing any part of the model. You can think of it as finding a way *within* the language model to describe the new concept.

### Examples of Embeddings

Embeddings can be used for new objects. Below is an example of injecting a toy cat. Note that the new concept (toy cat) can be used with other existing concepts (boat, backpack, etc) in the model.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-39.png?resize=480%2C115&ssl=1)](https://stable-diffusion-art.com/embedding/image-39-2/)

Example of embedding an object.

Embeddings can also be a new style. The example below shows embedding a new style and transferring the style to different context.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-41.png?resize=480%2C96&ssl=1)](https://stable-diffusion-art.com/embedding/image-41-2/)

Example of embedding a style.

## Where to Find Embeddings

Hugging Face host the [Stable Diffusion Concept Library](https://huggingface.co/sd-concepts-library), which is a repository of large number of custom embeddings.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-47.png?resize=480%2C199&ssl=1)](https://huggingface.co/sd-concepts-library)

Stable Diffusion concepts library.

[**Civtai**](https://civitai.com/) is another great site you can browse models, including embeddings. Filter with “textual inversion” to view embeddings only.

### Web Interface

[Stable Diffusion Conceptualizer](https://huggingface.co/spaces/sd-concepts-library/stable-diffusion-conceptualizer) is a great way to try out embeddings without downloading them.

First identify the embedding you want to test in the [Concept Library](https://huggingface.co/sd-concepts-library). Let’s say you want to use this [Marc Allante style](https://huggingface.co/sd-concepts-library/style-of-marc-allante). Next, identify the **token** needed to trigger this style. You can find it in the file `[token_identifier.txt](https://huggingface.co/sd-concepts-library/style-of-marc-allante/blob/main/token_identifier.txt)`, which is `<Marc_Allante>`.

Putting in the prompt

> `<Marc_Allante>` a dog

Gives you the unique Marc Allante style.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-42.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/embedding/image-42-2/)

The downside of web interface is you cannot use the embedding with a different model or change any parameters.

### AUTOMATIC1111

Using embedding in AUTOMATIC1111 is easy.

First, download an embedding file from the [Concept Library](https://huggingface.co/sd-concepts-library). It is the file named `learned_embedds.bin`. Make sure don’t right click and save in the below screen. That will save a webpage that it links to. Click of the file name and click the download button in the next page.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-43.png?resize=480%2C133&ssl=1)](https://stable-diffusion-art.com/embedding/image-43-2/)

The embedding file.

Next, **rename the file as the keyword you wanted to use** this embedding with. It has to be something not exist in the model. `marc_allante.bin` is a good choice.

Put it in the `embeddings` folder in the GUI’s working directory:

```
stable-diffusion-webui/embeddings
```

Restart the GUI. In startup terminal, you should see a message like:

> Loaded a total of 1 textual inversion embeddings.  
> Embeddings: marc\_allante

Use the filename as part of the prompt to

For example, the following prompt would work on AUTOMATIC1111.

> (`marc_allante:1.2)` a dog

We get the image with the expected style.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-44.png?resize=480%2C480&ssl=1)](https://stable-diffusion-art.com/embedding/image-44-2/)

### Note on Using Embeddings in AUTOMATIC1111

If you pay attention to the prompt, you would notice I have [increased the strength](https://stable-diffusion-art.com/fine-tune-your-ai-images-with-these-simple-prompting-techniques/#Adjust_keyword_strength_using_weight) of the triggering keyword `marc_allante`. I found that it is necessary to adjust the keyword strength. This may have something to do with the way AUTOMATIC1111 loads the embedding.

**You may have to play with the keyword strength to get the effect you want**. Below is an example of varying the strength while keeping the seed and everything else the same.

[![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/image-45.png?resize=480%2C189&ssl=1)](https://stable-diffusion-art.com/embedding/image-45-2/)

Adjust keyword strength to get the effect you want.

To further complicate the matter, the strength needed could be different for different seed values.

## Some Embeddings I Like

There are many embeddings available than I can try. Here’s a few I found that I like.

### wlop\_style

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00558-964685455-wlop_style-_0.6-m_wlop_1.2-woman-wearing-dress-perfect-face-beautiful-detailed-eyes-long-hair-birds.png?resize=480%2C349&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00566-964685455-wlop_style-_0.6-m_wlop_1.4-woman-wearing-dress-perfect-face-beautiful-detailed-eyes-long-hair-birds.png?resize=480%2C349&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00572-1548439776-wlop_style-_0.6-m_wlop_1.4-woman-wearing-dress-perfect-face-beautiful-detailed-eyes-long-hair-birds.png?resize=480%2C349&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00567-964685456-wlop_style-_0.6-m_wlop_1.4-woman-wearing-dress-perfect-face-beautiful-detailed-eyes-long-hair-birds.png?resize=480%2C349&ssl=1)

wlop\_style embedding with wlop-any model

If you have played with Stable Diffusion base models, you will find it impossible to generate [wlop](https://www.artstation.com/wlop)‘s style no matter how hard you try. Embedding together with a custom model can finally do this.

The [wlop\_style](https://huggingface.co/datasets/Nerfgun3/wlop_style) embedding is able to render some nice illustration style of the artist wlop. It should be used with SirVeggie’s [wlop-any](https://huggingface.co/SirVeggie/wlop) custom model. (See this [guide](https://huggingface.co/SirVeggie/wlop) for installing custom models.)

[Direct download link – wlop\_style embedding](https://huggingface.co/datasets/Nerfgun3/wlop_style/resolve/main/wlop_style.pt)

[Direct download link – wlop-any model](https://huggingface.co/SirVeggie/wlop/resolve/main/wlop-any.ckpt)

If you try it out, you may find it doesn’t work at all. What you need to do is [adjusting the prompt strength](https://stable-diffusion-art.com/embedding/#Note_on_using_embeddings_in_AUTOMATIC1111).

A working prompt for AUTOMATIC1111 is

> (wlop\_style :0.6) (m\_wlop:1.4) woman wearing dress, perfect face, beautiful detailed eyes, long hair, birds

Negative prompt:

> closed eyes, disfigured, deformed

**wlop\_style** is keyword for embedding, **m\_wlop** is keyword for the model.

Don’t get frustrated if you don’t get the style. Try changing the prompt strengths of the two keywords. Some objects may simply doesn’t work with the embedding. Try some common objects in wlop’s artworks.

### Kuvshinov

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00676-3637224931-kuvshinov-a-woman-with-beautiful-detailed-eyes-highlight-hair.png?resize=480%2C480&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00684-3472482072-kuvshinov_0.6-a-woman-with-beautiful-detailed-eyes-highlight-hair.png?resize=480%2C480&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00685-3472482073-kuvshinov_0.6-a-woman-with-beautiful-detailed-eyes-highlight-hair.png?resize=480%2C480&ssl=1)

![](https://i0.wp.com/stable-diffusion-art.com/wp-content/uploads/2022/12/00678-3637224933-kuvshinov-a-woman-with-beautiful-detailed-eyes-highlight-hair.png?resize=480%2C480&ssl=1)

Kuvshinov is a Russian illustration. You can use the [kuvshinov](https://huggingface.co/sd-concepts-library/kuvshinov) [embedding](https://huggingface.co/sd-concepts-library/kuvshinov) with Stable Diffusion [v1.4](https://stable-diffusion-art.com/models/#Stable_diffusion_v14).

[Direct download link](https://huggingface.co/sd-concepts-library/kuvshinov/resolve/main/learned_embeds.bin)

Prompt:

> (\_kuvshinov:1), a woman with beautiful detailed eyes, highlight hair

Negative prompt:

> disfigured, deformed

(Note I have renamed the embedding as `_kuvshinov.bin`)

## Difference Between Embedding, Dreambooth and Hypernetwork

There are three popular methods to fine-tune Stable Diffusion models: textual inversion (embedding), [dreambooth](https://stable-diffusion-art.com/dreambooth/) and hypernetwork.

**Embedding** defines new keyword to describe a new concept without changing the model. The embedding vectors are stored in .bin or .pt files. Its file size is very small, usually less than 100 kB.

**Dreambooth** injects a new concept by fine-tuning the whole model. The file size is typical of Stable Diffusion, around 2–4 GB. The file extension is the same as other models, ckpt.

**Hypernetwork** is an additional network attached to the denoising UNet of Stable Diffusion model. The purpose is to fine-tune a model without changing the model. The file size is typically about 100 MB.

## Pros and Cons of Using Embedding

One of the advantages of using embedding is its small size. With file size of 100 KB or less, it is simple to store multiple of them in your local storage. Because embeddings are just new keywords, they can be used together in the same image.

The drawback of using embedding is sometimes its not clear which model it is supposed to be used with. If the trainer didn’t say, you can start with [v1.4](https://stable-diffusion-art.com/models/#Stable_diffusion_v14) or [v1.5](https://stable-diffusion-art.com/models/#Stable_diffusion_v15). You may also want to include [VAE](https://stable-diffusion-art.com/how-to-use-vae/) to see if that makes any difference. For anime styles, it is not uncommon for trainers to use anime models like [Anything v3](https://stable-diffusion-art.com/models/#Anything_V3).

In general, I found using embedding a bit more difficult than using [custom models](https://stable-diffusion-art.com/models/). I had trouble reproducing the demo styles in many embeddings I downloaded. It’s true that I may get there if I keep tweaking the keyword strengths, but in reality people move on after a few tries.

---

#AI #article
