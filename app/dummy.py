import random

def math():
    randomlist = []
    longtermlist = []
    for i in range(0,6):
        n = random.randint(1,99)
        randomlist.append(n)
        for i in range(10):
            longtermlist.append(randomlist)
    return longtermlist