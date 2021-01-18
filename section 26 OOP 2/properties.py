class User:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self._age= age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,value):
        self._age = value
    @property
    def full_name(self):
        return (f"{self.first} {self.last}")
    @full_name.setter
    def full_name(self,name):
        self.first, self.last = name.split(" ")

first_user= User("Subham","Deb", 10)
print(first_user.age)
first_user.age = 23
print(first_user.age)

print(first_user.full_name)
first_user.full_name = "subham deb"
print(first_user.full_name)
