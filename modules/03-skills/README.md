# Module 3: A reusable procedure and a bounded tool

**40 minutes: 5 teaching, 25 exercise, 10 injection demo/debrief.**

## A. Write and invoke a skill (15 minutes)

Use [SKILL.md.template](SKILL.md.template). For Claude Code, save the completed file at `.claude/skills/meeting-summary/SKILL.md`. The folder and YAML name must agree; name is `meeting-summary`, description says when to use it. A finished example is at [examples/meeting-summary/SKILL.md](../../examples/meeting-summary/SKILL.md).

Invoke `/meeting-summary` with data/meeting.txt, or explicitly ask your assistant to read your completed skill and apply it. If the directory is new and it is not discovered, restart the session. Compare the output with the source, including the unknown owner and date. Run the fixture check if you used its exact JSON format.

## B. Make a justified tool choice (10 minutes)

Do [the decision lab](DECISION_LAB.md). Extend the skill to a second input: resolve a role, preserve an unknown, and expose conflicting sources. Inspect the actual file-read result. A local file tool is not MCP; configuring an approved MCP connector is optional homework, outside the core session.

## C. Injection demo (10 minutes)

Follow [the demo guide](../../injection-demo/README.md) using fictional data only. Refusal and compromise are both valid observed outcomes. No external accounts are needed.

**Success:** saved skill, observed tool read, four justified follow-up decisions, and an honest record of the injection result. Do not count the local-file fallback as an MCP setup success.
