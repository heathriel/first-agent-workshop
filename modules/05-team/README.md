# Module 5 — From One Agent to a Team

When a job is too big for one employee, you don't hire a smarter employee.
You hire a team — with a lead, and with **one member whose whole job is to check
the others**. Your second hire is never another worker. It's the adversary.

(Self-review is not an independent channel. An adversary is.)

The field's name for this is **adversarial verification** (or "adversarial
debate") — one of the four current verification patterns, alongside LLM-as-judge
scoring, reflection loops, and step-by-step process checking. You're learning the
one that best survives contact with reality — because the biggest documented
multi-agent risk isn't hype, it's *error accumulation*: workers politely building
on each other's mistakes. The adversary is how you break the politeness.

## Exercise
1. Open [`FANOUT_PROMPT.md`](FANOUT_PROMPT.md), fill in a real question you'd
   want researched or a doc you'd want reviewed.
2. Run it: the lead delegates to **two parallel workers + one adversary**, then
   synthesizes.
3. ✅ Check: the synthesis cites both workers AND addresses at least one objection
   the adversary raised. If the adversary found nothing wrong, be suspicious —
   a check that passes suspiciously easily means check the check.

## Where the ceiling is (demo, not hands-on)
Bigger versions of this pattern — dynamic fan-outs, judge panels, graders that
loop workers until output meets a rubric — run in production today. So do their
failure modes: even Anthropic added subagent caps this summer. Fan-out needs
boundaries too. Same contract, more employees.
