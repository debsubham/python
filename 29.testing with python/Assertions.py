def add_positive_numbers(x, y):
  assert x > 0 and y > 0, "Both numbers must be positive"
  return x + y


print(add_positive_numbers(10,50))
add_positive_numbers(100,-20)


def eat_junk(food):
  assert food in ["pizza","ice cream","candy","fried butter"], "food must be junk"              #python3 -O assertion.py is ignore the assert condition
  return f"you eating {food}"


print(eat_junk("pizza"))
eat_junk("apple")