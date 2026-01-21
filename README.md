# Why Did I Commit Today?

A beginner-friendly Python project for daily reflection and meaningful GitHub commits

---

## 1. Overview

Why Did I Commit Today? is a small command-line tool that helps you reflect on your work every day and record why you made a GitHub commit

Each day:
- You answer a few simple questions
- Your answers are saved as a Markdown file
- That file becomes your daily GitHub commit

---

## 2. Motivation

Many beginners focus on keeping a GitHub streak alive

This project focuses on something better:
- Intentional commits
- Honest reflection
- Building consistency without pressure

Even a small day counts, as long as it is real.

---

## 3. What the project does

When you run the script, it will:

1. Ask what you worked on today  
2. Ask why you decided to commit  
3. Ask how the day felt  
4. Save your answers in a Markdown file named with today’s date  

Nothing more. Nothing hidden

---

## 4. Project structure

```text
why-did-i-commit-today/
├── entries/
│   └── YYYY-MM-DD.md
├── reflect.py
└── README.md
```

- `reflect.py` runs the reflection
- `entries/` stores daily reflections
- `README.md` explains the project

---

## 5. How to run the project

Make sure Python is installed

From inside the project folder, run:

```bash
python reflect.py
```

Answer the questions when prompted

---

## 6. Output format

Each run creates a file inside `entries/` like this:

```md
# 2026-01-09

## What did I work on today?
Worked on my first reflection-based GitHub project

## Why did I commit today?
To stay consistent and build a habit

## How did it feel?
Calm and satisfying
```

This file is meant to be committed to GitHub

---


## 7. Possible future improvements

- Add more reflection questions
- Generate weekly summaries
- Track mood over time
- Optional automation

---

## 8. Final note

This project is not about perfection

It is about showing up once a day and being honest

One meaningful commit is enough
