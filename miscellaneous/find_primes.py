import math
from time import time

def is_prime(n):
    # this process takes O(sqrt(n))
    if n == 0 or n == 1:
        return False

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def find_primes(r):
    # overall process takes O(n sqrt(n))

    # r is range
    res = []
    for i in range(r):
        if is_prime(i):
            res.append(i)

    return res

start = time()
answer = find_primes(100)
print(answer)
print(f"Time elapsed : {(time() - start) * 1000} millseconds")