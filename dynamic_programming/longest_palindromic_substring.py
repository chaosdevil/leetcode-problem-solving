import random
import string
import os

from time import time

class Solution:
    def longestPalindromeV1(self, s: str) -> str:
        # plan : brute-force approach
        longest_palindrome = ""
        n = len(s)
        for i in range(n):
            for j in range(i, n+1):
                sub_str = s[i:j]
                # check if it is palindrome
                s_len = len(sub_str)
                left = 0
                right = s_len - 1
                is_palindrome = True
                while left < right:
                    if sub_str[left] != sub_str[right]:
                        is_palindrome = False
                        break
                    left += 1
                    right -= 1
                if is_palindrome and len(sub_str) > len(longest_palindrome):
                    longest_palindrome = sub_str
        return longest_palindrome

    def longestPalindromeV2(self, s: str) -> str:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        max_length = 1
        
        for i in range(n):
            dp[i][i] = 1
        
        start = 0
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                max_length = 2
                start = i
                
        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i + k - 1
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    
                    if k > max_length:
                        start = i
                        max_length = k
        return s[start:start+max_length]


    def longestPalindromeV3(self, s: str) -> str:
        # plan : bottom-up dynamic programming
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

    def longestPalindromeV4(self, s: str) -> str:
        if len(s) == 1:
            return s

        def expand(s, left, right):
            # expand around center
            l, r = left, right
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        
        start, end = 0, 0
        for i in range(len(s)):
            len1 = expand(s, i, i)
            len2 = expand(s, i, i+1)
            length = max(len1, len2)
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
                
        return s[start:end+1]
            
    def longestPalindromeV5(self, s):
        # Manacher's algorithm
        s_prime = "|".join(list(s))
        palindrome_radius = [0 for _ in range(len(s_prime))]
        result = ""

        center = 0
        radius = 0

        while center < len(s_prime):
            while center-(radius+1) >= 0 and center+(radius+1) < len(s_prime) \
                and s_prime[center-(radius+1)] == s_prime[center+(radius+1)]:
                radius += 1

            palindrome_radius[center] = radius

            old_center = center
            old_radius = radius
            center += 1
            radius = 0

            while center <= old_center + old_radius:
                mirrored_center = old_center - (center - old_center)
                max_mirrored_radius = old_center + old_radius - center
                if palindrome_radius[mirrored_center] < max_mirrored_radius:
                    palindrome_radius[center] = palindrome_radius[mirrored_center]
                    center += 1
                elif palindrome_radius[mirrored_center] > max_mirrored_radius:
                    palindrome_radius[center] = max_mirrored_radius
                    center += 1
                else:
                    radius = max_mirrored_radius
                    break

        longest_palindrome_s_prime = 2 * max(palindrome_radius) + 1
        longest_palindrome = (longest_palindrome_s_prime-1) // 2

        
        return longest_palindrome


if __name__ == "__main__":
    with open(os.path.dirname(__file__) + "/longest_palindromic_substring_testcase.txt", "r") as file:
        text = file.readline().strip()

    text = "cbba"

    solution = Solution()

    # start = time()
    # print(solution.longestPalindromeV1(text))
    # print(f"Time elapsed : {(time() - start) * 1000} milliseconds")

    # start = time()
    # print(solution.longestPalindromeV4(text))
    # print(f"Time elapsed : {(time() - start) * 1000} milliseconds")

    start = time()
    print(solution.longestPalindromeV5(text))
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")
