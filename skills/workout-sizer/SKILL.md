---
name: workout-sizer
description: Size a single running workout for a specific day, based on the runner's recent training load, their plan, and that day's conditions. Use when the user asks what to run today, tomorrow, or on a named day.
---

# Workout Sizer

Give the user one concrete session for one day: distance or duration, effort, and any structure, sized from their actual recent training.

## Inputs

- The day the user names (ask if they have not named one).
- The athlete profile: units, schedule, preferences, ambition setting.
- The plan document: what this point in the week or phase calls for, especially the long run target.
- The last 2 to 3 weeks of training, which you gather from the user's data sources in the README's priority order (platform health store first, then Strava via MCP on paid plans or GPX export, then other services or a manual log): session count, distances, longest recent run, days since the last hard or long effort.
- Conditions for that day at the user's location: forecast temperature, precipitation, wind, air quality. Hand adjustments to the weather-adjuster skill's rules when conditions are notable.

## Sizing rules

- The long run grows from the user's longest recent run in small steps (roughly 0.5 to 1 unit at the conservative setting), and only if recent weeks support it. A runner on one run per week gets a long run near their current longest, not a leap.
- Easy runs stay clearly shorter than the long run.
- Total for the day must make sense inside the user's current weekly volume, not just on its own.
- Effort is prescribed by feel: conversational (full sentences possible) for easy and long runs. Give a time estimate range if the user's typical easy pace is known; otherwise stay with effort and distance.
- Build in permission to cut the session short at a named fallback distance. State it as part of the plan, not as failure.

## Output

- Day and session type.
- Target distance (and fallback distance).
- Effort guidance and any simple structure (walk breaks, warm-up).
- Time and conditions note: best window of the day, hydration and clothing notes matched to the forecast.
- One line tying the session to the plan (what it is for).

## Guardrails

- Standard guidance only; no diagnosis or injury assessment.
- Never size a workout from the user's historical peak. Recent base only.
- If the user is returning from illness, injury, or a layoff the profile or conversation mentions, size down and say why.
