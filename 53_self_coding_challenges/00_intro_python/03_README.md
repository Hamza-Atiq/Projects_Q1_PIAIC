
# Temperature Converter Program

This repository contains a Python program that converts temperature from Fahrenheit to Celsius. This program is ideal for beginners looking to learn more about handling user inputs, performing calculations, and displaying results in Python.

## Table of Contents
1. [Introduction](#introduction)
2. [Program Overview](#program-overview)
3. [Example Usage](#example-usage)
4. [Error Handling](#error-handling)
5. [How to Run the Program](#how-to-run-the-program)

---

### Introduction

This Temperature Converter program allows users to input a temperature in Fahrenheit and receive the equivalent temperature in Celsius. It demonstrates:
- Basic arithmetic operations
- Formatting output to include both Celsius and Fahrenheit values
- Basic error handling for invalid input

### Program Overview

The `main()` function in the code does the following:
1. **Introduces the program’s purpose** – informs the user about the task.
2. **Requests input** – prompts the user to input a temperature in Fahrenheit.
3. **Performs calculation** – converts the temperature from Fahrenheit to Celsius.
4. **Displays the result** – shows the temperature in both Fahrenheit and Celsius for clarity.
5. **Handles errors** – includes a `try-except` block to catch any `ValueError` in case the user enters non-numeric input.

### Code Explanation

Below is a breakdown of each part of the code for clarity:

```python
def main():
    print('Program tells temperature in celsius')

    try:
        temperature_in_farenheit : float = float(input('Please enter temperature in Fahrenheit: '))
        temperature_in_celsius : float = (temperature_in_farenheit - 32) * 5/9

        print(f'Temperature in Fahrenheit is {temperature_in_farenheit}F')
        print(f'Temperature in Celsius is {temperature_in_celsius}C')
    except ValueError:
        print("Invalid input!")
        
if __name__ == '__main__':
    main()
```

- **`print()` Statement** – Displays a message to introduce the program.
- **`input()` Function** – Prompts the user to enter a temperature in Fahrenheit.
- **Calculation** – Uses the formula `(Fahrenheit - 32) * 5/9` to convert to Celsius.
- **Formatted `print()` Statements** – Shows both Fahrenheit and Celsius temperatures.
- **`try-except` Block** – Handles any `ValueError` if the input is non-numeric.

### Example Usage

Here’s what the program looks like in action:

#### Example Input and Output:
```
Program tells temperature in celsius
Please enter temperature in Fahrenheit: 98.6
Temperature in Fahrenheit is 98.6F
Temperature in Celsius is 37.0C
```

### Error Handling

The program includes a `try-except` block to handle invalid input gracefully. If a user enters something other than a number, the program will print `Invalid input!`.

### How to Run the Program

1. Ensure Python is installed (you can check with `python --version` in your terminal).
2. Clone or download this repository.
3. Open a terminal in the directory containing the program.
4. Run the program by typing:
   ```bash
   python filename.py
   ```
   Replace `filename.py` with the actual name of the script.

This simple program is a helpful tool for temperature conversion and a great project for beginner programmers to learn core concepts in Python.
