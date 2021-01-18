# try
# except
# else
# finally
while True: ##always true so the function run infinite times
    try:
        num = int(input("please enter a number :: "))
    except :
        print("thts's not a number")   ### if try have a error then its except run
    else:
        print("i'm in the else") ## if except not run then else will run
        break ##when its get integer else will run and break the function
    finally:
        print("runs no matter what")  ##its run no matter what


print ("excellent")