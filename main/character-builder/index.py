from data import *
import random
from pprint import pprint

def getName(): 
   print('What is your characters name?')
   name = input()
   return name

def randomFromList(list):
    max = len(list) - 1
    return list[random.randint(0, max)]

def createStat():
  return random.randint(3, 18)

def createStatsList(stat_list):
  final_stats = {}

  for stat in stat_list:
    final_stats[stat] = createStat()
  
  return final_stats

def getStartingKit(character_class):
  kit = starting_kits[character_class]
  return randomFromList(kit)

def getItemStat(item, dict):
  try:
   itemStat = dict[item]
   return itemStat
  except:
    return ''
  
def createCharacter():
  name = getName()
  character_class = randomFromList(classes)
  character_race = randomFromList(races)
  starting_stats = createStatsList(stats)
  starting_kit = getStartingKit(character_class)
  weapon = starting_kit['weapon']
  armor = starting_kit['armor']
  starting_weapon = {'type': weapon, 'stats': getItemStat(weapon, weapon_damage)}
  starting_armor = {'type': armor, 'stats': getItemStat(armor, armor_class)}

  character = {
    'name': name, 
    'class': character_class,
    'race': character_race,
    'stats': starting_stats,
    'kit': starting_kit,
    'weapon': starting_weapon,
    'armor': starting_armor,
  }

  pprint(character)

createCharacter()

