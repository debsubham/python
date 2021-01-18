class Animals:
  def __init__(self,name,species):
    self.name = name
    self.species = species
  def __repr__(self):
    return ("{self.name} is a {self.species}")
  def make_sound(self,sound):
    return ("{self.name} says {sound}")


class Cat(Animals):
  def __init__(self,name,species,breed,toy):
    # Animals.__init__(self,name,species)
    super().__init__(name, species)
    self.breed = breed
    self.toy = toy


sweety = Cat("kitty","cat","Scottish Fold","String")
print(sweety)
print(sweety.name)
print(sweety.species)
print(sweety.breed)
print(sweety.toy)