class First:
    def __init__(self):
        self.name = "Subham"
    def print(self,name):
        return name


class Second(First):
    pass


a = First()
b = Second()

print(a.print("babai"))
print(b.print("deb"))