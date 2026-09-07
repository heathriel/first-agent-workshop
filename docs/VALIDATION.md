# Validation record · September 7, 2026

- Eight automated tests pass. They cover valid/invalid fixture data, missing and duplicate actions, invented values, wrong types, reordered actions, malformed files, retry success/exhaustion, CLI errors, and timeouts. Live-controller subprocess responses are mocked; these tests do not contact a provider.
- Preflight and both fixture checks return the documented exit codes.
- Scripted rehearsal stops after two attempts on success; the impossible variant escalates after three with exit code 2. Traces inspected.
- Relative documentation links checked.
- All 29 slides rendered and visually reviewed; source-template fidelity check passes. Notes contain the complete talk track and facilitation cues. Timing totals 210 minutes, including two 10-minute breaks.

## Not verified live in this environment

Claude CLI is not installed or authenticated here. No paid model request, account-specific connector authorization, native skill discovery, fresh-session host loading, Copilot cloud assignment, or durable scheduled firing was executed. These remain facilitator preflight checks on the actual presentation laptop. The workshop contains manual and scripted fallbacks so an account problem need not block teaching.

This is a teaching fixture, not a production sandbox. The grader and answer keys are visible in the repository. A real deployment needs a protected evaluation environment and task-specific quality checks beyond exact JSON matching.
