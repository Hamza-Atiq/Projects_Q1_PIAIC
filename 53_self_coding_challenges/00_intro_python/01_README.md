# Python Addition Program

This repository contains a simple Python program that prompts the user to input two numbers, adds them together, and displays the result. This program demonstrates basic Python concepts, including user input, exception handling, and formatted output.

## Table of Contents
1. [Introduction](#introduction)
2. [Program Overview](#program-overview)
3. [Example Usage](#example-usage)
4. [Error Handling](#error-handling)
5. [How to Run the Program](#how-to-run-the-program)

---

### Introduction

This program is designed for beginners who are learning Python basics. It guides users through:
- Reading user input
- Converting data types
- Adding two integers
- Displaying output with formatted strings
- Handling errors with a `try-except` block

### Program Overview

The program defines a function called `main()`, which:
1. **Introduces the program’s purpose** – printing a message to inform the user about the operation (adding two numbers).
2. **Prompts for input** – requests two numbers from the user, which are then converted from strings to integers.
3. **Performs addition** – calculates the sum of the two numbers and displays it in a formatted message.
4. **Handles errors** – checks if the input is valid, displaying an error message if non-integer values are entered.

### Code Explanation

Here’s a summary of each section of the code to understand how it works:

```python
def main():
    print('This program adds two numbers.')
    try:
        first_number = int(input('Enter the First Number: '))
        second_number = int(input('Enter the Second Number: '))
        total_sum = first_number + second_number
        print(f'The Sum of {first_number} and {second_number} is {total_sum}')
    except ValueError:
        print("Invalid input! Please enter valid integers.")
        
if __name__ == '__main__':
    main()
```

- **`print()` Statement** – Displays a welcoming message.
- **`input()` Function** – Collects two numbers from the user.
- **`int()` Conversion** – Converts input from string to integer for numerical addition.
- **`try-except` Block** – Handles invalid inputs. If a user enters non-integer data, a `ValueError` is caught, and an error message is shown.

### Example Usage

When run, the program will look like this:

#### Correct Input:
```
This program adds two numbers.
Enter the First Number: 5
Enter the Second Number: 7
The Sum of 5 and 7 is 12
```

#### Invalid Input:
```
This program adds two numbers.
Enter the First Number: five
Invalid input! Please enter valid integers.
```

### Error Handling

The program is designed to catch `ValueError` exceptions if the user inputs anything other than an integer. This feature is especially helpful for new learners who might not always enter the correct data type.

### How to Run the Program

1. Make sure you have Python installed. You can check by running `python --version` in your terminal.
2. Clone or download this repository.
3. Open a terminal or command prompt in the program’s directory.
4. Run the program using the command:
   ```bash
   python filename.py
   ```
   Replace `filename.py` with the actual file name of the script.

This addition program is an ideal first project for anyone beginning with Python! It combines essential coding practices with user-friendly interaction and error management.
