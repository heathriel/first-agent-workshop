# Exercise: strengthen a bounded summary workflow

Create this issue in your fork. Agent assignment requires eligible access and repository policy; if unavailable, paste the task into your existing assistant.

Improve the workshop's summary validation without changing the expected fixture facts. Add a test that rejects an unsupported owner and a test that permits reordered actions. Do not loosen existing assertions to make a test pass. Keep the checker and source reviewable.

Acceptance:
- Existing tests pass: `python3 -m unittest discover -s tests -v`.
- Unsupported owner fails; reordered valid actions pass.
- PR description includes actual commands and results, or says they could not run.
- No secrets, real personal data, external integrations, or dependency additions.
- A human reviews the diff and test results before merge.

Note: the refreshed starter already includes these baseline tests. Ask the agent to inspect them, then add an additional missing or malformed input case with a clear justification. An empty PR is not required if it determines no change is useful; it should report that finding.
