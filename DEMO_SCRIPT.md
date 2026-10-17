# Demo script (about 10 minutes)

Story spine: *Word, BUT code. THEREFORE GitHub, BUT not for non-developers. THEREFORE a designed workflow. BUT source files are not a learning experience. THEREFORE publishing.*

## Before the session

Allow 30 minutes the day before.

1. Create a new GitHub repository (empty, no README). Then from this folder:
   ```bash
   git remote add origin https://github.com/<you>/<repo>.git
   git push -u origin PROD_202627_DEMO_01
   ```
2. Wait for **Actions → Publish production** to go green (it creates `gh-pages`). Then **Settings → Pages →** deploy from `gh-pages` root.
3. Make `PROD_202627_DEMO_01` the default branch (**Settings → Branches**), and add the protection rule described in `README.md`.
4. Push the two prepared drafts:
   ```bash
   git push origin DRAFT_DEMO_unit1_edit DRAFT_DEMO_missing_alt
   ```
5. In GitHub, open two pull requests into `PROD_202627_DEMO_01`:
   - `DRAFT_DEMO_unit1_edit` (should go green). Leave one inline comment on a line and one suggested change. Do **not** merge it.
   - `DRAFT_DEMO_missing_alt` (should go red). Leave it open.
6. Open these in tabs, in order: repository home, `README.md`, a lesson page in the file view, the green PR (Files changed), the red PR (Checks), Actions, the preview page, the production page, Blackboard with the link.
7. Take screenshots of each tab as a fallback. Zoom the browser to about 125%.
8. Decide your merge candidate. Easiest: make a third small edit live (below), or merge the green PR at the end and show the publish run.

## On stage

| Time | Beat | Show | Say |
|------|------|------|-----|
| 0:00 | Familiar world | A Word content script | "This is a content script. We decided to get rid of it. BUT..." |
| 1:30 | The repository | Repo home, `resources/content/unit-1/` | "Content sits in plain text next to the code it teaches. THEREFORE one source of truth." |
| 2:30 | Branch | Branch dropdown: `PROD_*` and `DRAFT_*` | "A branch is a safe workspace. Production is protected." |
| 3:30 | Edit | Press `.` on a draft branch, change a sentence, commit | "This is the actual source, not a copy of it." |
| 4:30 | Pull request (green) | PR conversation and Files changed | "BUT we did not want to lose the conversation Word gave us. THEREFORE the pull request is our review space." |
| 6:00 | Quality checks (red) | The failing PR: annotation on the missing alt text | "BUT reviewers cannot catch everything. THEREFORE some of our quality assurance is automated." |
| 7:00 | Preview | Actions run, then the draft preview page | "Reviewers read the page students will see, not a diff." |
| 8:00 | Merge and publish | Merge the green PR, watch Publish production run | "Merge, and it is published." |
| 9:00 | In the VLE | Production URL in Blackboard | "The VLE holds a link, not a copy. Update the source and the module updates." |

## If something goes wrong

- **Actions are slow:** use the pre-built preview and production pages; narrate the run you already have open.
- **Wi-Fi fails:** switch to the screenshots. The story still works.
- **Merge conflict talk:** if asked, say plainly that conflicts happen and that onboarding and clear ownership of files matter more than clever Git.

## Honest limits to mention

- Technology was the easy part. Terminology, confidence, roles and review responsibilities took longer.
- Most contributors work in the browser editor, not the command line.
- Say only what you can evidence. This demo repository is a cut-down illustration, not your production pipeline.
