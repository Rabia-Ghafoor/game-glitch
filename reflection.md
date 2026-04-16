# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
-- GO Lower notification regardless of the input 
-- even after clicking the new game, the game starting but with a caveat, because the note was still showing 
-- the 'show hint' button was not working as expected. Even after clikcing it multiple times, it failed to show any hints 
-- the data type for comparing the number was not correct
-- the range for the hard more was supposed to be narrower instead of (1-100)

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude Code and ChatGPT
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI suggestion to fix the intentional bugs baked within the game-glitch codebase were correct. 
Some of the AI suggestions Claude were good and detail orinted. AI pointed that when Hard mode is selected the range is supposed to be narrower not broader. So that was a good catch. 


- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Most of the suggestions were misleading

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
By using my prior knowledge and AI Claude Code and testing the app on the localhost as wll.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  Tested the data using assertequals 

- Did AI help you design or understand any tests? How?

Yes it gave me more ideas in  a few minutes. I would have eventually reached that stage too, but it would have taken me like 10-15 mins to thinks all cases, designs, drawbacks. So AI was definitely blazingly fast.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The reason why the secret number kept changing is because it follow the random number generator patteren

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I would explian reruns are essentially about starting the entire process the beginning, instead of fixing the problem at hand. It is analogous to sourcing the raw materials for the shoe, taking it factory, converting them to a shoe shape, and so on, instead of shoe lace, the problem at hand.

- What change did you make that finally gave the game a stable secret number?
Made lots of changes from the range for the hard mode, to data type for guessing the number.


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

I really like how I always use CLI commands for Git. So this is a small habit but meaningful to me, and makes me remember all the CLI commands on the top of my head. So, i I wil be using it.
- What is one thing you would do differently next time you work with AI on a coding task?
Be more succinct in my  prompts to AI
- In one or two sentences, describe how this project changed the way you think about AI generated code.
Definitely made me more reliant on AI, instead of training myself to look for cues.
