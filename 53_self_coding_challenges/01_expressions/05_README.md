
# Division Calculator

This Python program performs integer division, provides the remainder, and also shows the result of regular (floating-point) division.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Example Output](#example-output)

## Introduction

This program takes two integers as input: a dividend and a divisor. It calculates:
- The **quotient** of integer division (without decimals).
- The **remainder** of integer division.
- The **floating-point result** of the division.

## Installation

1. Clone the repository or download the `.py` file.
2. Ensure Python is installed on your machine.
3. Run the program from the terminal:

```bash
python division_calculator.py
```

## Usage

1. Run the program.
2. Input an integer as the dividend (the number to be divided).
3. Input an integer as the divisor (the number to divide by).
4. The program displays:
   - The integer quotient and remainder.
   - The exact floating-point result of the division.

## Code Explanation

### Main Function

```python
def main():
    dividend : int = int(input("Please enter an integer to be divided: "))
    divisor : int = int(input("Please enter an integer to divide by: "))

    quotient : int = dividend // divisor
    remainder : int = dividend % divisor
    simple_divide : int = dividend / divisor
    
    print(f"The result of this division is {quotient} with a remainder of {remainder}")
    print(f"Simple division result is {simple_divide}")
```

- **dividend**: The number to be divided, input by the user.
- **divisor**: The number to divide by, also input by the user.
- **quotient**: Result of integer division (using `//`), which discards the remainder.
- **remainder**: Result of the modulo operation (`%`), which gives the remainder of the division.
- **simple_divide**: Result of regular division (`/`), returning a floating-point number.

### Program Entry Point

```python
if __name__ == '__main__':
    main()
```

This ensures the program runs `main()` only if executed directly.

## Example Output

```
Please enter an integer to be divided: 25
Please enter an integer to divide by: 4
The result of this division is 6 with a remainder of 1
Simple division result is 6.25
```

In this example, dividing 25 by 4 gives:
- Quotient: 6
- Remainder: 1
- Exact division result: 6.25

