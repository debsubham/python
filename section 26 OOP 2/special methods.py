class Human:
  def __init__(self,first,last,age):
    self.first=first
    self.last = last
    self.age = age
  def __repr__(self):
    return f"Human name {self.first} {self.last}"
  def __len__(self):
    return self.age
  def __add__(self,other):
    if isinstance(other, Human):
      return Human(first = "NewBorn", last = self.last,age=0)
    return "second pertion is not an Inheritance of Human"

j = Human("Jenny", "Larsen",47)
k = Human("kenny","anderson",45)
print(j)
print(len(j))
print(k + j)