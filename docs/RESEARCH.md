# Research and documentation review · 2026-09-07

This is a focused review of evidence that changes a beginner workshop, not an exhaustive literature review. Distinguish research findings, vendor documentation, recent operational disclosures, and Heather's personal experience. Avoid a model leaderboard: participants need a workflow they can evaluate after models change.

| Evidence | What the workshop teaches | Limit |
|---|---|---|
| [Gloaguen et al., Evaluating AGENTS.md](https://arxiv.org/abs/2602.11988), 2026 | Unnecessary repository instructions can add work and cost; retain non-obvious constraints and test their value. | Evaluated coding-task settings, not a universal law of memory. Current abstract reports no general success improvement and over 20% greater average inference cost. Remove the blanket “−3% success” claim. |
| [Pan et al., Measuring Agents in Production](https://arxiv.org/abs/2512.04123), v4 June 4, 2026; accepted ICML 2026 oral | Small, controlled workflows are legitimate production patterns. | Study reports 20 case studies and 86 deployed-system respondents; 68% execute at most 10 steps before human intervention. Observational, self-reported sample, not a causal experiment or census. |
| [Kim et al., Towards a Science of Scaling Agent Systems](https://arxiv.org/abs/2512.08296), Dec 2025; [Google Research explanation](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/), Jan 28, 2026 | Compare teams with a single-agent baseline; decomposition and verification matter. | Controlled study across 180 configurations and four benchmarks. Parallelizable tasks can benefit; sequential tasks can suffer. A separate reviewer is not statistically independent merely because its prompt differs. |
| [Anthropic, Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), Jan 9, 2026 | Check outcomes and traces, use multiple trials, combine code and human review. | Engineering guidance, not peer-reviewed proof. The workshop's exact JSON fixture grader is intentionally narrow and does not certify general quality or safety. |
| [Anthropic, Improving alignment and security practices](https://www.anthropic.com/news/improving-alignment-security-efforts), Aug 31, 2026 | Explicit scope needs enforced isolation and monitoring that can stop execution. | Vendor disclosure about evaluation/training environments. Do not imply that these conditions describe every released customer model. |
| [Anthropic, Enterprise Frontier Safeguards](https://www.anthropic.com/news/enterprise-frontier-safeguards), Sep 1, 2026 | Ask who owns logs, reviews alerts, and controls data access. | Product announcement, not independent evidence of effectiveness; enterprise rollout is outside this workshop. |
| [OWASP Agentic Top 10 for 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | Treat retrieved material as untrusted and constrain capabilities. | Risk taxonomy, not a measured ranking of incident frequency. |

## Tool facts corrected

[Claude memory](https://code.claude.com/docs/en/memory): native CLAUDE.md can import AGENTS.md. Do not promise automatic AGENTS.md loading in every harness. [Gemini CLI](https://geminicli.com/docs/cli/gemini-md/) uses GEMINI.md; [OpenCode](https://opencode.ai/docs/rules/) documents AGENTS.md.

[Agent Skills specification](https://agentskills.io/specification): SKILL.md has name and description metadata; discovery paths and invocation depend on the host. [Claude skills](https://code.claude.com/docs/en/skills) documents .claude/skills/. The 'never' rule is our teaching convention, not a required standard field.

[Claude scheduling](https://code.claude.com/docs/en/scheduled-tasks): /loop is session scheduling, not a hard retry controller. [Desktop scheduling](https://code.claude.com/docs/en/desktop-scheduled-tasks) and [cloud routines](https://code.claude.com/docs/en/routines) have different runtime requirements. [CLI reference](https://code.claude.com/docs/en/cli-reference) documents the live runner's flags; it checks their presence before execution.

[MCP setup](https://code.claude.com/docs/en/mcp) is host-specific. A local Read tool is not MCP. [MCP security guidance](https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices) reinforces that protocol support is not trust.

[Copilot plans](https://github.com/features/copilot/plans): do not promise a free cloud-agent seat. Entitlement, usage allowances, repository settings, and organization policy can vary. Forking does not copy issues.

## Claims removed or qualified

Removed unattributed '60 billion tokens' quote, universal lab/tool-support counts, 'fastest-growing failure class', unverified summer caps, unsupported product anecdotes, and the untraced ClawHavoc count. These may be researchable individually but are not necessary to teach the workflow. Replaced 'reads are safe' with scoped access and untrusted-input handling. Replaced automatic always-on promises with a verified next-run plan. A2A/version chatter and speculative orchestration vocabulary were moved out of the core teaching to preserve exercise time.

The $20.50 budget, 4,096-token cap, mailbox, and meeting-summary stories are Heather's supplied anecdotes, not independently verified research. Preserve them as personal observations with bounded conclusions.
