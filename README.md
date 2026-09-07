# Build Your First Agent Workflow

**Heather Wilde · KCDC 2026 · Wednesday, September 9 · Room 2215-A**

Build a small agent workflow you can run again tomorrow: a job, explicit boundaries, persistent context, a reusable procedure, a bounded retry loop, and a review step. Claude Code is the guided tool. Bring another assistant if you already use one.

**Core session: 8:00–11:30, including two 10-minute breaks.** The original room block ends at noon; 11:30–12:00 is optional help, subject to the conference schedule. Research and tool documentation checked September 7, 2026. [Sources and corrections](docs/RESEARCH.md).

## Presentation

[Download the slide deck](presentation/build-your-first-agent-workflow-deck.pptx) · [Full speaker notes](presentation/SPEAKER_NOTES.md). The deck and exercises use the same 210-minute schedule.

## Set up before arrival

1. Install Git and Python 3.9+ (no Python packages needed). On Windows use `py -3` wherever this guide says `python3`.
2. Install [Claude Code](https://code.claude.com/docs/en/setup) and sign in using an eligible subscription, organization account, or API billing. Confirm access ahead of time; no particular plan price or free entitlement is promised. Other tools: [cheat sheets](cheatsheets/README.md).
3. Fork this repository, then clone **your fork**, and open a terminal in it:
   ```sh
   git clone https://github.com/YOUR-USERNAME/first-agent-workshop.git
   cd first-agent-workshop
   python3 workshop.py preflight
   ```
4. Open your agent in that folder. Ask: `Create output/hello.md containing hi, then read it back.` Confirm the file exists. This checks sign-in and file access separately from the Python preflight.
5. Use the included fictional [meeting transcript](data/meeting.txt), or bring a sanitized repetitive task. No work-account connector is required. Follow your organization's network policy. If setup is blocked, pair with a working laptop or use the browser/manual lane.

## Try the workshop now

```sh
python3 workshop.py check examples/summary.bad.json
python3 workshop.py check examples/summary.good.json
python3 workshop.py rehearse
python3 workshop.py rehearse --impossible
```

Expected: **FAIL (exit 1), PASS (exit 0), DONE after two attempts (exit 0), ESCALATED after three (exit 2)**. These rehearsal commands use scripted fixtures, make no model calls, and cost nothing. They demonstrate the controller and grader, not model competence. Results are in `output/rehearsal/`; a later rehearsal replaces only those rehearsal results.

For a **live agent**, start [Module 1](modules/01-first-agent/README.md). Ask your agent to produce `output/summary.json` from the transcript, then run the check. Do not give it the answer key or let it edit the grader. An agent with unrestricted filesystem access could still alter both; use a separate grader environment for a real deployment.

## The 210-minute run of show

| Time | Minutes | Work | Evidence |
|---|---:|---|---|
| 8:00–8:20 | 20 | Welcome, setup, demo, choose a job | Working file access; task selected |
| 8:20–8:55 | 35 | [1: First agent](modules/01-first-agent/README.md) | Output checked; boundary attempt recorded |
| 8:55–9:10 | 15 | [2: Memory](modules/02-memory/README.md) | Fresh session reads saved fact |
| 9:10–9:20 | 10 | Break 1 | Full ten minutes |
| 9:20–10:00 | 40 | [3: Skills + tools](modules/03-skills/README.md) | Procedure used; source checked; injection debrief |
| 10:00–10:30 | 30 | [4: Loops](modules/04-loops/README.md) | Success stops; impossible input escalates |
| 10:30–10:40 | 10 | Break 2 | Full ten minutes |
| 10:40–11:05 | 25 | [5: Team](modules/05-team/README.md) | Workers finish, reviewer checks, lead resolves |
| 11:05–11:30 | 25 | Contract, rerun, questions, share-out | Named owner, limits, next run, saved artifacts |

Exercises include time to launch, work, check, and debrief. If behind, shorten share-outs or optional connector setup. Keep both breaks and the failure test.

## Find your files

[Agent Contract](templates/AGENT_CONTRACT.md) · [Universal browser/manual lane](cheatsheets/universal.md) · [Facilitator guide](docs/FACILITATOR.md) · [Research](docs/RESEARCH.md) · [Injection demo](injection-demo/README.md).

`data/` contains fictional input. `examples/` contains clearly marked answer keys and a worked skill. `output/` is ignored by git so workshop results stay local unless you deliberately publish them. Keep real personal, customer, and secret data out of your public fork.

Questions: [open an issue](https://github.com/heathriel/first-agent-workshop/issues) or contact [@heathriel](https://twitter.com/heathriel).
