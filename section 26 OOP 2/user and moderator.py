class User:
  active_user = 0
  @classmethod
  def display_active_users(cls):
    return f"There are currently {cls.active_user}"
  @classmethod
  def form_string(cls, data_str):
    first,last,age = data_str.split(",")
    return cls(first,last,int(age))

  def __init__(self,first,last,age):
    self.first= first
    self.last= last
    self.age = int(age)
    User.active_user += 1
  def logout(self):
    User.active_user -= 1
    return f"{self.first} has logged out"
  def fullname(self):
    return f"{self.first} {self.last}"
  def initials(self):
    return f"{self.first[0]} {self.last[0]}"


class Moderator(User):
  def __init__(self,first, last, age, community):
    super.__init__(self,first, last, age)
    self.community = community
  def remove_post(self):
    return f"{self.fullname()} remove a post"


name1 = User("subham", "beb", 12)
print(name1.fullname())
print(name1.initials())
print(User.display_active_users())
print(name1.logout()) 
print(User.display_active_users())

name2= User.form_string("Babai,LDeb,12")
# name2.form_string("asfaa,sfafa,12")
print(name2.fullname())
print(name2.initials())
print(User.display_active_users())
print(name2.logout()) 
print(User.display_active_users())