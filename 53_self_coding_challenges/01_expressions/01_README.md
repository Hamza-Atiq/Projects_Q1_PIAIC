
# Dice Simulator

This program simulates rolling two six-sided dice. It demonstrates basic concepts like functions, loops, and random number generation using Python.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Example Output](#example-output)

## Installation

To run this code, you only need Python installed on your system. No external libraries are required since this program uses Python’s built-in `random` module.

1. Clone the repository or download the `.py` file.
2. Run the code from your terminal with:

```bash
python dice_simulator.py
```

## Usage

This script runs a simple dice simulator that rolls two dice three times and prints the results of each roll. It’s useful for understanding variable scope in functions, as well as for games or probability simulations.

## Code Explanation

### Imports

```python
import random
```

The `random` module is imported to generate random integers, simulating the rolls of a die.

### Constants

```python
NUM_SIDES = 6
```

`NUM_SIDES` is a constant representing the number of sides on each die. This can be modified to simulate dice with a different number of sides if desired.

### Functions

#### `roll_dice`

```python
def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1 : int = random.randint(1, NUM_SIDES)
    die2 : int = random.randint(1, NUM_SIDES)
    total : int = die1 + die2
    print(f'You rolled a {die1} and a {die2} for a total of {total}')
    return total
```

- **Purpose**: This function simulates the roll of two dice by generating two random numbers between 1 and `NUM_SIDES`.
- **Details**:
  - `die1` and `die2` store the result of each dice roll.
  - `total` calculates the sum of both dice, which is printed to the console.

#### `main`

```python
def main():
    """
    Program: dicesimulator
    ----------------------
    Simulates rolling two dice, three times. Prints
    the results of each die roll. This program is used
    to show how variable scope works.
    """
    for i in range(3):
        roll_dice()
```

- **Purpose**: The `main` function simulates rolling the dice three times by calling `roll_dice` in a loop.
- **Explanation**: The `for` loop iterates three times, calling `roll_dice` each time and displaying the result.

### Program Entry Point

```python
if __name__ == '__main__':
    main()
```

This section checks if the script is being run as the main module and, if so, calls `main()` to execute the dice simulation.

## Example Output

When you run the program, the output will look something like this:

```
You rolled a 3 and a 5 for a total of 8
You rolled a 2 and a 4 for a total of 6
You rolled a 1 and a 6 for a total of 7
```

Each roll displays the result of the two dice and their sum.

