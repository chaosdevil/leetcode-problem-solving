# https://leetcode.com/problems/count-sorted-vowel-strings/

from time import time


class Solution:

    def countVowelStrings(self, n: int) -> int:
        # plan : backtracking and memoization

        def backtrack(i, count):
            if count == 0:
                return 1

            result = 0
            for index in range(i, 5):
                if index >= i:
                    result += backtrack(i, count-1)
                    i += 1

            return result
            
        res = backtrack(0, n)
        
        return res


start = time()
solution = Solution()
print(solution.countVowelStrings(50))
print(f"Time elapsed : {(time() - start) * 1000} milliseconds")
