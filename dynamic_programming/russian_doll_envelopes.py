# https://leetcode.com/problems/russian-doll-envelopes/

from ast import literal_eval
from typing import List
from time import time
from bisect import bisect_left, bisect_right


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]):
        
        m = len(envelopes)

        if m <= 1:
            return 1
        
        # sort width in ascending order
        # sort height in descending order
        # O(n log n)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # initialize max length
        length = 0

        print(envelopes)

        # build pairs
                
        tail = [0 for _ in range(m)]

        for env in envelopes:
            idx = bisect_left(tail, env[1], 0, length)
            tail[idx] = env[1]
            if idx == length:
                length += 1

        return length

    def binarysearch(self, tail, env, left, right):
        mid = 0
        while left < right:
            mid = left + (right-left) // 2
            if tail[mid] == env:
                return mid
            if env[1] < tail[mid][1]:
                right = mid - 1
            else:
                left = mid + 1
        return mid
            


    

if __name__ == "__main__":

    with open(r"C:\Users\yoksu\Desktop\algorithms\dynamic_programming\russian_doll_envelopes.txt", "r") as file:
        envelopes = literal_eval(file.readline())

    # envelopes = [[1,1],[1,1],[1,1]]
    start = time()
    solution = Solution()
    print(solution.maxEnvelopes(envelopes))
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")

