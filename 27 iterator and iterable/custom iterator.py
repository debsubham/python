class Counter:
  def __init__(self,low,high):
    self.current = low
    self.high = high
  def __iter__(self):
    return (self)
  def __next__(self):
    if self.high > self.current:
      num = self.current
      self.current += 1
      return num
    raise StopIteration  

a = Counter(10,15)

for x in a:
  print(x)