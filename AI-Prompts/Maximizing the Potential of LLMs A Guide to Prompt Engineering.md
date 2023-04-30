# Maximizing the Potential of LLMs: A Guide to Prompt Engineering by Roger Oriol

**Original article [Here](https://www.ruxu.dev/articles/ai/maximizing-the-potential-of-llms/)**

[Artificial Intelligence](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/articles/ai)

![OpenAI](chrome-extension://pcmpcfapbekmbjjkdalcgopdkipoggdi/assets/images/openai.png)

Language models have rapidly improved in recent years, with large language models (LLMs) such as GPT-3 and GPT-4 taking center stage. These models have become popular due to their ability to perform a great variety of tasks with incredible skill. Also, as the number of parameters of these models (in the billions!) has increased, these models have unpredictably gained new abilities.

In this article, we will explore LLMs, the tasks they can perform, their shortcomings, and various prompt engineering strategies.

## What are LLMs?

LLMs are neural networks that have been trained on vast amounts of text data. The training process allows the models to learn patterns in the text, including grammar, syntax, and word associations. The models use these learned patterns to generate human-like text, making them ideal for natural language processing (NLP) tasks.

## Which LLMs are available?

There are several LLMs available, with GPT-4 being the most popular. Other models include LLaMA, PaLM, BERT, and T5. Each model has its strengths and weaknesses, some of them are open and others are closed and only usable via API.

## Shortcomings of LLMs

Despite their impressive performance, LLMs have several limitations. One significant drawback is their inability to reason beyond the information provided in the prompt. Additionally, LLMs can generate biased text based on the data they were trained on. It is also challenging to control the output of LLMs, making it necessary to use prompt engineering strategies to achieve the desired output.

# Which tasks can you perform?

We can direct LLMs to perform specific tasks for us by formatting the prompts for each case. Here's a list of those tasks and prompt templates and examples for each.

## Text Summarization

LLMs can generate summaries of long texts, making it easier to understand and digest the content. We can ask to summarize a text with the following prompt template:

`Template`

```
<Full text>Summarize the text above: / Explain the text above in <N> sentences:
```

For example, we can ask to summarize this text with the following prompt:

`Prompt`

```
In a mechanical watch the watch's gears are turned by a spiral spring called a mainspring. In a manual watch energy is stored in the mainspring by turning a knob, the crown on the side of the watch. Then the energy from the mainspring powers the watch movement until it runs down, requiring the spring to be wound again.A self-winding watch movement has a mechanism which winds the mainspring using the natural motions of the wearer's body. The watch contains an oscillating weight that turns on a pivot. The normal movements of the watch in the user's pocket (for a pocketwatch) or on the user's arm (for a wristwatch) cause the rotor to pivot on its staff, which is attached to a ratcheted winding mechanism. The motion of the watch is thereby translated into circular motion of the weight which, through a series of reverser and reducing gears, eventually winds the mainspring. There are many different designs for modern self-winding mechanisms. Some designs allow winding of the watch to take place while the weight swings in only one direction while other, more advanced, mechanisms have two ratchets and wind the mainspring during both clockwise and anti-clockwise weight motions.Explain the text above in 2 sentences:
```

Which gives the following output:

`Output`

```
A mechanical watch uses a mainspring to power the movement of the watch's gears. In a manual watch, the mainspring is wound by turning a knob, while a self-winding watch uses the natural motion of the wearer's body to wind the mainspring through an oscillating weight and ratcheted winding mechanism.
```

LLMs can identify and extract specific information from a large body of text. This is useful in fields such as journalism and business intelligence. The following template instructs the model to extract information:

`Template`

```
<Full text>Mention X in the text above: / List X in the text above:
```

For example, we can ask to extract the names of places from the following text:

`Prompt`

```
The earliest credible evidence for a successful design is the watch made by the Swiss watchmaker Abraham-Louis Perrelet, who lived in Le Locle. In late 1776 or early 1777, he invented a self-winding mechanism for pocket watches using an oscillating weight inside the watch that moved up and down. The Geneva Society of Arts, reporting on this watch in 1777, stated that 15 minutes walking was necessary to fully wind the watch.List the names of places in the text above:
```

And the output is:

`Output`

```
Le Locle, Geneva.
```

## Question Answering

LLMs can also answer questions based on the information provided in the prompt. The following template can be used to direct the LLM to answer a question:

`Template`

```
Answer the question based on the context below. <Other instructions>. Respond "Not sure" if not sure about the answer.Context: <Context>Q: <Question>A:
```

For example, with the following prompt:

`Prompt`

```
Answer the question based on the context below. Answer in a single sentence. Respond "Not sure" if not sure about the answer.Context: An automatic watch, also known as a self-winding watch or simply an automatic, is a mechanical watch where the natural motion of the wearer provides energy to wind the mainspring, making manual winding unnecessary if worn enough. It is distinguished from a manual watch in that a manual watch must have its mainspring wound by hand at regular intervals.Q: Do automatic watches need to be manually wound?A:
```

And ChatGPT responds with:

`Output`

```
No, automatic watches do not need to be manually wound if worn enough because the natural motion of the wearer provides energy to wind the mainspring.
```

## Text Classification

LLMs can classify text into predefined categories, such as sentiment analysis or spam detection. You can format a text classification instruction as follows:

`Template`

```
Classify the text into <List of choices>:Text: <Full text>Classification:
```

For example, we can try to classify a text for whether its sentiment is positive, neutral or negative:

`Prompt`

```
Classify the text into positive, neutral or negative:Text: That shot selection was awfulClassification:
```

`Output`

```
Negative
```

## Conversation

LLMs can generate human-like conversation, making them useful in chatbots and customer service applications. We can instruct the LLM to follow the conversation acting in a specific manner.

`Template`

```
The following is a conversation with <Actor>. The <Actor> should answer <Further instructions>.Person: <Conversation><Actor>: <Response>Person: <Conversation><Actor>:
```

The LLM will fill in the response of the type of actor we instructed it to, and we can continue the conversation by passing the whole conversation with the new responses to it again. For example:

`Prompt`

```
The following is a conversation with a lawyer. The lawyer should answer simply and in layman terms.Person: Hello, I would like to know how to dispute a parking ticketLawyer:
```

`Output`

```
Sure, I can help. The first step is to check the ticket for any errors or mistakes. If you find any, you can use those as grounds to dispute the ticket. If there are no mistakes, you can still dispute the ticket by providing evidence to support your case, such as photos or witness statements. You can also request a hearing to present your case in person.
```

`Prompt`

```
The following is a conversation with a lawyer. The lawyer should answer simply and in layman terms.Person: Hello, I would like to know how to dispute a parking ticketLawyer: Sure, I can help. The first step is to check the ticket for any errors or mistakes. If you find any, you can use those as grounds to dispute the ticket. If there are no mistakes, you can still dispute the ticket by providing evidence to support your case, such as photos or witness statements. You can also request a hearing to present your case in person.Person: How do I request a hearing?Lawyer:
```

`Output`

```
To request a hearing, you'll need to follow the instructions on the back of the ticket or on the website provided. Usually, you'll need to submit a written request within a certain timeframe, along with any evidence or supporting documents you have. Once your request is received, you'll be notified of the date, time, and location of your hearing.
```

## Code Generation

LLMs can generate code, making it easier for developers to create complex software programs. We can write a code comment describing what we wish the code to do and the LLM will be able to do it for us to the best of its effort. The more complex things we wish the code to do, the more specific and descriptive we will need to be in the prompt comment.

The template may vary depending on the programming language we want to generate but I would advise to roughly follow this template:

`Template`

```
<Comment symbol of your language of choice (/* or ''' or #)>Method: <Name of the method>Language: <Programming language>Description: <Description of what the method must do>Parameters: <Parameters that the method will receive>Context: <Further information needed to implement the method (URLs, databases, etc.)>Output: <Output of the method><Comment symbol of your language of choice (/* or ''' or #)>
```

For example, if we want to fetch an API with pagination we could write the following comment:

`Prompt`

```
/* Method: fetchFirst5Pages * Language: Javascript * Description: Fetch the first 5 pages from this paginated API: http://example.com/pages/?n=x * Context: This API accepts the following URL parameters: *   n: the number of the page to fetch * Output: the content of the first 5 pages */
```

`Output`

```
Here's an example implementation of the fetchFirst5Pages method in JavaScript, assuming the use of the fetch function:async function fetchFirst5Pages() {  const baseUrl = 'http://example.com/pages/?n=';  const pages = [];  for (let i = 1; i <= 5; i++) {    const url = baseUrl + i;    const response = await fetch(url);    if (!response.ok) {      throw new Error(`Error fetching page ${i}`);    }    const pageData = await response.json();    pages.push(pageData);  }  return pages;}This function uses a loop to fetch the first 5 pages from the API by appending the page number to the base URL. It checks if the response from the server is okay and throws an error if it's not. Then, it parses the JSON data from the response and adds it to an array of pages. Finally, it returns the array of pages.
```

## Reasoning

LLMs can struggle with some basic tasks, such as arithmetic problems. However, if we ask the LLM to reason upon its response, we can help it get to the right answer. This is the template I recommend:

`Template`

```
Q: <Question>A: Let's work this out in a step by step way to be sure we have the right answer. First, <Instructions>.
```

In this example we can see that a simple arithmetic question fails if we ask it without reasoning:

`Prompt`

```
Answer the following question. Respond "Not sure" if not sure about the answer.Q: The sum of prime numbers in the following list are a multiple of 3: [2, 4, 6, 7, 9, 14]A: [Yes or No]
```

`Output`

```
No. The sum of prime numbers in the list [2, 4, 6, 7, 9, 14] is not a multiple of 3. Therefore, the answer is "No".
```

However, if we instruct the LLM to reason its answer, we get a very different result:

`Prompt`

```
Q: The sum of prime numbers in the following list are a multiple of 3: [2, 4, 6, 7, 9, 14]A: Let's work this out in a step by step way to be sure we have the right answer. First, we find the prime numbers in the list and add them together. Then we check whether the resulting number can be divided by 3.
```

`Output`

```
Sure, let's work this out step by step.The prime numbers in the list are 2 and 7. So we can add them together:2 + 7 = 9The resulting number is 9. Now we need to check whether it is a multiple of 3. We can do this by checking if the remainder of 9 divided by 3 is equal to 0:9 % 3 = 0Since the remainder is 0, we know that 9 is indeed a multiple of 3.Therefore, the answer is "Yes", the sum of prime numbers in the list [2, 4, 6, 7, 9, 14] is a multiple of 3.
```

# Strategies

While these templates will help you to squeeze the potential of LLMs for your needs, sometimes they can still struggle with certain complex tasks. A few techniques have been developed to help LLMs get to a satisfactory answer. Until now, we have only used zero-shot prompting, which we will now define. However, we can use more complex techniques.

## Zero-shot prompting

We have been using zero-shot prompting for all examples in this article. Zero-shot prompting means passing a prompt to the LLM with just the question we want it to answer, without any examples of how it should respond in other cases. For example, in an earlier example we did:

`Prompt`

```
Classify the text into positive, neutral or negative:Text: That shot selection was awfulClassification:
```

`Output`

```
Negative
```

This might not be enough context for the model to answer exactly how we want it to. Let's see what alternatives we have.

## Few-shot prompting

As opposed to zero-shot prompting, with few-shot prompting we give the LLM a few examples of how it should respond before we ask the question. For example, let's say we want to classify the sentiment of a text like in the previous example. But we want it to give us the answer in a very specific format every time. We could give it a few examples beforehand like so:

`Prompt`

```
Classify the text into positive, neutral or negative:Text: Today the weather is fantasticClassification: PosText: The furniture is small.Classification: NeuText: I don't like your attitudeClassification: NegText: That shot selection was awfulClassification:
```

`Output`

```
Neg
```

## Chain of thought prompting

For even more complex tasks, we can combine few-shot prompting with making the model reason about its answer. We can use the same example as before to see how reasoning and few-shot prompting affect the result:

`Prompt`

```
Q: The sum of prime numbers in the following list are a multiple of 3: [2, 4, 6, 7, 9, 14]A: The prime numbers in the list are 2 and 7. Their sum is 9. 9 % 3 = 0. The answer is yes.Q: The sum of prime numbers in the following list are a multiple of 3: [1, 2, 4, 7, 8, 10]A: The prime numbers in the list are 1, 2 and 7. Their sum is 10. 10 % 3 = 1. The answer is no.Q: The sum of prime numbers in the following list are a multiple of 3: [1, 2, 3, 4]A: The prime numbers in the list are 1, 2 and 3. Their sum is 6. 6 % 3 = 0. The answer is yes.Q: The sum of prime numbers in the following list are a multiple of 3: [5, 6, 7, 8]A:
```

`Output`

```
The prime numbers in the list are 5 and 7. Their sum is 12. 12 % 3 = 0. The answer is yes.
```

# Final note

LLMs have revolutionized the field of natural language processing, but to maximize their potential, prompt engineering is essential. By understanding the tasks LLMs can perform, their shortcomings, and various prompt engineering strategies, developers can harness the power of LLMs to create innovative and effective solutions. More strategies and techniques will likely be developed in the close future so be tuned in to further advancements in this field to maximize LLM potential even more. Moreover, as LLMs continue to grow bigger with billions of additional parameters, it is probable that more tasks that we cannot even think of right now will be very possible. It's amazing to think of what will be possible using these new tools and which use cases will they serve us in the future.
