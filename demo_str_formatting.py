planets = {'Mercury': 57.91,
           'Venus': 108.2,
           'Earth': 149.597870,
           'Mars': 227.94
}

# Iterate through the dict keys and display planet names and their distance
# using str concatenation and escape chars.
for planet in planets.keys():
    print("\t\t" + planet + ": " + str(planets[planet]) + "Gm")

print("-" * 50)
for planet in planets.keys():
    print(planet.rjust(12) + ": " + str(planets[planet]) + " Gm")
    print(planet.rjust(12) + ": " + str(planets[planet]).rjust(12, '.') + " Gm")
    print(planet.rjust(12) + ": " + str(planets[planet]).center(12, '.') + " Gm")
    print(planet.rjust(12) + ": " + str(planets[planet]).ljust(12, '.') + " Gm")

for planet in planets.keys():
    print("{0:>12s}: {1:.>12.3f} Gm" .format(planet,planets[planet])) # 0,1 position
    #print("{planet:>12s}: {planets[planet]:.>12.3f} Gm") # 0,1 position
    print(f"{planet:>12s}: {planets[planet]:.>12.3f} Gm") # 0,1 position format strings after python 3.5
    # after colon format
    # s,f floating
    #<,>,^ justification
    # 12 number of justification
    # .> padding character for justification
    # 12.3 : floating point precision