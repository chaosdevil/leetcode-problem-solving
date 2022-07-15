from time import time
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks or len(matchsticks) < 4:
            return False
        
        length = len(matchsticks)
        perimeter = 0
        for i in range(length):
            perimeter += matchsticks[i]
        
        possible_side = perimeter // 4
        if possible_side * 4 != perimeter:
            return False
        
        n = len(matchsticks)
        
        matchsticks.sort(reverse=True)
        
        memo = dict()
        
        def is_square(mask, sides_done):
            total = 0
            for i in range(n-1, -1, -1):
                if not (mask & (1 << i)):
                    total += matchsticks[n-1-i]
                    
            if total > 0 and total % possible_side == 0:
                sides_done += 1
            
            if sides_done == 3:
                return True
            
            if (mask, sides_done) in memo:
                return memo[(mask, sides_done)]
            
            ans = False
            
            c = total // possible_side
            remaining = possible_side * (c+1) - total
            
            for i in range(n-1,-1,-1):
                if matchsticks[n-1-i] <= remaining and mask & (1 << i):
                    if is_square(mask ^ (1 << i), sides_done):
                        ans = True
                        break
            memo[(mask, sides_done)] = ans
            return ans
                   
        return is_square((1 << n) - 1, 0)
    

if __name__ == "__main__":
    matchsticks = [14,10,10,10,10,10,10,10,10,10,10,10,8,9,19]

    solution = Solution()

    start = time()
    print(solution.makesquare(matchsticks))
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")