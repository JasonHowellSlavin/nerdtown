# When refactoring, there were a few considerations
# 1: we saw a reassignment of the d10 variable to get a new randint 
# 2: the code required there to be a list of only 10 items, anything past 10 would get ignored
# 3: the same operation occured a few times

# so when refactoring, we tried to eliminate the variable reassignment by using a function,
# remove the dependency of list being 10 items by using the length of the list as the max
# remove the need to save output to variables by returning the capitalized string using method chaining. 

import random

adjective = ["small", "big", "cute", "sneaky", "unusual", "helpful", "mean", "red", "blue", "green"]   
animal = ["pig", "cow", "chicken", "zebra", "crayfish", "jellyfish", "worm", "boar", "dragon", "bull"]

def randomWordFromList(list):
    # get the max length
    max = len(list) - 1
    # return a random number from 0 to list length, and capitalize the result
    return list[random.randint(0, max)].capitalize()

# Testing
# call the function in our string concatination to have it return it's value 
print("Welccome To:", randomWordFromList(adjective) + " " + randomWordFromList(animal))