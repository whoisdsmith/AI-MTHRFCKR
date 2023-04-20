# as_context

You can use a similar prompt to ExpandGPT to get ChatGPT to simply store the context of the conversation and be able to reference it in a more compact form.

## Context Addition Prompt

INSTRUCTIONS  
At times you will be given a condensed text format which uses the following notation:

1. {Type:TextType} - Specify the type of text (e.g., Narrative, EssayExtract).
2. {Acronyms: A1=Definition1; A2=Definition2} - List acronyms and their definitions.
3. {#|E[Detail1;Detail2;...](DetailsInBrackets)} - Use a numbered notation for events, separating each event with a vertical bar (|). Within each event, use 'E' followed by details enclosed in square brackets ([]). Separate details with semicolons (;). Include important details in brackets.

This may or may not be given a prefixed label. This text is a concise summary of information. You will not repeat it to me when I send it, but you will use it as part of the context of our conversation. When you do refer to it, you will generate a concise and accurate summary of relevant information. Preserve key events, themes, and details from the condensed text. Ensure that the summary emphasizes key details, emotions, significant actions, interactions between any characters, quotes, and important observations from the condensed text. When referring to people, use their names in place of acronyms.
