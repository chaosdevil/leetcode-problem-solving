# https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/intermediate-algorithm-scripting/smallest-common-multiple

from time import time


def gcd(x, y):
    while y > 0:
        temp = x % y
        x = y
        y = temp
    return x

def smallest_commons(arr):
    if arr[0] > arr[1]:
        arr[0], arr[1] = arr[1], arr[0]
    nums = []
    for i in range(arr[0], arr[1]+1):
        nums.append(i)
    
    while len(nums) > 1:
        helper = []
        for i in range(1, len(nums)):
            lcm = abs(nums[i-1] * nums[i]) // gcd(nums[i-1], nums[i])
            helper.append(lcm)
        nums = helper
    
    return nums[0]


if __name__ == "__main__":
    start = time()
    print(smallest_commons([1,5]))
    print(smallest_commons([2, 10]))
    print(smallest_commons([23, 18]))
    print(smallest_commons([1, 13]))
    print(smallest_commons([1, 50]))
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")