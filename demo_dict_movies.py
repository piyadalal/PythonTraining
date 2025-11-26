#dictionaries are UNORDERED unique keys , create, grow and shrink
# from python 3.6, dict keys are INSERTION ORDER
import pprint

movies =  {'eric': ['pulp fiction', 'forest gump', 'platoon'],
'bertwin': ['kill bill', 'hateful 8', 'the firm'],
'stephan': ['james bond', 'Bourne', 'batman']
 }
print(movies['eric'][0])
print(movies.get('eric')[0])
print(movies['eric'][0][0])
print(movies)

# another way to iterate through dict is using iterator  for loop plus thekeys
for name in movies.keys():
    #print(f"{name} likes {movies[name]}")
    print(f"{name} likes {movies[name]}") # lookup to get values, easaier way is movies.items

# another way to iterate through dict is using iterator  for loop plus thekeys
for films in movies.values():
    #print(f"{name} likes {movies[name]}")
    print(f" recommended movie is {films}")

# another way to iterate through dict is using iterator  for loop plus thekeys
for (name,films) in movies.items():
    #print(f"{name} likes {movies[name]}")
    print(f" {name} likes {pprint.pformat(films)}")