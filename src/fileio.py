# Need to import a module called os
import os

#opening a fie with 'with' ensures that the file will be closed if the program should crash for some reason
with open("filename.txt", mode = 'w', encoding = 'utf-8') as file:
    file.write("Random Text\nyolo")
#various modes of opening a file are 'w' 'r' 'a'
with open("filename.txt", encoding = 'utf-8') as file:
    print(file.read())
