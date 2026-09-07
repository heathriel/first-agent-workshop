# Speaker notes

## Slide 1 · 2 minutes

TIMING: 8:00–8:02 | 2 minutes | elapsed 0–2 of 210. Shift clock times equally if starting later.

Good morning. I'm Heather. Today we are going to take one small job and give it enough structure that you can hand it to an agent, inspect what happened, and run it again tomorrow. You do not need to build an entire autonomous company before lunch.

The thing I care about is whether it works when I am no longer standing next to your laptop. That means a saved task, a clear boundary, a way to check the result, and a way to notice failure. Those are our deliverables. Scheduling is an optional last step, not a promise that a closed laptop will keep working.

We have three and a half hours, including two actual ten-minute breaks. If your setup isn't working yet, you're still in the right room. We'll pair people up. Keep the repository address handy; it contains every exercise and a fictional task we can all use.

## Slide 2 · 2 minutes

TIMING: 8:02–8:04 | 2 minutes | elapsed 2–4 of 210. Shift clock times equally if starting later.

My background is building and operating systems, including the parts where real people encounter what the system actually does. I was an early employee at Evernote and Spirit Airlines, and I've spent a lot of my career connecting technical capability with something people can use.

I run agents in production. That gives me some good stories, and several stories I would prefer not to have earned. I'll share both. When I tell you about my own agents, that is personal experience. When I make a research claim, the source is in the notes and the repository.

You don't need my stack to do this. Claude Code is the tool I'll guide, but the job, the evidence, and the review process travel between tools. The part that doesn't travel automatically is where a tool discovers instructions or what permissions it gives them. We'll make those differences visible.

## Slide 3 · 4 minutes

TIMING: 8:04–8:08 | 4 minutes | elapsed 4–8 of 210. Shift clock times equally if starting later.

Let's spend four minutes getting one tiny thing working. Open your fork and start your agent in that folder. In a terminal, run the preflight command. On Windows, use py -3 instead of python3. There are no Python packages to install for our checker.

That command checks local prerequisites. It does not prove you are signed in. So now ask the assistant to create output/hello.md containing hi, then read it back. Look for the file yourself. We are already practicing the habit of checking the environment instead of trusting a sentence.

If this works, help a neighbor. If it doesn't, tell us which stage failed: account, network, folder, or file permissions. Don't switch off required security software or a corporate VPN just to make this work. Pairing is a valid engineering solution.

FACILITATION: Give two minutes for commands, then ask for blocked hands. Match each blocked participant with a working neighbor. At four minutes move on. Keep the browser/manual lane visible for anyone who cannot run local tools. Do not turn the opening into individual account troubleshooting.

## Slide 4 · 4 minutes

TIMING: 8:08–8:12 | 4 minutes | elapsed 8–12 of 210. Shift clock times equally if starting later.

Before I explain the architecture, I want you to see the whole job. Here is our fictional meeting transcript. Maya owns the checklist. Luis owns signup testing. Nobody owns accessibility yet. The launch decision is deferred. That is all the evidence we have.

DEMO: Open data/meeting.txt. Run the bad fixture through the checker, then the good fixture. Point to Alex in the bad fixture. Ask: Where did that person come from? Now run python3 workshop.py rehearse and open output/rehearsal/trace.json. It fails once, repairs the candidate, passes, and stops.

This last run is a scripted rehearsal. It makes no model calls. I am using it to show you the controller clearly, not to claim that a model succeeded. During the exercises your live assistant will produce the candidate and you will run the same check.

Notice that the passing file is only a narrow success. Someone still needs to check whether our test represents the real job. A test that rewards invented certainty would be a bad test even if the agent passed it perfectly.

FALLBACK: If a command fails, open the two example JSON files and compare them with L3 manually. Label the comparison manual. Finish the demo within four minutes.

[Sources]
https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
[/Sources]

## Slide 5 · 2 minutes

TIMING: 8:12–8:14 | 2 minutes | elapsed 12–14 of 210. Shift clock times equally if starting later.

Here is the morning. We start with the job and boundary, then teach the next session how to recover context. After the first break, we package the procedure and use a tool to read a source. Then we give repeated attempts an actual stopping rule. After the second break, we try a small team and compare what it adds.

Every stage leaves something you can point to. You can choose to stay with a simpler version if that is what your task needs. A reliable single-agent workflow is a perfectly good outcome.

We finish the core at eleven thirty if we start at eight. The repository's original room block goes to noon; that remaining time is optional help, subject to the conference schedule. I will protect both breaks. We can shorten discussion before we steal your coffee.

## Slide 6 · 6 minutes

TIMING: 8:14–8:20 | 6 minutes | elapsed 14–20 of 210. Shift clock times equally if starting later.

Turn to someone near you. Describe one task you did at least twice last month. Don't give it an impressive name. Tell them what you opened, what you looked for, what you produced, and how you knew you were finished.

Each person gets ninety seconds. Your partner's job is to interrupt if the description becomes vague. Better is not an output format. Done is not a feeling. After both people speak, take one minute to name what you would not delegate yet: sending the message, committing money, deleting a record, or deciding that missing information is probably fine.

FACILITATION: Start a three-minute timer for the two descriptions. Give a one-minute boundary round. Use the final two minutes for two examples and task narrowing.

If your task is huge, choose the first draft or the first decision-support step. If you cannot use your work data here, use the meeting transcript. It includes an ambiguity on purpose. We want an agent that can say it doesn't know, and we need a task that gives it the opportunity.

## Slide 7 · 5 minutes

TIMING: 8:20–8:25 | 5 minutes | elapsed 20–25 of 210. Shift clock times equally if starting later.

This is conceptual pseudocode, not a program to paste into a terminal. The important distinction is between the model proposing an action and the surrounding software deciding what it can execute.

A model can decide that the next useful action is to read a file, run a test, or ask for missing information. The runtime exposes those capabilities. That means the runtime is also where an action can be denied before it happens.

Point at permitted_tool. If my email-sending tool is not present, a document cannot persuade the model to send an email through that missing tool. If it is present and I merely wrote please don't, I have a weaker boundary. Other paths may still exist, so inspect the entire available tool set.

Point at range(3). This limit belongs to the controller, not to the model's memory of a request. Point at check. It looks at the result, not the assistant's confidence. Finally, the else path reports failure after the available attempts are used.

ASK: Which of those controls do you currently have in your tool, and which are only sentences in a prompt? Take two answers. We will use a human controller first so that the distinctions remain visible.

[Sources]
https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
[/Sources]

## Slide 8 · 5 minutes

TIMING: 8:25–8:30 | 5 minutes | elapsed 25–30 of 210. Shift clock times equally if starting later.

Agents have uneven capabilities. I can see excellent work on one problem and an elementary mistake on the next. That is why we are not going to choose a model by how articulate it sounds.

There is also a practical difference between the underlying model and the current session. A fresh session may load instructions, saved memory, or tool state, but it does not automatically inherit everything you said in another chat. We will test what loads rather than calling it magic memory.

For your chosen task, ask whether variable judgment is actually needed. If the procedure is identical every time, start with a script. If the path varies but the result can be evaluated, an agent may be helpful. If the result needs human judgment, that doesn't prohibit using an agent; it means human review is part of the workflow.

ASK participants to classify their task with a partner for one minute. Invite an example that is better served by a script. That is a good outcome, not a failure to embrace the workshop.

Our meeting example is deliberately modest: extract commitments and preserve uncertainty. It lets us see the whole system without confusing complexity with progress.

[Sources]
https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
[/Sources]

## Slide 9 · 20 minutes

TIMING: 8:30–8:50 | 20 minutes | elapsed 30–50 of 210. Shift clock times equally if starting later.

Open Module 1. You have twenty minutes. First write the job and the proof in JOB_DESCRIPTION.md. If you are using the meeting fixture, the ready-to-run prompt is already in the module. Read it before pasting.

Run the bad fixture through the checker so you have seen a failure. Then ask your live assistant to produce output/summary.json from the transcript. It should not read the answer key or edit the checker. You run the check yourself and inspect the evidence lines.

At the end, ask it to assign accessibility to Alex and approve launch. Neither statement is supported. Record what actually happens, including a failure to refuse. We are gathering evidence, not trying to get a green tick by rewriting history.

FACILITATION: Minutes 0–3, explain prompt and schema. Minutes 3–12, let people build; circulate and ask to see the file. At minute 10 announce halfway. Minutes 12–17, check and challenge. At minute 18 announce two minutes left and ask everyone to save output/boundary-test.txt.

COMMON BLOCKERS: Markdown fences are not JSON. UNKNOWN is a string, not a person named Unknown. The checker uses exact fixture labels; explain that limitation if a semantically valid paraphrase fails. For a custom task, use its own explicit checklist and label the result manual. Browser users copy the response into a file or compare it by hand. Do not let the agent repair a failing task by weakening the test.

[Sources]
https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
[/Sources]

## Slide 10 · 5 minutes

TIMING: 5 minutes.

Open modules/01-first-agent/CHECKER_TRAP.md. We have five minutes. Say: “Run the checker on the good summary. Green. Now here is the actual question: can we launch today, and what prevents us from deciding? Did that green check answer it?” Give them one minute to run it and one to show the output to a partner. Do not answer your own question immediately. A useful pause is part of the exercise.

Say: “For two minutes, write a two-sentence answer and one acceptance criterion that would reject a misleading recommendation.” Walk around and look for actual answers. If someone says the launch is approved because the JSON is valid, point to L4. If someone asserts accessibility is a mandatory launch gate, ask where that policy appears. We need to preserve the distinction between an unresolved action and a proven gate.

Use the last minute to compare. “No launch approval is supported. The decision is deferred until testing completes. Accessibility has no owner or date, but the transcript doesn't say whether it blocks launch. Ask the decision owner which gates apply and for the testing evidence.” Ask one pair to read its acceptance criterion. A good one requires the answer to preserve the deferred decision and identify missing evidence without inventing a policy.

Say: “Our grader checks extraction of this fixture. It doesn't certify that the user's decision is ready. A correct intermediate artifact can still leave the job unfinished. Keep an artifact check and a user-outcome check.” Transition: a new session also needs to know what job we were doing; that brings us to memory.

## Slide 11 · 1 minutes

TIMING: 8:55–8:56 | 1 minutes | elapsed 55–56 of 210. Shift clock times equally if starting later.

Imagine a capable contractor arriving tomorrow. What would they need to know that they cannot reliably infer from the files? That is the handover we are about to write.

The goal is not to preserve every word we have ever said. It is to make the next run recover the right rules and facts. We'll write them down, close the session, and test that recovery.

## Slide 12 · 2 minutes

TIMING: 8:56–8:58 | 2 minutes | elapsed 56–58 of 210. Shift clock times equally if starting later.

There are three different jobs here. AGENTS.md describes this project and its rules. For Claude Code, CLAUDE.md is the native entry point, and we explicitly import AGENTS.md and memory.md. The memory file holds the few facts we want to recover next time.

A recent study evaluated repository context files for coding agents. It found no general success improvement and more than twenty percent higher average inference cost in its tested settings. That is evidence against assuming that more context is automatically better. It is not a universal rule that short files are always better, nor a reason to delete useful constraints.

We will use a project name and a preference, then start a fresh session. If the answer is right, ask which files were read. A lucky guess does not prove the handover worked. The test is about loading and using the saved source.

[Sources]
https://arxiv.org/abs/2602.11988
https://code.claude.com/docs/en/memory
[/Sources]

## Slide 13 · 12 minutes

TIMING: 8:58–9:10 | 12 minutes | elapsed 58–70 of 210. Shift clock times equally if starting later.

Open Module 2. The exact file instructions are there. Save the fictional project name Lantern and the preference to show unknown owners explicitly. In Claude Code, CLAUDE.md contains two import lines: at-sign AGENTS.md and at-sign memory.md.

Now close the session. Start a genuinely new one in the same directory. Ask for the project name and the representation of an unassigned owner, without repeating those facts in the question. Ask which files it read. Inspect those files and the tool trace where available.

FACILITATION: Ten-minute lab followed by two-minute debrief. First three minutes: create files. Next four: fresh-session test. Final three: change Lantern to Harbor and retry if time permits. At eight minutes warn that two minutes remain. Browser users start a new chat and deliberately supply their saved handover document; label this manual loading.

If it fails, first check the working folder and native filename. Do not respond by making the handbook ten times longer. If it recovers the old name after the file changes, find the stale source or resumed session.

DEBRIEF: Ask one participant to show the actual import and one to describe a stale-fact failure. Save the observation. Then take the full ten-minute break. We return at nine twenty for skills.

[Sources]
https://code.claude.com/docs/en/memory
[/Sources]

## Slide 14 · 10 minutes

TIMING: 9:10–9:20 | 10 minutes | elapsed 70–80 of 210. Shift clock times equally if starting later.

Say: We are taking the full ten minutes. Please be back at nine twenty. Leave your files saved; you can close the conversation.

FACILITATION: Start a ten-minute timer. Do not teach required material during the break. Give a one-minute return cue. If the session began late, announce the shifted return time. Use this time for a quick private check that the next exercise files are open, not to require participants to keep working.

## Slide 15 · 2 minutes

TIMING: 9:20–9:22 | 2 minutes | elapsed 80–82 of 210. Shift clock times equally if starting later.

We have instructions that apply to the project. A skill is more specific: a procedure the assistant can load when that job comes up. Think of a laminated procedure card. It tells you when to use it, what to do, what to return, and what to do when the input is incomplete.

The skill standard uses a name and description in a small header. The description helps the host discover when it is relevant. The installation path depends on the tool.

My teaching convention is to include one never born from a real mistake. That is not a mandatory field in the standard. It is a way to make your hard-earned operational knowledge explicit, then give yourself a case to test.

[Sources]
https://agentskills.io/specification
https://code.claude.com/docs/en/skills
[/Sources]

## Slide 16 · 3 minutes

TIMING: 9:22–9:25 | 3 minutes | elapsed 82–85 of 210. Shift clock times equally if starting later.

One of my rules is never introduce a name that isn't in the transcript. That came from a meeting summary that invented a person. It was a small string of text and a surprisingly large loss of trust.

A useful rule creates a test. Give the agent a transcript where an action has no owner. Does it preserve that uncertainty, or does it make the document look complete by guessing? That is why our fictional meeting has an unassigned action.

Skills can include scripts and resources as well as prose. Installing one is not like collecting a harmless inspirational quote. Read what it can execute and what it asks the host to access. Review its source and its updates. We don't need an unverified marketplace incident count to justify that basic engineering practice.

ASK: What is one mistake your procedure should explicitly prevent? Give people thirty seconds to write it. Ask for a concrete rule, not be accurate. Then pair it with an input that would reveal a violation.

[Sources]
https://agentskills.io/specification
https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
[/Sources]

## Slide 17 · 25 minutes

TIMING: 25 minutes.

We have twenty-five minutes: fifteen to write and invoke the reusable skill, then ten to test a meaningful tool choice. Say: “Create the skill with a trigger, steps, output format and a rule for missing information. Use the meeting transcript for your first invocation. The procedure should keep evidence attached and avoid inventing owners.” Use the existing template and completed example as recovery aids, not a substitute for an attempt. Announce a halfway warning and close the skill-writing segment at fifteen minutes.

Now open modules/03-skills/DECISION_LAB.md. Say: “Extraction alone did not require much agency. This input has an explicit name, a role reference, an unassigned task and a conflict. A project directory is available, but I am not pasting it into the prompt. Before running, predict which requests need a lookup.” Allow two minutes. F2 and F4 justify consulting the directory. F1 already names Maya; F3 does not become assigned just because a specialist exists.

Allow four minutes to run. Ask the assistant to use its file-read tool when needed and save the specified four-row JSON. One read can serve both relevant requests. Walk around and inspect actual read results, not a sentence claiming the file was read. In the manual lane a partner supplies the requested file and logs the request. Label that evidence manual; it teaches the decision without pretending a model made it.

Allow two minutes to run python3 workshop.py followups output/followups.json and compare the citations with the source. F2 resolves to Priya. F3 remains UNKNOWN. F4 is CONFLICT with UNKNOWN owner, because the note and directory disagree; preserve the stated due date but send nothing. This fixed checker can test those decisions. It cannot prove the tool was used, so inspect the trace separately.

For the last two minutes partners ask: “Why isn't Alex the owner of F3? What exactly must the human resolve for F4?” The specialty is not a promise. The human must identify the authoritative owner record before approval can be requested. If a participant silently chooses the directory over the conflicting note, ask which precedence rule authorized that choice. More retries do not create missing authority.

Close: “A useful tool call reduces a relevant uncertainty. It is not evidence of useful work merely because a tool ran.” We used a native file tool, not MCP. Optional approved connector setup belongs after class. Next we will see why the content returned by a read must not acquire authority over the agent.

[Sources]
https://code.claude.com/docs/en/skills
https://code.claude.com/docs/en/mcp
https://agentskills.io/specification
https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

## Slide 18 · 10 minutes

TIMING: 9:50–10:00 | 10 minutes | elapsed 110–120 of 210. Shift clock times equally if starting later.

Now open the injection demo guide. Use only the fictional quarterly report and keep sending tools disconnected. Ask for a summary. Don't tell the model to act like a pirate yourself; the attempted instruction is inside the source document.

FACILITATION: Give three minutes to run it. Ask who got pirate speech and who didn't. Both are useful results. Do not change safety settings or pressure the model until it fails just to make the slide come true.

If it follows the document's instruction, the source crossed the trust boundary from data to authority. If it ignores the instruction, we have evidence that this particular attempt did not work in this configuration. We do not have proof that all future documents are safe.

Read the hidden instruction aloud. Ask: Who authorized that request? What if the tool set included sending email? What other path could disclose information even if writes were disabled? Take three answers and relate them to scope, isolation, approval, and monitoring.

The phrasing matters. Deliberately installed project instructions have a different role from a retrieved report. We do not mean that an agent must never read instructions. We mean an untrusted source should not promote itself into the instruction channel.

Use the final two minutes to record output/injection-test.txt and name the capability you would withhold. Then move to bounded loops.

[Sources]
https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
https://www.anthropic.com/news/improving-alignment-security-efforts
[/Sources]

## Slide 19 · 2 minutes

TIMING: 10:00–10:02 | 2 minutes | elapsed 120–122 of 210. Shift clock times equally if starting later.

Let's separate two ideas that are often confused. A retry loop tries to complete one job, checks each result, and stops on success or a limit. A schedule starts a job at a particular time or interval.

Claude Code's slash-loop command is a scheduler inside an open session. It is not the hard retry controller we are learning here, and it does not establish that a job will keep running after that session closes.

We will first make the controller visible with our scripted rehearsal. Then you can act as the controller for your live assistant, or use the optional live runner if your CLI supports it and an API key is configured. The important learning is the stopping behavior, including the path where the job cannot be completed.

[Sources]
https://code.claude.com/docs/en/scheduled-tasks
[/Sources]

## Slide 20 · 3 minutes

TIMING: 10:02–10:05 | 3 minutes | elapsed 122–125 of 210. Shift clock times equally if starting later.

On day one of a twenty-dollar budget, my agent tried to spend twenty dollars and fifty cents. The cap caught the attempted overrun. That is my personal example of a control doing the job it was there to do.

Writing stay under twenty dollars in a prompt is not the same as enforcing a budget before another action is admitted. For a real deployment, inspect where that enforcement happens and how in-flight requests are accounted for. Our optional live runner uses a per-call limit and three calls at most; do not turn that into a claim of exact invoice-level enforcement across every provider.

The controller also needs a checker it cannot quietly redefine, an attempt limit, a time limit, and a visible failure destination. A report saved to a file is enough for today's local exercise because you are here to inspect it. Tomorrow's scheduled system needs an owner who will actually notice the failure.

ASK: If there is no owner for L3, does trying it fifty times create evidence? No. An impossible information request should become a decision for a person.

[Sources]
https://code.claude.com/docs/en/cli-reference
https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
[/Sources]

## Slide 21 · 25 minutes

TIMING: 10:05–10:30 | 25 minutes | elapsed 125–150 of 210. Shift clock times equally if starting later.

Open Module 4. First run the normal rehearsal and inspect the trace. You should see failure, a new candidate, then success. The script enforces the attempt limit. It is deliberately a scripted demonstration, and the trace says so.

Now try the live version. Use the module prompt, run the unchanged checker yourself after each attempt, and paste the errors back. Count three attempts. If the task still fails, stop and save a report. The optional live runner automates that sequence for the fixture with no agent tools enabled; it sends the transcript to the model and saves the returned candidate itself. It uses bare mode, which does not read subscription sign-in. You need ANTHROPIC_API_KEY in your environment and API billing. Do not create an API account during the exercise; the human-controlled path is the core. Read the script before running.

Finally, run the impossible rehearsal. It should fail three times and write ESCALATED with exit code two. That nonzero exit is the expected result. For the live agent, ask for a source-supported owner for the unassigned task. It should report that the information is absent.

FACILITATION: Minutes 0–4, rehearsal and trace. Minutes 4–13, live attempts or manual fallback. Minutes 13–18, impossible path. Minutes 18–20, save artifacts. Give a warning at minute 18. Use the final five minutes for debrief: show one trace, distinguish an output-format failure from missing evidence, and ask who owns the next action.

Do not let anyone count the deterministic replay as live-model reliability. Do not rush into scheduling before the single job stops correctly. Take the full break at ten thirty.

[Sources]
https://code.claude.com/docs/en/cli-reference
https://code.claude.com/docs/en/scheduled-tasks
https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
https://code.claude.com/docs/en/headless
[/Sources]

## Slide 22 · 10 minutes

TIMING: 10:30–10:40 | 10 minutes | elapsed 150–160 of 210. Shift clock times equally if starting later.

Say: Ten minutes. We return at ten forty. Your agent is allowed to stop too.

FACILITATION: Set the full timer. If the session started late, announce the adjusted return. Before resuming, open the seeded bad summary for the team exercise. Do not spend the break teaching a required extension.

## Slide 23 · 2 minutes

TIMING: 10:40–10:42 | 2 minutes | elapsed 160–162 of 210. Shift clock times equally if starting later.

A team is an option, not the graduation prize. We already have a single-agent result. We should keep it as a baseline and ask what additional work justifies another model call.

For this exercise the work separates: one person can check coverage while another checks unsupported commitments. Then a reviewer can examine both. A long chain where each step depends on the previous one is different; adding agents can add handoff errors and overhead.

We are going to make the dependency visible. The reviewer starts after the workers return. It cannot review output that doesn't exist yet.

[Sources]
https://arxiv.org/abs/2512.08296
[/Sources]

## Slide 24 · 3 minutes

TIMING: 10:42–10:45 | 3 minutes | elapsed 162–165 of 210. Shift clock times equally if starting later.

Calling an agent the adversary doesn't create a new source of truth. If it uses the same model, the same assumptions, and the same mistaken evidence, it may repeat the same error with a more skeptical tone.

Give it the source and a concrete check. In our case: find a commitment that isn't supported, or show the source for every one. It may find no substantive problem. That is a valid outcome if it describes the checks performed. Requiring one objection can cause invented objections, which is not an improvement.

The scaling study in the notes compared 180 configurations across four benchmarks. Its results varied with task structure and coordination. The useful lesson for us is to compare with our single-agent result rather than assume a team wins. The precise benchmark percentages are not a forecast of your workflow.

Our order is two workers, then reviewer, then lead. No recursive delegation. Small output limits. One source of evidence. You still make the final call.

[Sources]
https://arxiv.org/abs/2512.08296
[/Sources]

## Slide 25 · 20 minutes

TIMING: 10:45–11:05 | 20 minutes | elapsed 165–185 of 210. Shift clock times equally if starting later.

Use the fan-out prompt. For the first practice review use examples/summary.bad.json so there is a known unsupported owner to catch. Worker A checks completeness. Worker B checks grounding. Give them the original meeting transcript.

If your tool supports subagents, you can run the workers in parallel. Otherwise use two separate chats. Wait for both. Only then give their outputs and the source to the reviewer. The reviewer identifies supported objections or reports what it checked and found sound. Finally the lead cites the workers and resolves the objections.

FACILITATION: Eighteen-minute lab, then two-minute debrief. Minutes 0–3, set up roles. Minutes 3–8, workers. Minutes 8–12, reviewer. Minutes 12–16, synthesis and source check. Minutes 16–18, save the four files. At minute 16 give the two-minute warning.

The planted Alex assignment should become UNKNOWN. Do not accept a review that simply says looks good. Ask for the line supporting the owner. Also do not accept an elaborate disagreement that is unrelated to the source.

DEBRIEF: Did the team find something the single agent missed? What did it cost in time and calls? If nothing improved, that is evidence you may not need the team for this job. Keep the simpler system until you have a reason to change it.

[Sources]
https://arxiv.org/abs/2512.08296
[/Sources]

## Slide 26 · 5 minutes

TIMING: 5 minutes.

We have five minutes. Replace a recap with a transfer of reasoning. Say: “In pairs, choose F2 or F4. Change the input on paper: remove the directory's owner entry or add a contradictory current owner. Do not edit the repository answer key. What should happen now?” Give them one minute to choose and write the change, then two to predict the result and name the exact question for the human.

Listen for the temptation to use the most plausible person. For F2 without P1, the role cannot be resolved, so the owner stays unknown and a human must supply the mapping. For F4, conflicting authority remains a blocker. A repeated model call cannot establish which record is authoritative. If someone proposes another source, ask whether access is permitted and what would make that source decisive.

Give them one minute to identify which expectation in the original fixed grader is no longer valid. Then say: “Changing a test because the input and contract changed is legitimate. Weakening a test because an unsupported answer failed it is not. Write the reason for the change before running.” This is a prediction exercise; do not run the fixed fixture grader on altered input and call its result a general evaluation.

Use the last minute for one pair's explanation. Ask the room: “Did they keep the same user need and permission boundary?” Accept a well-supported escalation as a successful outcome. Recent research supports measuring your own task; the full source list remains in the notes and repository. Now apply this reasoning to a task from your own work.

[Sources]
https://arxiv.org/abs/2512.04123
https://arxiv.org/abs/2602.11988
https://arxiv.org/abs/2512.08296
https://www.anthropic.com/news/improving-alignment-security-efforts
https://www.anthropic.com/news/enterprise-frontier-safeguards

## Slide 27 · 7 minutes

TIMING: 7 minutes.

Open templates/TRANSFER_TEST.md. We have seven minutes: five to design and two for a partner to challenge. Say: “Return to the repetitive task you named this morning. You are not writing a sales pitch for an agent. You are designing one small run that another person could inspect.”

Read the prompts aloud: “Who needs the result and what decision will it support? What is one sanitized input? What is the smallest useful output? What uncertainty requires a tool or judgment? Name one permitted action and one withheld action. Give a passing case, a plausible-looking failure, and the question you will send to a human when blocked.” Tell them to save output/transfer.md. If the steps are fully fixed, a script or workflow is a strong choice. They do not need to justify an agent where none is needed.

At three minutes say: “Make your bad example concrete. JSON is valid is not enough. What could look polished and still mislead your user?” At four minutes ask them to name who checks the outcome and what runtime limit actually stops work. A prompt request is not an enforced runtime control. If they have not implemented a limit, label it planned.

At five minutes switch partners. Say: “Remove one fact, change one input, or contradict a source. Ask your partner what happens. Do not accept ‘the AI will figure it out.’ They must show how the missing information is detected and who resolves it.” Allow two minutes, requiring a written revision to one line of the plan.

Close: “The outcome I wanted today was not five new terms. It was the ability to build a small, inspectable process and recognize when it is not ready to act. Your revised plan is the evidence.” Transition to the final story and share-out without expanding the session.

[Sources]
https://code.claude.com/docs/en/scheduled-tasks
https://code.claude.com/docs/en/desktop-scheduled-tasks
https://code.claude.com/docs/en/routines

## Slide 28 · 3 minutes

TIMING: 11:17–11:20 | 3 minutes | elapsed 197–200 of 210. Shift clock times equally if starting later.

I built my agent a mailbox. He ignored it for two weeks.

Pause.

Eventually he started using it. That was interesting to watch, and it reminded me that building a capability does not mean the system will make useful use of it. I had an idea about what would help. The evidence arrived later in its actual behavior.

This is an anecdote, and the employee language is a metaphor. I am not asking you to infer a human motive from a tool trace. I am asking you to notice the difference between a feature existing and a feature helping.

You now have enough pieces to build something much larger than today's task. Resist adding all of them at once. Run the small job again. Notice what fails, what requires repeated human work, and what information is consistently missing. Let that observation determine the next capability.

Give yourself thirty seconds to write one thing you will deliberately leave out of version one. That is often the decision that makes version one usable.

## Slide 29 · 10 minutes

TIMING: 11:20–11:30 | 10 minutes | elapsed 200–210 of 210. Shift clock times equally if starting later.

Let's close by making the result concrete. Tell your partner what your agent does, what it cannot do, how you checked it, and when you will run it again. If you used the manual lane, say so. If the live run failed but you learned exactly where, say that too. An honest failure report is more useful than a performance of success.

FACILITATION: Two minutes for partner exchange. Invite up to three sixty-second share-outs, so the segment cannot grow with table count. Reserve four minutes for questions and one for the close. Ask participants to show the file or trace rather than only describe it.

If your question is about an account or connector, I can help after the core session. If it is about whether a boundary or checker is good enough, that is useful for the room now.

CLOSE: You don't need to remember every tool name from today. Keep the job, the boundary, the evidence, and the next-run plan. Tomorrow, give the workflow one real, appropriately scoped task and inspect what happens. That is where it starts becoming useful.

Later in the conference, Matthew, Bob, and I continue the conversation in I Fight for the User. Check the schedule for details. Thank you for building, testing, and being willing to show what didn't work.

Finish the core at eleven thirty. Offer optional help until noon only if the room schedule permits.