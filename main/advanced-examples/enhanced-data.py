import random
import pprint

## create a list of dicts that we can filter through
beer_list = [
  {
    'name': 'Bogwench Brown',
    'price': 0.5,
    'quality': 'poor',
    'taste': 'malty notes with a hint of sulfer and salt',
    'description': 'a mug full of a brackish green brown beer'
  },
  {
    'name': 'Golden Pastures Lager',
    'price': 2,
    'quality': 'high',
    'taste': 'light and crips, with a hint of honey',
    'description': 'a glass filled with a golden and bubbly'
  },
  {
    'name': 'Bullhorn Ale',
    'price': 1,
    'quality': 'medium',
    'taste': 'toasted malt with carmel undertones',
    'description': 'a large tankered of amber colered ale'
  },
  {
    'name': 'Smeggens Famrhouse Ale',
    'price': 1,
    'quality': 'medium',
    'taste': 'Fruity notes with a sour aftertaste',
    'description': 'a checkered mug full of purple brown beer'
  }
]

# two functions, one to get by price or by quality 
def getBeerByPrice(beer, value):
  return beer['price'] == value

def getBeerByQuality(beer, value):
  return beer['quality'] == value

# get a high priced beer 
high_priced_beer = list(filter(lambda beer: getBeerByPrice(beer, 2), beer_list))

pprint.pprint(high_priced_beer)
print('\n*\n*\n*\n')

# get a medium quality beer 
medium_quality_beer = list(filter(lambda beer: getBeerByQuality(beer, 'medium'), beer_list))

pprint.pprint(medium_quality_beer)
print('\n*\n*\n*\n')

# Lets play with some template strings / format strings and have a random beer get served up using our dicts' properties 
def bartenderServesRandomBeer(list):
  random_beer = list[random.randint(0, len(list) - 1)]
  name = random_beer['name']
  taste = random_beer['taste']
  description = random_beer['description']
  bartender_speech = f'"Hey stranger! Here you go, our finest beer!".\nThe bartender passes you {description}.\n"{name} is the name!".\nIt has {taste}'
  print(bartender_speech)

bartenderServesRandomBeer(beer_list)
print('\n*\n*\n*\n')

# Lets now use some user input to choose a beer, also using our list to give our user options
def askForBeerList(list):
  print('Ah, our whole list? Well, we have:')

  for index, beer in enumerate(list):
    name = beer['name']
    print(f'[{index}] {name}\n')

  choice = input('So what will it be? (type the number corisponding to the name and hit enter)')
  print(f'Ah, you chose {list[int(choice)]['name']}')

askForBeerList(beer_list)