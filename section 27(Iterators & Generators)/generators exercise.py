def week():
  allday = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  for day in allday:
    yield day


days = week()

print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
print(next(days))
# print(next(days))




def yes_or_no():
    condition = "yes"
    while 1 :
        yield ("yes" if condition == "yes" else "no")
        condition = "yes" if condition == "no" else "no"

gen =yes_or_no()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))