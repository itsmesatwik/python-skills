# dictionary tut
dict = {"key" : "val", "jey2":"val"}
dict["key"] # prints out "val" associated with key

#dictionaries are non sequential so printing a dict would give different results every time it is done

#dictionary problem

ques = "Enter Customer ? "
ques2 = "Customer Name: "
dict_list = []
while (True):
    ans = input(ques)
    if ans == 'y':
        name = input(ques2)
        name.strip()
        nameList = name.split()
        newDict = {"fname" : nameList[0], "lname" : nameList[1]}
        dict_list.append(newDict)
    else:
        break
for dict in dict_list:
    print(dict["fname"] + " " + dict["lname"])

# Done


