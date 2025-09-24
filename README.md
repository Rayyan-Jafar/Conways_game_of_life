# Conway’s Game of Life – Python (Console Version)

This project is a simple **Python console implementation** of **Conway’s Game of Life Automata**.
It simulates a 5×5 grid of cells that evolve across generations based on predefined rules.

---

## 📜 Rules of the Game

1. A cell with **exactly 2 neighbors** remains in its current state.
2. A cell with **more than 2 neighbors** becomes alive.
3. A cell with **less than 2 neighbors** dies.
4. ⚪ = Alive cell
5. ⚫ = Dead cell

---

## ▶️ How It Works

* The game starts with a **randomly generated 5×5 pattern** of alive (⚪) and dead (⚫) cells.
* On each step (generation), the cells are updated based on the rules above.
* The program continues until the pattern **stabilizes** (no further changes).
* Users press **ENTER** to move from one generation to the next.

---

## 📂 Project Structure

```
conways_game.py    # Main script containing the logic
```

---

## 🚀 Usage

1. Clone or download this repository.
2. Run the script in a terminal:

```bash
python conways_game.py
```

3. Read the instructions shown in the console.
4. Press **ENTER** to generate the next pattern.

---

## 🖼️ Example Output

```
~~~~~~~~~~~~~~~~~~~~~~CONWAYS GAME AUTOMATA~~~~~~~~~~~~~~~~~~~~~~
⬇ INSTRUCTIONS ⬇

1 : Cell having 2 neighbours remains same.
2 : Cell having more than 2 neighbours become alive.
3 : Cell having less than 2 neighbours become dead.
4 : ⚪ = Alive cell.
5 : ⚫ = Dead cell.

1️⃣ pattern...

['⚪', '⚫', '⚫', '⚪', '⚫']
['⚫', '⚫', '⚪', '⚪', '⚪']
['⚪', '⚫', '⚫', '⚪', '⚫']
['⚪', '⚫', '⚪', '⚫', '⚫']
['⚪', '⚪', '⚫', '⚫', '⚫']

Press ENTER → evolves to next pattern...
```

---
