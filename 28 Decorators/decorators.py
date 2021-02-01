
################## with normal inheritance function ########################
def be_polite(fn):
  def wrapper():
    print("What a pleasure to meet you")
    fn()
    print("have a great day")
  return wrapper

def greet():
  print("My name is colt")

def rage():
  print("I hate you")

greet = be_polite(greet)

poligte_rage = be_polite(rage)

poligte_rage()

##############################################################################
#######################same function with Decorators syntax ##################
##############################################################################  


def be_polite(fn):
  def wrapper():
    print("What a pleasure to meet you")
    fn()
    print("have a great day")
  return wrapper

@be_polite
def greet2():
  print("My name is colt")

@be_polite
def rage2():
  print("I hate you")

# greet = be_polite(greet)

# poligte_rage = be_polite(rage)

greet2()
rage2()