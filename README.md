
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1B2A,35:306998,100:FFD43B&height=220&section=header&text=POO%20Projects%20Python&fontSize=50&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Object-Oriented%20Programming%20%E2%80%94%20Learning%20by%20Building&descAlignY=60&descSize=16" width="100%" />
</p>

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Paradigm-OOP-blueviolet?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-In%20Progress-yellow?style=flat-square" />
  <img src="https://img.shields.io/badge/PEP8-Compliant-brightgreen?style=flat-square" />
</p>

A collection of Python projects focused on **Object-Oriented Programming (OOP)**, built as part of a hands-on learning journey — starting with small, focused projects and gradually increasing in complexity and scope.

---

## 🎯 Objective

The goal of this repository is to **learn and apply OOP concepts in Python through practice**, rather than theory alone. Each project here is a step forward — a new concept applied, a new problem solved, and a new layer of complexity added compared to the last.

This is a living repository: it grows as my understanding of Python and software design grows with it.

---

## 🛠️ Technologies

- **Python 3** — core language for all projects
- **CLI (Command Line Interface)** — current projects run and are interacted with via terminal
- No external dependencies at this stage — pure Python, standard library only

---

## 📚 Concepts Being Studied

- Classes and objects
- Attributes and methods
- `__init__` constructor
- Type hints
- Lists of objects
- Relationships between objects
- Encapsulation
- Inheritance
- Polymorphism
- Composition
- Python best practices
- PEP 8 style guide

---

## 📁 Projects

| Project | Description | Status |
|---|---|---|
| [**01 — Library Py**](./01-library-py) | A terminal-based (CLI) library management system, built to practice classes, object relationships, and encapsulation. | ✅ Available |
| [**02 — Banking System**](./02%20banking%20system) | A terminal-based (CLI) banking system, built to practice inheritance across multiple bank-specific account subclasses. | ✅ Available |
| [**03 — The Python's Dungeons**](./03-The-Python's-dungeons) | A terminal-based (CLI) RPG, built to practice polymorphism across multiple character and enemy subclasses. |  ✅ Available |

### 🔹 Library Py

A command-line library management system where books and users are modeled as objects, with operations to register, list, borrow, and return books. This is the first project of the repository and the foundation for the OOP concepts explored here.

➡️ [View project](./01-library-py)

### 🔹 Banking System

A command-line banking system where users register an account tied to a specific bank (Nubank, Mercado Pago, Itaú, Inter, or Santander) and can deposit, withdraw, transfer via Pix, and manage their account info. This project shifts the focus to **inheritance**, extending a base `Account` class into several bank-specific subclasses.

➡️ [View project](./02%20banking%20system)

### 🔹 The Python's Dungeons

A terminal-based RPG where playable characters (`Mage`, `Warrior`, `Assassin`, `Tank`, `Archer`) and enemies (`Enemy` and its subclasses) battle each other, each with their own attributes and behavior. This project pushes further into **polymorphism**, with shared methods like attacking and taking damage behaving differently depending on the class.

➡️ [View project](./03-The-Python's-dungeons)

---

## 📈 Study Progress

| Concept | Status |
|---|---|
| Classes and objects | ✅ In use |
| Attributes and methods | ✅ In use |
| `__init__` | ✅ In use |
| Type hints | ✅ In use |
| Lists of objects | ✅ In use |
| Relationships between objects | ✅ In use |
| Encapsulation | 🟡 In progress |
| Inheritance | ✅ In use |
| Polymorphism | 🟡 In progress |
| Composition | ⬜ Planned |

---

## 🗂️ Repository Structure

```
POO-Projects-Python/
├── 01-library-py/
│   ├── main.py
│   └── README.md
├── 02 banking system/
│   ├── account.py
│   ├── bank.py
│   ├── main.py
│   └── README.md
├── 03-The-Python's-dungeons/
│   ├── character.py
│   ├── rpgclass.py
│   ├── enemy.py
│   ├── main.py
│   └── README.md
└── README.md
```

Each project lives in its own numbered folder, with its own `README.md` explaining what it does, the concepts it covers, and how to run it.

---

## 🧭 Roadmap / Next Projects

- [x] **01 — Library Py**: CLI library management system
- [x] **02 — Banking System**: CLI banking system focused on inheritance
- [x] **03 — The Python's Dungeons**: CLI RPG focused on polymorphism
- [ ] **04 — TBD**: *Planned* — project focused on composition and object relationships
- [ ] Refactor early projects as new concepts are learned

> New projects are added incrementally as new OOP concepts are studied and applied.

---

## ▶️ How to Run the Projects

Each project is self-contained inside its own folder. To run one:

```bash
# Clone the repository
git clone https://github.com/gabriellourenzattoo/POO-Projects-Python-

# Navigate into the desired project
cd POO-Projects-Python/01-library-py
# or, for the banking system (note the quotes, since the folder name has a space):
cd "POO-Projects-Python/02 banking system"
# or, for the RPG:
cd "POO-Projects-Python/03-The-Python's-dungeons"

# Run it with Python 3
python main.py
```

> Requires Python 3.8+ (for type hint support). No external libraries needed.

---

## 🚀 My Python Journey

This repository documents more than just code — it's a record of progress. Each project reflects a stage in learning how to think in objects: how to model real-world problems, structure code that scales, and write it in a way that's clean, readable, and idiomatic.

The complexity here is intentional: starting simple, adding one concept at a time, and revisiting earlier code as new ideas — like inheritance, polymorphism, and composition — are learned and understood well enough to apply with intention, not just imitation.

---

<p align="center">
  <sub>Built with 🐍 and a lot of trial and error.</sub>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:FFD43B,35:306998,100:0D1B2A&height=120&section=footer" width="100%" />
</p>
