class GrumpyDict(dict):
  def __repr__(self):
    return 'None of your business'
  

data = GrumpyDict({"name" : "Subham", "title":"deb"})

print(GrumpyDict())