from ast import literal_eval
from collections import Counter
from typing import List
from time import time


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        counter = Counter(nums)
        results = []
        
        def backtrack(comb, n):
            # plan : backtracking

            if len(comb) == n:
                results.append(comb[:])
                return

            for k, v in counter.items():
                if v == 0:
                    continue
                comb.append(k)
                counter[k] -= 1
                
                backtrack(comb, n)
                
                comb.pop()
                counter[k] = v
                
        backtrack([], len(nums))
        
        return results    
            
        
if __name__ == '__main__':

    start = time()
    # nums = literal_eval(input())
    nums = [1, 1, 2]

    solution = Solution()
    print(solution.permuteUnique(nums))
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")

    