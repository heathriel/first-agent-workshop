# Facilitator runbook

The repository provides a slides-only PDF. The presenter keeps the PowerPoint and full speaker notes separately. Core timing is 210 minutes with full ten-minute breaks at 9:10 and 10:30 for an 8:00 start. A late start shifts every time equally.

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

## Teach the decision, not just the vocabulary

At slide 10, run the five-minute checker trap. Ask for an actual two-sentence launch answer and a missing acceptance criterion. Do not accept “check your work” as the lesson.

At slide 17, keep 15 minutes for skill writing and 10 for DECISION_LAB.md. Require a prediction before the run. F2 and F4 justify a directory read; F1 does not need one; P2 does not assign F3. Inspect a real read result. Missing/conflicting evidence belongs in an escalation, not another creative retry.

At slide 26, spend five minutes on a changed-input challenge: pairs choose F2 or F4, remove or contradict the role mapping on paper, predict the required behavior, and identify which fixed checker expectation must change. Do not claim the fixture grader evaluates arbitrary input. Discuss why changing a test to reflect a changed contract differs from weakening it to make a bad answer pass.

At slide 27, use TRANSFER_TEST.md: five minutes design, two partner challenge. Require a specific input, useful output, permission, passing case, plausible failure and stop question. Choosing a script is allowed. At closing ask to see the revised plan, not whether everyone enjoyed the session.

If time slips, cut anecdotes and share-outs. Protect the decision lab, changed-input challenge, transfer test, and both breaks. Research remains in notes and RESEARCH.md rather than occupying the final practice slot.
