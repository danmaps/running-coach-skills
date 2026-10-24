# Running Coach Skills

Skills for AI assistants that build running plans, review training, and recommend individual workouts from your recent activity.

## Get started

1. Download or clone this repository.
2. Configure your assistant to load the folders in `skills/`. Keep `references/` and `templates/` beside `skills/`; every skill links to the shared coaching rules. If your assistant copies skills into another directory, include those resources and preserve the relative paths.
3. Ask your assistant to create `athlete-profile.md` and `plan.md` from the [templates](templates/).
4. Connect a training-data source your assistant supports, provide an export, or use a manual log.

Try: “Build a plan around my current training,” “Review my last week,” or “What should I run today?”

## Skills

| Skill | Purpose |
| --- | --- |
| [plan-builder](skills/plan-builder/SKILL.md) | Build and revise a training plan. |
| [weekly-check-in](skills/weekly-check-in/SKILL.md) | Compare completed training with dated session targets. |
| [workout-sizer](skills/workout-sizer/SKILL.md) | Recommend a session from recent load and the accepted plan. |
| [route-builder](skills/route-builder/SKILL.md) | Find routes and check distance, access, and current conditions. |
| [post-run-debrief](skills/post-run-debrief/SKILL.md) | Review a completed run and record the takeaway. |
| [race-prep](skills/race-prep/SKILL.md) | Compare races and prepare pacing, taper, and logistics. |
| [strength-integration](skills/strength-integration/SKILL.md) | Coordinate running, strength, and cross-training. |
| [recovery-read](skills/recovery-read/SKILL.md) | Review personal recovery trends alongside training and reported feel. |
| [motivation](skills/motivation/SKILL.md) | Offer brief encouragement and sourced Coach Chris Bennett quotes when requested or enabled. |

## Your training files

- **`athlete-profile.md`**: goals, schedule, preferences, units, and data sources.
- **`plan.md`**: weekly structure, dated session targets, observations, and accepted changes.
- **`routes.md`**: optional route library with distance sources and access checks.

Keep these files in a private working folder outside the public repository. The assistant records observations during requested reviews and asks before changing future training targets. Your own edits take effect immediately.

## Training data

Use a source your assistant can actually access: a supported health-store connection, Strava connection, another fitness service, an activity export, or a manual log. Available fields and permissions vary. A source listed in your profile does not automatically grant access.

Reviews identify the period covered, last sync when available, missing fields, and any uncertainty. Activities mirrored between services count once. An empty result does not establish that you took a rest day.

GPX files contain geographic tracks; elevation and timestamps are optional. Distance may be calculated from track points, while duration requires timestamps. Indoor activities and other metrics may require another export format. See the [GPX specification](https://www.topografix.com/gpx/1/1/).

## Scope

These skills provide general training guidance. They do not diagnose injuries, provide rehabilitation, or give medical clearance. Recommendations account for recent training, recovery, reported symptoms, and practical constraints.

## Evaluation

[Behavioral scenarios](evals/README.md) cover incomplete data, duplicate activities, repeated reviews, unit conversions, and session changes. Run repository checks with:

```bash
python scripts/validate.py
```

## License

[MIT](LICENSE). Attributed third-party quotations remain the property of their respective rights holders; no affiliation or endorsement is implied.
