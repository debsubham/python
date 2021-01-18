class Aquatic:
    def __init__(self,name):
        print("Aquitic init")
        self.name = name
    def swim(self):
        return f"{self.name} is swimming"
    def greet(self):
        return f"I am {self.name} of the sea!!"

class Ambulatory: 
    def __init__(self,name):
        print("Ambulatory init")
        self.name = name
    def walk(self):
        return f"{self.name} is walking"
    def greet(self):
        return f"I am {self.name} of the land!!"


class Penguin(Aquatic,Ambulatory):
    def __init__(self,name):
        print("Penguin init")
        super().__init__(name)


captain_cook = Penguin("Captain Cook")

###main class and first inherit class will run but we can use any of the function of two inheritance
##example ==>
print(captain_cook.walk())
print(captain_cook.swim())