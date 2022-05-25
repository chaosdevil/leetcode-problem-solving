from time import time

def recursive_count_ways(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return recursive_count_ways(n-1) + recursive_count_ways(n-2) + recursive_count_ways(n-3)

def memoized_count_ways(n):
    memo = [-1] * (n+1)
    return memoized_count_ways_helper(n, memo)

def memoized_count_ways_helper(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif memo[n] > -1:
        return memo[n]
    else:
        memo[n] = memoized_count_ways_helper(n-1, memo) + memoized_count_ways_helper(n-2, memo) + memoized_count_ways_helper(n-3, memo)
    return memo[n]


if __name__ == "__main__":
    n = int(input("Number of steps of the staircase : "))

    # start = time()
    # print(recursive_count_ways(n))
    # print(f"Time elapsed : {(time() - start) * 1000} milliseconds")

    start = time()
    print(memoized_count_ways(n))
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")



