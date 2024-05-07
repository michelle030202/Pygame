# Four-Digit Number Guessing Game

This project is a four-digit number guessing game where the computer selects a secret number, and the player has to guess it. The computer provides hints to guide the player towards the correct answer. The game records and saves scores to a database.

## Features

- **Start a New Game**: The player can start a new game from the menu.
- **Enter Player Name**: Before starting, the player will be prompted to enter their name.
- **Four-Digit Number Selection**:
  - The computer will select a secret four-digit number.
  - No digit will be repeated in the secret number.
- **Guess the Number**:
  - The player will try to guess the computer's four-digit number.
  - The computer will provide feedback:
    - **+**: A digit is correct and in the same position.
    - **-**: A digit is correct but in a different position.

- **Scoring**:
  - The game will show the number of guesses required to find the correct number.
  - Scores will be saved to a database.
  - A formula will rank the best score based on the number of guesses and time taken.

## Example Gameplay

1. **Computer's Selection**: Suppose the computer selects the number `1234`.
2. **Player's Guess**: The player enters `1672`.
3. **Feedback**:
   - The computer displays `+-`.
   - **+** indicates the digit "1" is correct and in the right position.
   - **-** indicates the digit "2" is correct but in the wrong position.

## Database Integration
- The game will save player's scores and provide statistics.

## Setup and Installation
pip install -r requirements.txt
