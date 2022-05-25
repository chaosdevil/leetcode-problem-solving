from ast import literal_eval
from collections import Counter
from typing import List
from time import time


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        mapping = Counter(candidates)
        results = []
        
        def backtrack(comb, target):
            
            # if target < 0:
            #     return
            
            if target == 0 and comb not in results:
                results.append(comb[:])
                return
            
            for k in candidates:
                if target - k < 0:
                    continue
                if comb and k < comb[-1]:
                    continue
                if mapping[k] > 0:
                    comb.append(k)
                    mapping[k] -= 1
                    backtrack(comb, target-k)
                    comb.pop()
                    mapping[k] += 1
                
        backtrack([], target)
        
        return results
                    
                
if __name__ == "__main__":
    with open(r"C:\Users\yoksu\Desktop\algorithms\backtracking\combination_sum_II.txt", "r") as file:
        candidates = literal_eval(file.readline().strip())
        target = int(file.readline().strip())
    
    start = time()
    solution = Solution()
    
    print(solution.combinationSum2(candidates, target))
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")