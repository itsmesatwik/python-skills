class Dog:
    def __init__(self,name="",breed="", height=0):
        self.name = name
        self.breed = breed
        self.height = height

    def run(self):
        print("{} the dog runs".format(self.name))

    def eat(self, food):
        print("{} was eaten by our dog".format(food))

    def main():
        spot = Dog("Spot", "indie", 40)
        spot.run()
        spot.eat("bone")


main()



#getters and setters

class Square:
    def __init__(self, size=1):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self,value):
        if value.isFloat():
            self.__size = value
        else:
            print("xD")
    def getArea(self):
        return int(self.__size) * int(self.__size)

def main():
    square = Square()
    square.size(10)
    square.getArea()

main()
