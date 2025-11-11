# Hangman CLI Game

A colorful, terminal-based Hangman game written in Python.
Built as a final project for **CS50’s Introduction to Programming with Python.**



## 🧩 Features

- Interactive and easy-to-play command-line interface.
- Three difficulty levels (`Easy`, `Medium`, `Hard`) with different lives.
- Color-coded messages using **Colorama**.
- “Play Again” option after each game.
- Clean and modular code with **pytest** unit tests.



## 🚀 Getting Started

### 1️. Clone this repository
```bash
git clone https://github.com/cardonajsebas/hangman_game.git
cd hangman_game
```
### 2️. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```
### 3️. Install dependencies
```bash
pip install -r requirements.txt
```

### 4️. Run the game
```bash
python project.py
```

## 🧪 Running Tests

Run all tests using pytest:
```bash
pytest -v
```


## Project Structure
```bash
hangman/
│
├── project.py          # Main game logic
├── pics.py             # ASCII art and hangman pictures
├── test_project.py     # Unit tests using pytest
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```


## 🎮 Example Gameplay
```bash
=== Select Difficulty ===
1 -> Easy
2 -> Medium
3 -> Hard
0 -> Exit

Select 1, 2 or 3 (0 to Exit)
2

You selected: Medium.
The word has 6 characters.
_ _ _ _ _ _

Guess a letter:
> p
That's right! The letter 'P' is in the word.
```

## Notes

Works on Windows, macOS, and Linux.

Built with Python 3.13.

Uses Colorama for cross-platform color support.


## Author

John Sebastian Cardona

*Data Analyst & Python Developer*

