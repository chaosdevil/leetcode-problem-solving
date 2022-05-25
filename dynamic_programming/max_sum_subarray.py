import sys
from ast import literal_eval

nums = literal_eval(input())


def max_subarray(nums) -> int:
    # Kadane's algorithm
    max_so_far = -sys.maxsize
    max_ending_here = 0

    for i in range(len(nums)):
        max_ending_here = max_ending_here + nums[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


print(max_subarray(nums))