# ✊ Rock-Paper-Scissors Player Function

## 📖 Overview
This project implements a function called `player` in the file `RPS.py` to play the game of Rock-Paper-Scissors. The function is designed to respond strategically to the opponent's last move, enhancing the gameplay experience. The function takes a string input representing the opponent's last move and returns the next move to play.

## 🎮 Game Rules
Rock-Paper-Scissors is a simple hand game usually played between two people. Each player simultaneously forms one of three shapes with their hand:
- Rock (R) crushes Scissors (S)
- Scissors (S) cuts Paper (P)
- Paper (P) covers Rock (R)

The objective is to choose a move that defeats the opponent's move.

## 🔑 Key Features
- **Dynamic Response:** The `player` function analyzes the opponent's last move to determine the best counter-move.
- **First Move Handling:** The function can handle the first game scenario by accepting an empty string as input, indicating no previous play.

## 💻 Installation
To run this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/hbr-dev/RPS.git
   cd rps-player
2. Ensure you have Python installed on your machine. This project is compatible with Python 3.x.

## 🛠️ Usage

To use the player function, follow these steps:

1. Open the RPS.py file.

2. Call the player function with the opponent's last move as an argument:

  ````python
  from RPS import player
  
  next_move = player("R")  # Example: Opponent played Rock
  print(next_move)  # This will print the next move
  ```

3. For the first game, call the function with an empty string:
  ```python
  first_move = player("")  # No previous play
  print(first_move)  # This will print the initial move
  ```
