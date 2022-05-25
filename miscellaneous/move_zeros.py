from ast import literal_eval
from typing import List
from time import time

with open(r"C:\Users\yoksu\Desktop\algorithms\miscellaneous\move_zeros_input.txt", "r") as file:
    inp = literal_eval(file.readline())


def move_zeros(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                i += 1
            else:
                j = i
                while j < len(nums) - 1 and nums[j] == 0:
                    j += 1
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                i += 1


def move_zeros_new_version(nums):
    found_non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[found_non_zero] = nums[i]
            found_non_zero += 1
    for i in range(found_non_zero, len(nums)):
        nums[i] = 0

def check_output(answer, inp):

    for i in range(len(answer)):
        if answer[i] != inp[i]:
            return "not matched"
    return "matched"


start = time()
move_zeros_new_version(inp)
print(inp)
print(f"Time elapsed : {(time() - start) * 1000} milliseconds")
