# 🎲 Rock Paper Scissors Game

A fun command-line Rock Paper Scissors game built with Python where you play against the computer. First to 5 wins is the Champion!

## Features

- Play against the computer
- Score tracking (You vs Computer vs Ties)
- First to 5 wins declared Champion 🏆
- Input validation (handles wrong input gracefully)
- Clean, interactive menu-driven interface
- Emoji-enhanced display for a fun experience

## Requirements

- Python 3.x (no external libraries needed)

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Rafiqua-9Sultana/Rock-paper-scissors.git
   cd Rock-paper-scissors
   ```

2. **Run the game:**
   ```bash
   python rock_paper_scissors.py
   ```

## How to Play

- Enter `1` for 🪨 Rock
- Enter `2` for 📄 Paper
- Enter `3` for ✂️ Scissors
- Enter `4` to view current score
- Enter `5` to quit

## Example Output

```
========================================
    🎲 Rock Paper Scissors Game!
========================================
  Try to beat the computer!
  First to 5 wins is the Champion! 🏆
========================================

Choose your move:
  1. 🪨  Rock
  2. 📄  Paper
  3. ✂️   Scissors
  4. 📊  View Score
  5. 🚪  Quit
----------------------------------------
Enter your choice (1-5): 1

  You chose    : Rock
  Computer chose: Scissors

  🎉 You Win this round!

--- 📊 Current Score ---
  You     : 1
  Computer: 0
  Ties    : 0
------------------------
```

## Project Structure

```
Rock-paper-scissors/
│
├── rock_paper_scissors.py   # Main game script
├── screenshot.png           # Screenshot of the game running
└── README.md                # Project documentation
```

## Pushing to GitHub

```bash
git init
git add .
git commit -m "Initial commit: Rock Paper Scissors Game"
git branch -M main
git remote add origin https://github.com/Rafiqua-9Sultana/Rock-paper-scissors.git
git push -u origin main
```

## License

This project is open-source and free to use.
