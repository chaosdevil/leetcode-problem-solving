import math

n, m = list(map(int, input().split(" ")))

print(f"n = {n} m = {m}")
print()

# min(x + (n2^x-m)); x=0..logm/log2
x = int(math.log(m) / math.log(2))

s = """
x = 0...math.log(m) / math.log(2)
min(x + ((n*2) ^ x-m))
"""
print(s)
print()

# if m > n:
#     x = int(math.log2(m/n))
#     ans = n * 2 ^ x - m + x
# else:
#     ans = n - m

ans = 10000
for i in range(x):
    ans = min(ans, i + ((n*2) ^ (i - m)))
    
print(f"result : {abs(ans)}")