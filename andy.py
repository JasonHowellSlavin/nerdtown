
import random

#Lists
adjective = ["small", "big", "cute", "sneaky", "unusual", "helpful", "mean", "red", "blue", "green"]   
animals = ["pig", "cow", "chicken", "zebra", "crayfish", "jellyfish", "worm", "boar", "dragon", "bull"]
noun = ["apple", "beak", "crown", "cap", "den", "place", "pride", "rest"]
possessive_noun = ["king's", "queen's", "rougue's", "stag's", "rat's", "jay's","dunce's"]
quality = ["upscale", "decent", "low-end"]
beers = ["lager", "brown ale", "gruit"]
name_prefix = ["ash", "bal", "crag", "dol", "esk", "fred", "ger", "hope", "is", "jay"]
name_suffix = ["voss", "wick", "ton", "shaw", "port", "moth", "hurst", "gate", "fos", "bury"]
e_name_prefix = ["thoron", "kano", "bale", "kemen", "varda", "mereth", "rhos", "glin", "bril", "menel", "glam", "cham"]
e_name_suffix = ["on", "ath", "rim", "or", "dil", "dur", "nil", "nur", "iel", "lin", "aelin"]
place = ["in the back corner", "at a center table", "at the bar", "near the front door", "next to the hearth", "near the back exit", "in a booth"]
races = ["human", "elf", "dwarf"]
d_name_prefix = ["am", "bal", "dim", "har", "hod", "gra", "tor"]
d_name_suffix = ["dor", "thor", "dek", "teth", "goth", "bur"]
genders = ["male", "female", "non-binary"]

# Initialization number: this number is what sets up the program
num_patrons = random.randint(0, 60)
bar_seed = random.randint(0, 1) #this is supposed to set up different naming conventions

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
    

def bar_name_type():
    if bar_seed == 1:
        return randomWordFromList(adjective).capitalize() + " " + randomWordFromList(animals).capitalize()
    else:
        return randomWordFromList(possessive_noun).capitalize() + " " + randomWordFromList(noun).capitalize()

bar_population = crowd_size(num_patrons)
label = label_price()
bar_name = bar_name_type()



def generate_bartender():
    race = random.choice(races)

    if race == "human":
        name = randomWordFromList(name_prefix).capitalize() + randomWordFromList(name_suffix)
    elif race == "elf":
        name = randomWordFromList(e_name_prefix).capitalize() + randomWordFromList(e_name_suffix)
    else:
        race == "dwarf"
        name = randomWordFromList(d_name_prefix).capitalize() + randomWordFromList(d_name_suffix)

    gender = random.choice(genders)

    if gender == "male":
        pro1 = "he"
        pro2 = "him"
    elif gender == "female":
        pro1 = "she" 
        pro2 = "her"
    else:
        pro1 = "they"
        pro2 = "them"

    return {
        "name": name,
        "race": race.capitalize(),
        "gender": gender,
        "pronoun": pro1
    }
bt = generate_bartender()

# Testing
print("Welccome To: The", bar_name)
print("Quality:", randomWordFromList(quality).capitalize())
print("Available Beer:", randomWordFromList(beers).capitalize())
print("Price:", label["price"], "Copper", "-", label["quality"])
print(f"Popularity: {num_patrons} {bar_population['popularity']}, {bar_population['description']}")
print(f"{bt['name']} the {bt['race']} greets you with a friendly wave. {bt['pronoun'].capitalize()} invites you to take a seat.")
