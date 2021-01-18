

def myfunc():
    print("hello")
myfunc()

##FLIP A COIN
from random import random
def flip_coin():
    """this function use to toss a coin""" ##this is the comment about the function
    if(5>random()*10):
        print("Heads")
    else:
        print("tails")

flip_coin()
print(flip_coin.__doc__)