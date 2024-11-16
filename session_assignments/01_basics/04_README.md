
# Random Numbers Generator

## Overview
This Python program generates 10 random numbers within the range of 1 to 100. It displays the numbers in a single line for easy viewing and also returns the list for further use or processing.

## Features
- **Random Number Generation**: Uses Python's `random.randint()` to generate random numbers.
- **Output Formatting**: Displays all generated numbers on a single line for readability.
- **Reusable Functionality**: The program's main function can be imported and reused in other scripts.

## How It Works
1. The program uses the `random` module to generate 10 random integers.
2. The numbers are generated within the range of 1 to 100.
3. The generated numbers are printed in a single line, separated by spaces.
4. The list of generated numbers is also returned by the function, allowing it to be used programmatically.

## Usage

### Prerequisites
- Python 3.6 or later.

### Running the Script
1. Save the program to a file, e.g., `random_numbers.py`.
2. Open a terminal or command prompt.
3. Run the program using:

   ```bash
   python random_numbers.py
   ```

4. The program will generate and print 10 random numbers.

## Example Output
```plaintext
Generated numbers: 12 56 78 34 99 45 67 23 89 10
```

## Code Explanation

### Function: `random_numbers`
- **Purpose**: 
  - Generates a list of 10 random numbers.
  - Prints the numbers in a single line for convenience.
  - Returns the list of numbers for further use.
  
- **Implementation**:
  - Uses a list comprehension: `[random.randint(1, 100) for _ in range(10)]` to generate random integers efficiently.
  - The `print()` function with the unpacking operator (`*`) ensures numbers are displayed in a clean, space-separated format.

### Customization
- **Change Range**: Adjust the range of random numbers by modifying the arguments of `random.randint()` (e.g., `random.randint(10, 50)` for numbers between 10 and 50).
- **Change Quantity**: Modify the `range()` argument in the list comprehension to generate more or fewer numbers.
- **Output Formatting**: Change the `print()` statement to format the output differently (e.g., comma-separated).

## Reusability
This function can be imported into other scripts:
```python
from random_numbers import random_numbers

numbers = random_numbers()
print(f"Numbers for further use: {numbers}")
```

