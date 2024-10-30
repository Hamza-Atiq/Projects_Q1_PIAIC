def main():
    print('This program adds two numbers.')
    try:
        first_number : str = input('Enter the First Number: ')
        first_number : int = int(first_number)
        second_number : str = input('Enter the Second Number: ')
        second_number : int = int(second_number)

        total_sum: int = first_number + second_number

        print(f'The Sum of {first_number} and {second_number} is {total_sum}')
    except ValueError:
        print("Invalid input! Please enter valid integers.")

if __name__ == '__main__':
    main()
