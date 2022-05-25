from ast import literal_eval
from time import time
from typing import List

class Solution:
    
    def bucket_sort(self, nums, n_buckets):
        # create bucket
        n = len(nums)
        
        maximum = -1e6
        for num in nums:
            if num[0] > maximum:
                maximum = num[0]
        minimum = 1e6
        for num in nums:
            if num[0] < minimum:
                minimum = num[0]
                
        # get range
        r = (maximum - minimum) / n_buckets
        if r == 0:
            r = 1
        
        buckets = [[] for _ in range(n)]
        
        # scatter elements to buckets
        for i in range(n):
            diff = ((nums[i][0]-minimum)/r)-int((nums[i][0]-minimum)/r)
            if diff == 0 and nums[i][0] != minimum:
                buckets[int((nums[i][0]-minimum)/r)-1].append(nums[i])
            else:
                buckets[int((nums[i][0]-minimum)/r)].append(nums[i])
        
        for i in range(n):
            if len(buckets[i]) != 0:
                buckets[i].sort(key=lambda x: x[0])
                
        # concatenate buckets
        k = 0
        for bucket in buckets:
            if bucket:
                for i in range(len(bucket)):
                    nums[k] = bucket[i]
                    k += 1

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # plan : bucket sort
        n = len(nums)

        if n == 1:
            return False

        arr = []
        
        for i in range(n):
            arr.append((nums[i], i))
                    
        self.bucket_sort(arr, n // 2)
        
        print(arr)
        
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if abs(arr[i][0]-arr[j][0]) <= t and abs(arr[i][1]-arr[j][1]) <= k:
                    return True
                if abs(arr[i][0] - arr[j][0]) > t:
                    break
        return False


with open(r"C:\Users\yoksu\Desktop\algorithms\miscellaneous\contains_duplicate_real_input.txt", "r") as file:
    input = literal_eval(file.readline().strip())
    k = int(file.readline().strip())
    t = int(file.readline().strip())

start = time()
sol = Solution()
print(sol.containsNearbyAlmostDuplicate(input, k, t))
print(f"Time elapsed : {(time() - start) * 1000} milliseconds")