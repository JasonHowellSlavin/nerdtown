import random

# Takes a list that likely has a large first int, divides and adds quotiant to list and returns list +
def normalize_outlier(arr):
  remainder = arr.pop(0)
  quotient = int(remainder / len(arr))
  reduction_factor = 1.25

  # using a reduction factor to minimize the amount of addition to make a more normalized sum
  mapped_list = list(map(lambda n: n + int(quotient / reduction_factor), arr))
  difference = 100 - sum(mapped_list)
  mapped_list.insert(0, difference)
  return mapped_list

# returns a list with an array of percentages and a message
# will seek to normalize percentages, but the change of an outlier is fairly high
def precentage_array(entries=4, minimum=1):
  percentages = []
  available_percentage = 100
  min = minimum
  ent = entries
  message = ''
  exceeds_percent_toal = entries * minimum > available_percentage - (ent * min) < min

  if (exceeds_percent_toal):
    percentage_maximum = int(available_percentage/entries)
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