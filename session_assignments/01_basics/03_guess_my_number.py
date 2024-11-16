import random

def guess_my_number():
    """
    A number guessing game where the user has 5 attempts to guess a random number between 1 and 99.
    """
    secret_number: int = random.randint(1, 99)  # Random number between 1 and 99
    print("I am thinking of a number between 1 and 99...")
    
    attempts_allowed: int = 5  # Maximum attempts
    user_attempts: int = 0     # Tracks the user's attempts
    
    while user_attempts < attempts_allowed:
        try:
            # Remaining attempts
            attempts_left = attempts_allowed - user_attempts
            print(f"Attempts left: {attempts_left}")

            # User input
            user_number: int = int(input("Enter a guess between 1 and 99: "))

            # Validate input range
            if user_number < 1 or user_number > 99:
                print("Please enter a number within the range (1-99).")
                continue

            # Check user's guess
            if user_number > secret_number:
                print("Your guess is too high.")
            elif user_number < secret_number:
                print("Your guess is too low.")
            else:
                print(f"🎉 Congrats! You guessed it! The number was: {secret_number}")
                break

            user_attempts += 1  # Increment attempts
            
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    # Game over condition
    if user_attempts == attempts_allowed:
        print(f"Game Over! You've used all {attempts_allowed} attempts. The number was: {secret_number}.")

# Call the function
if __name__ == "__main__":
    guess_my_number()
