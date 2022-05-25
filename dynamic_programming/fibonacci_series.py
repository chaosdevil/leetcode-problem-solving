from time import time


# recursive version O(2^n)
def recursive_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)


# memoization version much lower time complexity
def memoized_fibonacci(n):
    memo = [0 for _ in range(n+1)]
    return memoized_fibonacci_helper(n, memo)

def memoized_fibonacci_helper(n, memo):
    if n == 0 or n == 1:
        return n
    if memo[n] == 0:
        memo[n] = memoized_fibonacci_helper(n - 1, memo) + memoized_fibonacci_helper(n - 2, memo)
    return memo[n]

def bottom_up_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    memo = [0] * n
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n-1] + memo[n-2]

def final_fibonacci(n):
    if n == 0:
        return 0
    a = 0
    b = 1
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return a + b


if __name__ == "__main__":
    n = int(input("Fibonacci location : "))
    start = time()
    print(recursive_fibonacci(n))
    print(f"Time elapsed : {(time() - start) * 1000}")

    start = time()
    print(memoized_fibonacci(n))
    print(f"Time elasped : {(time() - start) * 1000}")
    
    start = time()
    print(bottom_up_fibonacci(n))
    print(f"Time elapsed : {(time() - start) * 1000}")

    start = time()
    print(final_fibonacci(n))
    print(f"Time elasped : {(time() - start) * 1000}")
