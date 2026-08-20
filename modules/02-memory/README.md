# Module 2 — Memory + the Agent-Ready Repo

Your agent is brilliant and amnesiac. Every session starts from zero — unless you
write things down where it looks. Two files fix this:

- **AGENTS.md** — the employee handbook. Read natively by 20+ tools (Claude Code
  also reads CLAUDE.md). What this project is, what to never touch, how to prove work.
- **A memory file** — facts and preferences the agent maintains itself.

## Exercise
1. Copy [`AGENTS.md.template`](AGENTS.md.template) into the root of YOUR fork,
   fill it in for your excavated task.
2. Tell your agent one preference ("I like summaries as three bullets, spiciest
   first") and one fact ("my boss's name is ___") and ask it to remember them.
3. **Kill the session. Start a fresh one.**
4. ✅ Check: ask it to do the task — it follows the handbook AND your preference,
   without being retold.

## The rule that keeps this working
Memory is a diet, not a warehouse. One fact per line. If the file gets long, the
agent starts forgetting the important parts — I know because mine did (ask me about
the lobotomy story).

And it's not just me: research (ETH Zurich, 2026) found that BLOATED agent-config
files can make agents *worse* — lower success, ~20% higher cost. The current best
practice: keep AGENTS.md small, and put ONLY things the agent can't discover by
reading the repo itself (your rules, your preferences, your "nevers") — never a
dump of what the code already says. Write the handbook a good new hire would
actually read.
