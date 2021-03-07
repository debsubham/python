import json

j = json.dumps(["foo", {"bar" : ("baz", None, 1.0, 2)}])

print(j)

class Cat:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed

c = Cat("Charles", "Tabby")

cat_j = json.dumps(c.__dict__) ##dict representation of a class instance

print(cat_j)

import jsonpickle

encodedC = jsonpickle.encoded(c)

print(encodedC)
