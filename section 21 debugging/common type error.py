# ############################Types of Error##################### #

# SyntaxError =>>> def myfunc(( , None = 1, etc

# NameError   ==>>> non exsisting val--- name, fgsa,gfsag,asg

# TypeError ==>>>>

# IndexError =>>>>


def divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Don't divide by zero please")
    except TypeError:
        print("a and b must be ints or floats")
    else:
        print(f"answer is :: {result}")

print(divide(5,2))

