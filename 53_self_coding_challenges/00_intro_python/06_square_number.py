def main():

  print('Program calculate square of the number ')

  try:
    number : float = float(input('Enter the number to see its square : '))

    square : float = number * number

    print(f'The square of {number} is {square}')
  except ValueError:
    print('Invalid input!')

if __name__ == '__main__':
  main()
