#!/usr/bin/python

import random

blue = []
blues = range(1, 34)
reds = range(1, 17)

for i in range(6):
    choice = random.choice(blues)
    blue.append(choice)

blue.sort()
red = random.choice(reds)

print blue, ':', red
