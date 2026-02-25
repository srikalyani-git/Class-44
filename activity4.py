class parrot:
    species = "Bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sing(self,song):
        print(self.name, "age", self.age, "is singing", song)
    def dance(self):
        print(self.name, "is dancing")

bird1 = parrot("Peacock",10)
bird1.sing("song")
bird1.dance()
        