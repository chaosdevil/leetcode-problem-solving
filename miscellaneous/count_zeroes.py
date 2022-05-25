from time import time

def count_zeroes(power, n=10):
    return power * (n**(power-1) + 1) - (((n**power)-1) // 9)

def count_zeroes_v2(n):
    count = 0
    for i in range(1, n+1):
        count += str(i).count("0")
    return count

start = time()
print(count_zeroes(4, 9))
print(f"Time elapsed : {(time() - start) * 1000} milliseconds")

start = time()
print(count_zeroes_v2(9**4))
print(f"Time elapsed : {(time() - start) * 1000} milliseconds")