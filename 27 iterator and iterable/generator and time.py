import time

gen_start_time = time.time()
print(sum(n for n in range(100000)))
gen_stop = time.time() - gen_start_time


list_start_time = time.time()
print(sum([n for n in range(100000)]))
list_stop = time.time() - list_start_time


print(f"gen= {gen_stop}")


print(f"list= {list_stop}")

print(time.time())