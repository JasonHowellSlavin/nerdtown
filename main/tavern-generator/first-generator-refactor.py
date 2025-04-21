import random

adjective = ["small", "big", "cute", "sneaky", "unusual", "helpful", "mean", "red", "blue", "green"]   
animal = ["pig", "cow", "chicken", "zebra", "crayfish", "jellyfish", "worm", "boar", "dragon", "bull"]

def randomWordFromList(list):
    max = len(list)
    return list[random.randint(0, max)].capitalize()

# Testing
print("Welccome To:", randomWordFromList(adjective) + " " + randomWordFromList(animal))