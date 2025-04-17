from functools import lru_cache
import time

@lru_cache(maxsize=None)
def func(n):
    time.sleep(5)
    return n*5


print(func(10))
print(func(20))
print(func(30))
print("After caching of the value")
print(func(10))
print(func(20))
print(func(30))
print(func(7))