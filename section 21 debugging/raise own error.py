# raise ValueError("Invalide Name")
# raise NameError("blaH blaH")

#        ||
#        ||
#        ||
#        ||
#      \\  //
#       \\//
#        \/

def textcolor(text,color):
    colors = ["cyan", "yellow", "blue","green","magenta"]
    if type(text) is not str:
        raise TypeError("text must be instance of str")
    if color not in colors:
        raise ValueError("color is invalid")
    print(f"printed {text} in {color}" )

textcolor("Hello" , "yellow")
textcolor("Hello" , "red")