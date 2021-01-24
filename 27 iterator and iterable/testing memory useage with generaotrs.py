def fib_list(max):
  nums =[]
  a,b = 0,1
  while len(nums) < max :
    nums.append(b)
    a,b = b, a+b
  return nums


def fib_gen(max):
  x,y,count=0,1,0
  while count<max :
    x,y = y, x+y
    yield x
    count += 1
    






print(fib_list(30))

gen_nums = fib_gen(100)

###this way
print(next(gen_nums))
print(next(gen_nums))
print(next(gen_nums))
print(next(gen_nums))
print(next(gen_nums))
print(next(gen_nums))


#or this way

for n in fib_gen(10):
  print(n)
