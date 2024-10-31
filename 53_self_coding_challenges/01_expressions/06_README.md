
# Dice Roll Simulator

This Python program simulates the rolling of two dice, each with a configurable number of sides. It generates random numbers for each die roll and prints the results along with their total.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Example Output](#example-output)

## Introduction

The Dice Roll Simulator program rolls two dice with a specified number of sides (default is 6). Each die's result is displayed, as well as the combined total of the two dice.

## Installation

1. Clone the repository or download the `.py` file.
2. Ensure Python is installed on your machine.
3. Run the program from the terminal:

```bash
python dice_roll_simulator.py
```

## Usage

1. Run the program.
2. Each time you run it, it simulates a roll of two dice with a default of six sides each.
3. The program displays the number of sides, the result of each die, and their combined total.

## Code Explanation

### Main Function

```python
import random

num_sides_of_die : int = 6  # Number of sides on each die

def main():
    die1 : int = random.randint(1 , num_sides_of_die)  # Roll first die
    die2 : int = random.randint(1 , num_sides_of_die)  # Roll second die
    total_sum : int = die1 + die2  # Calculate the sum of both dice

    # Print out the results
    print(f"Dice have {num_sides_of_die} sides each.")
    print(f"First die : {die1}")
    print(f"Second die : {die2}")
    print(f"Total of two dice : {total_sum}")
```

- **num_sides_of_die**: Number of sides on each die. Default value is 6.
- **die1** and **die2**: Results of the random roll for each die, generated using `random.randint(1, num_sides_of_die)`.
- **total_sum**: Sum of `die1` and `die2`.

### Program Entry Point

```python
if __name__ == '__main__':
    main()
```

This ensures that `main()` runs only when the script is executed directly.

## Example Output

When the program runs, you may see output similar to the following:

```
Dice have 6 sides each.
First die : 4
Second die : 2
Total of two dice : 6
```

Each execution of the program rolls the dice again, so the numbers for `First die`, `Second die`, and `Total` vary each time.

