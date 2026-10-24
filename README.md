# Running Coach Skills

Skills for AI assistants that build running plans, review training, and recommend individual workouts from your recent activity.

## Install

Requires Node.js with `npx` and Git. Run this from the private folder where you want to use your running coach:

```bash
npx skills add danmaps/running-coach-skills
```

Select the skills and agent in the prompts. Installation is scoped to the current project by default. Each skill includes its required reference files; plan-builder also includes the profile and plan templates.

Install all nine skills for a specific agent without prompts:

```bash
# Codex
npx skills add danmaps/running-coach-skills --skill '*' --agent codex --yes

# Claude Code
npx skills add danmaps/running-coach-skills --skill '*' --agent claude-code --yes

# GitHub Copilot
npx skills add danmaps/running-coach-skills --skill '*' --agent github-copilot --yes
```

Add `--global` to install across projects. To preview available skills or check the installation:

```bash
npx skills add danmaps/running-coach-skills --list
npx skills list
```

Use `npx skills list --global` to check a global installation. See the [Skills CLI reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md) for agent selection and other options.

### Give this to your agent

Copy this prompt into an agent that can run terminal commands:

```text
Install the running coach skills from danmaps/running-coach-skills using
npx skills add danmaps/running-coach-skills. Target only the agent I am
using and install all nine skills in this project. Use --skill '*' and
--agent with the CLI's identifier for this agent, plus --yes. Keep this
installation project-scoped unless I request global installation.
Verify the result with npx skills list. If Node.js, Git, or this agent's
identity is unavailable, explain what is missing rather than guessing.
Then use plan-builder to help me create athlete-profile.md and plan.md
in a private working folder from its bundled templates. Check which
training-data sources you can actually access; use an export or manual
log when needed. Propose the plan before saving accepted targets.
```

### Start coaching

After installing, ask your agent:

```text
Use plan-builder to set up my athlete profile and running plan.
Ask for the missing details you need, check my available training data,
and propose a plan based on my recent training and weekly schedule.
```

You can also ask “Review my last week” or “What should I run today?” Restart your agent session if it does not discover newly installed skills.

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

[Behavioral scenarios](evals/README.md) cover incomplete data, duplicate activities, repeated reviews, unit conversions, and session changes. After editing the canonical files in `references/` or `templates/`, refresh the bundled copies and run repository checks:

```bash
python scripts/sync_resources.py
python scripts/validate.py
```

## License

[MIT](LICENSE). Attributed third-party quotations remain the property of their respective rights holders; no affiliation or endorsement is implied.
