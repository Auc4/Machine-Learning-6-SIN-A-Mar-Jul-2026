# Mid-Term Practical Evaluation — Machine Learning (6 SIN-A)

**Universidad Internacional del Ecuador — Computer Science School**
**Duration:** 90 minutes · **Modality:** Individual · **Weight:** 12 points
**Environment:** GitHub Codespaces

---

## How to start

1. Accept the GitHub Classroom invitation provided by the instructor.
2. Once your repository is created, click the green **"Code"** button → **"Codespaces"** tab → **"Create codespace on main"**.
3. Wait for the Codespace to finish building (≈ 60 seconds). The devcontainer is pre-configured — you do not need to run any setup commands.
4. Open `notebooks/exam.ipynb` from the file tree on the left.
5. Run the first cell (environment check). If it prints versions, you are ready.

## How to submit

```bash
git add .
git commit -m "Final exam submission"
git push
```

Paste your repository URL in Canvas before the timer expires. The Git commit timestamp is the official submission time.

## Repository layout

```
.
├── .devcontainer/        # Codespaces config — do not modify
├── data/
│   └── wine_quality.csv  # 1599 rows, 11 features + 'quality' target
├── notebooks/
│   └── exam.ipynb        # ← Your work goes here
├── src/
│   └── scale.py          # Contains a bug for Task 2
├── pyproject.toml        # UV-managed dependencies
└── README.md
```

## Rules

- **Open notes, open slides, open class repository, open official docs** (sklearn, pandas) are allowed.
- **AI assistants (ChatGPT, Claude, Copilot) are NOT allowed.** Codespaces activity is logged.
- **No communication with other students.** Two notebooks with essentially identical code → 0 for both.
- Phones, second screens, and external chat windows are not permitted during the 90 minutes.

## Tips

- Read all 11 tasks first. The big-ticket items are Tasks 5, 6, and 8.
- Save the notebook every 10 minutes (`Cmd/Ctrl + S`).
- Commit at the end of each Part. If something breaks, you still have credit.
- If Task 2 (the bug fix) takes more than 5 minutes, skip it and return at the end.

Good luck.
— Ing. Jonathan E. Tito O., MSc.
