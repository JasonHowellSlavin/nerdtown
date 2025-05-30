
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

# Initialization number: this number is what sets up the program
num_patrons = random.randint(0, 60)

#Code
def randomWordFromList(list):
    # get the max length
    max = len(list) - 1
    # return a random number from 0 to list length, and capitalize the result
    return list[random.randint(0, max)]

def removeWordFromList(list):
    # get the max length
    max = len(list) - 1
    index = random.randint(0, max)

    return list.pop(index)

def label_price():
    price = random.randint(1, 12)

    if price > 8:
        return {"price": price, "quality": "Expensive" }
    elif price >= 5:
        return {"price": price, "quality": "Fair" }
    else:
        return {"price": price, "quality": "Cheap" }

def elfish_bar_description():
    location_1 = removeWordFromList(place)
    location_2 = removeWordFromList(place)
    name_1 = removeWordFromList(e_name_prefix) + randomWordFromList(e_name_suffix)
    name_2 = removeWordFromList(e_name_prefix) + randomWordFromList(e_name_suffix)

    return f"Patrons: {name_1}{location_1}, {name_2}{location_2}"

def crowd_size(crowd):
    elfishness = random.randint(0, 2)
    packed_with_elves = elfish_bar_description()
    many_patrons = "some dudes"
    is_packed_with_elves = packed_with_elves if elfishness > 1 else many_patrons

    if crowd > 39:
        return {"popularity": "packed", "description": is_packed_with_elves}
    elif crowd >= 20:
        return {"popularity": "fairly busy", "description": "some dudes"}
    elif crowd >= 1:
        return {"popularity": "sparse", "description": "a few dudes"}
    else:
        return {"popularity": "empty", "description":  "empty of dudes"}

bar_population = crowd_size(num_patrons)
label = label_price()
bartender_name = randomWordFromList(name_prefix).capitalize() + randomWordFromList(name_suffix)
  
# Testing
print("Welccome To: The", randomWordFromList(adjective).capitalize() + " " + randomWordFromList(animals).capitalize())
print("Quality:", randomWordFromList(quality).capitalize())
print("Available Beer:", randomWordFromList(beers).capitalize())
print("Price:", label["price"], "Copper", "-", label["quality"])
print(f"Popularity: {num_patrons} {bar_population['popularity']}, {bar_population['description']}")