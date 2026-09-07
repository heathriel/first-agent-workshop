# Bounded team prompt

Act as lead. Review [DOCUMENT OR output/summary.json] against [SOURCE OR data/meeting.txt]. Do not change files or external records during review.

Phase 1: Run two workers, parallel only if supported. Worker A checks completeness and omissions. Worker B checks grounding, unsupported details, and uncertainty. Each cites exact source lines, has a 250-word limit and five-minute time box, and cannot spawn more agents. Use a lower-cost capable model for extraction if your tool supports model choice; use a stronger reviewer only when the difficulty warrants it.

Phase 2: AFTER BOTH RETURN, give their outputs AND the source to a separate reviewer. Test the weakest claims and missing cases. Report supported objections with evidence, or say no substantive objection found and list the tests performed. Do not invent an objection to satisfy a quota. Keep under 250 words.

Phase 3: Synthesize in 300 words. Cite Worker A and Worker B; resolve each reviewer objection with source evidence or identify the human decision still needed. Compare with the earlier single-agent result. Stop and report missing input if the source is unavailable.

Save or manually copy the four outputs to output/worker-a.txt, worker-b.txt, review.txt, synthesis.txt. A human runs the independent check. These are process checks, not a guarantee of accuracy.
