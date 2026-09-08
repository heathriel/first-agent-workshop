# Common setup and JSON problems

Use this page for five minutes, then pair or switch to the [browser/manual lane](../cheatsheets/universal.md). Setup debugging is not the learning objective.

## Python cannot open workshop.py

You are in the wrong folder. Open a terminal in the downloaded `first-agent-workshop` folder, the one that visibly contains `workshop.py`, and retry:

```sh
python3 workshop.py preflight
```

On Windows use `py -3 workshop.py preflight`.

## `python3` is not found

- Windows: try `py -3` in every command instead.
- macOS/Linux: use a paired laptop or the manual lane if Python cannot be installed within five minutes.
- Do not install `pytest` or any Python packages. The workshop has no package dependencies.

## The expected failure looks alarming

`check examples/summary.bad.json` is supposed to print FAIL and exit 1. `rehearse --impossible` is supposed to print ESCALATED and exit 2. Some terminals and IDEs display any nonzero result in red. That is evidence for the exercise, not an installation failure.

## The checker cannot find output/summary.json

Confirm the filename and folder. It must be exactly:

```text
first-agent-workshop/output/summary.json
```

Common mistakes are `summary.json.txt`, saving beside the repository, or creating an `output` folder inside a module. Ask your agent or editor to show the full path.

## The JSON is invalid

The file must contain JSON only. Remove Markdown fences, commentary before or after the object, smart quotes, and trailing commas. Run:

```sh
python3 -m json.tool output/summary.json
```

On Windows use `py -3 -m json.tool output/summary.json`. This checks syntax, not whether the facts are correct.

## The checker says the keys or fields are wrong

For the Module 1 fixture, the root has exactly `actions` and `decision`. Each of the three actions has exactly `task`, `owner`, `due`, and `evidence`, all strings. Do not add an explanation field. Compare the output to `data/meeting.txt` before looking at the answer key.

## The assistant cannot create files

Check that it was opened in the downloaded repository folder and that file access was approved. If the tool has no local file capability, copy its response into a plain-text editor yourself and label the check manual. If that still blocks you, use the browser/manual lane.

## Claude or another assistant is unavailable

The Python rehearsal does not require an assistant or make model calls. Complete it, then pair with a working participant or use the manual lane. Do not spend core workshop time creating API keys, changing corporate security settings, or debugging billing.

## Git is unavailable

Git is not required for the core exercises. Download the repository ZIP from GitHub, extract it, and work in that folder. You only need a fork and Git if you want to save your changes back to GitHub.
