#### python -m pip install pyfiglet
import pyfiglet
import termcolor

print("what message do you want to print?? ===>")
message = input("answer :")
print("what color do you want to print?? ===>")
messagecolor = input("answer : ")


finalResult = termcolor.colored(pyfiglet.figlet_format(message), messagecolor)

print(finalResult)
