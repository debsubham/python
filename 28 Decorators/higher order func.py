

def summing(n, func):
  total = 0
  for num in range(n):
    total += func(num)
  return total
def square(x):
  return x*x

def cube(x):
  return x*x*x

result = summing(3, square)
result2 = summing(3, cube)
print(result)
print(result2)


####################

from random import choice

def greet(person):
  def get_mood():
    msg = choice(("Hello there ","Go away ","I love you "))
    return msg
  result = get_mood() + person
  return result

print(greet("Subham"))
