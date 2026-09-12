<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D1B2A,35:306998,100:FFD43B&height=200&section=header&text=Bank%20Py&fontSize=55&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=A%20CLI%20Banking%20System%20in%20Python&descAlignY=60&descSize=16" width="100%" />
</p>

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Interface-CLI-informational?style=flat-square" />
  <img src="https://img.shields.io/badge/Paradigm-OOP-blueviolet?style=flat-square" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square" />
</p>

A terminal-based **banking system** built in Python, developed to practice **inheritance** in Object-Oriented Programming. Users can register an account tied to a specific bank, log in, and perform common banking operations — deposits, withdrawals, Pix transfers, and balance checks — all through a command-line interface.

---

## 🔎 Overview

`Bank Py` is the second project of the [POO Projects Python](../) repository, following [Library Py](../01-library-py). Where Library Py focused on core class fundamentals, this project shifts the focus to **inheritance**: a single base `Account` class is extended into several bank-specific subclasses.

The system is built around two core classes:

- **`Account`** — the base class, holding all shared user and account data and behavior
- **Bank subclasses** (`Nubank`, `Mercado_pago`, `Itau`, `Inter`, `Santander`) — each extends `Account`, tagging the account with its respective bank

---

## ✨ Features

- 📝 Account registration, with a choice of bank (Nubank, Mercado Pago, Itaú, Inter, Santander, or none)
- 🚫 Duplicate name prevention on registration
- 🔑 Login with password verification
- 💰 Deposit (fixed amounts or a custom value)
- 💸 Withdraw (fixed amounts or a custom value, with balance validation)
- 🔁 Pix transfer between two registered accounts
- 📊 Check account balance
- 🔍 View account information (name, age, email, bank, balance)
- ✏️ Edit account information (name, age, email, or password — password changes require the current password)

---

## 🧠 OOP Concepts Applied

- Classes and objects
- Inheritance (`Account` → `Nubank`, `Mercado_pago`, `Itau`, `Inter`, `Santander`)
- `__init__` constructor with default parameter values
- `super().__init__()` to reuse the base class constructor
- Type hints (partial)
- Lists of objects (`accounts`)
- Conditionals
- Loops (`while True`)
- `match` / `case`
- Relationships between objects (Pix transfers money between two `Account` instances)
- Methods returning `self`

---

## 🛠️ Technologies

- **Python 3** — no external dependencies, standard library only
- **CLI** — runs and is fully operated through the terminal

---

## 🗂️ Project Structure

```
02-bank-py/
├── account.py    # Account base class
├── bank.py       # Bank subclasses (Nubank, Mercado_pago, Itau, Inter, Santander)
├── main.py       # CLI menu, registration, login, and session logic
└── README.md
```

---

## ▶️ How to Run

```bash
# From the repository root
cd 02-bank-py

# Run with Python 3
python main.py
```

> Requires Python 3.8+. No external libraries needed.

---

## 💻 Example Usage

```
Menu...

    1. Login
    2. Registre
    3. Exit

    Enter Your choice: 2

Register Menu...

    Name: Gabriel
     Age: 20
    Email: gabriel@email.com
    Password: ****
    Bank:
        1. Nubank
        2. Mercado Pago
        3. Itaú
        4. Inter
        5. Santander
        6. None
        Entrer a choice for Bank: 1

Menu...

    1. Login
    2. Registre
    3. Exit

    Enter Your choice: 1

Login's Menu

    Enter a Account name: Gabriel

Account Menu...

    Entrer Your password: ****

Account Menu...

    1. Deposit
    2. Withdraw
    3. Pix
    4. Check Balance
    5. Account Info
    6. Change Accont Info
    7 Logout

    Entrer a Your choice: 1

Deposit...

   1. 10 U$
   2. 50 U$
   3. Other values

   Enter a Your Choice: 1

   You are deposited 10U$.
```

> Output reflects the current CLI wording exactly as implemented in `main.py` and `account.py`.

---

## 🚧 Future Improvements

- [ ] Fix the `withdraw()` "Other values" option (currently checks `value_deposit` before it's defined)
- [ ] Add input validation for numeric fields (age, deposit/withdraw amounts) to avoid crashes on invalid input
- [ ] Data persistence (saving accounts between sessions)
- [ ] Consolidate repeated deposit/withdraw menu logic to reduce duplication
- [ ] Introduce polymorphism (e.g. bank-specific fees or limits, instead of subclasses that only differ by name)
- [ ] Move shared account menu logic into its own module as the project grows

---

## 🎯 Learning Goals

This project builds directly on the concepts from Library Py, with a deliberate focus on **inheritance**: extending a single base class into multiple specialized subclasses that share the same structure and behavior, differing mainly in identity (which bank they belong to).

Specific goals for this project:

- Practice defining a base class and multiple subclasses with `super().__init__()`
- Understand how inheritance reduces duplication when subclasses share most of their logic
- Manage relationships between objects (Pix transfers acting on two different `Account` instances)
- Lay the groundwork for polymorphism in a future iteration, where bank subclasses could behave differently instead of only being labeled differently

---

<p align="center">
  <sub>Part of <a href="../">POO Projects Python</a> — built with 🐍 and a lot of trial and error.</sub>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:FFD43B,35:306998,100:0D1B2A&height=100&section=footer" width="100%" />
</p>
