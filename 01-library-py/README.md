<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1B2A,35:306998,100:FFD43B&height=200&section=header&text=Library%20Py&fontSize=55&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=A%20CLI%20Library%20Management%20System%20in%20Python&descAlignY=60&descSize=16" width="100%" />
</p>

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Interface-CLI-informational?style=flat-square" />
  <img src="https://img.shields.io/badge/Paradigm-OOP-blueviolet?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square" />
</p>

A terminal-based **library management system** built in Python, developed as a hands-on exercise in Object-Oriented Programming. It models books and people as objects, and handles the core logic of a real library: registering, logging in, borrowing, and returning books — all through a simple command-line interface.

---

## 🔎 Overview

`Library Py` is the first project of the [POO Projects Python](../) repository. It's intentionally scoped to be small enough to fully understand, while still touching the core mechanics of OOP: classes, object relationships, state management, and control flow.

The system revolves around two main classes:

- **`Book`** — represents a book in the library, including its availability status
- **`People`** — represents a registered user who can log in and borrow/return books

---

## ✨ Features

- 📖 Register new books
- 👤 Register new people
- 🔑 Login for registered people
- 📚 Borrow books
- 🔁 Return books
- ✅ Check if a book is available or currently borrowed
- 🔍 View book information
- 🔍 View people information
- 🚫 Duplicate prevention for both books and people (no duplicate registrations)

---

## 🧠 OOP Concepts Applied

- Classes and objects
- `__init__` constructor
- Attributes
- Methods
- Type hints
- Lists of objects
- Conditionals
- Loops
- `match` / `case`
- Relationships between objects
- `for` / `else`

---

## 🛠️ Technologies

- **Python 3** — no external dependencies, standard library only
- **CLI** — runs and is fully operated through the terminal

---

## 🗂️ Project Structure

```
01-library-py/
├── main.py
└── README.md
```

All logic currently lives in a single `main.py` file, containing the `Book` and `People` classes along with the CLI loop that drives the program.

---

## ▶️ How to Run

```bash
# From the repository root
cd 01-library-py

# Run with Python 3
python main.py
```

> Requires Python 3.8+ (for type hint support). No external libraries needed.

---

## 💻 Example Usage

```
==== LIBRARY PY ====
1. Register book
2. Register person
3. Login
4. Borrow book
5. Return book
6. Check book availability
7. View books
8. View people
0. Exit
> 1

Book title: Clean Code
Author: Robert C. Martin
Book "Clean Code" registered successfully.

> 2

Name: Gabriel
Registering person...
Person "Gabriel" registered successfully.

> 3

Name: Gabriel
Login successful. Welcome, Gabriel.

> 4

Book title: Clean Code
Book "Clean Code" borrowed by Gabriel.

> 6

Book title: Clean Code
Status: Borrowed
```

> This is a representative example of the current CLI flow — exact menu wording and prompts may vary slightly depending on the version of `main.py`.

---

## 🚧 Future Improvements

- [ ] Data persistence (saving books/people between sessions, e.g. to a file or database)
- [ ] Input validation and error handling improvements
- [ ] Refactor into multiple files/modules as the project grows
- [ ] Introduce inheritance (e.g. different types of library members)
- [ ] Introduce composition (e.g. a `Library` class managing books and people)

---

## 🎯 Learning Goals

This project exists to practice **thinking in objects** — modeling a real-world system (a library) using classes, relationships, and state, instead of relying on plain functions and global variables.

Specific goals for this project:

- Get comfortable designing classes with clear responsibilities
- Practice managing collections of objects (lists of `Book` and `People`)
- Apply control flow (`match`/`case`, `for`/`else`) in a practical context
- Build a foundation to later apply inheritance, polymorphism, and composition in more complex projects

---

<p align="center">
  <sub>Part of <a href="../">POO Projects Python</a> — built with 🐍 and a lot of trial and error.</sub>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:FFD43B,35:306998,100:0D1B2A&height=100&section=footer" width="100%" />
</p>
