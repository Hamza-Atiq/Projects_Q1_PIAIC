
# Double Until 100 Program

## Overview
This Python program takes a numerical input from the user and repeatedly doubles the value until it reaches or exceeds 100. The script is simple and interactive, making it a great introduction to loops and input handling in Python.

## Features
- **Interactive Input:** Users can input any number.
- **Doubling Logic:** The program doubles the input and prints each intermediate value.
- **Error Handling:** Handles invalid input gracefully with a descriptive message.

## Usage

### Prerequisites
- Python 3.7 or later installed on your system.

### Running the Script
1. Save the program in a file named `double_until_100.py`.
2. Open a terminal or command prompt and navigate to the folder where the script is saved.
3. Run the script using the command:

   ```bash
   python double_until_100.py
   ```

4. Follow the on-screen instructions.

### Example
```plaintext
Program doubles the input number until it reaches 100.
Enter a number: 12
24.0
48.0
96.0
192.0
```

If an invalid input is provided:
```plaintext
Program doubles the input number until it reaches 100.
Enter a number: abc
Invalid input!
```

## Code Explanation

### Main Function
- The `main()` function serves as the entry point for the script.
- It prompts the user to enter a number, reads the input, and checks if it is valid.
- If valid:
  - The input is doubled repeatedly using a `while` loop.
  - Each intermediate value is displayed until it reaches or exceeds 100.
- If invalid:
  - A `ValueError` exception is caught, and a message is displayed.

### Logic Flow
1. **Input Validation**:
   - Ensures that only numerical inputs are accepted.
2. **Doubling Logic**:
   - Uses a `while` loop to multiply the current value by 2 until it meets the condition.
3. **Output**:
   - Prints the intermediate results of each doubling step.
