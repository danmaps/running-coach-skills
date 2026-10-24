---
name: route-builder
description: Find, verify, and save running routes near the user, matched to a needed distance and terrain. Use when the user needs a route for a workout, is running somewhere new, or wants to build out their route library.
---

# Route Builder

Read and apply the [shared coaching rules](references/coaching-contract.md) before proceeding.

Build routes from the user's location, wherever that is. This skill is location-aware, not location-specific: it takes the location and home area from the athlete profile (or the place the user names for this request) and does the lookup live.

## Process

1. Establish the need: target distance, terrain (flat, hills, trail, track, treadmill fallback), surface preference, and constraints from the profile (dogs, stroller, training partners, time of day, safety preferences).
2. Read the route library before searching. Search for routes near the location using the sources available to the agent: trail and route databases, park and city trail pages, and the user's own recorded activities. The user's history is a route source in its own right: recorded runs from the platform health store, or GPX files from a Strava bulk export, can show previously recorded paths and derived distances, subject to recording quality. Recorded runs provide evidence of historical use and measured distance; they do not establish current public access or safety. Retrieve only route fields the athlete has permitted.
3. Track three separate facts for every route: historical use (recording date if any), distance evidence (source, measurement method, date, and uncertainty), and current access (official closure/access source and time checked, or unknown). Verify every distance from a source: a listed route length, a map measurement, or the user's recorded activity. Never present an estimated distance as confirmed. Label estimates as estimates.
4. Prefer loops and out-and-backs with clear start points, parking or transit notes, and bail-out options for long runs. Note water, restrooms, and lighting when sources mention them.
5. Present the route: name, sourced or derived distance with uncertainty, terrain and surface, public start point, historical-use evidence, current access status, and one line on why it fits this workout. Check official park or land-manager notices for closures and restrictions. If current access cannot be verified, label it unknown and avoid recommending a route through a reported closure. Never call a route safe merely because it was run before.
6. Save accepted routes to the user's route library (`routes.md`): name, broad location, distance and measurement method, terrain, surface, public start point, historical-use date, access source and check time, uncertainty, and notes. Update an existing route entry instead of duplicating it. Recheck time-sensitive access before reusing a saved route. The library grows over time and later route requests should check it before searching again.

## Variations

- Travel: if the user names a different city, build from that location and label the routes as travel routes in the library.
- Distance tuning: adjust a known route with a named add-on or an earlier turnaround point, and state the resulting total with the same verification standard.

## Guardrails

- Never invent a route or a distance. If nothing verified can be found, say so and offer the closest verified option.
- Respect closures and conditions reported by sources; flag them rather than routing through them.
- Do not store or share precise home coordinates, a home address, or private route endpoints. Use public trailheads or trim sensitive endpoints before saving or sharing route details. The profile's home area (neighborhood level) is enough.
