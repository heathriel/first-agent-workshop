# Build Your First Agent Workflow — KCDC 2026

**Heather Wilde · Half-day workshop · Wednesday, September 9, 2026 · 8:00am–12:00pm · Room 2215-A**

You're going to leave this room with a working autonomous agent — not a demo, not a
slide. Something that's still running when you get home.

## Before the workshop (do this at home — conference wifi is for agents, not installers)

1. **GitHub account** (free): [github.com/signup](https://github.com/signup)
2. **Claude account, Pro plan** ($20/mo): [claude.com](https://claude.com) — the guided rail
3. **Install Claude Code** (desktop app or CLI): [claude.com/claude-code](https://claude.com/claude-code) — launch it once and **sign in**
4. **Install Git** (2.23+): [git-scm.com/downloads](https://git-scm.com/downloads)
5. **Fork this repo** (button, top right), then clone your fork.

### The pre-flight check (5 minutes, the night before)
1. Open Claude Code, signed in.
2. Type: *"Create a file called hello.md that says hi, then read it back to me."*
3. It does it? **You're ready.** It doesn't? Contact me before Wednesday (see below).
4. Log in to github.com in your browser. Done.

**Corporate laptop?** You must be able to reach `claude.ai`, `api.anthropic.com`, and
`github.com`. Test the pre-flight ON the network setup you'll actually use; if your
VPN loses, plan to disconnect from it. No admin access needed on macOS/Linux;
Windows installers may show an admin prompt.

### Agent of choice
I teach from **Claude Code**, and if you've never built an agent, take that rail.
But this workshop teaches open standards — AGENTS.md, Agent Skills, MCP — so if you
already live in **Codex CLI, OpenCode, Gemini CLI, Cursor, DeepSeek Harness,** or
**Grok Build**, bring it: every template here is plain Markdown and will work. The
alternate lane is self-supported — see [cheatsheets/](cheatsheets/).

### Optional homework (highly recommended)
Before Wednesday, notice **one task you did at least twice last month that followed
the same steps both times**. Bring it. That's your agent's first job.

## What we build, hour by hour

| Module | You build | The check |
|---|---|---|
| 1. First agent | A goal + a boundary (a job description) | Does the task AND refuses the out-of-bounds ask |
| 2. Memory | An AGENTS.md + a memory file | New session still knows what you taught it |
| 3. Skills + tools | A SKILL.md + one real connector | Reads something true from YOUR data, your way |
| 4. Loops | A completion check + an agent that runs until it passes | The loop STOPS by itself — and escalates on failure |
| 5. Team | A fan-out: two workers + one adversary | Synthesis survives the adversary's objection |

Everything feeds the [Agent Contract worksheet](templates/AGENT_CONTRACT.md) — the
one-pager you take home.

## Repo map
- [`templates/`](templates/) — fill-in-the-blank starting points for every module
- [`modules/`](modules/) — per-module instructions and exercises
- [`cheatsheets/`](cheatsheets/) — alternate-tool lanes (Codex, OpenCode, Copilot, Zapier, …)
- [`injection-demo/`](injection-demo/) — a perfectly innocent document 🏴‍☠️

## Questions before the conference?
- **Best: [file an issue on this repo](https://github.com/heathriel/first-agent-workshop/issues)** —
  setup questions get answered once, where every other attendee can see the fix.
  (Filing an issue is also secretly your first rep with the tools we'll use all
  morning. You're welcome.)
- Quick ping: [@heathriel on X/Twitter](https://twitter.com/heathriel)

See you at 8am. Bring coffee. I'm serious about the coffee.
