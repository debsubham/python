# THE BASIC SYNTAX
# try:
# except:

try:
    foobnaafafaf ##if this text error then cxcept will run
except:
    print("alls Good")





###################Another example#####################

def get(dic, key):
    try:
        return dic[key]
    except KeyError:
        return None

d={"name" : "Subham"}

print(get(d,"name"))
