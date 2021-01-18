class Animal:
  def speak(self):
    raise NotImplementedError("Subclass needed to implement this method")

class Dog(Animal):
  def speak(self):
    return "Woof"

class Cat(Animal):
  def speak(self):
    return "Meow"

class Fish(Animal):
  pass

d = Dog()
f = Fish()
print(d.speak())
print(f.speak())

#####This is call Polymorphism And Another method call magic ==>> discussion in other file