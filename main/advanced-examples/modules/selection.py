from random import randint

def choose_by_letter(animal_list, letter):
  return list(filter(lambda item: item['letter'] == letter, animal_list))

def childrens_book(animal_list):
  animal = animal_list[randint(0, len(animal_list))]
  letter = animal['letter']
  animal_name = animal['animal']
  print(f'{letter.upper()} is for {animal_name}!')
