from time import time
from typing import List


class Solution:
    def generateParenthesisDP(self, n: int) -> List[str]:
        dp = [[] for i in range(n+1)]
        dp[0].append("")
        for i in range(n+1):
            for j in range(i):
                for x in dp[j]:
                    for y in dp[i-j-1]:
                        dp[i] += ['(' + x + ')' + y]
        return dp[n]

    def generateParenthesisBT(self, n: int) -> List[str]:
        results = []
        self.backtrack(results, "", 0, 0, n)
        return results
    
    def backtrack(self, results, current, op, cl, n):
        if len(current) == n * 2:
            results.append(current)
            return
        
        if op < n:
            current += '('
            self.backtrack(results, current, op+1, cl, n)
            current = current[:-1]
            
        if cl < op:
            current += ')'
            self.backtrack(results, current, op, cl+1, n)
            current = current[:-1]


if __name__ == "__main__":

    n = 3
    
    solution = Solution()

    start = time()
    print(solution.generateParenthesisDP(n))
    print(f"Time elapsed for dynamic programming : {(time() - start) * 1000} milliseconds")

    # start = time()
    # print(solution.generateParenthesisBT(n))
    # print(f"Time elapsed for backtracking : {(time() - start) * 1000} milliseconds")