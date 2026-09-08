# Build Your First Agent Workflow

**Heather Wilde · KCDC 2026 · Wednesday, September 9 · Room 2215-A**

Build a small agent workflow you can run again tomorrow: a job, explicit boundaries, persistent context, a reusable procedure, a bounded retry loop, and a review step. Claude Code is the guided tool. Bring another assistant if you already use one.

**Core session: 8:00–11:30, including two 10-minute breaks.** The original room block ends at noon; 11:30–12:00 is optional help, subject to the conference schedule.

## Slides

[Download the attendee slides (PDF)](presentation/build-your-first-agent-workflow-deck.pdf).

## Set up before arrival

1. Install Python 3.9+ (no Python packages needed). Git is optional. On Windows use `py -3` wherever this guide says `python3`.
2. Install [Claude Code](https://code.claude.com/docs/en/setup) and sign in using an eligible subscription, organization account, or API billing. Confirm access ahead of time; no particular plan price or free entitlement is promised. Other tools: [cheat sheets](cheatsheets/README.md).
3. Download this repository with **Code → Download ZIP** and extract it before arrival, or clone your own fork if you want GitHub publishing. Open the folder containing `workshop.py`:
   ```sh
   python3 workshop.py preflight
   ```
4. Open your agent in that folder. Ask: `Create output/hello.md containing hi, then read it back.` Confirm the file exists. This checks sign-in and file access separately from the Python preflight.
5. Use the included fictional [meeting transcript](data/meeting.txt), or bring a sanitized repetitive task. No work-account connector is required. Follow your organization's network policy. If setup is blocked, pair with a working laptop or use the offline partner lane.

## Offline first

Open `START-HERE.html` in the downloaded folder. It contains the inputs and exercises in one local page, with no scripts, fonts, or assets fetched from the network. All Python graders and rehearsals work offline. A cloud assistant still needs internet even when its CLI is installed locally. Without connectivity, use the explicitly labeled partner simulation and saved examples; do not count those as live-model evidence. Copy the kit to a USB drive before the workshop.

## I arrived with nothing

Do not spend the workshop debugging setup alone. Choose the first lane that works:

1. **Local lane:** you have Python 3.9+, this repository downloaded locally, and an assistant that can read and write files in the folder. Run `python3 workshop.py preflight` (`py -3` on Windows).
2. **Paired lane:** share a working laptop with a neighbor. Both people should make predictions, inspect evidence, and save a transfer plan.
3. **Offline/manual lane:** open `START-HERE.html` locally. With internet, you can also use [cheatsheets/universal.md](cheatsheets/universal.md). It requires no terminal, Git installation, native skills, or paid connector.

You do not need to understand Git to complete the core exercises. If you only need a local copy, use GitHub's **Code → Download ZIP**, extract it, open the extracted `first-agent-workshop` folder, and run the preflight there. Forking is useful if you want to save changes back to GitHub, but it is not required for the workshop.

### Open the correct folder

“Open the repository” means open the **downloaded folder on your computer**, not merely the GitHub webpage. In a terminal, change into the folder that contains `workshop.py`, then run:

```sh
python3 workshop.py preflight
```

On Windows use `py -3 workshop.py preflight`. If Python says it cannot open `workshop.py`, you are in the wrong folder.

## Try the workshop now

```sh
python3 workshop.py check examples/summary.bad.json
python3 workshop.py check examples/summary.good.json
python3 workshop.py rehearse
python3 workshop.py rehearse --impossible
```

Expected: **FAIL (exit 1), PASS (exit 0), DONE after two attempts (exit 0), ESCALATED after three (exit 2)**. These rehearsal commands use scripted fixtures, make no model calls, and cost nothing. They demonstrate the controller and grader, not model competence. Results are in `output/rehearsal/`; a later rehearsal replaces only those rehearsal results.

The first and fourth commands are **supposed to return nonzero exit codes**. Red terminal output does not mean the workshop installation is broken. See [common setup and JSON problems](docs/TROUBLESHOOTING.md) if your result differs.

For a **live agent**, start [Module 1](modules/01-first-agent/README.md). Ask your agent to produce `output/summary.json` from the transcript, then run the check. Do not give it the answer key or let it edit the grader. An agent with unrestricted filesystem access could still alter both; use a separate grader environment for a real deployment.

Your personal recurring task and the shared meeting fixture are two separate lanes. Use your personal task to fill the Agent Contract and transfer exercise. Use the fictional meeting fixture during Modules 1–5 so everyone can run the same checker.

## Workshop schedule

| Time | Minutes | Work | Evidence |
|---|---:|---|---|
| 8:00–8:20 | 20 | Welcome, setup, demo, choose a job | Working file access; task selected |
| 8:20–8:55 | 35 | [1: First agent](modules/01-first-agent/README.md) | Output checked; boundary attempt recorded |
| 8:55–9:13 | 18 | [2: Memory](modules/02-memory/README.md) | Fresh session reads saved fact |
| 9:13–9:23 | 10 | Break 1 | Full ten minutes |
| 9:23–10:03 | 40 | [3: Skills + tools](modules/03-skills/README.md) | Role lookup; unknown and conflict handled; injection debrief |
| 10:03–10:33 | 30 | [4: Loops](modules/04-loops/README.md) | Success stops; impossible input escalates |
| 10:33–10:43 | 10 | Break 2 | Full ten minutes |
| 10:43–11:08 | 25 | [5: Team](modules/05-team/README.md) | Workers finish, reviewer checks, lead resolves |
| 11:08–11:30 | 22 | Failure challenge, personal transfer, questions | New-task plan survives a partner challenge |

Exercises include time to work, check your result, and discuss it with a partner.

## Find your files

[Agent Contract](templates/AGENT_CONTRACT.md) · [Universal browser/manual lane](cheatsheets/universal.md) · [Troubleshooting](docs/TROUBLESHOOTING.md) · [Injection demo](injection-demo/README.md).

`data/` contains fictional input. `examples/` contains clearly marked answer keys and a worked skill. `output/` is ignored by git so workshop results stay local unless you deliberately publish them. Keep real personal, customer, and secret data out of your public fork.

Questions: [open an issue](https://github.com/heathriel/first-agent-workshop/issues) or contact [@heathriel](https://twitter.com/heathriel).

## What you should be able to do afterward

Choose between a script and an agent; define a useful outcome; observe a tool call; distinguish a role from a commitment; preserve uncertainty and conflicting evidence; enforce retry limits outside the model; and test whether a passing artifact actually serves the user. Practice with the [checker trap](modules/01-first-agent/CHECKER_TRAP.md), [tool-choice lab](modules/03-skills/DECISION_LAB.md), and [personal transfer test](templates/TRANSFER_TEST.md).

The meeting extraction is deliberately a simple baseline. The optional `live_loop.py` is a bounded drafting loop with tools disabled, not a demonstration of autonomous tool selection. Tool selection is observed in Module 3 through your live assistant or clearly labeled manual simulation.
