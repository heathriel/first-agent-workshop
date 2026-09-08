# Module 4: Retry with a stopping rule

**30 minutes: 5 explanation, 20 exercise, 5 debrief.**

A bounded retry loop checks work after each attempt and stops on success or a limit. A schedule starts work later. These are different controls. Claude Code `/loop` schedules prompts in an open session; it is not a durable service or a hard retry-until-valid controller.

1. Fill [LOOP_CRITERION.md](LOOP_CRITERION.md). Fix the checker before asking the agent to work.
2. Run `python3 workshop.py rehearse`. Expected FAIL then PASS, DONE after 2 attempts. Inspect output/rehearsal/trace.json. This uses scripted candidates, not an LLM.
3. In your live assistant, use this prompt:
   > Produce output/summary.json from data/meeting.txt using the Module 1 schema. Have me run python3 workshop.py check output/summary.json after each attempt and paste the errors. Make at most 3 attempts. Stop on PASS. Never alter the source, answer key, or checker. If still failing, write output/escalation.txt with attempts, evidence, blocker, and the decision needed from me. Do not send it externally.
4. You are the controller: count attempts, run the unchanged checker, and return its errors. For an automated controller, use the optional [live runner](../../live_loop.py): `python3 live_loop.py`. It requires a Claude CLI with ANTHROPIC_API_KEY set, makes billable model calls, and uses up to three calls with per-call budget/turn limits. Read the script first. It submits only the fictional fixture, uses no agent tools, and saves returned JSON itself.
5. Run `python3 workshop.py rehearse --impossible`. Expected three FAILs and ESCALATED, exit 2. **The nonzero exit and red terminal output are intentional.** This independently verifies the controller's failure path. For your live prompt, request a source-supported owner for L3; it must report missing information rather than inventing it. Record that result separately from the rehearsal.

**Success:** saved successful output, a trace or attempt log, and an escalation artifact. If a live model fails, keep the failed result and use rehearsal to complete the controller lesson. Do not count rehearsal as evidence of live-model reliability.

## Scheduling is optional

See [scheduling checklist](../../docs/SCHEDULING.md). Never claim this remains running after you close the laptop unless you configured and verified a durable scheduler. A manual next run is a valid core-workshop outcome.

## Optional Copilot lane

Use [COPILOT_ISSUE.md](COPILOT_ISSUE.md) to create an issue **in your fork** (forks do not copy issues; enable Issues under repository Settings if needed). Assign only if your account and organization expose the agent. Do not assume GitHub Free includes this entitlement. Review the diff and checks before merging. If access is missing, stay with the main exercise.

The optional runner uses bare mode, which does not read subscription sign-in. Set ANTHROPIC_API_KEY securely in your local environment; never put it in a file you commit. Provider API billing applies. The core human-controlled exercise works with your existing interactive subscription and does not require a new API key. [Bare-mode authentication](https://code.claude.com/docs/en/headless).

## Missing evidence

Three attempts is a ceiling, not a target. Stop earlier if the required evidence is absent. A checker PASS for `UNKNOWN` does not satisfy an additional demand for a named owner. Mark that demand BLOCKED and ask the human who owns accessibility. Using Alex with an UNVERIFIED label would still be a guess and violate the contract. Repeated fictional files are not independent confirmation. Preserve the failed proposal as evidence; do not adopt it.
