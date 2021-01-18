def current_beat():
  max = 100
  nums = (1,2,3,4)
  i = 0
  result = []
  while len(result) < max:
    if i >= len(nums):i=0
    result.append(nums[i])
    i += 1 
  return result


# with generators

def current_beat_with_yield():
  nums=(1,2,3,4)
  i=0
  while True:
    if i >= len(nums): i=0
    yield nums[i]
    i += 1

counter = current_beat_with_yield()

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

