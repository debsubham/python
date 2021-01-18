##### install TermColor #####
# CMD =>> python -m pip install termcolor

import termcolor

colortext =  termcolor.colored("Hi there", color="red" , on_color="on_cyan", attrs = ['blink'])

print(colortext)
