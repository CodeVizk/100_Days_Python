# Syntax to inheritance a class to another class
class Animal:
    def __init__(self):
        self.number_of_eyes = 2

    def breathe(self):
        print("Inhale", "Exhale")


class Fish (Animal):
    def __init__(self):
        super().__init__()


    def breathe(self):
        super().breathe()
        print("Doing in underwater")

    def swim(self):
        print("Moving in water.")

# Syntax super() is for super class or parent class
# The fish class is inheriting the properties of the Animal class
nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.number_of_eyes)
