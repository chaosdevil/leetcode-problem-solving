# https://leetcode.com/problems/ones-and-zeroes/

from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for s in strs:
            # count zeros and ones
            zeroes = s.count('0')
            ones = s.count('1')
            
            for i in range(m, zeroes-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeroes][j-ones] + 1)
                    
        return dp[m][n]


if __name__ == "__main__":
    strs =  ["10","0001","111001","1","0"]
    m = 5
    n = 3

    solution = Solution()
    print(solution.findMaxForm(strs, m, n))
