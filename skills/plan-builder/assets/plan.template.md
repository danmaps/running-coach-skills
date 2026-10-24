# Training Plan

Store accepted prescriptions here. Record observations during reviews; propose future target changes before saving them. Keep past targets and stable session IDs so later reviews can reconstruct what was prescribed.

## Goal
- Target:
- Date:
- Why this goal (the athlete's words):
- Timezone:
- Week starts on: Monday
- Display units: km | mi

## Current phase
- Phase: base | build | peak | taper | race week | recovery
- Phase focus:
- Started:

## Current base
- As of:
- Evidence period and coverage:
- Runs per week:
- Weekly distance and/or duration:
- Longest recent run:
- How training feels:

## Weekly structure
| Day | Session | Notes |
| --- | --- | --- |
| Mon | | |
| Tue | | |
| Wed | | |
| Thu | | |
| Fri | | |
| Sat | | |
| Sun | | |

## Progression rules
- Long run progression (physical amount; convert for display):
- Weekly volume progression:
- Easier week frequency:
- Ambition and constraints:

## Upcoming weeks
| Week of | Focus | Long run target | Weekly distance/duration target | Notes |
| --- | --- | --- | --- | --- |

## Dated sessions

Use ISO local dates and stable IDs. Target is distance or duration with units; effort is separately specified. Status: planned | completed | skipped | rest | unknown. Blank activity IDs mean no match established. A future row stays planned; missing evidence for a past row becomes unknown. Keep original targets after completion.

| Session ID | Local date | Type | Target | Effort | Status | Activity IDs |
| --- | --- | --- | --- | --- | --- | --- |

## Evidence coverage

Keep one current record per source and review period. Use unknown for fields the source does not expose.

| Source | Retrieved at | Requested local period / timezone | Actual coverage | Last sync | Fields / gaps |
| --- | --- | --- | --- | --- | --- |

## Observations

Upsert by observation key (session ID + canonical activity ID, or review period for a weekly summary). Retain cross-source aliases in the activity column. Record reported feel in the athlete's words and separate it from interpretation.

| Observation key | Date | Session ID / activity IDs | Actual distance / duration | Reported feel | Takeaway / correction |
| --- | --- | --- | --- | --- | --- |

## Adjustments log

Log accepted target changes once. Preserve previous values; include session IDs for changed sessions.

| Change ID | Accepted on | Session ID / scope | Previous value | New value | Reason |
| --- | --- | --- | --- | --- | --- |
