import string
import timeit

## Preventing Hash Crash ! ##
class Point(object):
    def __init__(self, x,y):
        self.x, self.y = x, y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

## Optimal Hash ##
def twoletter_hash(key):
    offset = ord('a')
    k1, k2 = key
    return (ord(k2) - offset) + 26 * (ord(k1) - offset)

class BadHash(str):
    def __hash__(self):
        return 42
    
class GoodHash(str):
    def __hash__(self):
        return ord(self[1]) + 26 * ord(self[0]) - 2619
    
baddict = set()
gooddict = set()
for i in string.ascii_lowercase:
    for j in string.ascii_lowercase:
        key = i + j
        baddict.add(BadHash(key))
        gooddict.add(GoodHash(key))
        
badtime = timeit.repeat("key in baddict", setup = "from __main__ import baddict, BadHash; key = BadHash('zz')",
                        repeat = 3, number = 1_000_000,
                        )

goodtime=timeit.repeat("key in gooddict", setup="from __main__ import gooddict, GoodHash; key = GoodHash('zz')",
                                              repeat=3, number=1_000_000,
                                              )
print(f"bad time: {min(badtime)}")
print(f"good time: {min(goodtime)}")
