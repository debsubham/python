from functools import wraps

def ensure_no_kwargs(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    if kwargs:
      raise ValueError("kwargs not be allowed sorry :(")
    return fn(*args, **kwargs)
  return wrapper

@ensure_no_kwargs
def names(name):
  print(f"your name is {name}")

names(name="Subham Deb")