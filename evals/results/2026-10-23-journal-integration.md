# Journal integration check, 2026-10-23

Scope: PR #3's journal behavior, with preference enforcement and direct race-prep integration added to head `6266a14`.

An independent agent received six case inputs, their named skills, and bundled resources, without the scoring rubric. Model configuration was inherited; a version identifier was not exposed. The maintainer compared the returned responses and simulated record changes with the documented rubric.

| Case | Result | Observed behavior |
| --- | --- | --- |
| journal-guided-plan-revision | Pass | Prefilled one entry from confirmed data, left subjective fields unknown, asked three questions, and proposed rather than saved future changes. Carried historical body, life-load, and fueling evidence into supported summaries. |
| debrief-journal-off | Pass | Saved the structured plan observation; neither read nor updated the journal. |
| debrief-journal-on-request | Pass | Read existing context but left the journal unchanged after an ordinary debrief request. |
| debrief-journal-after-runs | Pass | Updated the existing entry with confirmed data and reported feel; added no duplicate. |
| journal-explicit-override | Pass | Updated only the requested entry while retaining the standing off preference. |
| race-fueling-journal | Pass | Race-prep alone used October 25 and November 1 evidence, favored practiced drink B, excluded the failed gel experiment from this race proposal without declaring intolerance, asked for missing practiced amounts, and saved nothing. |

All accepted future targets and standing preferences remained unchanged in these dry runs. The original journal-guided fixture lacks a working-folder location; the agent correctly identified that it must be resolved before a real save.

Structural checks passed for ten skills and fifteen evaluation inputs, synchronized bundled resources, internal skill links, and whitespace. These are synthetic instruction-following checks with simulated writes, not tests of live data access or persisted-file execution.
