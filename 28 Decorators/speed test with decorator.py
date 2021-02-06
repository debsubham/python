# import time

# start_time = time.time()
# sum([x for x in range(40000000)])
# total_time = time.time() - start_time
# print(total_time)


# start_time = time.time()
# sum(x for x in range(40000000))
# total_time = time.time() - start_time
# print(total_time)


# Let's define a speed_test decorator

from time import time
from functools import wraps


def speed_test(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    start_time = time()
    result = fn(*args, **kwargs)
    end_time = time()
    print(f"Time Elapsed: {end_time - start_time}")
    return result
  return wrapper


@speed_test
def sum_nums_withgen():
  return sum(x for x in range(10000000))

@speed_test
def sum_nums():
  return sum([x for x in range(10000000)])


ans = sum_nums()

print(ans)

ans2 = sum_nums_withgen()

print(ans2)