#Description: This script will show HOWTO use generators

def get_numbers():
    """Return a collection of numbers"""
    numbers = []
    for x in range(0, 10):
        numbers.append(x)
    return numbers

for z in get_numbers(): #calls get_numbers only once but print z executes 10 times
    ## as gets a list of 10 numbers
    print(z)

def get_numbers():
    """Return a collection of numbers"""
    numbers = []
    for x in range(0, 10): # 1 million
        numbers.append(x)
    return numbers

for z in get_numbers():
    print(z)
## for larger dataset it creates a list in RAM as RAM is hit it pages to disk empties RAM then fills up again, dumps again in hard disk
# windows paging system

def get_numbers():
    """Return a collection of numbers"""
    numbers = []
    for x in range(0, 10): # 1 million
        yield x

for z in get_numbers():
    print(z)


print("-"*80)
print("USING GENEARATORS: Yield an object at a time from a collection -Produce one value at a time, on demand.No list stored in memory. Much faster for large datasets. ")


def generate_numbers():
    for x in range(11):   # 0 to 10 inclusive
        yield x

print("_" * 20)
# Alternatively, we could use a generator function with
# a while loop
gen = generate_numbers ()
while True:
    num = next(gen, -1)
    if num:
        print (num)
    else:
        break