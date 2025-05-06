import random

def set_difficulty():
  print('Please select a difficulty by choosing from the following options:\n' +
  '(Easy): 1-10, 3 guesses\n' + '(Medium): 1-50 4 guesses\n' + '(Hard): 1-100 5 guesses')
  difficulty = input('Type(easy/medium/hard)')
  print(f'You chose {difficulty}')
  return difficulty


set_difficulty()