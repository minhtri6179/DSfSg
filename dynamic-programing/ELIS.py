# 2,5,1,4,9
# Find the longest subsequence
nums = nums = [int(num) for num in input().split()]  # Reading input from STDIN


def solve(nums):
    if not nums:
        return 0
    f = [1] * len(nums)

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                f[i] = max(f[j] + 1, f[i])
    return max(f)


res = solve(nums)
print(res)
