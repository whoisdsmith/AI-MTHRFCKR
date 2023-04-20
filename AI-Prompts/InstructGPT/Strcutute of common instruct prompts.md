## Strcutute of common instruct prompts

A basic and useful structure of an instruct prompts can be look like this:

`Instruction` + `Direction to the next words`

  - `Generate a poem` + `based on following passage:`
  - `Create a report article` + `based on following passage`
  - `Write a summary` + `of the following passage`

### Example of using above structure

**Input:**

```
Write a poem based on the following:

ghosts, 4th dimension, AI, totalitarian, power
```

**Output:**

```
Ghosts of the 4th dimension roam,
A realm beyond our grasp, unknown.
Yet in this world, AI has grown,
Its power and influence has flown.

With algorithms and codes so bright,
It holds the key to endless might.
A totalitarian grip on sight,
And wields its power with all its might.

But is this power truly ours?
Or just a tool for those in power?
Their ghosts roam, but do they cower,
When faced with the consequences of their dower?

So let us heed this ghostly call,
And use AI for good, for all.
For in its power, we must not fall,
But rise above, and hear the call.
```

Better prompting ✅:

```
Write a thought-provoking poem that incorporates the themes of ghosts, the 4th dimension, AI, totalitarianism, and power. The poem should be structured in a traditional format with 4 stanzas and a consistent rhyme scheme.
```