#! /usr/bin/env python3
# Author: PDalal
# Version: 1.0
# Description: This script will demo HowTo generate 6 random lottery numbers
"""
    DocString
"""
import random

lotto = []
while len(lotto) < 6:
    num = random.randint(1, 50)
    if num not in lotto:
        lotto.append(num)
    else:
        print("duplicate num =", lotto)

# num = random.randint(1,50)
# lotto.append(num)
#
# num = random.randint(1,50)
# lotto.append(num)
#
# num = random.randint(1,50)
# lotto.append(num)
#
# num = random.randint(1,50)
# lotto.append(num)
#
# num = random.randint(1,50)
# lotto.append(num)
#
# num = random.randint(1,50)
# lotto.append(num)

print("lottery numbers = ", lotto)
