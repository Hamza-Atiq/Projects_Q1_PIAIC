def main():
    print("Program to double the input number until it reaches or exceeds 100.")
    
    while True:
        try:
            # Prompt user for input
            input_value: float = float(input("Enter a number less than 100 (non-zero): "))

            # Validate input
            if input_value == 0:
                print("Invalid input! Please enter a non-zero number.")
                continue
            elif input_value >= 100:
                print("The number is already greater than or equal to 100. Exiting program.")
                break

            # Doubling process
            curr_value = input_value
            print(f"\nStarting value: {curr_value}")
            while curr_value < 100:
                curr_value *= 2
                print(f"Doubled value: {curr_value:.2f}")

            print("\nThe number has reached or exceeded 100.")
            break
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
