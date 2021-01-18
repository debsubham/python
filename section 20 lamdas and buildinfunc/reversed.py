### list.reverse() /////  reversed(list) ###

nums = [1,2,3,4,5,6]

nums.reverse()
print(nums)

print(reversed(nums)) ##through a error object  ===>>>>> <list_reverseiterator object at 0x03438160>
print(list(reversed(nums)))

print(list(reversed("Hello"))) ### ['o', 'l', 'l', 'e', 'H']
print(''.join(list(reversed("Hello")))) ## olleH

for x in reversed(range(0,10)):
    print (x)