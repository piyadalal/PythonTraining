#! /usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print("-" * len(Belgium))


print(Belgium.replace(",", ":"))


fields = Belgium.split(",")


try:
    country_population = int(fields[1])
    capital_population = int(fields[3])
except ValueError:
    print("Error: Population fields are not numeric!")
    country_population = 0
    capital_population = 0


print(country_population + capital_population)


print("-" * len(Belgium))
