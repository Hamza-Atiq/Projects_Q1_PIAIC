
# Joke Bot

## Overview
**Joke Bot** is a simple Python script designed to deliver humor! The bot interacts with users through text input and responds with a joke if prompted. It’s a lightweight and fun way to lighten up your day.

## Features
- **Interactive Input:** Users can type commands to interact with the bot.
- **Humorous Response:** The bot tells a joke when prompted with the word `joke`.
- **Error Handling:** The bot gracefully handles unexpected input and responds appropriately.

## Usage

### Prerequisites
- Python 3.7 or later installed on your system.

### Running the Script
1. Clone or download the repository containing the `joke_bot.py` file.
2. Open a terminal or command prompt and navigate to the folder where the script is saved.
3. Run the script using the command:

   ```bash
   python joke_bot.py
   ```

4. Interact with the bot by entering a command. 
   - Type `joke` to hear a joke.
   - Type anything else to receive an apology message.

### Example
```plaintext
What do you want? joke
Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. 
A programmer tells her: get a liter of milk, and if they have eggs, get 12. 
Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 
"because they had eggs."

What do you want? hello
Sorry, I only tell jokes.
```

## Code Explanation

### Variables
- `Prompt`: Text to prompt the user for input.
- `Joke`: The joke text that is displayed when the user types `joke`.
- `Sorry`: A polite apology displayed for any input other than `joke`.

### Functionality
- **`joke_bot()`**:
  - Reads user input.
  - Checks if the input is `joke` and responds with humor.
  - Responds with an apology for other inputs.
- **Error Handling**:
  - A `try-except` block catches and handles invalid inputs gracefully.

### Script Entry Point
The script uses `if __name__ == '__main__':` to ensure the `joke_bot` function is executed only when the file is run directly, not imported as a module.

