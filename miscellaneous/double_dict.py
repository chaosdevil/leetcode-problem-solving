# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from collections import defaultdict
from time import time

d1 = defaultdict(defaultdict)
t = 10
while t > 0:
    code, size, n = input().strip().split(" ")
    if code not in d1:
        d2 = defaultdict(int)
        for s in ['S','M','L','XL']:
            d2[s] = 0
        d2[size] = int(n)
        d1[code] = d2
    else:
        if size in d1[code]:
            d1[code][size] += int(n)
        else:
            d1[code][size] = int(n)
    t -= 1

start = time()
d1 = sorted(d1.items(), key=lambda x: x[0])

for key, value in d1:
    for val in value.items():
        if val[1] != 0:
            print(key, end=" : ")
            print(f"{val[0]} {val[1]}")
print(f"Time elapsed : {(time() - start) * 1000} milliseconds")