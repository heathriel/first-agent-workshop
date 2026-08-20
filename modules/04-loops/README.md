# Module 4 — Loops: The Agent That Doesn't Stop Until It's Done

The pattern started life as "the Ralph loop"; the field now calls the discipline
**loop engineering**: **write a completion criterion a machine can check, run the
agent against it until it passes — and keep progress in files and git, not in the
agent's head.** Don't babysit the agent. Define done.

**A loop without a check that can fail is not automation — it's a runaway.**
Runaway loops are 2026's fastest-growing agent failure class. Budgets and step
caps are seatbelts; wear them. (Ask me about the day my $20 budget stopped at
$20.50. Best fifty cents I never spent.)

## Lane A — Claude Code
1. Fill in [`LOOP_CRITERION.md`](LOOP_CRITERION.md) — the check comes FIRST.
2. Run `/loop` with your task + criterion, **including the failure rule**
   ("after 3 failed attempts, stop and report").
3. ✅ Check: the loop STOPS on its own with the proof produced.
4. ✅ Check 2 (the important one): give it an impossible variant. It must
   escalate — not spin, not fabricate.
5. Bonus: schedule it (scheduled tasks → your excavated task, on the calendar).
   *If it isn't on the calendar, it doesn't exist.*

## Lane B — GitHub (no Claude sub needed)
1. In your fork: Issues → pick the prepared issue labeled `coding-agent-exercise`
   (or create one from [`COPILOT_ISSUE.md`](COPILOT_ISSUE.md)).
2. Assign it to **Copilot** (the **cloud agent** — GitHub's current name for it;
   it now self-reviews its work and lets you pick the underlying model).
3. ✅ Check: a PR appears, addressing the issue's acceptance checklist. Read the
   PR like a reviewer, not a fan: does it satisfy every checkbox?
