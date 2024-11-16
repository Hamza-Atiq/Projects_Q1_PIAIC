
# Guess My Number Game with Limited Attempts

## Overview
This Python program is an interactive number-guessing game where the computer randomly selects a number between 1 and 99. The player has 5 attempts to guess the number, with hints provided after each guess to aid in their journey.

## Features
- **Random Number Generation**: A secret number is chosen randomly between 1 and 99.
- **Player Interaction**: Players input guesses and receive feedback on their accuracy.
- **Attempt Tracking**: The game allows a maximum of 5 attempts to guess the number.
- **Input Validation**: Ensures that invalid or out-of-range inputs are handled gracefully.
- **Hints**: Guides the player with "too high" or "too low" feedback after each guess.

## How It Works
1. The computer randomly selects a number between 1 and 99.
2. The player has 5 attempts to guess the number.
3. After each guess:
   - The program provides feedback:
     - *"Your guess is too high."* if the guess is greater than the secret number.
     - *"Your guess is too low."* if the guess is smaller than the secret number.
   - The number of remaining attempts is displayed.
4. If the player guesses correctly within 5 attempts, they win.
5. If the player fails to guess the number in 5 attempts, the game ends with the secret number revealed.
6. Invalid inputs (non-numeric or out-of-range) are handled without affecting the attempt count.

## Usage

### Prerequisites
- Python 3.6 or later.

### Running the Script
1. Save the program to a file, e.g., `guess_my_number_with_attempts.py`.
2. Open a terminal or command prompt.
3. Run the program using:

   ```bash
   python guess_my_number_with_attempts.py
   ```

4. Follow the instructions to play the game.

## Example

### Gameplay
```plaintext
I am thinking of a number between 1 and 99...
Attempts left: 5
Enter a guess between 1 and 99: 50
Your guess is too high.
Attempts left: 4
Enter a guess between 1 and 99: 25
Your guess is too low.
Attempts left: 3
Enter a guess between 1 and 99: 37
Congrats! You guessed it! The number was: 37
```

### Game Over
```plaintext
I am thinking of a number between 1 and 99...
Attempts left: 5
Enter a guess between 1 and 99: 80
Your guess is too high.
Attempts left: 4
Enter a guess between 1 and 99: 10
Your guess is too low.
Attempts left: 3
Enter a guess between 1 and 99: 70
Your guess is too high.
Attempts left: 2
Enter a guess between 1 and 99: 65
Your guess is too high.
Attempts left: 1
Enter a guess between 1 and 99: 50
Your guess is too low.
Game Over! You've used all 5 attempts. The number was: 55.
```

### Invalid Input
```plaintext
I am thinking of a number between 1 and 99...
Attempts left: 5
Enter a guess between 1 and 99: abc
Invalid input. Please enter a valid integer.
Attempts left: 5
Enter a guess between 1 and 99: 150
Please enter a number within the range (1-99).
```

## Code Explanation

### Main Features
1. **Random Number Generation**: 
   - Uses `random.randint(1, 99)` to ensure a fair random selection of the secret number.
2. **Attempt Limitation**:
   - Tracks the user's attempts with `user_attempts` and ends the game after 5 incorrect guesses.
3. **Input Handling**:
   - Validates that the input is numeric and within the specified range.
4. **Feedback Mechanism**:
   - Provides hints (too high, too low) to guide the player.
5. **Game Over Condition**:
   - Concludes the game if the maximum attempts are reached.

