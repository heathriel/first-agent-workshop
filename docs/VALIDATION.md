# Validation record · September 7, 2026

- Eight automated tests pass. They cover valid/invalid fixture data, missing and duplicate actions, invented values, wrong types, reordered actions, malformed files, retry success/exhaustion, CLI errors, and timeouts. Live-controller subprocess responses are mocked; these tests do not contact a provider.
- Preflight and both fixture checks return the documented exit codes.
- Scripted rehearsal stops after two attempts on success; the impossible variant escalates after three with exit code 2. Traces inspected.
- Relative documentation links checked.
- All 29 slides rendered and visually reviewed; source-template fidelity check passes. Notes contain the complete talk track and facilitation cues. Timing totals 210 minutes, including two 10-minute breaks.

## Not verified live in this environment

Claude CLI is not installed or authenticated here. No paid model request, account-specific connector authorization, native skill discovery, fresh-session host loading, Copilot cloud assignment, or durable scheduled firing was executed. These remain facilitator preflight checks on the actual presentation laptop. The workshop contains manual and scripted fallbacks so an account problem need not block teaching.

This is a teaching fixture, not a production sandbox. The grader and answer keys are visible in the repository. A real deployment needs a protected evaluation environment and task-specific quality checks beyond exact JSON matching.

## Teaching-strength revision
Nine unit tests pass, including wrong role resolution, invented specialist commitment, suppressed conflict, missing citation, changed date, missing row and duplicate request cases. Module 3 now uses followups.txt plus project-context.txt; the original meeting fixture and optional tool-disabled live loop remain separate. Native tool decisions require observing a real assistant in class; automated fixture checks do not establish tool use. No paid live model call was made during this revision.

The deck retains 29 slides and 210 minutes, including two ten-minute breaks. The checker-trap, changed-input challenge and personal transfer test replace prior debrief/recap content.
