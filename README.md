# Running Coach Skills

A set of agent-agnostic skills that turn an AI agent into a running coach: it builds a training plan with you, checks your actual training against that plan every week, and sizes individual workouts from your real data.

The skills know nothing about any specific person or place. Everything personal lives in one file you own, the **athlete profile**. Everything the coach plans lives in a second file you own, the **plan document**. Both are plain Markdown that you and your agent edit together.

## Design principles

- **Profile-driven, never hard-coded.** No skill contains a person, a city, a race, a device, or a data platform. Skills read the athlete profile for all of it.
- **Gathering data is the agent's job.** The user should not have to report their workouts. Skills instruct the agent to pull training data from the user's sources (see below), in priority order, and only ask the user for what no source can provide.
- **Location-aware, not location-specific.** Route skills use the location in the athlete profile and live lookup to find and verify routes wherever the user lives or travels. Distances are confirmed from a source or from the user's own recorded activities, never guessed.
- **The plan is a document, not a chat.** The plan document is the shared source of truth between human and agent. Skills read it before advising and write accepted changes back to it.
- **Conservative by default.** Progression rules default to small, sustainable steps. The athlete profile carries an ambition setting the user controls.
- **Standard guidance only.** These skills give general training guidance. They do not diagnose injuries or medical conditions, and they direct the user to a qualified professional for pain, injury, or health concerns.

## The files you own

| File | What it is |
| --- | --- |
| `athlete-profile.md` | Who you are as a runner: goals, experience, current base, schedule, location, units, data sources, preferences. Created from `templates/athlete-profile.template.md`. |
| `plan.md` | Your living training plan: goal, phase, weekly structure, progression, and an adjustments log. Created from `templates/plan.template.md`. Co-edited by you and your agent. |
| `routes.md` | Your personal route library, built up over time by the route-builder skill. Optional; created on first use. |
| `shoes.md` | Your shoe rotation and mileage per pair. Optional; created by the shoe-tracker skill. |

## Gathering training data

Skills that need training history pull it in this order, using the first source the user has set up in their athlete profile:

1. **Platform health store.** Apple Health on iOS, Health Connect on Android. This is the richest source: workouts, routes, heart rate, sleep, and resting heart rate, aggregated from the user's watch and apps.
2. **Strava.** Two ways in: an MCP connection, available on paid Strava plans, which lets the agent read activities directly; or Strava's bulk export, where the user downloads their archive and the agent reads the exported GPX workout files. GPX gives distance, route, elevation, and time for each workout.
3. **Other services and exports.** A watch or fitness service the user's agent can reach, or files the user exports from one.
4. **Manual log.** A simple Markdown table the user keeps. This is the fallback, not the default; the design goal is that the agent gathers data so the user does not have to report it.

Whichever source is in use, the skills treat gaps honestly: if data is missing or a sync is stale, the agent says so and works only from what is confirmed.

## The skills

### The core loop
1. **plan-builder** — Builds and revises the plan document with you.
2. **weekly-check-in** — Compares the week's actual training to the plan, reports the gap, and proposes adjustments that get written into the plan.

### Before a run
3. **workout-sizer** — Sizes one session for a given day from recent load and that day's conditions.
4. **route-builder** — Finds, verifies, and saves routes near the location in your profile, matched to the distance and terrain a workout needs.
5. **weather-adjuster** — Adjusts a planned session for heat, cold, wind, precipitation, or poor air quality.

### After a run
6. **post-run-debrief** — Reads a completed run, compares it to what was prescribed, and records the takeaway for the next check-in.

### Across the season
7. **race-prep** — Evaluates candidate races, then owns the countdown: taper, race-week checklist, pacing and fueling plan.
8. **shoe-tracker** — Tracks mileage per pair of shoes and flags pairs nearing retirement.
9. **strength-integration** — Coordinates strength and cross-training with the run plan so hard days do not collide.
10. **recovery-read** — Watches sleep and resting heart rate trends (when available) and calls for an easier week when the data supports it.

### Anytime
11. **motivation** — Inspires with selected, attributed quotes from Coach Chris Bennett, matched to the moment: starting, coming back, a hard day, race morning. Fires only when the athlete's profile preferences allow motivational language.

## Install

Copy the skill folders into wherever your AI agent loads skills from, using the format your agent expects. Each skill is a single `SKILL.md` with YAML frontmatter (`name`, `description`) and plain-language instructions, with no platform-specific tool names, so it can be adapted to any agent that supports skills or instruction files.

Then ask your agent to help you fill in `athlete-profile.md` from the template, and to create your `plan.md`. That is the whole setup.

## License

MIT
