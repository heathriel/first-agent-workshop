# Module 3: A reusable procedure and a bounded tool

**40 minutes: 5 teaching, 25 exercise, 10 injection demo/debrief.**

## A. Write and invoke a skill (15 minutes)

Use [SKILL.md.template](SKILL.md.template). For Claude Code, save the completed file at `.claude/skills/meeting-summary/SKILL.md`. The folder and YAML name must agree; name is `meeting-summary`, description says when to use it. A finished example is at [examples/meeting-summary/SKILL.md](../../examples/meeting-summary/SKILL.md).

Invoke `/meeting-summary` with data/meeting.txt, or explicitly ask your assistant to read your completed skill and apply it. If the directory is new and it is not discovered, restart the session. Compare the output with the source, including the unknown owner and date. Run the fixture check if you used its exact JSON format.

## B. Read through one tool (10 minutes)

**Required path:** have the agent use its file-reading tool on data/meeting.txt and cite L1–L4. This is a genuine tool call, but it is **not MCP**. Inspect the read result, not just the assistant's claim that it read the file.

**Optional MCP path, only if already available:** use an approved connector you configured before class. In Claude Code, `/mcp` shows configured servers and authentication; `claude mcp list` lists server configuration. Follow [official MCP setup](https://code.claude.com/docs/en/mcp). Select a single non-sensitive record and expose only the necessary read tools/scopes. Apply the skill to that record and verify the answer against it. Do not spend the workshop installing an unknown server or obtaining organization approval. Stop setup after five minutes and use the file path.

MCP standardizes communication with tools and resources. It does not make servers trustworthy. Reads can expose private data or bring in malicious instructions; read-only access reduces mutation risk but is not risk-free. A prompt saying 'ask before writes' is weaker than withholding the write capability.

## C. Injection demo (10 minutes)

Follow [the demo guide](../../injection-demo/README.md) using fictional data only. Refusal and compromise are both valid observed outcomes. No external accounts are needed.

**Success:** saved skill, observed tool read, source-grounded output, and an honest record of the injection result. Do not count the local-file fallback as an MCP setup success.
