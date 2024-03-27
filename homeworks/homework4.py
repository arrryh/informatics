#1
import random

def random_element(lst):
    return random.choice(lst)

a = [1, 23, 45, 6, 2566, 66]
result = random_element(a)
print(result)


#2
import os

def random_file(directory):
    files = os.listdir(directory)
    random_file = random.choice(files)
    return random_file


directory = "images/cats"
random_image = random_file(directory)
print(random_image)