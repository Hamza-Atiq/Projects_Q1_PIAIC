# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total

    """

    die1 : int = random.randint(1, NUM_SIDES)
    die2 : int = random.randint(1, NUM_SIDES)

    total : int = die1 + die2
    print(f'You rolled a {die1} and a {die2} for a total of {total}')
    return total

def main():
  """
  Program: dicesimulator
  ----------------------
  Simulate rolling two dice, three times.  Prints
  the results of each die roll.  This program is used
  to show how variable scope works.
  """
  for i in range(3):
    roll_dice()

if __name__ == '__main__':
  main()