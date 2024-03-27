#1
import random

def random_element(lst):
    return random.choice(lst)

a = [1, 23, 45, 6, 2566, 66]
result = random_element(a)
print(result)



#2
import os

def random_file(lst):
    return random.choice(lst)

files = os.listdir('images/cats/')
file = random_file(files)
print(file)