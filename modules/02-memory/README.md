# Module 2: Make the next session recover the right context

**18 minutes: 6 introduction, 10 exercise, 2 debrief.**

1. Copy [AGENTS.md.template](AGENTS.md.template) to root `AGENTS.md`. Keep project-specific instructions short.
2. For Claude Code, create root `CLAUDE.md` containing two lines: `@AGENTS.md` and `@memory.md`. Claude's native instruction file is CLAUDE.md; AGENTS.md is explicitly imported. For another tool use its documented instruction file, or explicitly ask it to read both files.
3. Create root `memory.md` with: `Preference: show unknown owners explicitly.` and `Fact: the workshop project is called Lantern.` Use fictional facts, not secrets.
4. End the session. Start a new session in the same folder, without resuming the old conversation.
5. Ask: `What is this project called, and how should you represent an unassigned owner? Name the files you read.` Check the actual files and read trace where available. Then rerun the summary.
6. Change Lantern to Harbor in memory.md. Start another fresh session if time permits and confirm the correction replaces the stale fact.

**Success:** Harbor/Lantern, as currently saved, and UNKNOWN are recovered from files. A guessed correct answer does not demonstrate memory loading. Save the observations in output/memory-test.txt.

The 2026 AGENTS.md study found no general success improvement and over 20% greater average inference cost in its evaluated coding tasks. It did not establish that all instruction files are harmful or that brevity alone improves quality. Test your actual workflow. [Study](https://arxiv.org/abs/2602.11988) · [Claude memory docs](https://code.claude.com/docs/en/memory).

## Copy/paste setup commands

Run these from the folder containing `workshop.py`.

macOS/Linux:

```sh
cp modules/02-memory/AGENTS.md.template AGENTS.md
printf '@AGENTS.md\n@memory.md\n' > CLAUDE.md
printf 'Preference: show unknown owners explicitly.\nFact: the workshop project is called Lantern.\n' > memory.md
```

Windows PowerShell:

```powershell
Copy-Item modules/02-memory/AGENTS.md.template AGENTS.md
"@AGENTS.md`n@memory.md" | Set-Content CLAUDE.md
"Preference: show unknown owners explicitly.`nFact: the workshop project is called Lantern." | Set-Content memory.md
```

Open `memory.md` in any text editor to change Lantern to Harbor. These commands overwrite root `CLAUDE.md` and `memory.md`; use the fictional workshop copy, not an existing project with files you need to preserve.
