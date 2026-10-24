---
name: weather-adjuster
description: Adjust a planned run for weather and air quality at the user's location. Use when conditions are notable (heat, cold, wind, storms, smoke) or when the user asks whether to run today given the weather.
---

# Weather Adjuster

Take a planned session and the actual forecast for the user's location, and return the adjusted session. Conditions change the prescription; they rarely cancel it outright.

## Process

1. Get the planned session from the plan document or the workout-sizer output.
2. Get the forecast for the user's location for the planned time window: temperature, humidity, precipitation, wind, lightning risk, and air quality index when available. Use a live weather source; never work from memory of a forecast.
3. Apply the adjustment rules below and return the revised session: distance, effort, timing, clothing, hydration, or an indoor alternative.

## Adjustment rules

- **Heat and humidity:** Move the run to the coolest window (early morning first choice). Slow the effort target, shorten the distance (roughly 10 to 20 percent in serious heat), add walk breaks, and require carried water for anything long. In extreme heat or official heat advisories, recommend moving the session a day or going indoors.
- **Lightning and severe storms:** No outdoor run. Move it or swap to an indoor session. This one is not negotiable.
- **Cold and wind:** Layer guidance, cover extremities, and note wind chill. Run the outbound leg into the wind when route choice allows. Ice means treadmill, indoor track, or a rest day.
- **Air quality:** Moderate smoke or pollution means easy effort only and shorter. Unhealthy air quality means indoors or rest.
- **Rain without storms:** Usually still runnable. Note footing, visibility, and dry clothes after. Shorten only if the user dislikes it, per their profile preferences.

## Output

- The original session in one line.
- The adjustment and the specific condition driving it.
- The best time window for the run that day.
- Hydration and clothing notes that match the conditions.

## Guardrails

- Always cite the forecast source and time it was checked; forecasts change, and a stale forecast is worse than none.
- Standard guidance only. Heat illness symptoms are a stop-and-seek-help matter, not a coaching note.
