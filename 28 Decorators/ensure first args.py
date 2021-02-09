from functools import wraps

def ensure_first_args(val):
  def inner(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
      if args and args[0] != val:
        return f"first args need to be {val}"
      return fn(*args, **kwargs)
    return wrapper
  return inner


@ensure_first_args("burrito")
def fav_foods(*foods):
  print(foods)

print(fav_foods("burrito", "ice cream"))
print(fav_foods("ice cream","burrito"))

@ensure_first_args(10)
def add_to_ten(num1,num2):
  return num1 + num2

print(add_to_ten(10,60))
print(add_to_ten(11,60))
