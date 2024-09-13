import functools
import time

root=dict()
@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(2)
    root.update({n:n*n})


    return n*n
    
print(root)

print(fx(2))
print(fx(3))
print(fx(3)) # no time taken by this process because this process run store output in memory
print(root)