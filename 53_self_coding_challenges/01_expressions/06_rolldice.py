import random

num_sides_of_die : int = 6 
def main():

    die1 : int = random.randint(1 , num_sides_of_die)
    die2 : int = random.randint(1 , num_sides_of_die)

    total_sum : int = die1 + die2

    # Print out the results
    print(f"Dice have {num_sides_of_die} sides each.")
    print(f"First die : {die1}")
    print(f"Second die : {die2}")
    print(f"Total of two dice : {total_sum}")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
     