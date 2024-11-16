import random

def random_numbers():
    """
    Generate and return 10 random numbers between 1 and 100.
    Also, print the generated numbers in a single line.
    """
    number_list = [random.randint(1, 100) for _ in range(10)]  # Generate numbers
    print("Generated numbers:", *number_list)  # Print numbers on one line
    return number_list

# Call the function
numbers = random_numbers()
