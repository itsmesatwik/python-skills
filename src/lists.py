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

list4 = [1,2,3,4,5,6,7,6123,4,21,53,123,5,12,41,4,2,3,4,5,5,6]

#sort a list
list4.sort()

#reverse a list
list4.reverse()
