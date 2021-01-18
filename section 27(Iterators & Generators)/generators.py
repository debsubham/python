
def count_up_to(max):
      count = 1
      while count <= max :
         yield count
         count += 1

counter = count_up_to(5)

# lst = list(counter)

# print(lst)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))