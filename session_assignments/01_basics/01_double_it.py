def main():

  print('Program double the input number untill it reaches to 100 ')

  try:
    input_value : float = float(input("Enter a number: "))

    curr_value = input_value

    while curr_value < 100:
      curr_value *= 2
      print(curr_value , end= ' ')
  except ValueError:
    print('Invalid input!')

if __name__ == '__main__':
  main()