from collections import Counter
import sys
from time import time
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # plan : top-down
        dp = [amount+1] * (amount + 1)

        dp[0] = 0

        # for i in range(1, amount+1):
        #     for c in coins:
        #         if i - c >= 0:
        #             dp[i] = min(dp[i], 1 + dp[i - c])

        def memoize(i, target):

            if target == 0:
                dp[target] = i
                return dp[target]
            if target < 0:
                return 0
            
            for c in coins:
                if i - c >= 0:
                    count = memoize(i+1, i-c)
            return min(dp[i], 1 + count)
            
            
        memoize(1, amount)
        print(dp)

        return dp[amount]
        

if __name__ == "__main__":

    coins = [1,2,5]
    amount = 8

    start = time()
    solution = Solution()
    print(solution.coinChange(coins, amount))
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")
