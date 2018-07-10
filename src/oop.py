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
