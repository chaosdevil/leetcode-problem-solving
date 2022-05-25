import random
import string

from time import time

def longestPalindrome(s: str) -> str:
    # bottom-up dynamic programming
    # print(s)
    n = len(s)
    if n == 1:
        return s

    dp = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    max_length = 1
    start = 0

    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start = i
            max_length = 2

    for i in range(3, n+1):
        for j in range(n-i+1):
            k = j + i - 1
            if dp[j+1][k-1] and s[j] == s[k]:
                dp[j][k] = True
                if i > max_length:
                    start = j
                    max_length = i

    return s[start:start+max_length]



text = "".join(random.choices(string.ascii_lowercase, k=1000))
start = time()
print(longestPalindrome(text))
print(f"Time elapsed : {(time() - start) * 1000} milliseconds")

