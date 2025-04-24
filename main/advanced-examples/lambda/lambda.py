from pprint import pprint as oh_so_pretty

# definind "add" as a lambda function that takes parameters x,y
add = lambda x, y: x + y

# calling it
print(add(2,3))

# this is the same function, but defined normally
def addition(x, y):
    return x + y

print(addition(2, 6))

# you will likely use lamda functions as a callback for other functions, like map

# our list
numbers = [1, 2, 3, 4, 5]

# map is a function that goes through an iterable, does something (lambda) and returns a map object 
numbers_plus_one = map(lambda num: num + 1, numbers)

# we have to turn the return of map into a list to print it
oh_so_pretty(list(numbers_plus_one))

# same thing here, but with a defined function
def add_one(num):
    return num + 1

# interestingly, map knows to PASS the iterated value to the function in its first paramater as a paramater
long_numbers_plus_one = map(add_one, numbers)

# same output
oh_so_pretty(list(long_numbers_plus_one))

# lets see map pass the iterated item
words = ['hey', 'ho', 'lets', 'go']

word_map = map(lambda x: print(x), words)

# oooh, weird output, we see that hey ho lets go gets printed one at a time, but is followed by an array of [None, None, None, None]
# that is because our lambda did not return a value
oh_so_pretty(list(word_map))

# lets try with a traditional function, and see what happens
def print_and_add_z(word):
    print(word + 'z')
    return word + 'z'

word_map_two = map(print_and_add_z, words)

# similar outcome, but with a full list! 
oh_so_pretty(list(word_map_two))
