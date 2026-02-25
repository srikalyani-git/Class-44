class student:
    grade = 10
    name = "John"
    def intro(self):
        print("Hi I am a student")
    def func2(self):
        print("My name is", self.name, "and im in grade", self.grade )

john = student()
john.intro()
john.func2()