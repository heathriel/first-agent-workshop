# Module 5: Workers first, reviewer second

**25 minutes: 5 teaching, 18 exercise, 2 debrief.**

Teams are useful when work separates cleanly. They can add latency, cost, and correlated errors. Compare against the single-agent result you already have.

1. Use [FANOUT_PROMPT.md](FANOUT_PROMPT.md). Worker A checks action coverage; Worker B checks unsupported owners, dates, and decisions. Each sees the transcript and proposed summary. If your tool has no team feature, use the [four copy/paste prompts](ROLE_PROMPTS.md) in four ordinary chats.
2. Run A and B in parallel if available, or sequentially in separate chats. Neither may delegate further. Give each five minutes and a 250-word limit.
3. **Wait for both outputs.** Then give their outputs and original source to the adversary. It must test claims against the source, identify any substantive objection with evidence, or describe what it checked and found sound. Do not require it to invent a flaw.
4. The lead synthesizes in 300 words: cite both workers, address each objection, and state remaining uncertainty. A human reruns the grader.

Use examples/summary.bad.json to guarantee a seeded unsupported-owner flaw for the practice review. For your actual result, a clean review is possible. A separate chat is a separate context, not statistical independence; the same model and evidence may produce the same mistake.

**Success:** output/worker-a.txt, worker-b.txt, review.txt, and synthesis.txt. The seeded Alex assignment is caught and resolved to UNKNOWN, the source is cited, and a human checks the resolution. Sequential roles satisfy the exercise; you do not need a multi-agent subscription.

“Worker,” “reviewer,” and “lead” are roles in this exercise, not product features. Four ordinary chats are sufficient. Do not claim one chat created independent workers unless you actually observed separate executions and received both outputs.

## Complete the correction

Keep all three action records and the decision string required by the exercise. Copy the bad fixture to `output/summary.json`, change the unsupported owner to `UNKNOWN`, and run `python3 workshop.py check output/summary.json`. Do not edit the answer key. Schema redesign is a separate decision; a review recommendation alone does not establish that the corrected artifact passes.
