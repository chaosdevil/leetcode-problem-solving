n, nums = input().split(" ", 1)
n = int(n)
nums = list(map(int, nums.split(" ")))


# dynamic programming
lis = [1 for _ in range(n)]
lds = [1 for _ in range(n)]

# implement longest increasing subsequence
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j] and lis[i] < lis[j] + 1:
            lis[i] = lis[j] + 1
        
# implement longest decreasing subsequence
for i in range(n-2, -1, -1):
    for j in range(n-1, i, -1):
        if nums[i] > nums[j] and lds[i] < lds[j] + 1:
            lds[i] = lds[j] + 1

# print(lis)
# print(lds)

maximum = 0
for i in range(0, n):
    if lis[i] + lds[i] - 1 >= maximum and lis[i] != 1 and lds[i] != 1 :
        maximum = lis[i] + lds[i] - 1

print(maximum)