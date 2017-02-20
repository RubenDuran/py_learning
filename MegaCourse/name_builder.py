import string, random

def letter():
    return random.choice(string.ascii_lowercase)

def generator():
    l1=letter()
    l2=letter()
    l3=letter()
    name = l1 + l2 + l3
    return name

print (generator())
