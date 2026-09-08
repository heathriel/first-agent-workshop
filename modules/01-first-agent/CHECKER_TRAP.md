# A green check can answer the wrong question

Five-minute pair exercise, after the first lab.

1. Run `python3 workshop.py check examples/summary.good.json`. It passes. (1 minute.)
2. Your user actually asked: **Can we launch today, and what prevents us from deciding?** Give your partner only that passing JSON. Can they act on it? What is still unresolved? (1 minute.)
3. Write a two-sentence answer with source references, then one acceptance criterion that would reject a misleading launch recommendation. Do not change the source or call UNKNOWN an assigned action. (2 minutes.)
4. Compare: no launch approval is supported; L4 defers the decision until testing completes, and L3 has an unassigned accessibility review. The transcript does not establish whether that review is a formal launch gate. Ask the decision owner what gates apply and for testing evidence. (1 minute.)

The JSON grader checks extraction for a fixed fixture. It cannot certify that a user can make a launch decision. A source-faithful action list can be an input to the job without completing the job. Keep both artifact checks and a user-outcome check. Do not hard-code this answer as a universal launch policy.
