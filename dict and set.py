


dictionary = { "ABC" : "1111", "BDFAF" : "1516"}
print(f"SHIT {dictionary['ABC']}")

def list_unique_names(phonebook):
    unique_names = []
    for name, phonenumber in phonebook:
        first_name, last_name = name.split(" ", 1)
        for unique in unique_names:
            if unique == first_name:
                break
            else:
                unique_names.append(first_name)
        return len(unique_names)
   # O(n^2)

def set_unique_names(phonebook):
    unique_names = set()
    for name, phonenumber in phonebook:
        first_name, last_name =  name.split(" ", 1)
        unique_names.add(first_name)
    return len(unique_names)
    # O(n)

set_sample = [ ("AAA", "111-111-111"),
               ("BCD", "1818-11-151"),
             ]
def index_sequence(key, mask=0b111, PERTURB_SHIFT=5):
    perturb = hask(key)
    i = perturb & mask
    yield i
    while True:
        perturb >>= PERTURB_SHIFT
        i = (i*5 + perturb +1) & mask
        yield i

class City(str):
    def __hash__(self):
        return ord(self[0])
