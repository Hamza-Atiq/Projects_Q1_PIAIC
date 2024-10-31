
# Feet to Inches Converter

This program converts a length measurement in feet to inches using a simple conversion factor. It prompts the user to enter a value in feet, performs the conversion, and displays the result in inches.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Example Output](#example-output)

## Introduction

The program uses the conversion factor that 1 foot equals 12 inches to convert any length in feet entered by the user into inches.

## Installation

No external libraries are needed. Make sure you have Python installed on your system.

1. Clone the repository or download the `.py` file.
2. Run the code from your terminal:

```bash
python feet_to_inches_converter.py
```

## Usage

1. Run the program.
2. Enter the length in feet when prompted.
3. The program will output the equivalent length in inches.

## Code Explanation

### Constants

```python
INCHES_IN_FOOT : int = 12  # Conversion factor. There are 12 inches for 1 foot.
```

- `INCHES_IN_FOOT` is a constant representing the number of inches in one foot. It’s used to perform the conversion.

### Functions

#### `main`

```python
def main():
    feet : float = float(input("Enter number of feet: "))
    inches : float = feet * INCHES_IN_FOOT
    print(f"That is {inches} inches!")
```

- **Purpose**: The `main` function is the primary function that performs the conversion.
- **Details**:
  - `feet` stores the user-entered length in feet, converted to a float.
  - `inches` calculates the equivalent length in inches.
  - The program then prints the result in inches.

### Program Entry Point

```python
if __name__ == '__main__':
    main()
```

This ensures that `main()` is called when the script is run directly, making it the entry point of the program.

## Example Output

```
Enter number of feet: 5
That is 60.0 inches!
```

The program calculates the equivalent measurement in inches based on the feet entered by the user.

