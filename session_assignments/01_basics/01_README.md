
# Doubling Program

## Overview
This Python program accepts a number as input and repeatedly doubles it until the value reaches or exceeds 100. The program is interactive and includes input validation to handle errors gracefully.

## Features
- **Interactive Input**: Allows users to input a starting value.
- **Doubling Logic**: Repeatedly doubles the number and displays intermediate values.
- **Input Validation**: Handles invalid or zero inputs and terminates if the initial input is 100 or more.

## Usage

### Prerequisites
- Python 3.7 or later.

### Running the Script
1. Save the program in a file, e.g., `doubling_program.py`.
2. Open a terminal or command prompt.
3. Run the program using:

   ```bash
   python doubling_program.py
   ```

4. Follow the prompts to input a number.

### Example

#### Valid Input:
```plaintext
Program to double the input number until it reaches or exceeds 100.
Enter a number less than 100 (non-zero): 3

Starting value: 3.0
Doubled value: 6.00
Doubled value: 12.00
Doubled value: 24.00
Doubled value: 48.00
Doubled value: 96.00
Doubled value: 192.00

The number has reached or exceeded 100.
```

#### Edge Case Input:
```plaintext
Program to double the input number until it reaches or exceeds 100.
Enter a number less than 100 (non-zero): 150
The number is already greater than or equal to 100. Exiting program.
```

#### Invalid Input:
```plaintext
Program to double the input number until it reaches or exceeds 100.
Enter a number less than 100 (non-zero): abc
Invalid input! Please enter a valid number.

Enter a number less than 100 (non-zero): 0
Invalid input! Please enter a non-zero number.
```

## Code Explanation

### Main Function
- **Input Prompt**: Prompts the user for a number less than 100.
- **Validation**: Checks if the input is:
  1. A valid number.
  2. Non-zero.
  3. Less than 100.
- **Doubling Loop**: Repeatedly doubles the number and prints the intermediate values.
- **Exit Conditions**: Stops doubling when the number is 100 or more or if the input is invalid.

### Logic Flow
1. **Input Handling**:
   - Ensures the user provides a valid number.
   - Handles cases where input is 0 or 100+.
2. **Doubling Process**:
   - Uses a `while` loop to double the number until it reaches/exceeds 100.
3. **Error Handling**:
   - Catches invalid inputs (non-numeric or zero).

