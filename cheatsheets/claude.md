# Claude Code: guided lane

Documentation checked 2026-09-07. Authenticate before class; account eligibility and organization policy vary.

Open the repository folder in Claude Code. Run the hello-file preflight. Module 1 uses a normal prompt and your local file tools. Keep normal permission prompts enabled.

Module 2: root CLAUDE.md contains `@AGENTS.md` and `@memory.md`. Use `/context` to inspect loaded memory where supported; inspect the source files as well. Start a genuinely new session for the memory test.

Module 3: `.claude/skills/kcdc-meeting-summary/SKILL.md`; invoke `/kcdc-meeting-summary`. `/mcp` inspects configured connectors. The core exercise uses the local file-reading tool; MCP is optional.

Module 4: use the human-controlled three-attempt loop or `python3 live_loop.py`. `/loop` is scheduling, not the controller used here. CLI version support is checked by the live runner. Do not bypass permission prompts to rescue a demo.

Module 5: two workers first, reviewer after both, lead last. Sequential separate sessions are always the fallback.

[Setup](https://code.claude.com/docs/en/setup) · [Memory](https://code.claude.com/docs/en/memory) · [Skills](https://code.claude.com/docs/en/skills) · [MCP](https://code.claude.com/docs/en/mcp) · [CLI](https://code.claude.com/docs/en/cli-reference).
