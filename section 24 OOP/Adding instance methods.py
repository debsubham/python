class User:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age

    def full_name(self):
        return f"{self.first} {self.last}"
    def short_name(self):
        return f"{self.first[0]} {self.last[0]}"
    def likes(self , things):
        return f"{self.first} likes {things}"


user1 = User("Subham","Deb", 23)

print(user1.full_name())
print(user1.short_name())

print(user1.likes("Chicken")) ##only pass the things and it will automaticly fetch in User's methods