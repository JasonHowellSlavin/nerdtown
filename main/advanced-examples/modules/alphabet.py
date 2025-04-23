from data import animal_list
from pprint import pprint as pretty
import selection

animals_with_q = selection.choose_by_letter(animal_list, 'a')
pretty(animals_with_q)

selection.childrens_book(animal_list)