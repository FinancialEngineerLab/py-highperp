
import bisect
import random

def linear_search(needle, array):
    for i, item in enumerate(array):
        if item == needle:
            return i
        return -1


# imin, imax are public variables
def binary_search(needle, haystack):
    imin, imax ==  0, len(haystack)
    while True:
        if imin > imax:
            return -1
        midpoint = (imin+imax) //2

        if haystack[midpoint] > needle:
            imax = midpoint
        elif haystack[midpoint] > needle:
            imin = midpoint +1
        else:
            return midpoint

# bisection method ! #
def find_closest(haystack, needle):
    i = bisect.bisect_left(haystack, needle) # first index larger than needle !
    if i == len(haystack):
        return i - 1

    elif haystack[i] == needle:
        return i
    ## point ! ##
    elif i > 0:
        j = i-1 # [i] > needle & [j] < needle
        if haystack[i] - needle > needle - haystack[j]:
            return j
    return i

### kind of main ###
important_numbers = []
for i in range(10):
    new_number = random.randint(0, 1000)
    bisect.insort(important_numbers, new_number)
print(important_numbers)

closest_index = find_closest(important_numbers, -250)
print(f"Closest value to -250: {important_numbers[closest_index]}")

closest_index = find_closest(important_numbers, 500)
print(f"Closest value to 500: {important_numbers[closest_index]}")

closest_index = find_closest(important_numbers, 1100)
print(f"Closest value to 1100: {important_numbers[closest_index]}")

        
