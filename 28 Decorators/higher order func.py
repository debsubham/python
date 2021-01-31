

def summing(n, func):
  total = 0
  for num in range(n):
    total += func(num)
  return total
def square(x):
  return x*x

result = summing(10, square)


print(result)