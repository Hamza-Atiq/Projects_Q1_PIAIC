def main():

  print('Program calculate the perimeter of traingle')

  try:
    side1 : float = float(input('Enter the first side1 : '))
    side2 : float = float(input('Enter the second side2 : '))
    side3 : float = float(input('Enter the third side3 : '))

    perimeter = side1 + side2 + side3

    print(f'The perimeter of traingle is {perimeter}')
  except ValueError:
    print('Invalid input!')

if __name__ == '__main__':
  main()