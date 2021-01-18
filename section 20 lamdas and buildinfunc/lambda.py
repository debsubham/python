myfunction = lambda a,b : a+b

print(myfunction.__name__)
print(myfunction(30,20))
singles = (1,2,3,4,5)

doubles = list(map(lambda x: x*2, singles))
print (doubles)