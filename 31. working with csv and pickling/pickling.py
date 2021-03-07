class Animal:
  def __init__(self, name, species):
    self.name = name
    self.species = species
  def __repr__(self):
    return f"{self.name} is  a {self.species}"
  def make_sound(self, sound):
    print(f"this animals says{sound}")


class Cat(Animal):
  def __init__(self, name, breed, toy):
    super().__init__(name, species="Cat")
    self.breed = breed
    self.toy = toy

  def play(self):
    print(f"{self.name} plays with {self.toy}")

first_cat1 = Cat("pussy", "spanish", "car")

# first_cat1.play()

import pickle


##first step of pickling(save as binary)
# with open("pets.pickle", "wb") as file:
#   pickle.dump(first_cat1, file)


##second step pickling(open binary to normal value)
with open("pets.pickle", "rb") as file:
  zombie_blue = pickle.load(file)
  print(zombie_blue)
  print(zombie_blue.play())

