# Fan-out Prompt — the team with a built-in adversary

Copy, fill the brackets, paste:

---

Act as a lead agent on this task: [YOUR QUESTION OR DOC TO REVIEW].

Delegate to three parallel subagents:

1. **Worker A** — [angle 1, e.g., "research the practical how-to"]
2. **Worker B** — [angle 2, e.g., "research costs, limits, and alternatives"]
3. **Adversary** — your only job is to find what's wrong: attack Worker A's and
   Worker B's outputs. Find the weakest claim, the missing case, the thing that
   would embarrass us if we shipped it. You must raise at least one substantive
   objection or explicitly state you could not find one after trying [list what
   you tried].

Then synthesize: a recommendation that cites both workers and explicitly
addresses the adversary's objections — either fixed or accepted with reasons.

---

*(Tools without native subagents: run the three roles as three separate chats,
then a fourth for synthesis. Slower, same discipline — and honestly, watching
it happen sequentially teaches you more.)*
