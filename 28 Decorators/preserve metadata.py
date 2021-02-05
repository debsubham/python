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