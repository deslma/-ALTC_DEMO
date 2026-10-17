# Curriculum development demo

A small, working example of developing an online module as a **Jupyter Book** in GitHub: draft branches, pull requests, automated quality checks, preview builds and publishing. It accompanies the showcase *Chuck that script: Word Documents to Pull Requests*.

The module content ("Introduction to Machine Learning") is invented for the demo. The workflow mirrors a real programme repository.

## How the repository works

| Branch | Purpose | Who edits it |
|--------|---------|--------------|
| `PROD_<year>_<module>_<n>` | The reviewed, publishable version of the module. Protected. | Nobody directly: changes arrive by pull request |
| `DRAFT_<module>_<topic>` | A safe workspace for one piece of development | Anyone on the team |

1. **Branch** from the production branch into a `DRAFT_*` branch.
2. **Author** in Markdown or notebooks under `resources/content/`.
3. **Push.** A preview of your draft is built and published automatically; quality checks run.
4. **Open a pull request** into the `PROD_*` branch. Reviewers comment on the exact lines that changed and read the preview.
5. **Merge** once approved. The production branch is rebuilt and published.

Preview and publish addresses follow the branch name, with each underscore becoming a slash:

```
DRAFT_DEMO_unit1_edit   ->  https://<owner>.github.io/<repo>/DRAFT/DEMO/unit1/edit/
PROD_202627_DEMO_01     ->  https://<owner>.github.io/<repo>/PROD/202627/DEMO/01/
```

That production address is the link you place in the VLE.

## Folder structure

```
resources/
  _config.yml          book settings (avoid editing)
  _toc.yml             table of contents: add new pages here
  content/
    home.md
    unit-1/
      intro.md
      lesson-1/        lesson-1.md, lesson-1a.md, lesson-1b.ipynb
      unit-1-images/   images for this unit
      summary.md
scripts/qa_check.py    automated content checks
QA_CHECKLIST.md        human review checklist
.github/workflows/     preview, publish and pull request checks
```

## Writing content

- Pages are Markdown (MyST). Notebooks are `.ipynb`; every notebook is **re-run on each build**, and a failing cell fails the build.
- Start every page with one `#` heading and do not skip heading levels.
- Every image needs alt text: `![Describe what the image shows](path/to/image.png)`.
- Learning objectives use the `learning-objectives` admonition (see `lesson-1.md`).

## Three ways to work

1. **In the browser (easiest).** Open a file on GitHub, press `.` to open the web editor, or use the pencil icon. Create or switch to a `DRAFT_*` branch when prompted.
2. **GitHub Codespaces.** Choose *Code → Codespaces → Create codespace on branch*. Dependencies install automatically (see `.devcontainer`).
3. **Locally.**
   ```bash
   git clone <repository-url>
   cd <repository>
   git checkout PROD_202627_DEMO_01
   git checkout -b DRAFT_DEMO_my_change
   pip install -r requirements.txt
   python scripts/qa_check.py
   jupyter-book build resources      # open resources/_build/html/index.html
   ```

## One-off repository setup

Do these once after pushing the repository to GitHub (details in `DEMO_SCRIPT.md`):

1. Push the `PROD_*` branch first and wait for the *Publish production* run to finish. It creates the `gh-pages` branch.
2. **Settings → Pages:** deploy from branch `gh-pages`, folder `/ (root)`.
3. **Settings → Branches:** add a protection rule for the pattern `PROD_*` that requires a pull request, at least one approval and the status check *Quality checks and test build*.
4. Optional: add an `AZURE_CONNECTION_STRING` repository secret to also publish to Azure Blob Storage.
