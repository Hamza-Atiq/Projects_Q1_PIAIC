def main():
  print('Program about Favourite animal')
  try:
    animal_name = str = input('Please enter your favourite animal ? ')

    print(f'My favourite animal is also {animal_name}')
  except ValueError:
    print('Invalid input!')

if __name__ == '__main__':
  main()