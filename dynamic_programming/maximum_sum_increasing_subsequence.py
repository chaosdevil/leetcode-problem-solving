n, nums = input().split(" ", 1)
n = int(n)
nums = list(map(int, nums.split(" ")))

# dynamic programming
def max_sum_increasing_subsequence(nums, n):
    maximum = 0

    dp = [0 for _ in range(n)]

    for i in range(n):
        dp[i] = nums[i]

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + nums[i]:
                dp[i] = dp[j] + nums[i]

    for i in range(n):
        if maximum < dp[i]:
            maximum = dp[i]

    return maximum


print(max_sum_increasing_subsequence(nums, n))