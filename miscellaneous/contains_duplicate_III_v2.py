from ast import literal_eval
from time import time
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        buckets = {}

        for i, v in enumerate(nums):
            index = v // (t+1)

            if index in buckets:
                return True

            if ((index-1) in buckets) and (abs(buckets[index-1]-v) <= t):
                return True

            if ((index+1) in buckets) and (abs(buckets[index+1]-v) <= t):
                return True

            buckets[index] = v

            if len(buckets) > k:
                buckets.pop(nums[i-k] // (t+1))

        return False


with open(r"C:\Users\yoksu\Desktop\algorithms\miscellaneous\contains_duplicate_real_input.txt", "r") as file:
    input = literal_eval(file.readline().strip())
    k = int(file.readline().strip())
    t = int(file.readline().strip())

start = time()
sol = Solution()
print(sol.containsNearbyAlmostDuplicate(input, k, t))
print(f"Time elapsed : {(time() - start) * 1000} milliseconds")