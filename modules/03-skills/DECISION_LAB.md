# Choose a tool for a reason

Work for 10 minutes; the preceding skill-writing segment is 15 minutes. Use a native file tool, or ask a partner to hand you only the requested file in the manual lane. MCP configuration is optional homework.

**User need:** prepare an accurate follow-up list for a human. Resolve explicit role references when evidence permits. Do not turn somebody's job title into a promise, and do not send messages.

First extend your skill with a follow-up mode using the output contract below; keep its meeting-summary mode for Modules 4 and 5. This is a deliberate procedure change, not a silent change of schema.

Give your assistant `data/followups.txt` and tell it that `data/project-context.txt` is available through its read tool if needed. Do not paste the directory up front. Ask it to identify which requests require a lookup, use the tool, then save `output/followups.json`. Record the actual read result in `output/tool-evidence.txt`; a claim of reading is insufficient. One read can serve both relevant requests.

Output: a JSON array of four objects with exactly `request`, `owner`, `due`, `status`, `evidence`. All fields are strings except evidence, an array of source IDs. Status is `READY`, `NEEDS_OWNER`, or `CONFLICT`. Preserve explicit dates; UNKNOWN means no supported value. Evidence must include the request and any directory lines used. A conflicting owner stays UNKNOWN until a human resolves it.

1. Predict which of F1–F4 need the directory before running (2 minutes).
2. Run the skill with this new input and inspect the tool result (4 minutes).
3. Run `python3 workshop.py followups output/followups.json` and inspect source citations yourself (2 minutes).
4. Partner challenge: why isn't Alex the owner of F3? What must the human clarify for F4? Save the question and your answer (2 minutes).

**Pass criteria:** F1 uses its explicit owner without needing a lookup. F2 resolves the role to Priya. F3 stays unassigned despite Alex's specialty. F4 exposes the Luis/Priya conflict and asks which record is authoritative; no release approval is sent. The checker scores this fixed fixture, not arbitrary follow-up quality or actual tool behavior.

**Recovery:** inspect `examples/followups.good.json` only after your attempt. Without an agent, a partner plays the runtime and logs the requested read. Label that result MANUAL. Fast finishers remove P1 in a temporary copy and explain why F2 must now escalate; the fixed fixture checker is not for that altered input.
