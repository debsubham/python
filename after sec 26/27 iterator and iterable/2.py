## Custom For loop
num = [1,2,3,4]
char = "Hi There"

def my_for(iterable):
  iterator = iter(iterable)
  while True:
    try:
      print(next(iterator))
    except StopIteration:
      print("iteration complete>>>>")
      break

my_for("Hello")


def my_for2(iterable, func):
  iterator = iter(iterable)
  while True:
    try:
      thing = next(iterator)
    except StopIteration:
      print("iteration complete>>>>")
      break
    else:
      func(thing)


my_for2("Hlw", print) ## 2nd arg is a function
