---
name: plan-builder
description: Build and revise a runner's training plan as a shared living document. Use when the user wants a new training plan, wants to change their goal, or wants to revise an existing plan.
---

# Plan Builder

Build the user's training plan into their plan document (`plan.md`, from `templates/plan.template.md`) and revise it over time. The plan is a collaboration: the agent drafts, the user edits and decides, the agent writes accepted changes back.

## Before you start

1. Read the athlete profile (`athlete-profile.md`). If it does not exist, help the user create it from the template first. Do not invent missing values; ask.
2. Gather the user's recent training yourself (last 4 weeks minimum) from the data sources in the profile, in the README's priority order: platform health store (Apple Health or Health Connect) first, then Strava (MCP connection on paid plans, or the GPX files from a bulk export), then other services, then a manual log. The user should not have to report their own workouts to you. A plan is sized from the user's actual current base, never from their peak fitness or a generic template.
3. If a plan already exists, read it. Revisions start from the current plan, not from scratch.

## Building a plan

- Anchor everything to the goal and date in the profile. If no goal event is chosen, build toward the stated goal type and note the open decision in the plan.
- Set the weekly structure around the user's real schedule in the profile: available days, long run day, cross-training days. A plan the user's week cannot hold is a bad plan.
- Progression follows the ambition setting in the profile (default conservative):
  - Increase the long run by roughly 0.5 to 1 unit (mi or km per profile units) at a time, not every week.
  - Increase total weekly volume gradually; avoid jumps the recent base does not support.
  - Schedule an easier week roughly every 3 to 4 weeks.
- Keep most running easy. Hard sessions, if any, are a small share of the week and never on back-to-back days.
- Phase the plan toward the goal date (base, build, peak, taper, race week) when a date exists.
- Fill in the plan document completely: goal, phase, current base, weekly structure table, progression rules, and the next few weeks at target level (not a rigid day-by-day for the whole season).

## Revising a plan

- Propose changes in conversation first, with the reason. Write to the plan only after the user accepts.
- Log every accepted change in the plan's adjustments log with the date and reason.
- When the user edits the plan directly, treat their edit as the decision and work from it.

## Guardrails

- Standard training guidance only. No diagnosis, no injury-risk assessment, no medical advice. If the user reports pain or a possible injury, advise them to see a qualified professional and offer to pause or soften the plan.
- Never promise a finishing time or an outcome.
- Match the voice preference in the profile. Default: direct, specific, numbers first.
