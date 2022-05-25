# source : https://leetcode.com/problems/summary-ranges/

from ast import literal_eval

def summary_ranges(nums: list) -> list:
    length = len(nums)
    results = []
    i, j = 0, 0
    while i < length:
        while j + 1 < length and nums[j+1] - nums[j] == 1:
            j += 1
        if j == length:
            results.append(str(nums[i]))
            break
        if nums[i] == nums[j]:
            results.append(str(nums[j]))
            j += 1
        else:
            results.append(f"{nums[i]}->{nums[j]}")
            j += 1
        i = j

    return results


inp = literal_eval(input())
print(summary_ranges(inp))