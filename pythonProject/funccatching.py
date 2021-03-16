import time
from functools import lru_cache

@lru_cache(maxsize=3)
def M(n):
    for i in range(n):
        print(i)
        time.sleep(1)

if __name__ == '__main__':
    print("first time")
    M(3)
    M(1)
    M(2)
    print("second time")
    input()
    M(3)
    M(1)
    M(2)
    M(4)






