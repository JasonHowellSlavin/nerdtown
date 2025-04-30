
import random


#Lists
adjective = ["small", "big", "cute", "sneaky", "unusual", "helpful", "mean", "red", "blue", "green"]   
animals = ["pig", "cow", "chicken", "zebra", "crayfish", "jellyfish", "worm", "boar", "dragon", "bull"]
quality = ["upscale", "decent", "low-end"]
beers = ["lager", "brown ale", "gruit"]
name_prefix = ["ash", "bal", "crag", "dol", "esk", "fred", "ger", "hope", "is", "jay"]
name_suffix = ["voss", "wick", "ton", "shaw", "port", "moth", "hurst", "gate", "fos", "bury"]

#Code
def randomWordFromList(list):
    # get the max length
    max = len(list) - 1
    # return a random number from 0 to list length, and capitalize the result
    return list[random.randint(0, max)].capitalize()

def randomWordFromList_u(list):
    max = len(list) - 1
    return list[random.randint(0, max)]

def indef_art.str(word): #doesnt work
    if word[0] == "u" or "e":
        return "an" + str(word)
    else:
        return "a" + str(word)
    
    

def label_price(price):
    if price > 8:
        return "expensive"
    elif price >= 5:
        return "fair"
    else:
        return "cheap"
    
price = random.randint(1, 12)
label = label_price(price).capitalize()

def crowd_size(guys):
    if guys > 39:
        return "packed"
    elif guys >= 20:
        return "fairly busy"
    elif guys >= 1:
        return "sparse"
    else:
        return "empty"
    
guys = random.randint(0, 50)
size = crowd_size(guys).capitalize()

def patrons(guys):
    if guys > 39:
        return "like six dudes"
    elif guys >= 20:
        return "some dudes"
    elif guys >= 1:
        return "a few dudes"
    else:
        return "empty of dudes"
    
bartender = randomWordFromList(name_prefix) + randomWordFromList_u(name_suffix)

# Testing
print("Welccome To: The", randomWordFromList(adjective) + " " + randomWordFromList(animals))
print("Quality:", randomWordFromList(quality))
print("Available Beer:", randomWordFromList(beers))
print("Price:", price, "Copper", "-", label)
print("Popularity:", guys, size)
print(patrons(guys))
print(bartender)
print(indef_art(bartender))
#print('Welcome to:', indef_art(adjective) + ' ' + randomWordFromList(adjective) + ' ' + randomWordFromList(animals))
