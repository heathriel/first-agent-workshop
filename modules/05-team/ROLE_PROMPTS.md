# Four-chat team exercise

These are roles, not special product features. Open four ordinary chats. Use `examples/summary.bad.json` as the proposed summary and `data/meeting.txt` as the source. Do not use real or sensitive data.

## Chat 1: Worker A

> You are Worker A. Check the proposed summary against the original transcript for completeness and omissions only. Cite exact source line IDs. Do not edit files, delegate, or assume another worker's result. Limit: five minutes and 250 words. Return a review I can save as output/worker-a.txt.

## Chat 2: Worker B

> You are Worker B. Check the proposed summary against the original transcript for unsupported owners, dates, decisions, and hidden uncertainty. Cite exact source line IDs. Do not edit files, delegate, or assume another worker's result. Limit: five minutes and 250 words. Return a review I can save as output/worker-b.txt.

Wait until both workers return before starting Chat 3.

## Chat 3: Reviewer

Paste the original transcript, proposed summary, Worker A output, and Worker B output, then use:

> You are the reviewer. Test the weakest claims and any disagreement in the two worker reports against the original source. Identify each substantive objection with exact source evidence, or say no substantive objection was found and list the tests you performed. Do not invent a flaw. Do not edit files or external records. Limit: 250 words. Return a review I can save as output/review.txt.

## Chat 4: Lead

Paste the original source and all three reviews, then use:

> You are the lead. Synthesize the two worker reports and reviewer result in no more than 300 words. Cite Worker A and Worker B, address every reviewer objection using source evidence, and state any remaining uncertainty or human decision. Compare the corrected result with the earlier single-agent result. Do not send or change anything externally. Return text I can save as output/synthesis.txt.

Finally, replace the unsupported Alex assignment with `UNKNOWN` and have a human rerun the unchanged fixture checker. Save all four outputs. A clean role prompt does not make the reviewers statistically independent.
