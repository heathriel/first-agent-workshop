# Module 3 — Skills + Tools

## Part A: your first skill (the laminated procedure card)
A **skill** is a procedure your agent can be handed: a folder with a `SKILL.md` —
plain Markdown with a small header. It's an open standard (agentskills.io) read by
~40 tools including Claude Code, Codex, Cursor, and Copilot.

**A skill is not done until it contains one "never" born from a real mistake.**
Mine have rules like "never introduce a name that isn't in the transcript" —
because exactly one hallucinated name in a meeting summary cost me exactly one
pile of trust. Yours will too. Pre-pay for that lesson here.

### Exercise A
1. Copy [`SKILL.md.template`](SKILL.md.template) into a folder named for your
   procedure (e.g. `my-standup-summary/SKILL.md`) in your agent's skills location.
2. Fill in: when to use it, the steps, the output format, and **one guard rule**.
3. ✅ Check: invoke it. Output matches YOUR format, and the guard holds when you
   try to trip it.

## Part B: one real connector (MCP — "USB-C for agents")
Pick ONE from the menu (via Settings → Extensions/Connectors in Claude Code, or
your tool's MCP config): Gmail · Google Calendar · Google Drive · Slack · Notion ·
GitHub · Zapier MCP (reaches 7,000+ apps).

- Reads are safe; writes should ask first. Start read-only.
- ✅ Check: your agent tells you something TRUE from your actual data, formatted
  by your skill from Part A.

## One warning before you go skill shopping
There are skill marketplaces now, and this year's cautionary tale is the
"ClawHavoc" campaign: ~1,184 malicious skills published to an open marketplace.
A skill is code-adjacent: **read a skill before you install it**, prefer sources
you trust, and remember agent security is a supply-chain problem first and a
prompt-injection problem second. (You write your own skills today — that's the
safest marketplace there is.)

## Then report to the front for the 🏴‍☠️ demo.
