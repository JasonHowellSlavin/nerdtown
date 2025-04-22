
import random

adjective = ["small", "big", "cute", "sneaky", "unusual", "helpful", "mean", "red", "blue", "green"]   
animal = ["pig", "cow", "chicken", "zebra", "crayfish", "jellyfish", "worm", "boar", "dragon", "bull"]
quality = ["upscale", "decent", "low-end"]
beers = ["lager", "brown ale", "gruit"]
pops = ["Dump"] #don't know what I'm doing here. Can't figure out why I need this list to make crowd work

def randomWordFromList(list):
    # get the max length
    max = len(list) - 1
    # return a random number from 0 to list length, and capitalize the result
    return list[random.randint(0, max)].capitalize()

def label_price(value):
    if value > 8:
        return "expensive"
    elif value >= 5:
        return "fair"
    else:
        return "cheap"
    
for beer in beers:
    price = random.randint(1, 12)  # Random coin value between 1 and 12
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
    
for pop in pops: #why does it only work if I have this line?
    guys = random.randint(1, 50)
    size = crowd_size(guys).capitalize()
    

# Testing
print("Welccome To: The", randomWordFromList(adjective) + " " + randomWordFromList(animal))
print("Quality:", randomWordFromList(quality))
print("Available Beer:", randomWordFromList(beers))
print("Price:", price, "Copper", "-", label)
print("Popularity:", guys, size)