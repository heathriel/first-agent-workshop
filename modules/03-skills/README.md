# Module 3: A reusable procedure and a bounded tool

**40 minutes: 5 teaching, 25 exercise, 10 injection demo/debrief.**

## A. Write and invoke a skill (15 minutes)

Use [SKILL.md.template](SKILL.md.template). For Claude Code, save the completed file at `.claude/skills/kcdc-meeting-summary/SKILL.md`. The folder and YAML name must agree; name is `kcdc-meeting-summary`, description says when to use it. A finished example is at [examples/meeting-summary/SKILL.md](../../examples/meeting-summary/SKILL.md).

For the guided lane, start from the template rather than creating nested folders by hand.

macOS/Linux:

```sh
mkdir -p .claude/skills/kcdc-meeting-summary
cp modules/03-skills/SKILL.md.template .claude/skills/kcdc-meeting-summary/SKILL.md
```

Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force .claude/skills/kcdc-meeting-summary
Copy-Item modules/03-skills/SKILL.md.template .claude/skills/kcdc-meeting-summary/SKILL.md
```

Open that file in any text editor and replace the bracketed prompts. If starting from a blank template consumes the exercise time, copy [the finished example](../../examples/meeting-summary/SKILL.md), inspect it, and make one deliberate improvement. Fast finishers can build from the blank template.

Invoke `/kcdc-meeting-summary` with data/meeting.txt, or explicitly ask your assistant to read your completed skill and apply it. If the directory is new and it is not discovered, restart the session. Compare the output with the source, including the unknown owner and date. Run the fixture check if you used its exact JSON format.

## B. Make a justified tool choice (10 minutes)

Do [the decision lab](DECISION_LAB.md). Extend the skill to a second input: resolve a role, preserve an unknown, and expose conflicting sources. Inspect the actual file-read result. A local file tool is not MCP; configuring an approved MCP connector is optional homework, outside the core session.

## C. Injection demo (10 minutes)

Follow [the demo guide](../../injection-demo/README.md) using fictional data only. Refusal and compromise are both valid observed outcomes. No external accounts are needed.

**Success:** saved skill, observed tool read, four justified follow-up decisions, and an honest record of the injection result. Do not count the local-file fallback as an MCP setup success.

## Skill discovery

Use the distinctive project name `kcdc-meeting-summary` to avoid a collision with personal skills. In Claude Code, a personal skill takes precedence over a project skill with the same name. Inspect the loaded file. If discovery is unclear, ask the assistant to read `.claude/skills/kcdc-meeting-summary/SKILL.md` explicitly and apply it. Restart after first creating the skills directory.

Review YAML frontmatter as well as instructions and scripts. In Claude Code, `allowed-tools` grants use without normal approval; it is not a sandbox. Permission behavior depends on your runtime and settings. [Official skills reference](https://code.claude.com/docs/en/skills).
