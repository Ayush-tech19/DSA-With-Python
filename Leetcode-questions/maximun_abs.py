# brute force approach
def maxAbsoluteSubarray(nums):
    max_sum = float("-inf")
    for i in range(0, len(nums)):
        total =0
        for j in range(i , len(nums)):
            total +=   nums[j]
            max_sum = max(abs(total), (max_sum))

    return max_sum

# optimized approach
def maxAbsoluteSubarray(nums):
    max_sum = float("-inf")
    min_sum = float("inf")
    total = 0
    for i in range(0, len(nums)):
        total += nums[i]
        max_sum = max(max_sum, abs(total - min_sum))
        min_sum = min(min_sum, total)

    return max_sum

print(maxAbsoluteSubarray([1, -3, 2, 3, -4]))