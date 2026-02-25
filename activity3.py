class parrot:
    species = "Bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age

bird1 = parrot("Peacock", 10)
bird2 = parrot("Pigeon", 5)
print(bird1.species, "and", bird2.species, "are objects")
print(bird1.name,"age",bird1.age, "and", bird2.name,"age",bird2.age)