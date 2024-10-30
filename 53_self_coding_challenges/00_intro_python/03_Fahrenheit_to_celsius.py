def main():

  print('Program tells temperature in celsius')

  try:

    temperature_in_farenheit : int = float(input('Please enter temperature in farenheit ? '))

    temperature_in_celsius : int = (temperature_in_farenheit - 32) * 5/9

    print(f'Temperature in farenheit is {temperature_in_farenheit}F')
    print(f'Temperature in celsius is {temperature_in_celsius}C')
  except ValueError:
    print('Invalid input!')

if __name__ == '__main__':
  main()