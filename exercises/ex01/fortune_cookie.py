"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730393281"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint



# Begin your solution here...
def my_fortune (x: int) -> str:
    fortune : str = ""
    if x == 1:
        fortune = "You will receive all A's this semester."
        return fortune
    else:
        if x == 2:
            fortune = "Their will be sunny weather today."
            return fortune
        else:
            if x == 3:
                fortune = "You will find love on Valentine's Day."
                return fortune
            else:
                fortune = "You will recieve great wealth in the coming days."
                return fortune

x : int = randint (1, 4)
print ("Your fortune cookie says...")
print (my_fortune(x))
print ("Now, go spread positive vibes")


