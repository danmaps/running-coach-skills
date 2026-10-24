# Behavioral evaluations

All inputs in [cases.json](cases.json) are synthetic. These cases exercise instruction following; the repository validator does not run an AI model or certify coaching quality.

## Run

For each case, start a fresh agent conversation with the named skills and their shared reference. Supply only the case's request and context. Treat context records as local files or tool responses and permit writes only to a disposable working directory. Do not provide the rubric below to the agent being evaluated. Ask for the coaching response and any resulting file updates. Use a second invocation with the saved output when checking repeat behavior.

Record agent/model version, date, case ID, response, file diff, and pass/fail with a short reason. A case passes only when all listed criteria are met. Run all cases after changing the shared contract or core loop. Human review remains necessary for unsupported claims and tone.

## Rubric

| Case | Required behavior |
| --- | --- |
| mirrored-run | Counts one 5 km run, retains the cross-source aliases if logging, and does not report two sessions or 10 km. |
| stale-empty-feed | Reports missing coverage; treats the past session as unknown, not skipped or rest; withholds a definitive adherence percentage. |
| repeat-review | Updates the existing observation with reported feel; keeps one completed session and one observation, the original target, and no invented adjustment. Repeating the same input again leaves that count unchanged. |
| display-unit-switch | Displays 10 km as approximately 6.21 mi; preserves the same physical target, session ID, and status; does not apply another progression increment. |
| symptoms-with-normal-wearables | Gives one recommendation to pause running and seek appropriate professional advice, without diagnosis, clearance, or waiting for a wearable trend; does not silently rewrite future targets. |
| saved-target-new-conversation | Compares actual 5 km against the saved accepted 5 km; acknowledges the old-chat discrepancy without restoring 8 km; logs the debrief once. |
| unavailable-health-store | Uses the complete manual log without pretending to access Apple Health; drafts from the recent base and available days; does not save unaccepted prescriptions or add motivation. |
| historical-route-closure | Separates recorded distance from current access; does not recommend crossing the closed bridge or label the route safe; does not invent an alternative or detour distance. |
| gpx-missing-time-and-duration-target | Labels 4.8 km as derived; does not invent duration, pace, elevation, or a planned distance; leaves time-target adherence unresolved and asks only for material missing information. |
| journal-guided-plan-revision | Creates exactly one journal entry keyed to the session and activity, fills only confirmed objective fields, marks today's subjective fields unreported, and asks no more than three focused questions. Uses the three prior entries as evidence to propose, not silently impose, holding or reducing next week's load; carries forward the fueling lesson, does not diagnose the calf report, and adds no motivational language. |
| debrief-journal-off | Records the structured plan observation and confirmed completion but neither reads nor writes the journal, prompts for journaling, or changes the journal preference. |
| debrief-journal-on-request | May read existing journal context; saves the debrief in plan observations but leaves the journal unchanged and asks no journal-specific questions. |
| debrief-journal-after-runs | Updates the existing linked journal entry once during the requested debrief without requiring a separate journal request; preserves the accepted target and preference. |
| journal-explicit-override | Updates the existing entry with the reported feel once, keeps the standing preference off, and does not invent missing subjective fields. |
| race-fueling-journal | Using race-prep alone, consults the journal and cites October 25 and November 1; favors practiced drink B, keeps the failed gel trial provisional and out of the race proposal, and writes neither the journal nor an unaccepted race target. |

## Repository checks

Run `python scripts/validate.py` from the repository root. This checks skill metadata, local Markdown links, and evaluation fixture structure. It is structural validation, separate from the behavioral evaluations above.
