#Brute Force Solution
def smallerNumbersThanCurrent(nums):
        if len(nums) == 1:
            return [0]
        result = []
        for i in range(0, len(nums)):
            count = 0
            for j in range(0,len(nums)):
                if nums[i] > nums[j]:
                    count += 1
            result.append(count)
        return result

#Optimized Solution
def func(nums):
    ans = []
    mapi = {}
    sorted_arr = sorted(nums)
    for i , num in enumerate(sorted_arr):
        if num not in mapi:
            mapi[num] = i
        return [mapi[num] for num in nums]