#TUPLES: IMMUTABLE RO, ORDERED, SEQUENCED,
movies = 'snatch', 'the beach','cruel intentions', 'mask' , 'halloween', 'free rainer', 'life of brian'
# print(type(movies))
# print(isinstance (movies, tuple))
# print(hex(id(movies)))
# print(len(movies))
# print(min(movies))
# print(max(movies))
#movies = 'snatch', 1,'cruel intentions', 'mask' , 'halloween', 'free rainer', 'life of brian'
print(type(movies))
print(movies.__len__())
print(isinstance (movies, tuple))
print(hex(id(movies)))
print(len(movies))
print(min(movies))
print(max(movies))
print(dir(movies))

a=10
b=11
(a,b) = (10,20)
(a, b, *c) = range(10,60,10)

print((a, b, c))
(a, *b, c) = range(10,60,10) # unpakced as list
print((a, b, c))

# LIST : ORDERED, SEQUENCED, RW, (same like set)
films = list(movies)
print(type(films))

numbers = (10,50,2,6)
print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(sorted(numbers, reverse=False))
print(sorted(numbers, key=abs))
print(sorted(numbers, key=abs, reverse=True))
items = ["10", "2", "33", "4"]
print(sorted(items, key=str))
items.pop(0) # index
#items.remove("10") # value
items.reverse()
#items.sort() # sorts in place
items = [10, 2, 33, 3]

print(sorted(items)) # creates new list)
print(items)
print(items.sort())
print(items)

