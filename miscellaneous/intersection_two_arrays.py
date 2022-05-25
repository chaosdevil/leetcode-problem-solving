# https://leetcode.com/problems/intersection-of-two-arrays-ii/submissions/

from collections import Counter
from typing import List
from ast import literal_eval


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        
        if len(counter1) <= len(counter2):
            result = []
            for k in counter1.keys():
                if k in counter2.keys():
                    if counter1[k] <= counter2[k]:
                        result.extend([k] * counter1[k])
                    else:
                        result.extend([k] * counter2[k])
            return result
        else:
            result = []
            for k in counter2.keys():
                if k in counter1.keys():
                    if counter1[k] <= counter2[k]:
                        result.extend([k] * counter1[k])
                    else:
                        result.extend([k] * counter2[k])
            return result

nums1 = literal_eval(input())
nums2 = literal_eval(input())

print(intersect(nums1, nums2))