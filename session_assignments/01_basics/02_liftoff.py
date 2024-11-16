def main():

  try:
    
    print('Program count the numbers in reverse order and then ask lift of')
    input_value : int = int(input("Enter a number : "))

    for i in range(input_value, 0, -1):
      print(i , end = " " )

    print("Lift off!")

  except ValueError:
    print('Invalid input!')

if __name__ == '__main__':
  main()