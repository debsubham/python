class WithOut_repr:
    def __init__(self,first,last):
        self.first = first
        self.last = last
    def print_it(self):
        return f"{self.first} {self.last}"

class With_repr:
    def __init__(self,first,last):
        self.first = first
        self.last = last
    def __repr__(self):
        return f"{self.first}"
    def print_it(self):
        return f"{self.first} {self.last}"


user1 = WithOut_repr("suhbham","deb")
print(user1.print_it())
print(user1) ###return address


user2 = With_repr("suhbham", "deb")
print(user2.print_it())
print(user2) ###return self.first


