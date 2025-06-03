import random

# Takes a list that likely has a large first int, divides and adds quotiant to list and returns list +
def normalize_outlier(arr):
  if not arr:
    return []
    
  remainder = arr.pop(0)
  quotient = int(remainder / len(arr))
  reduction_factor = 1.25

  # using a reduction factor to minimize the amount of addition to make a more normalized sum
  mapped_list = [n + int(quotient / reduction_factor) for n in arr]
  difference = 100 - sum(mapped_list)
  mapped_list.insert(0, difference)
  return mapped_list

# returns a list with an array of percentages and a message
# will seek to normalize percentages, but the change of an outlier is fairly high
def precentage_array(entries=4, minimum=1):
  if entries <= 0:
    return {"percentages": [], "message": "Invalid number of entries"}
    
  percentages = []
  available_percentage = 100
  min = minimum
  ent = entries
  message = ''
  exceeds_percent_toal = entries * minimum > available_percentage - (ent * min) < min

  if (exceeds_percent_toal):
    min = 1
    message = 'Enteries and minimum exceeded percentage allocation, returning new max and min'

  for i in range(0, entries):
    # ensure we don't try to add something in a negative range
    if(available_percentage == 0):
      percentages.insert(0, 0)
      continue
    
    # make sure we insert whatever else is left at the last to get 100%
    if(i == entries - 1):
      percentages.insert(0, available_percentage)
      continue

    if(min > available_percentage or available_percentage - (ent * min) < min): 
      percentages.insert(0, available_percentage)
      min = 0
      available_percentage = 0
      continue

    percentage = random.randint(min, available_percentage - (ent * min))
    percentages.insert(0, percentage)
    available_percentage = available_percentage - percentage
    ent -= 1

  if (exceeds_percent_toal):
    percentages = normalize_outlier(percentages)

  return {"percentages": percentages, "message": message}

# TESTING CODE BELOW

# per1 = precentage_array(10, 44)
# print(per1, sum(per1['percentages']))


# for i in range(0, 2000):
#   per2 = precentage_array(8, 22)

#   if (sum(per2) != 100):
#     print(f'Not 100, {sum(per2)}, {per2}')

# Use Case: 
""" 
Create a demographic for the tavern
"""
character_species = ['Dwarf', 'Elf', 'Halfling', 'Human', 'Gnome']

# For good distributions, you want a larger minimum or a minumim ~halfway of what would be needed for it * entries == 100
distrubtion = precentage_array(len(character_species), 10)
distrubtion_kv = {}

for i in range(0, len(distrubtion['percentages'])):
  distrubtion_kv[character_species[i]] = distrubtion['percentages'][i]

print(distrubtion_kv)