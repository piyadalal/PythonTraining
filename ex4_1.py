#! /usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# 1. Line of hyphens
print("-" * len(Belgium))

# 2. Replace commas with colons
print(Belgium.replace(",", ":"))

# 3. Sum populations
fields = Belgium.split(",")
population = int(fields[1])
capital_pop = int(fields[3])
print(population + capital_pop)

# 4. Line of hyphens
print("-" * len(Belgium))