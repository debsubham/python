class User:
    total_online = 0
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        User.total_online += 1

    def full_name(self):
        return f"{self.first} {self.last}"
        
    def short_name(self):
        return f"{self.first[0]} {self.last[0]}"
    def likes(self , things):
        return f"{self.first} likes {things}"
    def logout(self):
        User.total_online -= 1
        return (f"{self.first}, you are Logged out")


user1 = User("Subham","Deb", 23)

print(user1.full_name())
print(user1.short_name())
print(user1.likes("Chicken")) ##only pass the things and it will automaticly fetch in User's methods


user2 = User("Babai","Deb", 24)

print(user2.full_name())
print(user2.short_name())
print(user2.likes("Mutton"))

print(User.total_online)

print(user2.logout())
print(User.total_online)