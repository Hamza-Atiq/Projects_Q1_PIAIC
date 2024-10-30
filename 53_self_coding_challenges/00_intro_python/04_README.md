
# Friends' Ages Program

This repository contains a Python program that calculates and displays the ages of five friends based on predefined relationships among their ages. This program is ideal for those learning about basic variables, simple arithmetic operations, and string formatting in Python.

## Table of Contents
1. [Introduction](#introduction)
2. [Program Overview](#program-overview)
3. [Example Usage](#example-usage)
4. [How to Run the Program](#how-to-run-the-program)

---

### Introduction

This program defines the ages of five friends—Anton, Beth, Chen, Drew, and Ethan—using simple arithmetic relationships between them. It outputs the ages of each friend based on these predefined calculations, making it a fun example for learning about variable assignment and output formatting in Python.

### Program Overview

The program follows these steps:
1. **Prints the purpose of the program** – Introduces the task to the user.
2. **Defines ages** – Calculates the ages of each friend based on simple arithmetic relationships:
   - Anton’s age is predefined.
   - Beth’s age is six years older than Anton’s.
   - Chen’s age is twenty years older than Beth’s.
   - Drew’s age is the sum of Chen and Anton’s ages.
   - Ethan’s age is the same as Chen’s.
3. **Displays each age** – Prints the calculated age for each friend.

### Code Explanation

Below is a breakdown of the code:

```python
def main():
    print('Program tells the age of 5 friends')

    anton : int = 21
    beth : int = 6 + anton
    chen : int = 20 + beth
    drew : int = chen + anton
    ethan : int = chen

    print(f"Anton is {anton}")
    print(f"Beth is {beth}")
    print(f"Chen is {chen}")
    print(f"Drew is {drew}")
    print(f"Ethan is {ethan}")

if __name__ == '__main__':
    main()
```

- **Variable Declarations** – Each friend’s age is calculated based on the relationships among their ages.
- **Formatted Output** – Displays each friend’s name and age using `print()` with f-string formatting.

### Example Usage

Here’s what the program looks like when run:

```
Program tells the age of 5 friends
Anton is 21
Beth is 27
Chen is 47
Drew is 68
Ethan is 47
```

### How to Run the Program

1. Make sure Python is installed (verify by typing `python --version` in your terminal).
2. Clone or download this repository.
3. Open a terminal in the directory containing the program.
4. Run the program with:
   ```bash
   python filename.py
   ```
   Replace `filename.py` with the actual name of the script.

This simple program is a great exercise for learning basic arithmetic and variables in Python.

