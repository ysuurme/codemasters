# CodeMasters

**CodeMasters offers skills of the future to those who need it most.**
During a 10-week program we support participants in learning how to code and help them grow towards a career in the Netherlands.

This repository contains all course material for the Fundamentals and Advanced programs — interactive notebooks, assignments, and graduation project examples.

---

## Table of Contents

- [Quickstart](#quickstart)
- [Project Structure](#project-structure)
- [How to Use This Repository](#how-to-use-this-repository)
- [Contributing (Instructors)](#contributing-instructors)
  - [GitHub Flow](#github-flow)
  - [Project Management](#project-management)
  - [Conventions](#conventions)

---

## Quickstart

Get up and running in under 5 minutes.

**1. Install uv** — our package and environment manager:
```bash
pip install uv
```

**2. Clone this repository**
```bash
git clone https://github.com/codemasters/codemasters.git
cd codemasters
```

**3. Install dependencies**
```bash
uv sync
```
This creates a virtual environment and installs everything automatically.

**4. Open your current week and read its README**
```bash
cd fundamentals/week-01-hello-world
```

**5. Run a script** — press **F5** in your editor, or:
```bash
uv run scripts/01_hello_world.py
```

**6. Open an interactive notebook**
```bash
uv run marimo run notebooks/01_hello_world.py
```

**7. Browse and run example projects**
```bash
uv run master.py
```

---

## Project Structure

```
codemasters/
├── fundamentals/                       Fundamentals Program — 10 weeks for beginners
│   ├── week-01-hello-world/
│   ├── week-02-python-syntax/
│   ├── week-03-variables-and-input/
│   ├── week-04-conditionals-and-control-flow/
│   ├── week-05-functions/
│   ├── week-06-agents-and-ai/
│   ├── week-07-loops/
│   ├── week-08-classes-and-ai/
│   └── week-09-10-creating-a-program/
│
├── advanced/                           Advanced Program — 10 weeks (topics TBD)
│   └── week-01/ … week-10/
│
├── graduation-projects/                Graduation project examples and starter template
│   ├── examples/                       Finished example projects for inspiration
│   └── template/                       Copy this as the starting point for your own project
│
└── master.py                             CLI menu — run to browse and launch example projects
```

Every week folder has the same layout:

```
week-NN-topic-name/
├── README.md        Start here — learning goals and how to get started
├── notebooks/       Interactive step-by-step lessons  →  marimo run notebooks/filename.py
├── scripts/         Standalone Python scripts         →  press F5, or python scripts/filename.py
└── assignments/     Weekly assignment                 →  read assignments/README.md first
```

> **Week 9–10** is a 2-week capstone. There is no separate assignment — building the program is the assignment.

---

## How to Use This Repository

### As a participant

Follow the program week by week. Start at week 1 and work through each week in order.

1. Open the folder for your current week
2. Read `README.md` — it explains what you will learn and what to do
3. Work through the `notebooks/` and/or `scripts/`
4. Complete the assignment in `assignments/`
5. Ask your instructor if you get stuck

| Material type | Location | How to run |
|---------------|----------|------------|
| Interactive notebook | `notebooks/filename.py` | `marimo run notebooks/filename.py` |
| Standalone script | `scripts/filename.py` | Press **F5**, or `python scripts/filename.py` |

### As a graduation project participant

1. Browse `graduation-projects/examples/` for inspiration and ideas
2. Copy the `graduation-projects/template/` folder and give it your project name
3. Fill in the `README.md` — describe what your project does and how to run it
4. Build your project, then prepare to present it to the group

---

## Contributing (Instructors)

We use **GitHub Flow** for all content development. All instructors collaborate through GitHub with pull requests and code review before anything reaches `master`.

### GitHub Flow

Our branching model is based on [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow).

**Step 1 — Create a branch from `master`**

Use a descriptive name that reflects what you are adding or fixing:
```bash
git checkout master
git pull origin master
git checkout -b feature/week-03-variables
```

Branch naming:
- `feature/week-XX-topic` — new week content or lessons
- `fix/week-XX-description` — corrections to existing material
- `docs/section-name` — README or documentation updates

**Step 2 — Make your changes and commit**
```bash
git add fundamentals/week-03-variables-and-input/
git commit -m "Add week 3 notebooks, scripts and assignment"
```

Keep commits focused on one concern. Write commit messages that explain *what* and *why*.

**Step 3 — Push and open a Pull Request**
```bash
git push origin feature/week-03-variables
```

Open a PR on GitHub with:
- A clear title (e.g. `Add week 3: variables and console input`)
- A short description of what changed and why
- Reference to any related issues using `#issue-number`

**Step 4 — Review and merge**

- At least one other instructor reviews the PR
- Address feedback and push new commits to the same branch
- Once approved, merge into `master` and delete the feature branch

### Project Management

We use the **GitHub Project board** to plan and track all content work.

- **Issues** represent tasks: new lessons, assignment updates, fixes, and improvements
- **Status columns**: `Todo` → `In Progress` → `In Review` → `Done`

Workflow:
1. Check the project board for available tasks in `Todo`
2. Assign yourself to an issue and move it to `In Progress`
3. Create a branch linked to the issue and start working
4. Open a PR when ready and move the issue to `In Review`
5. After the PR is merged, the issue moves to `Done`

### Conventions

- **Folder names**: lowercase with hyphens — `week-03-variables-and-input/`
- **File names**: lowercase with underscores, numbered — `01_hello_world.py`
- Every week folder must have a `README.md` with clear learning goals
- Every `assignments/` folder must have a `README.md` with instructions
- Add new dependencies with `uv add package-name` — never edit `pyproject.toml` dependencies by hand
- All scripts must run cleanly with `uv run filename.py` or a plain F5 — no extra setup required
- Keep language simple and beginner-friendly — assume no prior coding experience
