def log_function_data(fn):
  def wrapper(*args, **kwargs):
    """I AM Wrapper Function"""
    print(f"you are about all call {fn.__name__}")
    print(f"Here's the documentation: {fn.__doc__}")
    return fn(*args, **kwargs)
  return wrapper

@log_function_data
def add(x,y):
  """Adds Two Numbers Together"""
  return x + y

print(add(10,30))


print(add.__doc__) ##this doc reflects wrapper function
print(add.__name__) ##this name reflects wrapper function




from functools import wraps


def log_function_data2(fn):
  @wraps(fn)
  def wrapper2(*args, **kwargs):
    """I AM Wrapper Function"""
    print(f"you are about all call {fn.__name__}")
    print(f"Here's the documentation: {fn.__doc__}")
    return fn(*args, **kwargs)
  return wrapper2

@log_function_data2
def add2(x,y):
  """Adds Two Numbers Together"""
  return x + y

print(add2(10,30))


print(add2.__doc__) ##this doc reflects add function
print(add2.__name__) ##this name reflects add  function
