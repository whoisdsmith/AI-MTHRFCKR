## Style & Format

---

When creating prompts, adopting a specific style is essential for several reasons. A well-defined style helps in the following ways:

1. Consistency: A consistent style makes your prompts more predictable and easier to understand for the AI model. It ensures that the model receives clear instructions and produces the desired output across multiple prompts.
2. Clarity: A well-defined style ensures that your instructions are clear and unambiguous. This reduces the chances of the AI model misunderstanding your prompt or generating irrelevant or undesired responses.
3. Efficiency: A good style allows you to communicate your requirements effectively, reducing the need for multiple iterations or adjustments to the prompt. This saves time and resources.
4. Customization: By adopting a specific style, you can tailor the output to match your desired tone, format, and level of detail. This is particularly useful when trying to generate content that adheres to a particular brand voice, industry standard, or target audience.

When choosing a style for your prompts, consider the following factors:

1. Detail and specificity: Be as specific and detailed as possible about the desired context, outcome, length, format, and style.
2. Instruction placement: Put instructions at the beginning of the prompt, and use separators like ### or """ to separate the instruction and context.
3. Examples: Provide examples of the desired output format, which helps the model understand your expectations better.
4. Avoid fluff: Use concise and precise language to minimize ambiguity and confusion.
5. Positive instructions: Instead of just saying what not to do, say what to do instead.

By carefully considering the style and crafting your prompts accordingly, you can improve the quality and relevance of the AI model's responses, ultimately making your interactions with the AI more efficient and effective. [read more](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)

---

Identifying Main Arguments

```
Identify the main arguments presented in the following text. List them in the format below.

Argument 1:
Argument 2:
...
Text: """
{text input here} 

"""
```

Review Analysis

```
Analyze the customer review provided below and list the positive and negative aspects mentioned. write them in the format below.

Positive aspects:

- Aspect 1:
- Aspect 2: 
... 

Negative aspects:

- Aspect 1:
- Aspect 2:
...

Review: """
{customer_review_here}
"""
```

Comparing Ideas

```
Compare the two ideas presented in the following text. Please provide the similarities and differences in the format below.

Similarities:

- Similarity 1:
- Similarity 2: 
- ... 

Differences:

- Difference 1:
- Difference 2: 
- ...

Text: """
{text input here}
"""
```

Identifying Key Information

```
Extract the key information from the following paragraph. First, identify the main problem, then list any solutions mentioned, and finally note the potential benefits of implementing these solutions. Use following format.

Main problem:

- Problem 1
- Problem 2
...

Solutions:

- Solution 1:
- Solution 2: 
...

Potential benefits:

- Benefit 1:
- Benefit 2:
...

Text: """

{text input here}

"""
```

Generating Ideas

```
Generate a list of 10 creative ideas for a new mobile app. The app should be focused on helping people improve their mental health and wellbeing. List them in the format below.

Idea 1:
Idea 2:
...
Idea 10:
```

Paraphrasing

```
Paraphrase the following sentence: 

Artificial intelligence has the potential to transform many aspects of our lives, but it also comes with significant risks.

New sentence: While artificial intelligence can revolutionize various aspects of our existence, it is not without considerable dangers.
```

Extraction with defined format

```
Extract the important entities mentioned in the article below. First extract all company names, then extract all people names, then extract specific topics which fit the content and finally extract general overarching themes
Desired format:
Company names: <comma_separated_list_of_company_names>
People names: -||-
Specific topics: -||-
General themes: -||-

Text: """
{text input here}
"""
```

Extraction using few-shot

```
Extract keywords from the corresponding texts below.

Text: {text1}
Keywords: {example_of_keywords_for_text1}
###
Text: {text2}
Keywords: {example_of_keywords_for_text2}
###
Text: {text3}

Keywords:
```