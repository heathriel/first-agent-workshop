# Facilitator runbook

The deck speaker notes contain the spoken script, exercise launch, time checks, likely questions, and transitions. Core timing is 210 minutes with full ten-minute breaks at 9:10 and 10:30 for an 8:00 start. A late start shifts every time equally.

## Rehearse the day before

Run `python3 workshop.py preflight`, both fixture checks, both rehearsal modes, and `python3 -m unittest discover -s tests -v`. Negative checks intentionally return nonzero. Then perform Module 1 in your signed-in live tool, a fresh-session memory test, skill invocation, and the optional live runner. The included automated tests do not certify third-party authentication, native skill discovery, model behavior, or a real scheduler.

Show the source transcript, actual result, checker, and a failure trace in the opening demo. You may show your production example instead if it is prepared and sanitized, but do not imply the included replay is that production agent. Keep the local replay ready if service access fails.

The public repository includes answer keys. They are for teaching and recovery, not secure hidden evals. A production grader belongs outside the agent's writable environment. Do not ask participants to disconnect a required corporate VPN or disable permission safeguards.

## Keep the room moving

Pair anyone blocked after five minutes. Let fast finishers help neighbors. Stop optional connector configuration at five minutes. Use the fictional transcript for anyone without a checkable task. During exercises announce halfway and two-minute warnings, then ask to see evidence rather than a raised hand claiming success.

If running ten minutes late, take five minutes from glossary/research discussion and five from final share-outs. Preserve both breaks, failure testing, and a saved next-run plan. Park account-specific troubleshooting until optional help time.

## Exit evidence

Each participant should have: job description and contract; checked output; boundary observation; loaded memory observation; completed skill; read/source evidence; success and escalation traces; worker/reviewer synthesis; named owner and next run. Manual-lane participants label manual checks. Scheduling remains optional and must be observed before being called durable.

Personal stories in the deck come from Heather's supplied slides. Keep them in her voice and do not present them as research findings. Date-sensitive claims use linked primary sources in the notes and RESEARCH.md.
