import math
from math import sin

def test1(x):
    res = 1
    for _ in range(1000):
        res += math.sin(x) # best : twice
    return res


def test2(x):
    res = 1
    for _ in range(1000):
        res += sin(x) # no visible
    return res

def test3(x, sin = math.sin): # not python like
    res = 1
    for _ in range(1000):
        res += sin(x)

