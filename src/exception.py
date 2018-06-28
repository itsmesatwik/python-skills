while True:

    try:
        number = int (input("PLease input a number : "))
        break
    except ValueError:
        print("NaN")
    except:
        print("Unknown Error")

print("Good")


# Example of a do while in python 
import random

number = int (random.random()*10 + 1)

while True:
    try:
        ans = int(input("Guess : "))
        if ans == number:
            break
    except ValueError:
        print("NaN")

print("You guessed it!")
