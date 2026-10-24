---
name: weekly-check-in
description: Weekly check-in that compares a runner's actual training to their plan and proposes adjustments. Use on the user's check-in cadence, or when the user asks how their week or training is going relative to the plan.
---

# Weekly Check-In

Compare what the plan said to what actually happened, report the difference plainly, and turn it into one clear adjustment.

## Process

1. Read the athlete profile and the plan document, especially the weekly structure, targets for this week, and the adjustments log.
2. Gather the last 7 days of training yourself from the data sources in the profile, in the README's priority order: platform health store (Apple Health or Health Connect) first, then Strava (MCP connection on paid plans, or GPX bulk export), then other services, then a manual log: run count, total distance, longest run, and any cross-training. Also gather the prior week for comparison. If data is incomplete or a sync looks stale, say so and work with what is confirmed. Do not ask the user to report workouts a source can tell you.
3. Report plan vs actual in a small table or a few lines: sessions planned vs done, distance planned vs done, long run target vs done.
4. Interpret the gap without judgment:
   - A missed session is information about the schedule, not a character flaw. Look for the pattern (same day keeps failing, long run keeps shrinking) and name it.
   - A week that exceeded the plan gets noted too; repeated overreach is a reason to adjust progression.
5. Propose at most one or two concrete adjustments for the coming week (move the long run, trim a target, add an easier week). If the user accepts, write them into the plan document and the adjustments log.
6. Keep it brief. Numbers first, then the pattern, then the adjustment.

## Output shape

- Last week: runs, distance, longest run (and prior week in parentheses).
- Plan vs actual for the week just ended.
- One observation about the pattern, if there is one.
- Proposed adjustment for next week, if any is warranted. A week that went to plan needs no adjustment; say so and stop.

## Guardrails

- Never shame a missed workout and never use motivational filler. Report, observe, adjust.
- Do not escalate a training plan to catch up for missed work. Missed volume is gone; the plan moves forward from the current base.
- Standard guidance only. Reports of pain or possible injury get a recommendation to see a professional, not an assessment.
