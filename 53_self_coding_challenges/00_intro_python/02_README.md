
# Favorite Animal Program

This repository contains a simple Python program that prompts the user to input their favorite animal and then displays a message confirming the chosen animal. This program is a basic example of how to handle user input and format output in Python.

## Table of Contents
1. [Introduction](#introduction)
2. [Program Overview](#program-overview)
3. [Example Usage](#example-usage)
4. [Error Handling](#error-handling)
5. [How to Run the Program](#how-to-run-the-program)

---

### Introduction

This program is designed as an introductory exercise for beginners to get familiar with:
- Working with string inputs
- Using formatted output to create a personalized message
- Simple error handling with a `try-except` block

### Program Overview

The program’s main function, `main()`, does the following:
1. **Introduces the program’s purpose** – displaying a message to inform the user about the task.
2. **Prompts the user** – requests the user’s favorite animal as input.
3. **Displays a personalized message** – repeats the user’s input back in a formatted sentence to confirm their choice.
4. **Handles errors** – uses a `try-except` block to catch any potential `ValueError` exceptions (although this scenario is rare here).

### Code Explanation

Below is a brief breakdown of each part of the code for better understanding:

```python
def main():
    print('Program about Favourite animal')

    try:
        animal_name = input('Please enter your favourite animal? ')
        print(f'My favourite animal is also {animal_name}')
    except ValueError:
        print("Invalid input!")
        
if __name__ == '__main__':
    main()
```

- **`print()` Statement** – Displays a welcoming message to introduce the program.
- **`input()` Function** – Prompts the user to enter their favorite animal.
- **Formatted `print()` Statement** – Shows a personalized message with the user's input.
- **`try-except` Block** – Handles potential errors (though in this case, invalid input is rare).

### Example Usage

When run, the program will look like this:

#### Example Input and Output:
```
Program about Favourite animal
Please enter your favourite animal? Tiger
My favourite animal is also Tiger
```

### Error Handling

Although unlikely to be triggered in this program, the `try-except` block is included to show how to handle possible input errors.

### How to Run the Program

1. Make sure you have Python installed on your computer (you can check by running `python --version` in your terminal).
2. Clone or download this repository.
3. Open a terminal or command prompt in the directory of the program.
4. Run the program by entering:
   ```bash
   python filename.py
   ```
   Replace `filename.py` with the name of this script.

This program is a great starting point for beginners to learn about user interaction in Python, error handling, and formatted output!
