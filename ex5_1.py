
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += 'Oke' # acts as extend which adds iterable one by one to list and modifies list in place
print(cheese)
cheese.append('Oke')
print(cheese)
print("-" * 50)

tup = 'Hello'
print(len(tup))
tup = 'Hello',
print(len(tup))
print("-" * 50)

import random
lotto = set()
# Create an empty set.
while len(lotto) < 6:
    num = random.randint(1, 50)
    lotto.add(num) # Add new number to set.
print("Lottery numbers = ", lotto)

print("-" * 50)

machines = {'user100': 'yogi',
'user1': 'booboo',
'user2': 'rupert',
'user3': 'teddy',
'user4': 'care',
'user5': 'winnie',
'user6': 'sooty',
'user7': 'padders',
'user8': 'polar',
'user9': 'grizzly',
'user10': 'baloo',
'user11': 'bungle',
'user12': 'fozzie',
'user13': 'huggy',
'user14': 'barnaby',
'user15': 'hair',
'user16': 'greppy'
}
#user14 no longer has a machine assigned.
#machines.pop('user14')
machines['user14']  = None
print(machines)
machines['user15'] = 'cinnamon'
print(machines)
machines['user17'] = machines['user16']
del machines['user16']
print(machines)


#make a copy of dict and then modify
for (k,v) in list(machines.items()):
    if k == 'user16':
        del machines[k]
        machines['user17'] = v
print(machines)


key_to_move = None
value_to_move = None

for k, v in machines.items():
    if k == 'user16':
        key_to_move = k
        value_to_move = v
        break

if key_to_move:
    del machines[key_to_move]
    machines['user17'] = value_to_move

print("-" * 50)

unallocated = []
for (k,v) in list(machines.items()):
    if k == 'user4':
        unallocated.append(v)
        machines.pop(k)
    if k == 'user5':
        unallocated.append(v)
        machines.pop(k)
    if k == 'user6':
        unallocated.append(v)
        machines.pop(k)



unallocated = []
for user in ('user4', 'user5', 'user6'):
    unallocated += [machines.pop(user)]

print(unallocated)
print(machines)

print("-" * 50)

remove_keys = ['user3', 'user4', 'user5']
for k, v in list(machines.items()):
    if k in remove_keys:
        unallocated.append(v)
        machines.pop(k)

for (k,v) in list(machines.items()):
    if k == "user8":
        #machines[k].append("Kodiak")
        pass

machines['user8'] = [machines['user8'], 'kodiak']
print(machines)

list(machines['user8']).append("Kodiak")
print(machines)

print("-" * 50)

for (k,v) in list(machines.items()):
    print(f"{k}: {v}")


print("-" * 50)
unallocated.sort(key=str.lower, reverse=False) # inplace sorting
print(unallocated)
# OR
print(sorted(unallocated, reverse=False))


print("-" * 50)

import timeit

setup_code = """
items_list = list(range(1000000))
items_set = set(range(1000000))
"""

# Test membership in list
list_test = "999999 in items_list"

# Test membership in set
set_test = "999999 in items_set"

# Run tests
list_time = timeit.timeit(stmt=list_test, setup=setup_code, number=10)
set_time  = timeit.timeit(stmt=set_test,  setup=setup_code, number=10)

print("List membership time :", list_time)
print("Set membership time  :", set_time)

