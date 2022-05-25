from time import time

start = time()

inp = input().split(" ")
s = inp[0]
k = int(inp[1])

# do combination
from itertools import combinations

# sort string
s = "".join(sorted(s))

for sub_k in range(1, k+1):
    for combine in combinations(s, sub_k):
        print("".join(combine))


print(f"Time elapsed : {(time() - start) * 1000} milliseconds")
