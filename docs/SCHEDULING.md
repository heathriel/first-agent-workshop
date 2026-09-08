# Make tomorrow's run explicit

The required workshop outcome is a saved workflow you can run again. Scheduling is an optional extension.

For Claude Code, `/loop` schedules repeated prompts inside an open CLI session. Tasks only fire while the session is running and idle; resuming can restore unexpired tasks. Desktop scheduled tasks depend on the local runtime being available. For durable execution, configure a supported cloud routine or another scheduler and verify its prerequisites; do not assume a local timer is a hosted service.

Before enabling recurrence record: owner, time zone, trigger, runtime/machine, permissions, input scope, maximum attempts, cost/usage limit, overlap prevention, duplicate-write protection, failure destination, and disable procedure. Preview one run and its output. Observe one actual scheduled firing. Confirm what happens if the machine is asleep or credentials expire. For external changes, design idempotency and obtain action approval.

A valid completion today: `Tomorrow at 09:00 local time, I will run the saved prompt manually and inspect the result.` If scheduling is enabled, show the scheduler entry and one executed run. Otherwise do not claim the agent is still running.

[CLI scheduling](https://code.claude.com/docs/en/scheduled-tasks) · [Desktop scheduling](https://code.claude.com/docs/en/desktop-scheduled-tasks) · [Cloud routines](https://code.claude.com/docs/en/routines).

Recurring CLI tasks expire after seven days (reference checked September 8, 2026). Verify the scheduler you actually deploy.
