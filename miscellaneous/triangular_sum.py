def triangular_sum(nums):
    if len(nums) == 1:
        return nums[0]

    new_nums = []
    for i in range(1, len(nums)):
        if nums[i-1] + nums[i] < 10:
            new_nums.append(nums[i-1] + nums[i])
        else:
            new_nums.append(nums[i-1] + nums[i] - 10)

    return triangular_sum(new_nums)


nums = [2,6,6,2,5,7]
print(triangular_sum(nums))



