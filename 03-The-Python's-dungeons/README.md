<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1B2A,35:306998,100:FFD43B&height=200&section=header&text=The-Phython's-Dungeons&fontSize=55&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=A%20Terminal-Based%20RPG%20to%20Practice%20OOP&descAlignY=60&descSize=16" width="100%" />
</p>

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Interface-CLI-informational?style=flat-square" />
  <img src="https://img.shields.io/badge/Paradigm-OOP-blueviolet?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-In%20Development-yellow?style=flat-square" />
</p>

A terminal-based (CLI) RPG built in Python as a study project, focused on practicing Object-Oriented Programming — characters, enemies, and a battle system, all modeled with classes.

---

## 📖 About the Project

This project is an RPG played entirely through the terminal, created with the main goal of **practicing Object-Oriented Programming in Python**. Instead of learning OOP through theory alone, the idea is to apply the concepts in a system with its own identity: characters with distinct attributes and behaviors, enemies, and a battle system connecting it all together.

The project is under constant evolution — new classes, enemies, and mechanics are being added as new OOP concepts are studied and applied.

---

## ⚔️ Features

**Implemented:**
- Main menu with the options: `1. Character`, `2. Battle`, `3. Logout`
- Playable character system, each with their own attributes and behavior
- Battle system between characters and enemies

**In development:**
- Expansion of the battle system
- Balancing and new mechanics per class
- Gradual addition of planned enemies

---

## 🧙 Classes

- **`Character`** — base class from which all playable characters inherit. Defines the core attributes and behaviors shared by every character class.
- **`Mage`** — character focused on magic-based attacks.
- **`Warrior`** — melee combat character, with higher resistance.
- **`Assassin`** — character focused on fast, precise attacks.
- **`Tank`** — character focused on resisting and absorbing damage.
- **`Archer`** — ranged attack character.
- **`Enemy`** — class representing the enemies faced in battle.

Each character class inherits from `Character`, reusing the base structure and overriding specific behavior as needed.

---

## 👾 Enemies

Some of the enemies already implemented or planned for the battle system:

- Goblin
- Skeleton
- Orc
- Wolf
- Troll
- Dark Mage
- Golem
- Vampire
- Dragon

> Not all enemies listed are necessarily implemented yet — this list represents both existing and planned enemies for the project.

---

## 🛠️ Technologies

- **Python**
- **Object-Oriented Programming**
- **`random`** (standard library module)
- **Type Hints**

---

## 📚 Concepts Practiced

- Classes and objects
- Inheritance
- Encapsulation
- Polymorphism
- Methods
- Constructors (`__init__`)
- `super()`
- Type hints
- Conditional structures
- Randomization (`random` module)

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/gabriellourenzattoo/POO-Projects-Python-/new/main/03-The-Python's-dungeons

# Navigate into the project folder
cd The-Python's-dungeons

# Run with Python 3
python main.py
```

> Requires Python 3.8+ (for type hint support). No external dependencies.

---


---

## 👨‍💻 Goal

This project is part of my journey learning Python and Object-Oriented Programming. It's a space to apply what I've been studying in practice, make mistakes, fix them, and learn along the way. The intention is to eventually evolve toward more advanced and complex projects.

---


---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:FFD43B,35:306998,100:0D1B2A&height=100&section=footer" width="100%" />
</p>
