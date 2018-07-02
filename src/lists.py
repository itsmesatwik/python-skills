import math
import random

#lists in python are dynamic and can hold multiple data types

# creates a list from values 0 to 9
oneToten = list(range(10))

#strings are lists of characters

# combine lists easily

listRand = list(range(5))

list3 = oneToten + listRand

list3.append("lol")

#multi dimenstional lists

multiDlist = [[0] * 10 for i in range(10)]

for i in range(10):
    for j in range(10):
        list[i][j] = i*j


