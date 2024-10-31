
# Pythagorean Theorem Calculator

This Python program calculates the length of the hypotenuse (side BC) in a right triangle given the lengths of the other two sides (AB and AC) using the Pythagorean theorem.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Example Output](#example-output)

## Introduction

The program applies the Pythagorean theorem:

\[
BC = \sqrt{AB^2 + AC^2}
\]

where:
- **AB** and **AC** are the lengths of the two sides of the right triangle.
- **BC** is the length of the hypotenuse, calculated using the square root function from Python's `math` library.

## Installation

1. Clone the repository or download the `.py` file.
2. Make sure Python is installed on your machine.
3. Run the code from the terminal:

```bash
python pythagorean_calculator.py
```

## Usage

1. Run the program.
2. Enter the lengths of the two sides, **AB** and **AC**, when prompted.
3. The program will calculate and display the length of the hypotenuse, **BC**.

## Code Explanation

### Importing the `math` Library

```python
import math  # Import the math library so we can use the sqrt function
```

The `math` library provides mathematical functions, including `sqrt`, which calculates the square root of a given number.

### Main Function

```python
def main():
    ab : float = float(input("Enter the length of AB : "))
    ac : float = float(input("Enter the length of AC : "))

    bc : float = math.sqrt(ab**2 + ac**2)
    print(f"The length of BC (the hypotenuse) is : {bc}")
```

- **Purpose**: `main` function gathers user input for the side lengths **AB** and **AC**, performs the Pythagorean theorem calculation, and prints the hypotenuse.
- **Details**:
  - `ab` and `ac`: The lengths of sides AB and AC entered by the user, converted to `float` for accurate calculations.
  - `bc`: Calculates the hypotenuse using `math.sqrt(ab**2 + ac**2)`.

### Program Entry Point

```python
if __name__ == '__main__':
    main()
```

This ensures that `main()` is called only when the script is run directly.

## Example Output

```
Enter the length of AB : 3
Enter the length of AC : 4
The length of BC (the hypotenuse) is : 5.0
```

Here, the program calculates the hypotenuse based on the lengths 3 and 4, producing an output of 5, consistent with the Pythagorean theorem.

