import random

d10 = random.randint(0, 9)

adjective = ["small", "big", "cute", "sneaky", "unusual", "helpful", "mean", "red", "blue", "green"]
    
animal = ["pig", "cow", "chicken", "zebra", "crayfish", "jellyfish", "worm", "boar", "dragon", "bull"]

random_adjective = adjective[d10]
d10 = random.randint(0, 9)
random_animal = animal[d10]
cap_adjective = random_adjective.capitalize()
cap_animal = random_animal.capitalize()

# Testing
print("Welccome To:", cap_adjective + " " + cap_animal)