
import random


#Lists
adjective = ["small", "big", "cute", "sneaky", "unusual", "helpful", "mean", "red", "blue", "green"]   
animals = ["pig", "cow", "chicken", "zebra", "crayfish", "jellyfish", "worm", "boar", "dragon", "bull"]
quality = ["upscale", "decent", "low-end"]
beers = ["lager", "brown ale", "gruit"]
name_prefix = ["ash", "bal", "crag", "dol", "esk", "fred", "ger", "hope", "is", "jay"]
name_suffix = ["voss", "wick", "ton", "shaw", "port", "moth", "hurst", "gate", "fos", "bury"]
e_name_prefix = ["thoron", "kano", "bale", "kemen", "varda", "mereth", "rhos", "glin", "bril", "menel", "glam", "cham"]
e_name_suffix = ["on", "ath", "rim", "or", "dil", "dur", "nil", "nur", "iel", "lin", "aelin"]
place = ["in the back corner", "at a center table", "at the bar", "near the front door", "next to the hearth", "near the back exit", "in a booth"]

#Code
def randomWordFromList(list):
    # get the max length
    max = len(list) - 1
    # return a random number from 0 to list length, and capitalize the result
    return list[random.randint(0, max)].capitalize()

def randomWordFromList_u(list):
    max = len(list) - 1
    return list[random.randint(0, max)]
    
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

guys = random.randint(40, 50)
random_index = random.randint(0, len(place) - 1)
random_index2 = random.randint(0, len(place) - 2)
random_index3 = random.randint(0, len(e_name_prefix) - 1)
elfishness = random.randint(0, 2)
size = crowd_size(guys).capitalize()
bartender = randomWordFromList(name_prefix) + randomWordFromList_u(name_suffix)
elf_name = e_name_prefix.pop(random_index3) + randomWordFromList_u(e_name_suffix)
elf_name2 = randomWordFromList(e_name_suffix) + randomWordFromList_u(e_name_suffix)
bartender_name = bartender
random_word_1 = place.pop(random_index)
random_word_2 = place.pop(random_index2)
num_patrons = random.randint(0, 100)
bartender_elf_name = elf_name
  


def patrons(guys):
    if guys > 39 and elfishness > 1:
        return "Patrons:" + " " + elf_name + random_word_2 + elf_name2 + random_word_1
    elif guys >= 20:
        return "some dudes"
    elif guys >= 1:
        return "a few dudes"
    else:
        return "empty of dudes"

# Testing
print("Welccome To: The", randomWordFromList(adjective) + " " + randomWordFromList(animals))
print("Quality:", randomWordFromList(quality))
print("Available Beer:", randomWordFromList(beers))
print("Price:", price, "Copper", "-", label)
print("Popularity:", guys, size)
print(elfishness)
print(patrons(guys))