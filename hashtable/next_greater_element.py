from time import time
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        length = len(nums2)
        d = dict()
        for i in range(len(nums2)):
            d[nums2[i]] = i
        
        for i in range(len(nums1)):
            idx = d[nums1[i]]
            while idx < length:
                if nums2[idx] > nums1[i]:
                    nums1[i] = nums2[idx]
                    break
                idx += 1
            if idx == length:
                nums1[i] = -1
                
        return nums1


if __name__ == "__main__":
    nums1 = [1,3,5,2,4]
    nums2 = [6,5,4,3,2,1,7]

    start = time()
    solution = Solution()
    print(solution.nextGreaterElement(nums1, nums2))
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")