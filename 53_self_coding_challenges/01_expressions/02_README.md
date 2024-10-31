
# Mass-Energy Equivalence Calculator (E = mc²)

This program calculates the energy in joules for a given mass using Einstein's famous equation \( E = mc^2 \). It takes mass in kilograms from the user, computes the energy, and displays it in joules.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Example Output](#example-output)

## Introduction

The formula \( E = mc^2 \) states that energy \( E \) is equal to mass \( m \) multiplied by the speed of light \( c \) squared. This program implements this formula to calculate the energy for a given mass.

## Installation

No installation of external libraries is required. Just ensure Python is installed on your system.

1. Clone the repository or download the `.py` file.
2. Run the code from your terminal:

```bash
python mass_energy_calculator.py
```

## Usage

1. Run the program.
2. Enter the mass in kilograms when prompted.
3. The program will output the energy in joules.

## Code Explanation

### Constants

```python
c : int = 299792458  # The speed of light in m/s
```

- `c` is a constant representing the speed of light in meters per second (m/s). It’s used in the formula \( E = mc^2 \) for energy calculations.

### Functions

#### `main`

```python
def main():
    mass_in_kg : float = float(input("Enter kilos of mass: "))
    energy_in_joules : float = mass_in_kg * (c ** 2)

    print("e = m * C^2...")
    print(f"m = {mass_in_kg} kg")
    print(f"C = {c} m/s")
    print(f"{energy_in_joules} joules of energy!")
```

- **Purpose**: The `main` function prompts the user for mass input, calculates the energy in joules using \( E = mc^2 \), and prints the details.
- **Details**:
  - `mass_in_kg` is the mass entered by the user, converted to a float.
  - `energy_in_joules` stores the calculated energy.
  - The results are displayed to show the user the input mass, the speed of light used in the calculation, and the computed energy in joules.

### Program Entry Point

```python
if __name__ == '__main__':
    main()
```

This block checks if the script is the main module being run and, if so, calls `main()` to execute the program.

## Example Output

Upon running the program, the output will resemble:

```
Enter kilos of mass: 2
e = m * C^2...
m = 2.0 kg
C = 299792458 m/s
179751035747363520 joules of energy!
```

The program calculates the energy based on the mass entered by the user, providing an understanding of the vast amount of energy represented by even small amounts of mass.

